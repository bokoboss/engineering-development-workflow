# Engineering Development Workflow

A reusable, evidence-first workflow for developing and safely operating engineering software with humans, ChatGPT, coding agents, GitHub, explicit success gates, focused reasoning skills, lean context, independent review, cost-aware model routing, and bounded continuous operations.

Current workflow version: **v1.7.1 baseline**.

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

v1.7 adds risk-based process routing: **FAST / STANDARD / STRICT**. The selected mode controls ceremony and verification depth, not the quality floor. It also makes the explicit target project root the default writable filesystem boundary for coding agents.

Installing this workflow into a target repository does **not** install anything into ChatGPT. A complete adoption therefore has two sides: set up the ChatGPT Project control plane and bootstrap the target repository.

Before first Codex execution on an adopted project, bootstrap/validate the repository so it contains an installer-managed pinned workflow snapshot under `.engineering-workflow/`. ChatGPT reads current upstream policy; Codex reads the local pinned router/policies/skills. Version drift must be surfaced and reconciled rather than silently mixed.

## Work modes

See [`WORK_MODE_ROUTING.md`](WORK_MODE_ROUTING.md).

- **FAST** — localized, reversible, non-protected work with a concrete proof path and strong targeted verification. Uses a compact packet and skips unnecessary research/scrutiny/independent-review ceremony unless a trigger emerges.
- **STANDARD** — ordinary feature/bug work with normal bounded planning and relevant regression/CI review.
- **STRICT** — protected engineering/safety/security/legal, destructive, architectural/schema/public-contract, system/global, broad/low-reversibility, or similarly high-impact work.

All modes share the same quality floor: inspect before modify, bounded scope, no unrelated changes, appropriate validation, actual diff review, required CI, and no completion claim with failed mandatory gates.

Work mode is separate from model tier. STRICT does not automatically mean Sol.

## Workspace safety

See [`WORKSPACE_SAFETY.md`](WORKSPACE_SAFETY.md).

The default writable boundary is the explicit target project root only. Without explicit human approval for a specific external action, coding agents must not modify another repository, create persistent external working directories, edit user/system configuration, install globally, or create/modify/delete files outside the project. External/system mutation is a STRICT trigger and must stop for approval first.

## Core loop

`Route mode -> Understand -> Bound -> Route executor -> Execute -> Verify -> Audit -> Accept / Escalate`

Two conditional controls may be inserted where risk justifies them:
- **Research Gate** before committing to a direction when important feasibility/evidence unknowns remain;
- **Independent Review** before acceptance when a fresh second pass materially reduces executor blind spots or confirmation bias.

The default operating pattern is:

1. Start from ChatGPT or a human lead, classify FAST / STANDARD / STRICT, establish the target project root, and then establish the authoritative project state and a lean working context.
2. Research material unknowns before converting them into assumptions.
3. Scrutinize high-impact plans and decisions before implementation.
4. Route only the remaining execution work to the cheapest model that can reliably finish the bounded task.
5. Use parallel workers only for genuinely independent workstreams with explicit ownership and integration contracts.
6. Prefer deterministic tests, schemas, validators, CI, settings, workspace-boundary guards, and protection rules over instruction-only compliance where possible.
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
| Assess whether a recurring/event-driven loop is ready for A1/A2/A3 autonomy | `skills/loop-readiness/SKILL.md` |

`SKILL.md` is the router. See [`docs/skill-system.md`](docs/skill-system.md) for routing, progressive disclosure, Gotchas, and mandatory scrutiny cases.

Scrutiny is a required gate unless explicitly documented as not applicable for material architecture/interface/schema changes, protected engineering or safety/security-sensitive logic, major high-cost work packages, high-risk pre-merge decisions, and important acceptance decisions based on incomplete or contradictory evidence.

Research and independent review are risk-based rather than mandatory ceremony for every change.

## Continuous operations (optional)

See [`CONTINUOUS_OPERATIONS.md`](CONTINUOUS_OPERATIONS.md).

v1.6 adds a small outer operational layer for recurring/event-driven work:

`Observe / Discover -> Triage -> Autonomy Gate -> invoke the existing core workflow when action is justified -> persist operational outcome -> wait / trigger again`

This does **not** replace the development workflow. New loop patterns default to **A1 observe/report**, GitHub/project evidence remains authoritative, and operational state is optional derived memory rather than a second source of truth. Action-capable A2/A3 loops require explicit boundaries, finite attempts/no-progress detection, budgets, verification, human escalation, observability, and pause/kill controls.

