# Changelog

All notable changes to the workflow contract are documented here. Semantic Versioning is used for the workflow itself.

## [Unreleased]

### Added
- Apache License 2.0 (`Apache-2.0`) as the repository redistribution license.
- `NOTICE` attribution file.

### Changed
- README now documents the public reuse and redistribution terms explicitly.
- Repository validation now requires `LICENSE` and `NOTICE`.

### Pending
- Collect external feedback after real project adoption.

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
