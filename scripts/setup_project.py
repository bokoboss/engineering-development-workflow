#!/usr/bin/env python3
"""Safely install or upgrade the Engineering Development Workflow in a target repo.

This tool is intentionally stdlib-only and performs no network access. Run it from a
checked-out copy of this workflow repository so the source revision is explicit and
reproducible.

Safety model:
- the explicit target project root is the only writable boundary;
- filesystem root, user home, and the workflow source checkout are rejected targets;
- installer-managed writes through symlinks/junctions/reparse-like link paths are refused;
- project-owned files are preserved;
- conflicts block mutation;
- this installer has no arbitrary delete/cleanup operation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict

WORKFLOW_REPO = "https://github.com/bokoboss/engineering-development-workflow"
WORKFLOW_VERSION = "1.7.1"
MANIFEST_NAME = ".engineering-workflow.json"
LOCAL_WORKFLOW_DIR = ".engineering-workflow"

SOURCE_ROOT = Path(__file__).resolve().parents[1]

PROJECT_OWNED = {
    "AGENTS.md": """# Project Agent Instructions

This project follows the Engineering Development Workflow:
https://github.com/bokoboss/engineering-development-workflow

Before changing code:
1. Read `PROJECT_PROFILE.md`.
2. Read the project-local pinned router at `.engineering-workflow/SKILL.md`.
3. Apply `.engineering-workflow/WORK_MODE_ROUTING.md` and state FAST / STANDARD / STRICT.
4. Apply `.engineering-workflow/WORKSPACE_SAFETY.md`.
5. Inspect the actual repository and current Git/GitHub state.
6. Preserve project-specific invariants and protected behavior.
7. Define success gates before implementation.

## Workspace safety

The writable filesystem boundary is this project root only.

Do not create, modify, move, or delete files outside this project; modify another repository;
install tools/packages globally; or change user/system configuration unless the human owner
explicitly approves the exact external action first.

If an external/system write appears necessary, stop and report the exact resource, requested
mutation, reason, safer project-local alternative, and rollback before asking for approval.

Project-specific instructions belong below this line and override the shared workflow only where
explicitly stated. They may make the boundary stricter but must not silently weaken protected
engineering/security/safety/human-approval requirements.

## Project-specific instructions

