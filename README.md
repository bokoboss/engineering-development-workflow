# Engineering Development Workflow

A reusable, evidence-first workflow for developing engineering software with humans, ChatGPT, coding agents, GitHub, explicit success gates, focused reasoning skills, lean context, independent review, and cost-aware model routing.

Current workflow version: **v1.5.0 baseline**.

License: **Apache-2.0**.

## Why this exists

Engineering software fails in different ways from ordinary CRUD software: calculations must be auditable, assumptions must be visible, protected behavior must not drift, UX must reflect real engineering work, context must stay usable, and completion must be supported by evidence rather than agent confidence.

This repository turns those needs into a repeatable development system.

## Core architecture

The intended operating model is:

```text
                    Shared Workflow Repo
        bokoboss/engineering-development-workflow
                  /                    \
                 /                      \
                v                        v
       ChatGPT Project             Target GitHub Repo
        control plane              shared project state
             |                           |
             |                           v
             |                         Codex
             |                    execution plane
             |                           |
             +--------- GitHub ----------+
                         |
                    PR / CI / Evidence
                         |
                         v
            Independent review when needed
                         |
                         v
                  ChatGPT final review
```

**ChatGPT is the control plane. GitHub is the shared state/source of truth. Codex is the execution plane when local code, runtime, browser, or environment work is actually required.**

Installing this workflow into a target repository does **not** install anything into ChatGPT. A complete adoption therefore has two sides: set up the ChatGPT Project control plane and bootstrap the target repository.

## Core loop

`Understand -> Bound -> Route -> Execute -> Verify -> Audit -> Accept / Escalate`

Two conditional controls may be inserted where risk justifies them:
- **Research Gate** before committing to a direction when important feasibility/evidence unknowns remain;
- **Independent Review** before acceptance when a fresh second pass materially reduces executor blind spots or confirmation bias.

The default operating pattern is:

1. Start from ChatGPT or a human lead and establish the authoritative project state and a lean working context.
2. Research material unknowns before converting them into assumptions.
3. Scrutinize high-impact plans and decisions before implementation.
4. Route only the remaining execution work to the cheapest model that can reliably finish the bounded task.
5. Use parallel workers only for genuinely independent workstreams with explicit ownership and integration contracts.
6. Prefer deterministic tests, schemas, validators, CI, settings, and protection rules over instruction-only compliance where possible.
7. Treat tests, CI, real-data checks, browser/UAT evidence, engineering references, independent review, and human approval as gates appropriate to the change.
8. Return to ChatGPT for review of actual GitHub diff and evidence before acceptance.

## Focused skill layer

The core workflow stays authoritative, while reusable skills provide more specific procedures for recurring situations:

| Situation | Skill |
|---|---|
| Resolve feasibility, dependency, methodology, compatibility, or evidence unknowns before planning | `skills/research-gate/SKILL.md` |
| Challenge a plan, architecture, risky change, or merge readiness | `skills/scrutinize/SKILL.md` |
| Diagnose a bug, regression, failing CI, or runtime defect | `skills/systematic-debug/SKILL.md` |
| Obtain a fresh-context/cross-model/human second pass for material acceptance risk | `skills/independent-review/SKILL.md` |
| Preserve lessons after a significant resolved defect/incident | `skills/postmortem/SKILL.md` |
| Turn long/mixed technical output into a decision-ready status | `skills/technical-status/SKILL.md` |
| Keep long or multi-step work bounded and resumable | `skills/long-task-guard/SKILL.md` |

`SKILL.md` is the router. See [`docs/skill-system.md`](docs/skill-system.md) for routing, progressive disclosure, Gotchas, and mandatory scrutiny cases.

Scrutiny is a required gate unless explicitly documented as not applicable for material architecture/interface/schema changes, protected engineering or safety/security-sensitive logic, major high-cost work packages, high-risk pre-merge decisions, and important acceptance decisions based on incomplete or contradictory evidence.

Research and independent review are risk-based rather than mandatory ceremony for every change.

## Context management

See [`CONTEXT_MANAGEMENT.md`](CONTEXT_MANAGEMENT.md).

The key rule is: **context is a working set, not a dumping ground**. Keep durable truth in GitHub/project documents, load only the relevant workflow/skill material, use concise checkpoints, and deliberately choose between continuing context and starting fresh context.

Fresh or isolated context is particularly useful for broad exploration, diagnostics, independent review, and work where the main thread needs the conclusion rather than every intermediate tool call.

Product-specific context percentages or commands are operational hints, not universal workflow law.

## Recommended onboarding

### 1. Set up the ChatGPT Project control plane

