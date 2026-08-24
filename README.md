# Engineering Development Workflow

A reusable, evidence-first workflow for developing engineering software with humans, ChatGPT, coding agents, GitHub, explicit success gates, and cost-aware model routing.

Current workflow version: **v1.1.0 baseline**.

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
- `templates/` — reusable project and execution contracts.
- `docs/` — philosophy, quick start, and examples.

## Quick start

1. Read `docs/quick-start.md`.
2. Copy `templates/PROJECT_PROFILE.md` into the target project and fill it from the actual repository.
3. Add project-specific `AGENTS.md` instructions.
4. Turn the next change into an Issue or `templates/EXECUTION_CONTRACT.md` packet.
5. Define success gates before implementation.
6. Choose model + effort using `MODEL_ROUTING_POLICY.md`.
7. Execute, validate, review, and attach evidence.

## Important distinction

This repository is a shared workflow. Project-specific equations, client constraints, secrets, local paths, licensed references, and product facts belong in the project repository, not here.

## Status and licensing

The repository is public, but a redistribution license has not yet been selected. Until a license is added, normal copyright rules apply. License selection is intentionally tracked separately before the first stable public release.
