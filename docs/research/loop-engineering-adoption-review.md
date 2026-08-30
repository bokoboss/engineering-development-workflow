# Loop Engineering Adoption Review — Foundation Research for v1.6

Status: Research decision record  
Issue: #17  
Workflow baseline reviewed: v1.5.0 (`f9510c1a6df04bbb21293a4bbc72a958cbf39711`)  
External source reviewed: `cobusgreyling/loop-engineering` at `ffeb5a37d0a0d397bb7438609b1713da1c69f204` on 2026-08-30  
Research verdict: **GO WITH CONDITIONS**

## 1. Decision

The Engineering Development Workflow should add a **Continuous Operations Layer** in v1.6, but it should not import or depend on the Loop Engineering harness wholesale.

The new layer should sit **around** the existing v1.5 core development workflow:

```text
Continuous Operations Layer
  Observe / Discover
  -> Triage
  -> Decide whether action is justified
  -> Call the existing Engineering Development Workflow
  -> Persist operational outcome
  -> Wait / trigger again
```

The existing core remains authoritative for any actual development work:

```text
Research
-> Scrutinize
-> Bound / Plan
-> Execute
-> Verify
-> Independent Review
-> Accept / Remediate
```

This separation is important. Continuous operations should decide **when work deserves attention** and maintain operational continuity across runs. It must not create a second implementation, acceptance, or engineering-governance system.

## 2. Why this is a real capability gap

v1.5 already covers:
- research before uncertain implementation;
- scrutiny before high-impact work;
- bounded execution contracts;
- cost-aware model routing;
- task-specific workers and worktree isolation;
- deterministic verification;
- independent review;
- human approval for protected changes;
- context management and resumable handoffs.

What v1.5 does not yet formalize is the outer operational loop:
- discovering new work without a human starting the next chat;
- deciding whether a finding is actionable, ignorable, or waiting;
- remembering what a recurring watcher already saw or tried;
- preventing repeated automated attempts on the same failure;
- constraining repeated-agent cost over time;
- coordinating multiple recurring watchers;
- deciding when to notify the human rather than reporting every run;
- defining a safe progression from observation to assisted action.

Loop Engineering provides strong prior art specifically in these areas.

## 3. Source concepts reviewed

The review covered:
- `README.md`, `LOOP.md`, and `STATE.md`;
- `docs/concepts.md`;
- `docs/primitives.md`;
- `docs/loop-design-checklist.md`;
- `docs/operating-loops.md`;
- `docs/failure-modes.md`;
- `docs/anti-patterns.md`;
- `docs/safety.md`;
- `docs/multi-loop.md`;
- `docs/architecture-diagrams.md`;
- `docs/refactor.md`;
- `tools/loop-audit/README.md`;
- `starters/thin-loop/README.md`;
- `patterns/daily-triage.md`;
- `patterns/pr-babysitter.md`;
- `patterns/ci-sweeper.md`;
- `patterns/issue-triage.md`.

The source repository describes a loop as a system that discovers work, assigns or proposes action, verifies results, and persists state instead of requiring a person to type the next prompt. It also distinguishes a single-agent harness from the scheduled/stateful loop that operates harness runs over time.

## 4. Concept comparison

| Loop Engineering concept | Current v1.5 coverage | Decision |
|---|---|---|
| Discover / observe recurring work | Not formalized | **Adopt** |
| Triage before action | Partly covered by research/scrutiny, but not recurring operational triage | **Adopt** as separate operational step |
| Report-only first | Not formalized | **Adopt** |
| Autonomy levels | Not formalized | **Adapt** to our own risk model |
| Durable loop state | Handoffs/project state exist, but not recurring watcher state | **Adapt** |
| Maker/checker split | Independent review already covers it | **Already covered**; reuse existing rule |
| Worktree isolation | Already covered | **Already covered** |
| Hard retry/attempt cap | Stop conditions exist but not a loop-wide circuit breaker | **Adopt** |
| Daily/token budget | Cost-aware routing exists, but no recurring-operation budget | **Adopt** in tool-independent form |
| Kill/pause switch | Not formalized | **Adopt** |
| Selective notifications | Not formalized | **Adopt** |
| Run logging / observability | Evidence exists per task, not per recurring run | **Adapt** |
| Multi-loop collision control | Parallel execution covers one task, not recurring loops | **Adapt**, initially policy only |
| Least-privilege connectors | Security/governance already covers principle | **Already covered**, make operationally explicit |
| Path allowlist / denylist | Protected areas exist per task | **Adapt** for automated actions |
| Numeric readiness score | No equivalent | **Defer**; use deterministic readiness gates first |
| Mandatory `STATE.md` | No | **Reject as universal rule** |
| Product-specific `/loop`, `/goal`, Claude/Grok/OpenCode mechanics | No | **Reject from core** |
| Wholesale loop CLI / harness installation | No | **Reject** |
| Multi-agent patch consensus / swarm | No | **Defer**; not needed for first v1.6 scope |
| Auto-merge | No | **Reject for initial v1.6 pilot** |

