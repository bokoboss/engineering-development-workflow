import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "setup_project.py"
MANIFEST = ".engineering-workflow.json"


def run_cli(command: str, target: Path):
    return subprocess.run(
        [sys.executable, str(SCRIPT), command, str(target)],
        text=True,
        capture_output=True,
        check=False,
    )


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class SetupProjectTests(unittest.TestCase):
    def make_target(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        return Path(temp.name)

    def test_fresh_install_and_validate(self):
        target = self.make_target()
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((target / "AGENTS.md").is_file())
        self.assertTrue((target / "PROJECT_PROFILE.md").is_file())
        self.assertTrue((target / MANIFEST).is_file())
        self.assertTrue((target / "docs/development/ENGINEERING_WORKFLOW.md").is_file())
        self.assertTrue((target / ".engineering-workflow/SKILL.md").is_file())
        self.assertTrue((target / ".engineering-workflow/WORK_MODE_ROUTING.md").is_file())
        self.assertTrue((target / ".engineering-workflow/WORKSPACE_SAFETY.md").is_file())
        self.assertTrue((target / ".engineering-workflow/skills/scrutinize/SKILL.md").is_file())
        manifest = json.loads((target / MANIFEST).read_text(encoding="utf-8"))
        self.assertEqual(manifest["workflow_version"], "1.7.1")
        self.assertEqual(manifest["local_workflow_dir"], ".engineering-workflow")
        self.assertIn("VALIDATION PASS", result.stdout)
        valid = run_cli("validate", target)
        self.assertEqual(valid.returncode, 0, valid.stderr)

    def test_install_is_idempotent(self):
        target = self.make_target()
        first = run_cli("install", target)
        self.assertEqual(first.returncode, 0, first.stderr)
        before = {p.relative_to(target): p.read_bytes() for p in target.rglob("*") if p.is_file()}
        second = run_cli("install", target)
        self.assertEqual(second.returncode, 0, second.stderr)
        after = {p.relative_to(target): p.read_bytes() for p in target.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_existing_project_owned_files_are_preserved(self):
        target = self.make_target()
        agents = "# Existing project rules\nDo not overwrite me.\n"
        profile = "# Existing project profile\nVerified facts live here.\n"
        (target / "AGENTS.md").write_text(agents, encoding="utf-8")
        (target / "PROJECT_PROFILE.md").write_text(profile, encoding="utf-8")
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((target / "AGENTS.md").read_text(encoding="utf-8"), agents)
        self.assertEqual((target / "PROJECT_PROFILE.md").read_text(encoding="utf-8"), profile)

    def test_upgrade_updates_untouched_managed_old_version(self):
        target = self.make_target()
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        rel = "docs/development/ENGINEERING_WORKFLOW.md"
        path = target / rel
        old = "# Simulated older installer-managed version\n"
        path.write_text(old, encoding="utf-8")
        manifest_path = target / MANIFEST
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["managed"][rel] = sha(old)
        manifest["workflow_version"] = "1.0.0"
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        upgrade = run_cli("upgrade", target)
        self.assertEqual(upgrade.returncode, 0, upgrade.stderr)
        self.assertNotEqual(path.read_text(encoding="utf-8"), old)
        self.assertIn("VALIDATION PASS", upgrade.stdout)

    def test_upgrade_refuses_modified_managed_file(self):
        target = self.make_target()
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        rel = "docs/development/ENGINEERING_WORKFLOW.md"
        path = target / rel
        custom = "# Project-local modification that must survive\n"
        path.write_text(custom, encoding="utf-8")
        upgrade = run_cli("upgrade", target)
        self.assertEqual(upgrade.returncode, 2)
        self.assertIn("locally modified", upgrade.stderr)
        self.assertEqual(path.read_text(encoding="utf-8"), custom)

    def test_validate_detects_drift(self):
        target = self.make_target()
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        path = target / "docs/development/templates/EXECUTION_CONTRACT.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nlocal edit\n", encoding="utf-8")
        valid = run_cli("validate", target)
        self.assertEqual(valid.returncode, 1)
        self.assertIn("VALIDATION FAILED", valid.stderr)


    def test_created_agents_contains_project_root_safety_boundary(self):
        target = self.make_target()
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        agents = (target / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("writable filesystem boundary is this project root only", agents)
        self.assertIn(".engineering-workflow/WORK_MODE_ROUTING.md", agents)
        self.assertIn(".engineering-workflow/WORKSPACE_SAFETY.md", agents)

    def test_refuses_filesystem_root_target(self):
        root = Path(Path.cwd().anchor)
        if not str(root):
            self.skipTest("platform does not expose a filesystem anchor")
        result = run_cli("install", root)
        self.assertEqual(result.returncode, 2)
        self.assertIn("filesystem-root target", result.stderr)

    def test_refuses_user_home_target(self):
        result = run_cli("install", Path.home())
        self.assertEqual(result.returncode, 2)
        self.assertIn("user-home target", result.stderr)

    def test_refuses_workflow_source_target(self):
        result = run_cli("install", ROOT)
        self.assertEqual(result.returncode, 2)
        self.assertIn("overlaps workflow-source checkout", result.stderr)

    def test_refuses_symlink_managed_destination_escape(self):
        target = self.make_target()
        outside_temp = tempfile.TemporaryDirectory()
        self.addCleanup(outside_temp.cleanup)
        outside = Path(outside_temp.name)
        link = target / ".engineering-workflow"
        try:
            link.symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable on this platform")

        marker = outside / "must-not-change.txt"
        marker.write_text("safe", encoding="utf-8")
        result = run_cli("install", target)
        self.assertEqual(result.returncode, 2)
        self.assertIn("symlink/junction", result.stderr)
        self.assertEqual(marker.read_text(encoding="utf-8"), "safe")
        self.assertFalse((outside / "SKILL.md").exists())

    def test_refuses_symlink_target(self):
        real_target = self.make_target()
        link_parent = tempfile.TemporaryDirectory()
        self.addCleanup(link_parent.cleanup)
        link = Path(link_parent.name) / "project-link"
        try:
            link.symlink_to(real_target, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable on this platform")
        result = run_cli("install", link)
        self.assertEqual(result.returncode, 2)
        self.assertIn("target must not be a symlink/junction", result.stderr)


if __name__ == "__main__":
    unittest.main()
