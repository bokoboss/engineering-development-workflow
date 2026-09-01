#!/usr/bin/env python3
"""Validate stable-release metadata and extract release notes.

Stdlib-only. This script does not perform network access or GitHub mutation.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

README_RE = re.compile(r"Current workflow version: \*\*v(?P<version>\d+\.\d+\.\d+) baseline\*\*\.")
WORKFLOW_RE = re.compile(r"^Version: (?P<version>\d+\.\d+\.\d+)$", re.MULTILINE)
INSTALLER_RE = re.compile(r'^WORKFLOW_VERSION = "(?P<version>\d+\.\d+\.\d+)"$', re.MULTILINE)
CHANGELOG_HEADING_RE = re.compile(
    r"^## \[(?P<version>\d+\.\d+\.\d+)\] - (?P<date>\d{4}-\d{2}-\d{2})$",
    re.MULTILINE,
)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def match_version(pattern: re.Pattern[str], text: str, source: str) -> str:
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f"cannot determine version from {source}")
    return match.group("version")


def current_version() -> str:
    versions = {
        "README.md": match_version(README_RE, read("README.md"), "README.md"),
        "ENGINEERING_DEV_WORKFLOW.md": match_version(
            WORKFLOW_RE, read("ENGINEERING_DEV_WORKFLOW.md"), "ENGINEERING_DEV_WORKFLOW.md"
        ),
        "scripts/setup_project.py": match_version(
            INSTALLER_RE, read("scripts/setup_project.py"), "scripts/setup_project.py"
        ),
    }
    unique = set(versions.values())
    if len(unique) != 1:
        detail = ", ".join(f"{path}={version}" for path, version in versions.items())
        raise RuntimeError(f"release version mismatch: {detail}")

    version = next(iter(unique))
    headings = {match.group("version") for match in CHANGELOG_HEADING_RE.finditer(read("CHANGELOG.md"))}
    if version not in headings:
        raise RuntimeError(f"CHANGELOG.md has no stable release section for {version}")
    return version


def notes_for(version: str) -> str:
    changelog = read("CHANGELOG.md")
    heading = re.search(
        rf"^## \[{re.escape(version)}\] - \d{{4}}-\d{{2}}-\d{{2}}$",
        changelog,
        re.MULTILINE,
    )
    if not heading:
        raise RuntimeError(f"CHANGELOG.md has no release section for {version}")

    start = heading.end()
    next_heading = re.search(r"^## \[\d+\.\d+\.\d+\] - ", changelog[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(changelog)
    body = changelog[start:end].strip()
    if not body:
        raise RuntimeError(f"release notes for {version} are empty")
    return f"# v{version}\n\n{body}\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("current", help="print the current stable workflow version")
    notes = sub.add_parser("notes", help="print release notes for one stable version")
    notes.add_argument("version")
    sub.add_parser("verify", help="verify current stable release metadata")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        version = current_version()
        if args.command == "current":
            print(version)
        elif args.command == "notes":
            print(notes_for(args.version), end="")
        else:
            # Also ensure current release notes are extractable.
            notes_for(version)
            print(f"RELEASE METADATA PASS (v{version})")
        return 0
    except RuntimeError as exc:
        print(f"RELEASE METADATA FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
