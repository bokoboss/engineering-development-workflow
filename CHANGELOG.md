# Changelog

All notable changes to the workflow contract are documented here. Semantic Versioning is used for the workflow itself.

## [Unreleased]

### Pending
- Collect external feedback after real project adoption.
- Foundation research for a possible Local Workspace Evidence Bridge completed in `docs/research/local-workspace-evidence-bridge-adoption-review.md`. Concept verdict: `GO WITH CONDITIONS`; direct adoption of pinned `XiaoDuoYa/codex-with-chatgpt` v0.1.1: `NO-GO AT THIS TIME`. No v1.7 workflow contract or candidate installation is introduced by this research-only change.

## [1.7.2] - 2026-09-01

### Added
- `SECURITY.md` with private vulnerability-reporting guidance and explicit installer/filesystem-safety scope.
- Conservative `.gitignore` that intentionally does not hide project-local `.engineering-workflow/` artifacts.
- `.github/CODEOWNERS` for core workflow, safety, scripts, tests, workflows, templates, and skills.
- `docs/GITHUB_REPOSITORY_CONFIGURATION.md` separating desired GitHub-level rules/metadata from committed repository policy.
- `docs/validation-design.md` documenting deterministic substring/cross-contract validation scope and semantic limitations.
- `scripts/release_metadata.py` for stdlib-only stable-version consistency and CHANGELOG release-note extraction.
- `.github/workflows/release.yml` to publish tags/releases only after successful validation of `main`.
- Negative validator regression tests proving selected unsafe/invalid repository states fail.
- Release-metadata tests proving current metadata passes, historical notes remain extractable, and version mismatch fails closed.

### Changed
- Stable workflow version updated to v1.7.2.
- `VERSIONING.md` now requires an accepted commit, green validation, `vX.Y.Z` Git tag, and matching GitHub Release for stable versions.
- Release automation is fail-closed: publication requires successful main validation **and merged-PR provenance**, existing tags are never retargeted, each release records its accepted commit SHA, existing releases are verified against that recorded SHA and left unchanged, and historical backfill is limited to explicitly verified v1.7.0/v1.7.1 SHAs.
- Repository validation now checks security/release/configuration files, release workflow anchors, release metadata tooling, negative validator tests, and GitHub-level configuration documentation.
- Validation CI now includes stable-release metadata verification.
- Validation CI now runs monthly as a low-frequency GitHub Actions/runtime drift safety net; this is not a substitute for branch protection.

### Repository configuration note
- Desired `main` ruleset/branch-protection and repository About metadata are documented, but committed Markdown is not treated as evidence that those GitHub-level settings are active.
- At v1.7.2 preparation time the connected GitHub integration exposed no mutation action for rulesets/branch protection or About description/topics. Those controls remain to be applied and independently verified at the GitHub repository-setting layer.
- Tag/release creation is handled by the repository's own post-validation release workflow, so v1.7.0, v1.7.1, and v1.7.2 publication must be verified after the v1.7.2 merge.

## [1.7.1] - 2026-09-01

### Fixed
- FAST eligibility now requires a concrete proof path before mutation instead of relying on the subjective phrase "strong guidance".
- Added explicit "looks FAST but is not" negative examples for engineering, security/auth, network exposure, schema/migration, dependency, and unclear-root-cause cases.
- Repository validation now deterministically protects `SECURITY_AND_GOVERNANCE.md` headings and critical invariants.
- Repository validation now requires `.github/workflows/validate.yml` and verifies that CI still runs both the repository contract validator and installer regression suite.
- Added deterministic cross-contract checks linking security/workspace safety, work-mode routing, Codex/ChatGPT execution instructions, and CI.

### Added
- `docs/CHEAT_SHEET.md` as a one-page onboarding, work-mode, safe Codex handoff, and evidence-reuse reference.
- Optional workflow-efficiency sampling fields in `templates/POSTMORTEM.md` and `templates/EVIDENCE_PACKAGE.md` for selected tuning/pilot work.

### Changed
- Workflow/installer metadata updated to v1.7.1.
- Efficiency metrics remain explicitly optional so routine FAST work does not acquire new reporting ceremony.

## [1.7.0] - 2026-09-01

