# Quick Start

## Recommended adoption path

Use the safe bootstrap installer from an explicit checkout of this workflow repository:

```bash
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py install /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

See `docs/installation.md` for Windows examples, upgrade behavior, ownership rules, and a ready-to-use Codex installation prompt.

## For an existing project

1. Run `inspect` before making changes.
2. Run `install`; existing `AGENTS.md` and `PROJECT_PROFILE.md` are preserved.
3. Inspect the actual target repository and fill `PROJECT_PROFILE.md` only from verified facts.
4. Put project-specific permanent instructions in the project's `AGENTS.md`.
5. Identify protected behavior and required human approvals.
6. Create a GitHub Issue or fill `docs/development/templates/EXECUTION_CONTRACT.md` for the next change.
7. Define success gates before coding.
8. Use the upstream `MODEL_ROUTING_POLICY.md` to choose model + effort + chat reuse/new-chat strategy.
9. Execute in an isolated branch/worktree where appropriate.
10. Validate the project itself and fill evidence/acceptance artifacts for significant work.
11. Review actual diff + evidence before merge.
12. Update `PROJECT_PROFILE.md` and handoff when the accepted baseline changes.

## Upgrading the workflow scaffold

Update the workflow checkout to the revision you want, then run:

```bash
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py upgrade /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

The installer refuses to overwrite a managed file that has been modified locally.

## Minimal adoption

If the full system is too much for a small repository, start with:
- `AGENTS.md`
- `PROJECT_PROFILE.md`
- an Issue with scope/out-of-scope/success gates
- PR evidence

Add more templates only when they reduce recurring ambiguity or verification burden. Manual adoption remains valid when Python is unavailable.
