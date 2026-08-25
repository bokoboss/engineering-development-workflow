# Skill System

The Engineering Development Workflow has one core workflow and a small set of reusable skill modules. Skills are focused reasoning/execution protocols that are activated by context; they do not replace the core workflow.

## 1. Relationship to the core workflow

The core remains:

`Understand -> Bound -> Route -> Execute -> Verify -> Audit -> Accept / Escalate`

Skills plug into that loop when a recurring situation needs a more specific procedure.

```text
Core workflow
   |
   +-- scrutinize -------- challenge readiness / risk / assumptions
   +-- systematic-debug -- diagnose defects from evidence
   +-- postmortem -------- preserve lessons after significant fixes
   +-- technical-status -- turn raw execution output into a decision
   +-- long-task-guard ---- keep multi-step work bounded and resumable
```

The root `SKILL.md` is the router. Individual `skills/*/SKILL.md` files contain the focused procedure.

## 2. Skill routing

| Situation | Skill |
|---|---|
| Check a plan, concept, architecture, risky change, or merge readiness | `scrutinize` |
| Bug, regression, CI/runtime failure, or unexplained behavior | `systematic-debug` |
| Significant resolved defect/incident with reusable lessons | `postmortem` |
| Long agent report, mixed CI results, or "what is the real status?" | `technical-status` |
| Multi-step work, long execution, many gates, or resumable work | `long-task-guard` |

More than one skill may apply. Example: a long phase blocked by a reproducible defect may use `long-task-guard` for the overall task and `systematic-debug` for the blocker.

## 3. Mandatory scrutiny gates

`skills/scrutinize/SKILL.md` is mandatory unless explicitly documented as not applicable when:
- a major work package is about to start and the cost of a wrong direction is material;
- architecture, public interfaces, schemas, or core project structure will change materially;
- protected engineering, safety-critical, security-sensitive, or similarly high-impact behavior may change;
- a high-risk PR is being considered for merge;
- important acceptance decisions rely on incomplete or contradictory evidence.

Scrutiny should not become ceremony for trivial edits. Use it where a wrong decision has meaningful downstream cost.

## 4. Skills and ChatGPT/Codex roles

Skills are primarily control-plane protocols. ChatGPT should execute as much of the skill as can be completed reliably from repository/GitHub/docs/evidence before sending implementation work to Codex.

Examples:
- ChatGPT can perform most scrutiny and technical-status translation directly.
- ChatGPT can define a debugging reproducer/hypothesis plan; Codex may be needed to run local/runtime diagnostics and implement the fix.
- A postmortem should be assembled from verified GitHub/test evidence after the fix is accepted.
- Long-task guard governs both ChatGPT planning and Codex execution packets.

## 5. Evidence discipline

A skill output does not override objective gates. Tests, CI, browser/runtime validation, real data, engineering references, and required human approvals remain authoritative according to the project contract.

Skills must distinguish:
- verified fact;
- agent/user claim;
- inference;
- unknown or missing evidence.

## 6. External inspiration and licensing

This skill system was informed by general lessons from using public agent-skill repositories and by repeated project experience. The skill modules in this repository are original workflow-native definitions and are licensed under Apache-2.0 with the rest of this repository.

Do not import third-party skill text into this repository unless its license is compatible and attribution/notice obligations are handled explicitly.