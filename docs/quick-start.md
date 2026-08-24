# Quick Start

## For an existing project

1. Inspect the actual repo and fill `templates/PROJECT_PROFILE.md`.
2. Put project-specific permanent instructions in the project's `AGENTS.md`.
3. Identify protected behavior and required human approvals.
4. Create a GitHub Issue or fill `templates/EXECUTION_CONTRACT.md` for the next change.
5. Define success gates before coding.
6. Use `MODEL_ROUTING_POLICY.md` to choose model + effort + chat reuse/new-chat strategy.
7. Execute in an isolated branch/worktree where appropriate.
8. Validate and fill `templates/EVIDENCE_PACKAGE.md` / `templates/ACCEPTANCE_GATE.md` for significant work.
9. Review actual diff + evidence before merge.
10. Update `PROJECT_PROFILE.md` and handoff when the accepted baseline changes.

## Minimal adoption

If the full system is too much for a small repository, start with:
- `AGENTS.md`
- `PROJECT_PROFILE.md`
- an Issue with scope/out-of-scope/success gates
- PR evidence

Add more templates only when they reduce recurring ambiguity or verification burden.