Create a ChatGPT Project for the software project and copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into its Project Instructions.

See **[`docs/chatgpt-project-setup.md`](docs/chatgpt-project-setup.md)**.

### 2. Bootstrap the target repository

Clone this workflow repository, inspect the target, then install:

```bash
git clone https://github.com/bokoboss/engineering-development-workflow.git
cd engineering-development-workflow
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py install /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

The installer is stdlib-only and performs no network access. It preserves project-owned `AGENTS.md` and `PROJECT_PROFILE.md`, tracks installer-managed files with SHA-256 hashes, and refuses to overwrite locally modified managed files during upgrades.

The installer intentionally installs the **core project scaffold**, not a duplicate of the complete upstream policy/skill library. ChatGPT reads the current shared workflow and translates relevant conclusions into the target project's execution contract, gates, and Codex prompt.

For Windows, upgrade instructions, ownership rules, conflict behavior, and a ready-to-use Codex installation prompt, see **[`docs/installation.md`](docs/installation.md)**.

### 3. Start development from ChatGPT

Ask ChatGPT to inspect the shared workflow and project repository, verify the project profile/current GitHub state, apply any relevant research/scrutiny/context/review rules, and complete everything that can be reliably done in ChatGPT before recommending Codex execution.

## Repository map

- `ENGINEERING_DEV_WORKFLOW.md` — normative end-to-end workflow.
- `CONTEXT_MANAGEMENT.md` — lean working context, fresh-context, isolation, checkpoint, and progressive-disclosure policy.
- `MODEL_ROUTING_POLICY.md` — cost-aware model and reasoning-effort policy.
- `UX_UI_WORKFLOW.md` — task-oriented engineering UX/UI method.
- `DEBUGGING_PROTOCOL.md` — reproducer-first defect workflow.
- `REVIEW_AND_SCRUTINY.md` — pre-implementation and pre-merge scrutiny principles.
- `PARALLEL_EXECUTION.md` — task-specific worker, independent reviewer, and integration rules.
- `ACCEPTANCE_AND_EVIDENCE.md` — success gates, deterministic enforcement, and completion evidence.
- `SECURITY_AND_GOVERNANCE.md` — protected changes, secrets, licensed material, and approvals.
- `SKILL.md` — root router for the core workflow and focused skills.
- `skills/` — focused reusable protocols for research, scrutiny, debugging, independent review, postmortems, status translation, and long tasks.
- `docs/skill-system.md` — how and when focused skills apply and grow through progressive disclosure.
- `ACKNOWLEDGEMENTS.md` — external inspiration, provenance, licensing status, and attribution records.
- `AGENTS.md` — concise repository instructions for coding agents.
- `scripts/setup_project.py` — safe bootstrap/upgrade/validation installer for target repositories.
- `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` — reusable ChatGPT Project control-plane instructions.
- `templates/` — reusable project, execution, acceptance, evidence, handoff, and postmortem contracts.
- `docs/` — philosophy, ChatGPT setup, installation, quick start, skills, and examples.

## Quick start

1. Create the ChatGPT Project and install `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` as Project Instructions.
2. Bootstrap and validate the target repository with `scripts/setup_project.py` or ask Codex to do it.
3. Inspect the actual target repository and fill `PROJECT_PROFILE.md` only from verified facts plus explicit project context.
4. Add project-specific permanent instructions to `AGENTS.md`.
5. Start the next development task from ChatGPT control plane.
6. Apply the research gate only when important unknowns remain; apply scrutiny where risk requires it.
7. Create the Issue/execution contract with explicit success gates and any independent-review requirement.
8. Invoke Codex only when execution-plane capabilities are required, using `MODEL_ROUTING_POLICY.md` for model + effort selection.
9. Validate, independently review when justified, inspect actual GitHub evidence, and accept or remediate.

## Attribution and acknowledgements

This project gives explicit credit when identifiable external work materially influences a reusable workflow rule, skill, template, architecture decision, or validation method.

See [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) for the current attribution register and the distinction between **conceptual inspiration**, **adapted material**, and **copied/embedded material**. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the rule contributors should follow when introducing externally influenced work.

A source can deserve credit even when no literal text or code is copied. Conversely, a public repository without a compatible declared license is not treated as permission to copy its contents.

## Important distinction

This repository is a shared workflow. Project-specific equations, client constraints, secrets, local paths, licensed references, and product facts belong in the project repository, not here. ChatGPT Project Instructions should stay concise and point back to the shared workflow rather than duplicating its full policy.

## License

Licensed under the **Apache License, Version 2.0** (`Apache-2.0`). You may use, modify, redistribute, and use this work commercially subject to the terms of the license. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