## 5. Proposed continuous-operations architecture

```text
                       Human Owner
                           ^
                           | actionable escalation / approval
                           |
                +----------+-----------+
                | Continuous Operations|
                |       Layer          |
                +----------------------+
                | Observe / Discover   |
                | Triage               |
                | Autonomy Gate        |
                | Budget / Circuit     |
                | Operational State    |
                | Notification Policy  |
                +----------+-----------+
                           |
                 action justified?
                     /          \
                   no            yes
                   |              |
              record/exit         v
                         Engineering Development Workflow
                         Research when needed
                         -> Scrutinize
                         -> Bound
                         -> Route
                         -> Execute
                         -> Verify
                         -> Independent Review
                         -> Human/Acceptance Gate
                                  |
                                  v
                         operational outcome
                                  |
                                  +----> loop state / run log
```

Key rule: **the continuous layer may trigger the core workflow; it does not replace any core gate.**

## 6. Autonomy model to adopt

Use our own labels to avoid treating the external levels as a copied contract.

### A0 — Defined / inactive
The loop has a purpose, watched scope, triggers, and guardrails, but does not run automatically.

### A1 — Observe and report
The loop may:
- inspect authorized sources;
- classify findings;
- persist a compact operational result;
- notify only when the notification rule is satisfied.

It may not:
- edit code;
- change issue/PR state beyond explicitly allowlisted low-risk annotations;
- invoke an unattended coding remediation path;
- merge anything.

**New loops should start here.**

### A2 — Assisted action
The loop may perform narrowly bounded, reversible actions under an explicit allowlist, such as:
- prepare a branch/worktree;
- draft a minimal fix;
- run tests;
- open or update a PR;
- apply allowlisted labels/comments.

Requirements:
- independent verifier for code mutation;
- finite attempt cap;
- operational budget;
- human merge/acceptance unless a later explicit exception is approved;
- protected areas remain outside unattended action.

### A3 — Bounded unattended operation
Reserved for mature patterns whose signal quality, verifier, budget, rollback, observability, and allowlist have been demonstrated in real use.

A3 is **not** a goal for every loop. Some loops should remain A1 or A2 permanently.

### Engineering autonomy ceiling

Protected engineering methodology, safety-critical logic, security-sensitive behavior, destructive migrations, legal/regulatory interpretation, and other human-owned decisions:
- may be observed and escalated at A1;
- may enter A2 implementation only under an explicit human-authorized work item and existing core workflow gates;
- must never be autonomously accepted or merged merely because a loop/verifier passes;
- should not be eligible for generic A3 action.

## 7. State architecture

### 7.1 GitHub remains authoritative

The external source's own current `STATE.md` is derived from live open PRs/issues, which is the correct direction for us.

Our rule should be:

> Operational state is memory/cache/ledger, not project truth.

Authoritative facts continue to come from:
1. accepted repository state;
2. project contracts and decision records;
3. live Issues/PRs/checks/CI;
4. verified runtime evidence.

A loop must refresh live facts before acting on remembered state.

### 7.2 State is optional when the source already holds enough truth

The source repository's thin-loop starter intentionally uses GitHub issues and Action summaries without `STATE.md`. We should preserve this principle.

Do **not** require a state file merely to raise a readiness score.

State is warranted only when the loop needs memory not already represented reliably by the live system, such as:
- last action and outcome;
- attempt count;
- failure fingerprint;
- human override;
- notification already sent;
- cooldown / next eligible action;
- active ownership/lock;
- cross-run suppression of duplicate work.

### 7.3 Separate operational state by loop

Do not let several loops append arbitrary text into one shared file.

If durable state is required, use namespaced state or a pluggable backend. Exact storage should remain implementation-specific. The contract should define a minimum schema, not force Markdown.

Suggested logical fields:

```text
loop_id
last_run
watched_item_id
authoritative_revision/head_sha
last_observed_status
last_action
last_outcome
attempt_count
failure_fingerprint
human_override
notification_fingerprint
acting_owner
cooldown_until
next_action
```

### 7.4 Separate state from run history

Current state answers **what is true now**.

Append-only run history answers **what did the loop do and why**.

Do not overload one artifact with both jobs.

## 8. Budget and circuit-breaker policy

