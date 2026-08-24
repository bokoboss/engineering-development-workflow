#!/usr/bin/env python3
"""Safely install or upgrade the Engineering Development Workflow in a target repo.

This tool is intentionally stdlib-only and performs no network access. Run it from a
checked-out copy of this workflow repository so the source revision is explicit and
reproducible.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict

WORKFLOW_REPO = "https://github.com/bokoboss/engineering-development-workflow"
WORKFLOW_VERSION = "1.3.0"
MANIFEST_NAME = ".engineering-workflow.json"

SOURCE_ROOT = Path(__file__).resolve().parents[1]

PROJECT_OWNED = {
    "AGENTS.md": """# Project Agent Instructions\n\nThis project follows the Engineering Development Workflow:\nhttps://github.com/bokoboss/engineering-development-workflow\n\nBefore changing code:\n1. Read `PROJECT_PROFILE.md`.\n2. Inspect the actual repository and current Git/GitHub state.\n3. Preserve project-specific invariants and protected behavior.\n4. Define success gates before implementation.\n5. Use the shared workflow's model-routing policy for coding-agent execution.\n\nProject-specific instructions belong below this line and override the shared workflow only where explicitly stated.\n\n## Project-specific instructions\n\n- Fill this section from verified repository facts.\n""",
    "PROJECT_PROFILE.md": None,
}

MANAGED_SOURCES = {
    "docs/development/ENGINEERING_WORKFLOW.md": None,
    "docs/development/templates/EXECUTION_CONTRACT.md": "templates/EXECUTION_CONTRACT.md",
    "docs/development/templates/ACCEPTANCE_GATE.md": "templates/ACCEPTANCE_GATE.md",
    "docs/development/templates/EVIDENCE_PACKAGE.md": "templates/EVIDENCE_PACKAGE.md",
    "docs/development/templates/HANDOFF.md": "templates/HANDOFF.md",
    "docs/development/templates/POSTMORTEM.md": "templates/POSTMORTEM.md",
    "docs/development/templates/CODEX_PROMPT.md": "templates/CODEX_PROMPT.md",
    ".github/ISSUE_TEMPLATE/engineering-workflow-task.md": ".github/ISSUE_TEMPLATE/implementation-task.md",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def workflow_reference() -> str:
    return f"""# Engineering Development Workflow Reference\n\nThis project adopts the shared Engineering Development Workflow.\n\n- Upstream: {WORKFLOW_REPO}\n- Installed workflow version: {WORKFLOW_VERSION}\n- Local project authority: `PROJECT_PROFILE.md` and project-specific `AGENTS.md`\n\n## Operating rule\n\nUse the upstream repository as the normative workflow source. Keep project-specific facts,\ncommands, invariants, protected behavior, approvals, and accepted-baseline state in this\nrepository.\n\nDefault control loop:\n\n`Understand -> Bound -> Route -> Execute -> Verify -> Audit -> Accept / Escalate`\n\nFor coding-agent work, prepare a bounded execution contract, choose the cheapest model that\ncan reliably finish the task, prefer Luna for well-specified execution, diagnose failures\nbefore escalation, and require objective evidence before claiming completion.\n\n## Local reusable templates\n\nSee `docs/development/templates/`. These copies are installer-managed. Do not edit them\ndirectly; customize an instantiated work item instead.\n"""


def desired_project_owned() -> Dict[str, str]:
    profile = read_text(SOURCE_ROOT / "templates/PROJECT_PROFILE.md")
    return {
        "AGENTS.md": PROJECT_OWNED["AGENTS.md"],
        "PROJECT_PROFILE.md": profile,
    }


def desired_managed() -> Dict[str, str]:
    result: Dict[str, str] = {}
    for dest, source in MANAGED_SOURCES.items():
        result[dest] = workflow_reference() if source is None else read_text(SOURCE_ROOT / source)
    return result


def load_manifest(target: Path) -> dict | None:
    path = target / MANIFEST_NAME
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
        "schema_version": 1,
        "workflow_repo": WORKFLOW_REPO,
        "workflow_version": WORKFLOW_VERSION,
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
        print(f"PROJECT-OWNED {rel}: {'present' if (target / rel).is_file() else 'missing'}")
    for rel, desired in managed.items():
        path = target / rel
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
        path = target / rel
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
    target = target.resolve()
    if not target.is_dir():
        print(f"ERROR: target is not a directory: {target}", file=sys.stderr)
        return 2

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
        path = target / rel
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            if rel not in created_owned:
                created_owned.append(rel)
            print(f"created project-owned: {rel}")
        else:
            print(f"preserved project-owned: {rel}")

    for rel, content in managed.items():
        path = target / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_file() and read_text(path) == content:
            print(f"current managed: {rel}")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"{'updated' if manifest else 'created'} managed: {rel}")

    manifest_data = build_manifest(managed, created_owned)
    (target / MANIFEST_NAME).write_text(
        json.dumps(manifest_data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote manifest: {MANIFEST_NAME}")
    return validate(target)


def validate(target: Path) -> int:
    target = target.resolve()
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
        if not (target / rel).is_file():
            errors.append(f"missing project-owned file: {rel}")

    desired = desired_managed()
    recorded = manifest.get("managed", {})
    for rel, content in desired.items():
        path = target / rel
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

    if errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"VALIDATION PASS ({len(desired)} managed files, {len(PROJECT_OWNED)} project-owned files)")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["inspect", "install", "upgrade", "validate"])
    parser.add_argument("target", nargs="?", default=".", help="target repository directory (default: .)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target)
    try:
        if args.command == "inspect":
            return inspect(target.resolve())
        if args.command in {"install", "upgrade"}:
            return apply(target, args.command)
        return validate(target)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
