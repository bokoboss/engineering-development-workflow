# Engineering Development Workflow

Version: 1.4.1

## 1. Purpose

Provide a reusable control system for software work where correctness, auditability, cost, regression risk, engineering judgment, and real-world usability matter.

## 2. Roles

### Human owner
Owns product intent, high-impact trade-offs, protected engineering decisions, safety/security approvals, and final acceptance where required.

### ChatGPT / control-plane lead
Do as much non-environment-dependent work as possible before coding execution: research, repository/GitHub inspection, requirements clarification, decomposition, architecture/UX reasoning, scrutiny, acceptance criteria, test planning, prompt preparation, PR/diff/CI review, and final synthesis.

### Coding agent / executor
Make bounded changes in the real repository/environment, run tests, inspect runtime/browser behavior, produce artifacts, and return evidence.

### Optional coding-agent orchestrator
Used only when execution itself is complex enough to justify an intelligent in-repo coordinator. It should delegate bounded work rather than consume premium capacity on routine bulk implementation.

## 3. Source of truth

Use this precedence unless a project explicitly overrides it:

1. Repository state and accepted commit/branch.
2. Project `AGENTS.md`, `PROJECT_PROFILE.md`, PRD/architecture/decision records.
3. Current Issue / execution contract.
4. Verified CI/test/runtime evidence.
5. Conversation history and memory as convenience, not authoritative project state.

When chat context is long, stale, or missing, reconstruct from Git/GitHub and project documents rather than guessing.

## 4. Focused skills

The core workflow remains authoritative. Use root `SKILL.md` to route recurring situations into the focused modules under `skills/`.

- `skills/scrutinize/SKILL.md` — challenge assumptions, plans, risky changes, and merge/acceptance readiness.
- `skills/systematic-debug/SKILL.md` — reproduce defects, isolate root cause, fix narrowly, and prove regression safety.
- `skills/postmortem/SKILL.md` — preserve reusable lessons after significant resolved defects or incidents.
- `skills/technical-status/SKILL.md` — translate long or mixed technical output into verified status and next action.
- `skills/long-task-guard/SKILL.md` — keep multi-step work bounded, observable, resumable, and resistant to scope drift.

Scrutiny is a required gate unless explicitly documented as not applicable for material architecture/interface/schema changes, protected engineering or safety/security-sensitive logic, major high-cost work packages, high-risk pre-merge decisions, and important acceptance decisions based on incomplete or contradictory evidence.

Skills refine a stage; they do not override project contracts, evidence requirements, model-routing rules, or human approvals.

## 5. End-to-end loop

### Stage 0 — Establish state
- Confirm repository, branch, accepted baseline, dirty/local constraints, standard commands, protected behavior, and current objective.
- Inspect before modifying.
- For long or multi-step work, use `long-task-guard` to establish checkpoints and stop conditions.

### Stage 1 — Understand and scrutinize
- Translate the request into user outcome and engineering behavior.
- Identify ambiguity, invariants, risks, affected contracts, and likely regressions.
- Route through `scrutinize` when required by the mandatory gate or when a plan/decision needs adversarial review.

### Stage 2 — Bound the work
Create an execution contract containing objective, scope, out-of-scope, constraints, protected areas, likely modules, dependencies, success gates, validation, stop conditions, and definition of done.

Prefer one coherent phase/PR when the work is related and still reviewable. Split only when scope, risk, dependency, ownership, or reviewability justifies it.

### Stage 3 — Route execution
Use `MODEL_ROUTING_POLICY.md`.

Default principle: **cheapest model that can reliably finish the bounded task**.

Do not use a premium model to compensate for a vague packet that ChatGPT or the human lead could improve first.

### Stage 4 — Execute
- Work on an isolated branch/worktree when appropriate.
- Preserve existing contracts unless explicitly authorized.
- Fix root cause before polish or unrelated cleanup.
- Add or update tests with the implementation.
- For long execution, use `long-task-guard` checkpoints to preserve state and scope.
- Stop rather than silently expanding scope when a stop condition is reached.

### Stage 5 — Verify
Run the gates required by the change: targeted tests, regression suites, type/lint/build checks, package/runtime checks, browser/E2E, artifact comparison, numerical/reference equivalence, real-data validation, performance/security checks, or CI.

### Stage 6 — Audit and review
Review the actual diff and evidence against the Issue/contract, not merely the executor summary. Check scope containment, behavior, regression risk, documentation, UX, security, protected areas, and unresolved assumptions.

Use `technical-status` when evidence is spread across long logs, executor reports, CI, PRs, or multiple attempts. Use `scrutinize` again for high-risk pre-merge/acceptance decisions.

### Stage 7 — Diagnose failures
A failed attempt is not an automatic reason to use a stronger model.

For defects, regressions, CI failures, or runtime failures, route through `systematic-debug`.

Classify the failure:
- specification failure -> improve the packet;
- environment/tooling failure -> repair environment/tooling;
- scope discovery -> re-plan;
- integration conflict -> reconcile ownership/contracts;
- demonstrated capability limitation -> escalate model tier.

### Stage 8 — Accept, remediate, or block
Accept only when required gates pass and required approvals exist. Otherwise remediate or mark the work blocked with explicit missing evidence.

For significant resolved defects/incidents with reusable lessons, run `postmortem` after acceptance/closure. Do not use postmortem as a substitute for unresolved debugging.

## 6. Completion semantics

Implementation exists != work complete.

A completion claim must identify:
- accepted commit/PR;
- gates executed and outcomes;
- exact CI status when CI is required;
- evidence for protected or engineering logic;
- known limitations and deferred items;
- human approvals still required.

## 7. Handoff

For a new chat, phase, or executor, use a compact authoritative handoff: repo, baseline, completed work, open issues, protected behavior, validation commands, current objective, recommended model/effort, and next success gates.

For long work, preserve the latest checkpoint and unresolved blockers so a new chat/executor can resume without reconstructing from prose history alone.

Use the existing chat when scope is continuous and context remains useful; start a new chat when context pollution, phase change, or excessive rereading would reduce reliability or cost efficiency.
