# Engineering Development Workflow

Version: 1.1.0

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

## 4. End-to-end loop

### Stage 0 — Establish state
- Confirm repository, branch, accepted baseline, dirty/local constraints, standard commands, protected behavior, and current objective.
- Inspect before modifying.

### Stage 1 — Understand and scrutinize
- Translate the request into user outcome and engineering behavior.
- Identify ambiguity, invariants, risks, affected contracts, and likely regressions.
- For architectural, methodology, safety-critical, or large changes, perform explicit scrutiny before implementation.

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
- Stop rather than silently expanding scope when a stop condition is reached.

### Stage 5 — Verify
Run the gates required by the change: targeted tests, regression suites, type/lint/build checks, package/runtime checks, browser/E2E, artifact comparison, numerical/reference equivalence, real-data validation, performance/security checks, or CI.

### Stage 6 — Audit and review
Review the actual diff and evidence against the Issue/contract, not merely the executor summary. Check scope containment, behavior, regression risk, documentation, UX, security, protected areas, and unresolved assumptions.

### Stage 7 — Diagnose failures
A failed attempt is not an automatic reason to use a stronger model.

Classify the failure:
- specification failure -> improve the packet;
- environment/tooling failure -> repair environment/tooling;
- scope discovery -> re-plan;
- integration conflict -> reconcile ownership/contracts;
- demonstrated capability limitation -> escalate model tier.

### Stage 8 — Accept, remediate, or block
Accept only when required gates pass and required approvals exist. Otherwise remediate or mark the work blocked with explicit missing evidence.

## 5. Completion semantics

Implementation exists != work complete.

A completion claim must identify:
- accepted commit/PR;
- gates executed and outcomes;
- exact CI status when CI is required;
- evidence for protected or engineering logic;
- known limitations and deferred items;
- human approvals still required.

## 6. Handoff

For a new chat, phase, or executor, use a compact authoritative handoff: repo, baseline, completed work, open issues, protected behavior, validation commands, current objective, recommended model/effort, and next success gates.

Use the existing chat when scope is continuous and context remains useful; start a new chat when context pollution, phase change, or excessive rereading would reduce reliability or cost efficiency.
