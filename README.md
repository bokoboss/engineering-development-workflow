# Engineering Development Workflow

A reusable, evidence-first workflow for developing engineering software with humans, ChatGPT, coding agents, GitHub, explicit success gates, and cost-aware model routing.

Current workflow version: **v1.2.0 baseline**.

## Why this exists

Engineering software fails in different ways from ordinary CRUD software: calculations must be auditable, assumptions must be visible, protected behavior must not drift, UX must reflect real engineering work, and completion must be supported by evidence rather than agent confidence.

This repository turns those needs into a repeatable development system.

## Core loop

`Understand -> Bound -> Route -> Execute -> Verify -> Audit -> Accept / Escalate`

The default operating pattern is:

1. ChatGPT or a human lead does as much reasoning, research, repo inspection, decomposition, UX/architecture work, and acceptance design as possible before coding execution.
2. Route execution to the cheapest model that can reliably finish the bounded task.
3. Prefer Luna for well-specified execution; increase reasoning effort before automatically escalating model tier when that is economically sensible.
4. Use Terra or Sol only when ambiguity, cross-module judgment, risk, or demonstrated capability limits justify them.
5. Use parallel workers only for genuinely independent workstreams with explicit ownership and integration contracts.
6. Treat tests, CI, real-data checks, browser/UAT evidence, engineering references, and human approval as gates appropriate to the change.

## Install into another repository

Clone this workflow repository, inspect the target, then install:

```bash
git clone https://github.com/bokoboss/engineering-development-workflow.git
cd engineering-development-workflow
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py install /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

The installer is stdlib-only and performs no network access. It preserves project-owned `AGENTS.md` and `PROJECT_PROFILE.md`, tracks installer-managed files with SHA-256 hashes, and refuses to overwrite locally modified managed files during upgrades.

For Windows, upgrade instructions, ownership rules, conflict behavior, and a ready-to-use Codex installation prompt, see **[`docs/installation.md`](docs/installation.md)**.

## Repository map

- `ENGINEERING_DEV_WORKFLOW.md` — normative end-to-end workflow.
- `MODEL_ROUTING_POLICY.md` — cost-aware model and reasoning-effort policy.
- `UX_UI_WORKFLOW.md` — task-oriented engineering UX/UI method.
- `DEBUGGING_PROTOCOL.md` — reproducer-first defect workflow.
- `REVIEW_AND_SCRUTINY.md` — pre-implementation and pre-merge scrutiny.
- `PARALLEL_EXECUTION.md` — rules for subagents and independent workers.
- `ACCEPTANCE_AND_EVIDENCE.md` — success gates and completion evidence.
- `SECURITY_AND_GOVERNANCE.md` — protected changes, secrets, licensed material, and approvals.
- `AGENTS.md` — concise repository instructions for coding agents.
- `SKILL.md` — router for using this workflow as a reusable skill.
- `scripts/setup_project.py` — safe bootstrap/upgrade/validation installer for target repositories.
- `templates/` — reusable project and execution contracts.
- `docs/` — philosophy, installation, quick start, and examples.

## Quick start

1. Read `docs/installation.md` and `docs/quick-start.md`.
2. Use `scripts/setup_project.py inspect` before adoption.
3. Install the shared workflow scaffold without overwriting project-owned files.
4. Inspect the actual target repository and fill `PROJECT_PROFILE.md` only from verified facts.
5. Add project-specific permanent instructions to `AGENTS.md`.
6. Turn the next change into an Issue or execution contract with explicit success gates.
7. Choose model + effort using `MODEL_ROUTING_POLICY.md`.
8. Execute, validate, review, and attach evidence.

## Important distinction

This repository is a shared workflow. Project-specific equations, client constraints, secrets, local paths, licensed references, and product facts belong in the project repository, not here.

## Status and licensing

The repository is public, but a redistribution license has not yet been selected. Until a license is added, normal copyright rules apply. License selection is intentionally tracked separately before the first stable public release.
