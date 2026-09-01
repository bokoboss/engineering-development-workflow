from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_REL = Path("scripts/validate_repository.py")


class ValidateRepositoryNegativeTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.copy = Path(self.tempdir.name) / "repo"
        shutil.copytree(
            ROOT,
            self.copy,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".pytest_cache"),
        )

    def run_validator(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.copy / VALIDATOR_REL)],
            cwd=self.copy,
            text=True,
            capture_output=True,
            check=False,
        )

    def replace_required_text(self, rel: str, required: str) -> None:
        path = self.copy / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(required, text, f"test fixture missing expected text in {rel}")
        path.write_text(text.replace(required, "REMOVED_BY_NEGATIVE_TEST", 1), encoding="utf-8")

    def assert_validation_fails(self, expected_fragment: str) -> None:
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        combined = result.stdout + result.stderr
        self.assertIn("Repository validation FAILED", combined)
        self.assertIn(expected_fragment, combined)

    def test_current_repository_copy_passes(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Repository validation PASS", result.stdout)

    def test_missing_security_invariant_fails(self):
        self.replace_required_text(
            "SECURITY_AND_GOVERNANCE.md",
            "Human approval is a design control, not a failure of automation.",
        )
        self.assert_validation_fails("SECURITY_AND_GOVERNANCE.md")

    def test_missing_fast_proof_invariant_fails(self):
        self.replace_required_text(
            "WORK_MODE_ROUTING.md",
            "at least one concrete proof path exists before mutation",
        )
        self.assert_validation_fails("WORK_MODE_ROUTING.md")

    def test_missing_workspace_boundary_invariant_fails(self):
        self.replace_required_text(
            "WORKSPACE_SAFETY.md",
            "**the explicit target project root, and only that project root.**",
        )
        self.assert_validation_fails("WORKSPACE_SAFETY.md")

    def test_missing_ci_validator_command_fails(self):
        self.replace_required_text(
            ".github/workflows/validate.yml",
            "python scripts/validate_repository.py",
        )
        self.assert_validation_fails(".github/workflows/validate.yml")

    def test_missing_ci_installer_test_command_fails(self):
        self.replace_required_text(
            ".github/workflows/validate.yml",
            "python -m unittest discover -s tests -p 'test_*.py' -v",
        )
        self.assert_validation_fails(".github/workflows/validate.yml")


if __name__ == "__main__":
    unittest.main()