### Added
- `WORK_MODE_ROUTING.md` with explicit **FAST / STANDARD / STRICT** risk-based process modes.
- Common quality floor across all modes so FAST removes ceremony rather than correctness.
- Compact `templates/FAST_EXECUTION_PACKET.md` for eligible low-risk work.
- `WORKSPACE_SAFETY.md` defining the target project root as the default writable boundary and requiring explicit human approval for external/system mutations.
- Revision-bound evidence reuse rules to avoid repeating valid tests/reviews merely because a workflow stage changes.
- Installer-managed project-local workflow snapshot under `.engineering-workflow/`, including root router, work-mode/workspace-safety policies, core execution policies/templates, and focused `skills/*/SKILL.md`.
- Installer regression coverage for dangerous-target rejection, local workflow installation, symlink escape refusal, and project-root safety instructions.

### Changed
- Core routing now selects work mode before loading the rest of the workflow/skill set.
- FAST defaults to targeted inspect/validation/diff review/required CI without research, formal scrutiny, independent review, full repo reconstruction, or broad regression unless a trigger emerges.
- STANDARD preserves the normal bounded workflow; STRICT preserves full evidence-first controls for protected/high-impact work.
- Model tier and work mode are explicitly separate; STRICT does not automatically imply Sol.
- ChatGPT execution recommendations now include work mode, rationale, workspace write boundary, local policies/skills, model/effort/chat choice, evidence reuse, success gates, and stop/escalation conditions.
- Codex execution prompts now begin from the project-local `.engineering-workflow/SKILL.md` and enforce project-root-only default writes.
- Target repositories should be bootstrap-installed and validated before first Codex feature/fix execution.
- Installer metadata updated to v1.7.0 and hardened to reject filesystem-root, user-home, workflow-source, and managed symlink/junction escape targets while remaining stdlib-only and network-free.
- Existing project-owned file preservation and conflict-safe upgrade behavior remains intact.

### Safety note
- v1.7 does not authorize global package installation, modification of another repository, user/system configuration changes, or external filesystem writes for convenience. Such operations are STRICT and require explicit human approval for the exact action.

## [1.6.0] - 2026-08-30

### Added
- `CONTINUOUS_OPERATIONS.md` defining a tool-independent outer operational layer for recurring/event-driven work without replacing the core development workflow.
- A0-A3 autonomy model with A1 observe/report as the default starting level and an explicit human-owned ceiling for protected engineering/safety/security/legal/destructive decisions.
- `skills/loop-readiness/SKILL.md` with qualitative `READY FOR A1`, `READY FOR A2`, `READY FOR A3`, and `NOT READY` outcomes.
- `templates/LOOP_CONTRACT.md` for source of truth, operational state, action boundaries, budget/circuit breaker, notifications, human gates, observability, and pause/kill controls.
- `patterns/pr-ci-watcher.md` as the first A1 report-only reference pattern.
- Foundation adoption research at `docs/research/loop-engineering-adoption-review.md` with a `GO WITH CONDITIONS` verdict.

### Changed
- Root skill routing and core workflow now distinguish one-off development from optional continuous operations.
- Operational state is explicitly derived memory/cache/ledger and may not supersede live GitHub/project evidence; extra state is optional when the authoritative system already holds enough truth.
- Action-capable recurring loops require finite attempts/no-progress detection, explicit budgets/model ceilings, verification, human escalation, observability, and pause/kill behavior before higher autonomy is considered.
- Notification policy defaults to silence on no-op and suppression of unchanged duplicate findings.
- Multi-loop guidance now requires one action owner per item/branch, namespaced state, shared protected-area policy, and collision escalation without introducing a distributed locking runtime.
- ChatGPT Project Instructions, Quick Start, project setup guidance, skill system, installer reference/template set, and repository self-validation aligned to v1.6.0.
- Existing v1.5 research, scrutiny, independent-review, context, model-routing, security/governance, evidence, and human-approval authority remains unchanged.

### Attribution note
- `cobusgreyling/loop-engineering` (MIT License; Cobus Greyling and contributors) materially informed the foundation research around recurring work discovery, phased autonomy, operational state, circuit breakers, budgets, selective notifications, observability, and multi-loop coordination. See `ACKNOWLEDGEMENTS.md`. v1.6 policy/skill/pattern wording is independently written; the external CLI/plugin/harness is not embedded or required.

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