Use [`templates/LOOP_CONTRACT.md`](templates/LOOP_CONTRACT.md) and [`skills/loop-readiness/SKILL.md`](skills/loop-readiness/SKILL.md) when continuous operation is actually needed. The first reference pattern, [`patterns/pr-ci-watcher.md`](patterns/pr-ci-watcher.md), is intentionally A1/report-only with no automatic code mutation, Codex remediation, close, or merge.

Most projects do not need to configure a loop during initial onboarding.

## Context management

See [`CONTEXT_MANAGEMENT.md`](CONTEXT_MANAGEMENT.md).

The key rule is: **context is a working set, not a dumping ground**. Keep durable truth in GitHub/project documents, load only the relevant workflow/skill material, use concise checkpoints, and deliberately choose between continuing context and starting fresh context.

Fresh or isolated context is particularly useful for broad exploration, diagnostics, independent review, and work where the main thread needs the conclusion rather than every intermediate tool call.

Product-specific context percentages or commands are operational hints, not universal workflow law.

## Project-local pinned workflow

The safe installer now installs the execution-side workflow library inside each adopted project under `.engineering-workflow/`, including the root router, mode routing, workspace safety, core policies, templates, and focused `skills/*/SKILL.md` modules. These files are installer-managed and versioned in `.engineering-workflow.json`.

This is intentional duplication for the **execution plane**: Codex should be able to read the exact workflow version approved for the project without relying on network access. ChatGPT Project Instructions remain concise and continue to point to current upstream policy.

## Recommended onboarding

### 1. Set up the ChatGPT Project control plane

Create a ChatGPT Project for the software project and copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into its Project Instructions.

See **[`docs/chatgpt-project-setup.md`](docs/chatgpt-project-setup.md)**. For the shortest operational summary, see **[`docs/CHEAT_SHEET.md`](docs/CHEAT_SHEET.md)**.

### 2. Bootstrap the target repository before Codex feature work

Clone this workflow repository, inspect the target, then install:

```bash
git clone https://github.com/bokoboss/engineering-development-workflow.git
cd engineering-development-workflow
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py install /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

The installer is stdlib-only and performs no network access. It preserves project-owned `AGENTS.md` and `PROJECT_PROFILE.md`, tracks installer-managed files with SHA-256 hashes, and refuses to overwrite locally modified managed files during upgrades.

The installer installs both the project scaffold and a pinned **project-local workflow/skill snapshot** under `.engineering-workflow/`. ChatGPT uses current upstream policy to route and prepare work; Codex begins from `.engineering-workflow/SKILL.md` and reads only the local policies/skills required by the selected mode/task.

For Windows, upgrade instructions, ownership rules, conflict behavior, and a ready-to-use Codex installation prompt, see **[`docs/installation.md`](docs/installation.md)**.

### 3. Start development from ChatGPT

Ask ChatGPT to inspect the shared workflow and project repository, verify the project profile/current GitHub state, apply any relevant research/scrutiny/context/review rules, and complete everything that can be reliably done in ChatGPT before recommending Codex execution.

## Repository map

- `WORK_MODE_ROUTING.md` — FAST / STANDARD / STRICT risk-based process routing and evidence reuse.
- `WORKSPACE_SAFETY.md` — project-root-only default write boundary and external/system approval protocol.
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
- `docs/CHEAT_SHEET.md` — one-page FAST/STANDARD/STRICT onboarding and safe Codex handoff.
- `docs/` — philosophy, ChatGPT setup, installation, quick start, skills, and examples.

## Quick start

1. Create the ChatGPT Project and install `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` as Project Instructions.
2. Bootstrap and validate the target repository with `scripts/setup_project.py` or ask Codex to do it.
3. Inspect the actual target repository and fill `PROJECT_PROFILE.md` only from verified facts plus explicit project context.
4. Add project-specific permanent instructions to `AGENTS.md`.
5. Start the next development task from ChatGPT control plane; ChatGPT must state FAST / STANDARD / STRICT before Codex execution.
6. Apply the research gate only when important unknowns remain; apply scrutiny where risk requires it; do not load every gate/skill for FAST work.
7. Use `templates/FAST_EXECUTION_PACKET.md` for eligible FAST work; use the full execution contract for STANDARD/STRICT or when complexity warrants it.
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