Recurring automation changes cost economics because even a cheap run becomes expensive at high cadence.

Each action-capable loop should define:
- cadence or event trigger;
- early-exit condition;
- maximum action attempts per item;
- no-progress / repeated-failure fingerprint;
- maximum worker spawns per run;
- maximum allowed model tier or escalation authority;
- daily/period budget in the units the execution platform can measure;
- maximum automatic PRs/actions per period where relevant;
- human approval required to raise a budget;
- pause and kill conditions.

Do not copy fixed token numbers or a universal three-attempt rule. The important contract is **finite and explicit**.

If no attempt/budget policy exists, the loop must remain A1 report-only.

### Circuit breaker

Before repeating an action, check:
1. Is this the same item/revision?
2. Is the observed failure materially the same?
3. Did the prior action make measurable progress?
4. Is the attempt cap still available?
5. Is the budget still available?
6. Has a human override or pause been recorded?

If the answer requires guessing, stop and escalate rather than retry.

Model escalation is not a substitute for a circuit breaker. A loop must not automatically walk Luna -> Terra -> Sol merely because it can.

## 9. Notification policy

Default: **silence on no-op**.

Notify the human only for a new actionable state such as:
- a required decision/approval;
- a new CI failure or materially changed failure;
- a PR newly blocked by review/merge conflict;
- required checks absent/unknown when the repository policy matters;
- an item ready for human merge/acceptance;
- attempt cap, budget, or circuit breaker reached;
- a protected/high-risk change detected;
- an operational loop incident.

For A1 overview loops, periodic digest mode is acceptable.

Repeated notification for the same unchanged finding should be suppressed unless an explicit aging/escalation threshold is reached.

## 10. Multi-loop coordination

v1.6 should define coordination rules even if the first implementation uses only one loop.

Minimum rules:
- one action owner per branch/PR/item at a time;
- report-only loops do not compete with action loops;
- action loops check for existing ownership before mutation;
- separate namespaced state;
- shared protected-area/denylist policy;
- aggregate budget awareness;
- explicit priority when two loops want the same item;
- human inbox for ambiguous ownership;
- integration still follows the core workflow.

Do not build a distributed locking framework in the first v1.6 increment. Start with policy and a minimal ownership field/guard.

## 11. Readiness gate for loops

We should create a future `loop-readiness` focused skill, but initially avoid a numeric 0–100 score.

A numeric score can become a target that rewards files-on-disk rather than proven operational quality. The source itself mitigates this by checking activity, but our first version should be simpler.

A loop readiness record should produce:
- `READY FOR A1`;
- `READY FOR A2`;
- `READY FOR A3`;
- `NOT READY`.

Required dimensions:
1. clear purpose and non-goals;
2. watched scope and trigger/cadence;
3. live source-of-truth definition;
4. state strategy and prune/refresh rule;
5. action allowlist / protected denylist;
6. verifier/independent-review strategy;
7. finite attempt cap and no-progress detection;
8. budget and model-escalation boundary;
9. human handoff destination and triggers;
10. notification policy;
11. observability/run history;
12. collision/ownership rule;
13. rollback/pause/kill mechanism;
14. least-privilege tool access;
15. success metrics and graduation criteria.

A3 should require evidence from actual A1/A2 operation, not documentation alone.

## 12. First pilot recommendation

### Pilot: PR/CI Watcher — A1 only

This is preferred over autonomous remediation as the first continuous-operations experiment.

#### Goal
Reduce manual checking of open PRs and CI while preserving human control.

#### Observe
- open project PRs;
- head SHA;
- CI/check status;
- required-check policy when known;
- review state / changes requested;
- merge conflict;
- relevant inactivity threshold.

#### Classify
- healthy / pending;
- new CI failure;
- checks absent or policy unknown;
- changes requested / blocked review;
- merge conflict;
- ready for human merge/review;
- stale / needs decision.

#### Action
At A1:
- no code edits;
- no automatic Codex remediation;
- no auto-merge;
- no automatic closure;
- report only new actionable findings.

#### State
Prefer live GitHub as the spine. Add a lightweight watcher ledger only if required for:
- duplicate notification suppression;
- aging;
- human override;
- failure fingerprint history.

#### Metrics for the first observation period
- actionable findings / total notifications;
- false-positive rate;
- duplicate-notification rate;
- mean time from new failure/blocker to human awareness;
- runs that exit with no action;
- cost per actionable finding;
- number of findings that would have caused an unsafe automated action if A2 had been enabled.

#### Graduation
Do not enable A2 until the A1 watcher demonstrates stable signal quality over a meaningful observation period and its failure modes are understood.