- Fill this section from verified repository facts.
""",
    "PROJECT_PROFILE.md": None,
}

BASE_MANAGED_SOURCES = {
    "docs/development/ENGINEERING_WORKFLOW.md": None,
    "docs/development/templates/EXECUTION_CONTRACT.md": "templates/EXECUTION_CONTRACT.md",
    "docs/development/templates/FAST_EXECUTION_PACKET.md": "templates/FAST_EXECUTION_PACKET.md",
    "docs/development/templates/ACCEPTANCE_GATE.md": "templates/ACCEPTANCE_GATE.md",
    "docs/development/templates/EVIDENCE_PACKAGE.md": "templates/EVIDENCE_PACKAGE.md",
    "docs/development/templates/HANDOFF.md": "templates/HANDOFF.md",
    "docs/development/templates/POSTMORTEM.md": "templates/POSTMORTEM.md",
    "docs/development/templates/CODEX_PROMPT.md": "templates/CODEX_PROMPT.md",
    "docs/development/templates/LOOP_CONTRACT.md": "templates/LOOP_CONTRACT.md",
    ".github/ISSUE_TEMPLATE/engineering-workflow-task.md": ".github/ISSUE_TEMPLATE/implementation-task.md",
}

LOCAL_POLICY_FILES = [
    "SKILL.md",
    "ENGINEERING_DEV_WORKFLOW.md",
    "WORK_MODE_ROUTING.md",
    "WORKSPACE_SAFETY.md",
    "CONTEXT_MANAGEMENT.md",
    "MODEL_ROUTING_POLICY.md",
    "SECURITY_AND_GOVERNANCE.md",
    "ACCEPTANCE_AND_EVIDENCE.md",
    "DEBUGGING_PROTOCOL.md",
    "REVIEW_AND_SCRUTINY.md",
    "PARALLEL_EXECUTION.md",
    "UX_UI_WORKFLOW.md",
    "CONTINUOUS_OPERATIONS.md",
]

LOCAL_TEMPLATE_FILES = [
    "templates/EXECUTION_CONTRACT.md",
    "templates/FAST_EXECUTION_PACKET.md",
    "templates/ACCEPTANCE_GATE.md",
    "templates/EVIDENCE_PACKAGE.md",
    "templates/HANDOFF.md",
    "templates/POSTMORTEM.md",
    "templates/CODEX_PROMPT.md",
    "templates/LOOP_CONTRACT.md",
]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_linklike(path: Path) -> bool:
    """Return True for symlinks and, where supported, Windows junctions."""
    try:
        if path.is_symlink():
            return True
        junction_check = getattr(path, "is_junction", None)
        if junction_check is not None and junction_check():
            return True
    except OSError:
        # Fail closed when link metadata itself cannot be established safely.
        return True
    return False


def is_within(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def resolve_safe_target(raw_target: Path) -> Path:
    """Resolve and reject targets that are too broad or unsafe for mutation."""
    expanded = raw_target.expanduser()
    if is_linklike(expanded):
        raise RuntimeError(f"target must not be a symlink/junction: {expanded}")

    try:
        target = expanded.resolve(strict=True)
    except OSError as exc:
        raise RuntimeError(f"target cannot be resolved: {expanded}: {exc}") from exc

    if not target.is_dir():
        raise RuntimeError(f"target is not a directory: {target}")

    if target.parent == target:
        raise RuntimeError(f"refusing filesystem-root target: {target}")

    try:
        home = Path.home().resolve(strict=True)
    except OSError:
        home = Path.home().resolve()
    if target == home:
        raise RuntimeError(f"refusing user-home target: {target}")

    source = SOURCE_ROOT.resolve()
    if target == source or is_within(target, source) or is_within(source, target):
        raise RuntimeError(
            f"refusing target that overlaps workflow-source checkout: {target}"
        )

    return target


def safe_destination(target: Path, rel: str) -> Path:
    """Return a project-contained managed path, failing closed on link escapes."""
    rel_path = Path(rel)
    if rel_path.is_absolute() or not rel_path.parts or ".." in rel_path.parts:
        raise RuntimeError(f"unsafe managed relative path: {rel}")

    current = target
    for part in rel_path.parts:
        current = current / part
        if current.exists() or is_linklike(current):
            if is_linklike(current):
                raise RuntimeError(f"refusing managed path through symlink/junction: {rel}")
            try:
                resolved = current.resolve(strict=True)
            except OSError as exc:
                raise RuntimeError(f"cannot resolve managed path {rel}: {exc}") from exc
            if not is_within(resolved, target):
                raise RuntimeError(f"managed path escapes target: {rel}")

    candidate = target / rel_path
    # Resolve the deepest existing parent to catch unusual mount/link behavior.
    parent = candidate.parent
    while not parent.exists() and parent != target:
        parent = parent.parent
    try:
        resolved_parent = parent.resolve(strict=True)
    except OSError as exc:
        raise RuntimeError(f"cannot resolve managed parent for {rel}: {exc}") from exc
    if not is_within(resolved_parent, target):
        raise RuntimeError(f"managed parent escapes target: {rel}")

    return candidate


def workflow_reference() -> str:
    return f"""# Engineering Development Workflow Reference

This project adopts the shared Engineering Development Workflow.

- Upstream: {WORKFLOW_REPO}
- Installed workflow version: {WORKFLOW_VERSION}
- Project-local pinned workflow: `{LOCAL_WORKFLOW_DIR}/`
- Local project authority: `PROJECT_PROFILE.md` and project-specific `AGENTS.md`

## Operating rule

