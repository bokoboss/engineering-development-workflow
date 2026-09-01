from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_REL = Path("scripts/release_metadata.py")


class ReleaseMetadataTests(unittest.TestCase):
    def run_script(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(root / SCRIPT_REL), *args],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_current_release_metadata_passes(self):
        result = self.run_script(ROOT, "verify")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("RELEASE METADATA PASS (v1.7.3)", result.stdout)

    def test_historical_release_notes_are_extractable(self):
        for version in ("1.7.0", "1.7.1", "1.7.2"):
            with self.subTest(version=version):
                result = self.run_script(ROOT, "notes", version)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertTrue(result.stdout.startswith(f"# v{version}\n"))

    def test_version_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            copy = Path(temp) / "repo"
            shutil.copytree(
                ROOT,
                copy,
                ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".pytest_cache"),
            )
            readme = copy / "README.md"
            text = readme.read_text(encoding="utf-8")
            self.assertIn("Current workflow version: **v1.7.3 baseline**.", text)
            readme.write_text(
                text.replace(
                    "Current workflow version: **v1.7.2 baseline**.",
                    "Current workflow version: **v9.9.9 baseline**.",
                    1,
                ),
                encoding="utf-8",
            )
            result = self.run_script(copy, "verify")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("release version mismatch", result.stderr)


if __name__ == "__main__":
    unittest.main()
