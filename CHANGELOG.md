# Changelog

All notable changes to the workflow contract are documented here. Semantic Versioning is used for the workflow itself.

## [Unreleased]

### Pending
- Collect external feedback after real project adoption.

## [1.5.0] - 2026-08-26

### Added
- `skills/research-gate/SKILL.md` for conditional evidence-backed feasibility and direction decisions using `GO`, `GO WITH CONDITIONS`, `NO-GO`, and `NEEDS MORE EVIDENCE` outcomes.
- `skills/independent-review/SKILL.md` for risk-based fresh-context, cross-model, deterministic, or human second-pass verification.
- `CONTEXT_MANAGEMENT.md` for lean working sets, progressive disclosure, fresh-context decisions, context isolation, recovery from polluted context, and authoritative handoffs.
- `Gotchas` convention for focused skills, populated with recurring high-signal failure modes from real workflow use.
- Research and independent-review fields in execution and acceptance templates.

### Changed
- Core workflow now routes material unknowns through a research gate before committing to implementation direction.
- High-risk acceptance should not rely solely on executor self-report; independent review is required when the project/risk contract calls for it.
- Independent review does not automatically require a stronger model; a fresh context at the same capable tier is explicitly supported.
- Parallel execution guidance now prefers task/feature-specific worker packets over vague generic roles and supports fresh-context reviewers as test-time review.
- Acceptance guidance now prefers deterministic enforcement through tests, schemas, validators, settings, protection rules, or CI when those can reliably enforce a requirement.
- Skill architecture now supports progressive disclosure through optional `references/`, `examples/`, `scripts/`, and `templates/` rather than continuously enlarging `SKILL.md`.
- ChatGPT Project Instructions and Quick Start now include research, context, and independent-review routing.
- Installer/workflow metadata updated to v1.5.0; installer ownership and conflict behavior remain unchanged.

### Attribution note
- `shanraisshan/claude-code-best-practice` (MIT License, Shayan Rais) materially informed the v1.5.0 discussion around Research -> Plan -> Implement gating, cross-model/fresh-context review, context hygiene, progressive disclosure, task-specific workers, and deterministic guardrails. See `ACKNOWLEDGEMENTS.md`. The workflow-native text and contracts in this repository are independently written rather than copied wholesale.

## [1.4.1] - 2026-08-25

### Added
- `ACKNOWLEDGEMENTS.md` as a structured register for material external inspiration, provenance, licensing status, and attribution.
- Explicit credit to `thananon/9arm-skills` for concept-level inspiration that contributed to the focused skill-layer discussion.

### Changed
- CONTRIBUTING now requires material external influences to be documented as `conceptual inspiration`, `adapted`, or `copied/embedded`, together with source and license/status information.
- README now surfaces the acknowledgements and attribution policy.
- Repository validation now requires the attribution contracts and verifies the current workflow metadata as v1.4.1.
- Installer/workflow metadata updated to v1.4.1; installer ownership and conflict behavior are unchanged.

### Attribution note
- `thananon/9arm-skills` had no declared repository license when reviewed on 2026-08-25. No text, code, or skill implementation was copied from it; the acknowledgement records conceptual influence only.

## [1.4.0] - 2026-08-25

### Added
- Focused reusable skill layer under `skills/`.
- `scrutinize` skill for readiness, risk, assumption, and high-impact decision review.
- `systematic-debug` skill for reproducer-first root-cause diagnosis and regression proof.
- `postmortem` skill for preserving lessons after significant resolved defects/incidents.
- `technical-status` skill for turning long or mixed technical evidence into decision-ready status.
- `long-task-guard` skill for bounded, observable, resumable multi-step execution.
- `docs/skill-system.md` describing routing, mandatory scrutiny cases, ChatGPT/Codex responsibilities, and evidence discipline.
- Apache License 2.0 (`Apache-2.0`) as the repository redistribution license and `NOTICE` attribution file.

### Changed
- Root `SKILL.md` is now an explicit router into focused skill modules.
- Core workflow now integrates skill routing at scrutiny, execution, debugging, audit, acceptance, and handoff stages.
- Scrutiny is now a required gate for selected high-impact work unless explicitly documented as not applicable.
- ChatGPT Project Instructions now route through the current upstream skill system before coding-agent execution.
- Installer metadata and workflow reference now identify v1.4.0 and explain that focused skills remain upstream rather than being duplicated into every target repository.
- README documents the skill layer and public Apache-2.0 reuse terms.

### Licensing note
- Skill modules in this repository are original workflow-native definitions. No third-party skill text was imported from repositories without a declared compatible license.

## [1.3.0] - 2026-08-24

### Added
- ChatGPT Project control-plane onboarding guide.
- Reusable `CHATGPT_PROJECT_INSTRUCTIONS.md` template.
- Explicit two-sided onboarding model: ChatGPT Project control plane + target repository bootstrap.
- Architecture documentation clarifying GitHub as shared state and Codex as execution plane.

### Changed
- Recommended onboarding now starts with ChatGPT Project setup before repository bootstrap.
- Quick Start and README now state explicitly that installing the repository scaffold does not install anything into ChatGPT.
- Workflow installer metadata now identifies the shared workflow as v1.3.0.

## [1.2.0] - 2026-08-24

### Added
- Safe stdlib-only project bootstrap installer with `inspect`, `install`, `upgrade`, and `validate` commands.
- Target-repository manifest with SHA-256 tracking for installer-managed files.
- Project-owned file protection for `AGENTS.md` and `PROJECT_PROFILE.md`.
- Conflict-safe upgrade behavior that refuses to overwrite locally modified managed files.
- Automated installer tests for fresh install, idempotence, preservation, upgrade, conflict refusal, and drift detection.
- Installation guide with Windows examples and a ready-to-use Codex adoption prompt.
- CI gate for bootstrap installer tests.

### Changed
- Installer-based adoption became the recommended repository-bootstrap path while manual adoption remains supported.

## [1.1.0] - 2026-08-24

### Added
- ChatGPT-first control-plane principle.
- Cost-aware Luna-first model routing with reasoning-effort selection.
- Diagnose-before-escalate policy for Luna -> Terra -> Sol escalation.
- Optional Sol-orchestrated Luna workers for complex parallelizable execution.
- Explicit success gates, stop conditions, and evidence packages.
- Controlled parallel execution rules and worker ownership.
- Task-oriented engineering UX/UI workflow.
- Reproducer-first debugging protocol and scrutiny/review workflow.
- Project profile, execution contract, acceptance gate, evidence, handoff, postmortem, and Codex prompt templates.
- Repository self-validation script and GitHub Actions validation.

### Preserved from v1.0
- Repository/GitHub as source of truth.
- Issue as auditable work order and PR as delivery/evidence surface.
- CI/tests/browser/reference validation as objective gates.
- Human approval for protected engineering, safety-critical, destructive, or high-impact changes.