ChatGPT/control-plane work should read the current upstream workflow. Coding agents executing in
this repository should read the project-local pinned snapshot beginning at
`{LOCAL_WORKFLOW_DIR}/SKILL.md`.

Before coding-agent execution:
1. route the task with `{LOCAL_WORKFLOW_DIR}/WORK_MODE_ROUTING.md`;
2. apply `{LOCAL_WORKFLOW_DIR}/WORKSPACE_SAFETY.md`;
3. load only the additional policies/skills required by the selected mode/task;
4. keep all unapproved writes inside this project root.

FAST / STANDARD / STRICT controls process intensity, not correctness. FAST uses a compact packet
when eligible. STANDARD uses the normal bounded flow. STRICT applies the full evidence-first
workflow for protected/high-impact work.

Do not silently mix incompatible upstream and local policy versions. If the local snapshot is
missing or materially outdated for the current task, install/upgrade/validate it first.

## Local reusable templates

See `docs/development/templates/`. These copies are installer-managed. Do not edit them directly;
customize an instantiated work item instead.
"""


def desired_project_owned() -> Dict[str, str]:
    profile = read_text(SOURCE_ROOT / "templates/PROJECT_PROFILE.md")
    return {
        "AGENTS.md": PROJECT_OWNED["AGENTS.md"],
        "PROJECT_PROFILE.md": profile,
    }


def local_workflow_sources() -> Dict[str, str]:
    result: Dict[str, str] = {}
    for source in LOCAL_POLICY_FILES + LOCAL_TEMPLATE_FILES:
        result[f"{LOCAL_WORKFLOW_DIR}/{source}"] = source

    skills_root = SOURCE_ROOT / "skills"
    for source_path in sorted(skills_root.glob("*/SKILL.md")):
        source = source_path.relative_to(SOURCE_ROOT).as_posix()
        result[f"{LOCAL_WORKFLOW_DIR}/{source}"] = source
    return result


def desired_managed() -> Dict[str, str]:
    sources = dict(BASE_MANAGED_SOURCES)
    sources.update(local_workflow_sources())

    result: Dict[str, str] = {}
    for dest, source in sources.items():
        result[dest] = workflow_reference() if source is None else read_text(SOURCE_ROOT / source)
    return result


def load_manifest(target: Path) -> dict | None:
    path = safe_destination(target, MANIFEST_NAME)
    if not path.exists():
        return None
    try:
        data = json.loads(read_text(path))
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"invalid {MANIFEST_NAME}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("managed"), dict):
        raise RuntimeError(f"invalid {MANIFEST_NAME}: missing managed map")
    return data


def build_manifest(managed: Dict[str, str], project_owned_created: list[str]) -> dict:
    return {
        "schema_version": 2,
        "workflow_repo": WORKFLOW_REPO,
        "workflow_version": WORKFLOW_VERSION,
        "local_workflow_dir": LOCAL_WORKFLOW_DIR,
        "managed": {path: sha256_text(text) for path, text in sorted(managed.items())},
        "project_owned_created": sorted(project_owned_created),
    }


def current_hash(path: Path) -> str | None:
    if not path.is_file():
        return None
    return sha256_text(read_text(path))


def inspect(target: Path) -> int:
    manifest = load_manifest(target)
    managed = desired_managed()
    owned = desired_project_owned()
    print(f"Target: {target}")
    print(f"Source workflow version: {WORKFLOW_VERSION}")
    print(f"Manifest: {'present' if manifest else 'absent'}")
    if manifest:
        print(f"Installed workflow version: {manifest.get('workflow_version', 'unknown')}")
    for rel in owned:
        path = safe_destination(target, rel)
        print(f"PROJECT-OWNED {rel}: {'present' if path.is_file() else 'missing'}")
    for rel, desired in managed.items():
        path = safe_destination(target, rel)
        cur = current_hash(path)
        want = sha256_text(desired)
        if cur is None:
            status = "missing"
        elif cur == want:
            status = "current"
        elif manifest and manifest.get("managed", {}).get(rel) == cur:
            status = "managed-old-version"
        else:
            status = "modified/conflict"
        print(f"MANAGED {rel}: {status}")
    return 0


def preflight(target: Path, mode: str, manifest: dict | None, managed: Dict[str, str]) -> list[str]:
    conflicts: list[str] = []
    if mode == "upgrade" and manifest is None:
        return [f"{MANIFEST_NAME} is missing; run install first"]

    previous = (manifest or {}).get("managed", {})
    for rel, desired in managed.items():
        path = safe_destination(target, rel)
        cur = current_hash(path)
        if cur is None or cur == sha256_text(desired):
            continue
        if mode == "install" and manifest is None:
            conflicts.append(f"{rel}: existing unmanaged file would be overwritten")
            continue
        old_hash = previous.get(rel)
        if old_hash is None:
            conflicts.append(f"{rel}: not recorded as installer-managed")
        elif cur != old_hash:
            conflicts.append(f"{rel}: locally modified since installation")
    return conflicts


def apply(target: Path, mode: str) -> int:
    manifest = load_manifest(target)
    managed = desired_managed()
    owned = desired_project_owned()
    conflicts = preflight(target, mode, manifest, managed)
    if conflicts:
        print("Installation blocked by conflicts:", file=sys.stderr)
        for item in conflicts:
            print(f"- {item}", file=sys.stderr)
        print("No installer-managed files were changed.", file=sys.stderr)
        return 2

    created_owned = list((manifest or {}).get("project_owned_created", []))
    for rel, content in owned.items():
        path = safe_destination(target, rel)
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            if rel not in created_owned:
                created_owned.append(rel)
            print(f"created project-owned: {rel}")
        else:
            print(f"preserved project-owned: {rel}")

    for rel, content in managed.items():
        path = safe_destination(target, rel)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_file() and read_text(path) == content:
            print(f"current managed: {rel}")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"{'updated' if manifest else 'created'} managed: {rel}")

    manifest_path = safe_destination(target, MANIFEST_NAME)
    manifest_data = build_manifest(managed, created_owned)
    manifest_path.write_text(
        json.dumps(manifest_data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote manifest: {MANIFEST_NAME}")
    return validate(target)


def validate(target: Path) -> int:
    try:
        manifest = load_manifest(target)
    except RuntimeError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1
    if manifest is None:
        print(f"VALIDATION FAILED: {MANIFEST_NAME} is missing", file=sys.stderr)
        return 1

    errors: list[str] = []
    for rel in desired_project_owned():
        try:
            path = safe_destination(target, rel)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        if not path.is_file():
            errors.append(f"missing project-owned file: {rel}")

    desired = desired_managed()
    recorded = manifest.get("managed", {})
    for rel, content in desired.items():
        try:
            path = safe_destination(target, rel)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        cur = current_hash(path)
        want = sha256_text(content)
        if cur is None:
            errors.append(f"missing managed file: {rel}")
        elif cur != want:
            errors.append(f"managed file differs from this workflow source: {rel}")
        if recorded.get(rel) != cur:
            errors.append(f"manifest hash mismatch: {rel}")

    if manifest.get("workflow_repo") != WORKFLOW_REPO:
        errors.append("manifest workflow_repo mismatch")
    if manifest.get("workflow_version") != WORKFLOW_VERSION:
        errors.append("manifest workflow_version mismatch")
    if manifest.get("local_workflow_dir") != LOCAL_WORKFLOW_DIR:
        errors.append("manifest local_workflow_dir mismatch")

    if errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALIDATION PASS ({len(desired)} managed files, {len(PROJECT_OWNED)} project-owned files)")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inspect", "install", "upgrade", "validate"])
    parser.add_argument("target", nargs="?", default=".", help="target project directory (default: .)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        target = resolve_safe_target(Path(args.target))
        if args.command == "inspect":
            return inspect(target)
        if args.command in {"install", "upgrade"}:
            return apply(target, args.command)
        return validate(target)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
