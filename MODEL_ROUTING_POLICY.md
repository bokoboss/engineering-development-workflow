# Model Routing Policy

Version: 1.2.0

## 1. Objective

Minimize **cost to verified completion**, not merely token count, model price, or number of attempts.

Model capability and reasoning effort are separate routing axes.

## 2. Control-plane rule

Before invoking a coding agent, ChatGPT or the human lead should complete as much research, repo inspection, decomposition, architecture/UX reasoning, acceptance design, and prompt preparation as practical. This converts ambiguous work into bounded execution packets and increases the share of work that lower-cost models can complete reliably.

## 2A. Work mode first

Apply `WORK_MODE_ROUTING.md` before model selection.

Work mode and model tier are separate axes:
- FAST often fits Luna Medium, or Luna High for a slightly broader but still low-risk bounded change;
- STANDARD often fits Luna High/Max;
- STRICT does not automatically require Sol. After ChatGPT has completed high-risk reasoning and bounded the implementation, a lower-cost executor may still be appropriate if the execution itself is mechanical and strongly testable.

Do not use a stronger model as a substitute for scrutiny, evidence, workspace safety, or a clear packet.

## 3. Default routing

Current profile as of 2026-08-24; model availability and economics can change and should be re-verified periodically.

- **Luna Medium** — small, direct, patterned work with strong tests and low ambiguity.
- **Luna High** — multi-file implementation with clear boundaries and established contracts.
- **Luna Max** — difficult or long execution that is well specified, testable, and bounded; preferred before automatic escalation when increased reasoning within Luna is economically sensible.
- **Terra High/Max** — middle-tier escalation for tasks requiring materially more judgment, cross-module synthesis, or when repeated Luna attempts would likely cost more than a stronger worker.
- **Sol High/Max** — reserve for ambiguous architecture, unknown-root-cause investigation, conflicting contracts, major migrations, high-risk engineering/security/safety logic, final adjudication, or other tasks where premium capability materially reduces failure risk.

Do not assume `Sol Low` is more cost-effective than `Luna Max`; model tier and effort must be evaluated separately.

## 4. Luna-first principle

For bounded implementation, refactoring with preserved contracts, test creation/repair, UI implementation against a clear UX specification, and debugging with a reliable reproducer, consider Luna first.

The strongest default pattern is often:

`ChatGPT plans -> Luna executes -> tests/CI produce evidence -> ChatGPT reviews`

## 5. Escalation

Use:

`Luna -> diagnose -> Terra -> Sol`

not:

`Luna failed -> Sol immediately`.

Escalate only after determining that the problem is a capability limitation rather than a weak specification, broken environment, undiscovered dependency, or integration mistake.

## 6. Orchestrated execution

Use a premium orchestrator only when in-repository coordination itself is complex enough to justify it.

A useful pattern for large parallelizable work is:

`ChatGPT control plane -> Sol technical orchestrator -> bounded Luna workers -> Sol integration verification -> CI/evidence -> ChatGPT final review`

Sol should orchestrate and adjudicate rather than spend premium capacity on routine edits that workers can perform.

## 7. Retry economics

Choose the route expected to minimize total verified cost including:
- initial execution;
- context rereads;
- retries;
- failed CI;
- merge conflict/reconciliation;
- human review;
- remediation.

A cheaper worker that requires many retries can be more expensive than a stronger worker used once.

## 8. Recommendation format

Whenever recommending Codex/coding-agent execution, state:
- work mode (FAST / STANDARD / STRICT) and rationale;
- workspace write boundary and whether any external write is explicitly approved;
- model;
- reasoning effort;
- existing chat or new chat;
- why this tier is sufficient;
- why a higher tier is not currently required;
- explicit escalation trigger, including work-mode escalation when scope/risk grows.