### Possible A2 follow-up
After A1 is proven, allow a very narrow CI-remediation path:
- only explicit failure classes;
- minimal patch in isolated branch/worktree;
- existing `systematic-debug` when root cause is unclear;
- independent verifier;
- finite attempts;
- human merge.

This is deliberately deferred from the foundation research PR.

## 13. Failure modes that must become v1.6 design inputs

The following source failure modes map directly to gaps we should explicitly design against:

| Failure mode | Our required mitigation |
|---|---|
| Infinite fix loop | finite attempt cap + no-progress fingerprint + escalation |
| State rot | refresh from live GitHub + prune resolved items |
| Verifier theater | existing independent-review + deterministic tests |
| Notification fatigue | actionable-only notifications + dedupe |
| Token/cost burn | cheap discovery pass + early exit + recurring budget |
| Over-reach | action allowlist + protected areas + smallest bounded work item |
| Comprehension debt | human review/summary for material changes; no volume metric as success |
| Cognitive surrender | human approval remains a design control |
| Parallel collision | one owner per item/branch + isolated worktrees |
| Escalation failure | explicit human inbox/notification on breaker trip |
| Flake fighting | classify infra/flake vs regression before code mutation |

## 14. Concepts intentionally not adopted as universal rules

Do not make the following part of the tool-independent v1.6 core:
- mandatory `STATE.md`;
- mandatory Markdown state;
- fixed polling intervals;
- fixed token budgets;
- fixed three-attempt rule;
- specific `/loop`, `/goal`, MCP, Claude, Grok, Codex, or OpenCode commands;
- mandatory numeric readiness scoring;
- automatic dependency upgrades;
- auto-merge;
- broad unattended refactoring;
- multi-agent consensus as a default;
- copying/installing the source repository's CLIs or plugin stack.

These can be implementation options or future experiments if evidence justifies them.

## 15. Licensing and provenance

Source: https://github.com/cobusgreyling/loop-engineering  
Reviewed revision: `ffeb5a37d0a0d397bb7438609b1713da1c69f204`  
License: MIT License  
Copyright notice in source: Copyright (c) 2026 Cobus Greyling and contributors.

This review uses the source as **conceptual inspiration and prior art**. No source file, CLI, skill, or substantial source text is embedded wholesale.

If a future implementation copies or materially adapts source code/text, the MIT copyright and permission notice must be preserved as required by that license.

## 16. Proposed v1.6 scope

If Issue #17 is accepted, open a separate implementation issue for v1.6 with only the following initial contract:

1. add a tool-independent Continuous Operations policy;
2. define A0-A3 autonomy levels and engineering autonomy ceilings;
3. define operational-state vs source-of-truth rules;
4. define recurring budget, circuit breaker, notification, pause/kill, and collision rules;
5. add a `loop-readiness` skill with qualitative readiness outcomes;
6. integrate the continuous layer into root routing without changing core acceptance authority;
7. add a reusable A1 PR/CI Watcher pattern/specification;
8. update templates only where needed to record loop autonomy, state, budget, and handoff boundaries;
9. preserve all v1.5 research/scrutiny/model/evidence/human-approval rules;
10. do **not** implement generic auto-remediation or auto-merge in this version.

## 17. Conditions attached to GO

The verdict is **GO WITH CONDITIONS**.

Before v1.6 can be accepted:

- The Continuous Operations Layer must remain subordinate to the existing core workflow.
- GitHub/project evidence remains authoritative; operational state is derived memory, never a competing source of truth.
- New patterns start at A1 unless an explicit adoption record justifies otherwise.
- A2/A3 require finite attempts, budget, verifier, action boundaries, observability, human escalation, and pause/kill controls.
- Protected engineering/safety/security/legal/destructive decisions retain mandatory human ownership.
- No automatic model-tier escalation beyond a loop's explicit budget/authority.
- No auto-merge in the initial PR/CI Watcher pilot.
- The first pilot is report-only PR/CI monitoring and must collect signal-quality/cost evidence before assisted action is enabled.
- External influence is credited in `ACKNOWLEDGEMENTS.md`.
- Any future copied/adapted source material preserves MIT requirements.

## 18. Research verdict

**GO WITH CONDITIONS**

The strongest idea to adopt is not “agents should run continuously.” It is:

> Recurring agent work becomes safe and useful only when discovery, state, verification, budget, bounded retries, selective human escalation, and operational observability are designed as first-class controls.

That outer operational discipline complements rather than replaces the Engineering Development Workflow. v1.6 should therefore add a small continuous-operations layer around the existing evidence-first core, prove it first with an A1 PR/CI Watcher, and expand autonomy only from measured evidence.
