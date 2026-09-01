# Installation and Project Adoption

The workflow can be adopted manually or through the safe bootstrap installer. For projects where Codex/coding agents will mutate code, the recommended path is to bootstrap and validate the workflow **before the first feature/fix execution** so the executor can read the pinned local router/policies/skills.

The recommended path is to use the installer from a checked-out copy of this repository. The installer performs **no network access**; the workflow source revision you checked out is exactly the revision that gets installed. All installer-created/managed content stays below the explicit target project root.

## 1. Clone the workflow repository

```bash
git clone https://github.com/bokoboss/engineering-development-workflow.git
cd engineering-development-workflow
```

For a stable/reproducible adoption, check out the workflow revision you intend to use before installing it.

```bash
git checkout main
```

When stable tags exist, prefer a specific tag for reproducibility.

## 2. Inspect a target repository

From the workflow repository:

```bash
python scripts/setup_project.py inspect /path/to/target-repo
```

On Windows PowerShell, for example:

```powershell
python scripts/setup_project.py inspect D:\R&D\my-project
```

`inspect` is read-only. It reports project-owned files, managed files, missing files, version drift, and conflicts.

## 3. Install

```bash
python scripts/setup_project.py install /path/to/target-repo
```

A fresh install creates, when absent:

- `AGENTS.md` — project-owned starter instructions;
- `PROJECT_PROFILE.md` — project-owned profile template;
- `.engineering-workflow.json` — installer manifest;
- `.engineering-workflow/` — installer-managed pinned workflow snapshot containing `SKILL.md`, FAST/STANDARD/STRICT routing, workspace safety, core policies/templates, and focused `skills/*/SKILL.md` modules;
- `docs/development/ENGINEERING_WORKFLOW.md` — local workflow reference;
- `docs/development/templates/` — installer-managed execution/evidence templates, including the compact FAST packet;
- `.github/ISSUE_TEMPLATE/engineering-workflow-task.md` — reusable engineering task template.

### Safety boundary

The installer rejects:
- filesystem root as a target;
- the user's home/profile directory as a target;
- the workflow source checkout itself as a target;
- installer-managed destinations that pass through symlinks/junctions/link-like paths.

It does not perform network access or arbitrary recursive deletion. It never uses a different directory as a hidden staging/workspace destination.

### Ownership rule

`AGENTS.md` and `PROJECT_PROFILE.md` become **project-owned**. The installer never overwrites them after creation.

Files recorded in `.engineering-workflow.json` are **installer-managed**. Their hashes are tracked so an upgrade can distinguish an untouched managed file from a project-local modification.

## 4. Validate

```bash
python scripts/setup_project.py validate /path/to/target-repo
```

Validation fails when:

- the manifest is missing or invalid;
- a required project-owned file is missing;
- an installer-managed file is missing or modified;
- the manifest hashes do not match;
- the target was installed from a different workflow version than the source currently being used for validation;
- the local `.engineering-workflow/` snapshot is missing/drifted;
- a managed destination violates the workspace containment/link safety rule.

## 5. Upgrade

First update the checked-out workflow repository to the desired revision, then inspect and upgrade the target:

```bash
git pull
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py upgrade /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

Upgrade behavior is conservative:

- untouched installer-managed files can be updated;
- project-owned files are preserved;
- locally modified installer-managed files block the upgrade instead of being overwritten;
- conflicts must be reviewed explicitly;
- new/updated workflow and skill files remain inside `.engineering-workflow/` and other documented managed project paths;
- no arbitrary project/user content is deleted.

## 6. After installation

Before Codex feature/fix work, confirm `python scripts/setup_project.py validate <target>` passes. Codex should begin at `.engineering-workflow/SKILL.md`, apply `.engineering-workflow/WORK_MODE_ROUTING.md`, and obey `.engineering-workflow/WORKSPACE_SAFETY.md` before mutation.

Installation is only the bootstrap step. The project still needs repository-specific facts.

1. Have ChatGPT or a human inspect the actual repository.
2. Fill `PROJECT_PROFILE.md` only with verified facts: baseline SHA, commands, architecture, invariants, protected behavior, validation matrix, known risks, and next objective.
3. Add permanent project-specific rules to `AGENTS.md`.
4. Run the project's own tests/CI; installer validation does not replace product validation.
5. Commit the adoption through a normal branch/PR and review the diff before merge.

## 7. Ask Codex to install it

For most repositories this is bounded mechanical work. A cost-effective default is **Luna Medium** for a simple repository or **Luna High** when existing `AGENTS.md`, GitHub templates, or CI conventions require careful integration.

Ready-to-use prompt:

```text
Install the Engineering Development Workflow from
https://github.com/bokoboss/engineering-development-workflow
into this repository.

Before changing files:
1. identify the exact target project root; do not create/modify/delete anything outside it;
2. inspect this repository, its current Git state, existing AGENTS.md, PROJECT_PROFILE.md,
   .github templates, CI, and project documentation;
3. do not overwrite project-specific instructions or existing project-owned files;
4. do not change global packages, user/system configuration, another repository, or the workflow
   source checkout; use the workflow checkout only as read-only installer input;
5. clone or otherwise obtain an explicit revision of the workflow repository and use its
   scripts/setup_project.py installer;
6. run `inspect` before `install` or `upgrade`;
7. after installation, verify `.engineering-workflow/SKILL.md`, `WORK_MODE_ROUTING.md`, and
   `WORKSPACE_SAFETY.md` exist inside the target project;
8. populate PROJECT_PROFILE.md only from facts you can verify from this repository; do not invent
   commands, architecture, baselines, or protected behavior;
9. preserve existing CI/application behavior and keep this change scoped to workflow adoption;
10. run `python scripts/setup_project.py validate <target>` from the workflow checkout plus all
   relevant validation for this repository;
11. open a PR with the exact workflow revision used, files created/preserved, validation evidence,
   conflicts or limitations, and any project-specific follow-up still requiring human input.

If the installer reports a conflict or workspace-safety refusal, stop and report it instead of forcing an overwrite or bypassing the boundary.
Do not merge the PR automatically.
```

### Recommended routing

- Simple/fresh repo: `Luna / Medium / new Codex chat`.
- Existing repo with project rules/templates: `Luna / High / existing project chat if context is clean; otherwise new chat with a compact handoff`.
- Use Luna Max only when adoption requires non-trivial integration across many existing conventions.
- Escalate to Terra/Sol only if the blocker is demonstrated capability/judgment complexity, not merely an installer conflict or incomplete project information.

## 8. Minimal manual adoption

If Python is unavailable or the repository is intentionally tiny, manual adoption remains valid. At minimum create:

- `AGENTS.md`;
- `PROJECT_PROFILE.md` based on `templates/PROJECT_PROFILE.md`;
- an Issue with scope, out-of-scope, success gates, and protected-change approvals;
- PR evidence for implementation and validation.

Manual adoption remains possible, but when Codex is expected to execute repeatedly, the installer is preferred because it provides the pinned local skill/policy snapshot and deterministic workspace-safety checks.
