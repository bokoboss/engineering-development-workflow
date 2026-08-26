# Skill System

The Engineering Development Workflow has one core workflow and a small set of reusable skill modules. Skills are focused reasoning/execution protocols that are activated by context; they do not replace the core workflow.

## 1. Relationship to the core workflow

The core remains:

`Understand -> Bound -> Route -> Execute -> Verify -> Audit -> Accept / Escalate`

Research is inserted conditionally before committing to a direction when material unknowns remain. Independent review is inserted conditionally before acceptance when a fresh second pass materially reduces risk.

Skills plug into that loop when a recurring situation needs a more specific procedure.

```text
Core workflow
   |
   +-- research-gate ------ resolve material feasibility/evidence unknowns
   +-- scrutinize --------- challenge readiness / risk / assumptions
   +-- systematic-debug --- diagnose defects from evidence
   +-- independent-review - obtain a fresh-context / cross-model second pass
   +-- postmortem --------- preserve lessons after significant fixes
   +-- technical-status --- turn raw execution output into a decision
   +-- long-task-guard ----- keep multi-step work bounded and resumable
```

The root `SKILL.md` is the router. Individual `skills/*/SKILL.md` files contain the focused procedure. `CONTEXT_MANAGEMENT.md` defines how to keep the active working set lean and when to use fresh or isolated context.

## 2. Skill routing

| Situation | Skill |
|---|---|
| Feasibility, current external evidence, new dependency/methodology, or material unknown blocks confident planning | `research-gate` |
| Check a plan, concept, architecture, risky change, or merge readiness | `scrutinize` |
| Bug, regression, CI/runtime failure, or unexplained behavior | `systematic-debug` |
| High-risk plan/implementation benefits from a materially fresh second pass | `independent-review` |
| Significant resolved defect/incident with reusable lessons | `postmortem` |
| Long agent report, mixed CI results, or "what is the real status?" | `technical-status` |
| Multi-step work, long execution, many gates, or resumable work | `long-task-guard` |

More than one skill may apply. Example: a new integration may use `research-gate`, then `scrutinize`; its implementation may later require `systematic-debug` and a risk-based `independent-review` before acceptance.

## 3. Mandatory scrutiny gates

`skills/scrutinize/SKILL.md` is mandatory unless explicitly documented as not applicable when:
- a major work package is about to start and the cost of a wrong direction is material;
- architecture, public interfaces, schemas, or core project structure will change materially;
- protected engineering, safety-critical, security-sensitive, or similarly high-impact behavior may change;
- a high-risk PR is being considered for merge;
- important acceptance decisions rely on incomplete or contradictory evidence.

Scrutiny should not become ceremony for trivial edits. Use it where a wrong decision has meaningful downstream cost.

Research and independent review are conditional rather than universally mandatory. Use the research gate when important unknowns would otherwise be converted into assumptions. Use independent review when executor blind spots or confirmation bias are material acceptance risks.

## 4. Skills and ChatGPT/Codex roles

Skills are primarily control-plane protocols. ChatGPT should execute as much of the skill as can be completed reliably from repository/GitHub/docs/evidence before sending implementation work to Codex.

Examples:
- ChatGPT can perform most research gating, scrutiny, technical-status translation, and GitHub-side independent review directly.
- ChatGPT can define a debugging reproducer/hypothesis plan; Codex may be needed to run local/runtime diagnostics and implement the fix.
- A fresh Codex session or different model may be used as an independent reviewer when the material evidence requires local repository execution.
- A postmortem should be assembled from verified GitHub/test evidence after the fix is accepted.
- Long-task guard governs both ChatGPT planning and Codex execution packets.

A stronger model is not automatically required for independent review. Fresh context at the same capable tier may be sufficient and cheaper. Escalate reviewer capability only when the review itself requires greater judgment.

## 5. Evidence discipline

A skill output does not override objective gates. Tests, CI, browser/runtime validation, real data, engineering references, independent verification, and required human approvals remain authoritative according to the project contract.

Skills must distinguish:
- verified fact;
- agent/user claim;
- inference;
- unknown or missing evidence.

Prefer deterministic enforcement over instruction-only compliance when a requirement can be reliably checked or blocked by tests, schemas, validators, settings, sandboxing, branch protection, or CI.

## 6. Progressive disclosure and skill structure

Keep a focused skill's `SKILL.md` as the concise trigger/procedure contract. When a skill needs reusable supporting material, add it beside the skill instead of bloating the root router or every context:

```text
skills/<skill>/
├── SKILL.md
├── references/   # optional deeper policy/domain material
├── examples/     # optional worked examples
├── scripts/      # optional deterministic helpers
└── templates/    # optional reusable outputs
```

Create supporting directories only when they earn their maintenance cost. Empty scaffolding does not improve the workflow.

Every focused skill contains a `## Gotchas` section as the standard place for recurring, high-signal failure modes learned from real use. If a new skill has no observed reusable Gotcha yet, state that explicitly rather than inventing generic filler. A Gotcha should prevent a repeated mistake or blind spot; one-off project facts do not belong there.

## 7. External inspiration and licensing

This skill system was informed by repeated project experience and study of public agent-development practices. `ACKNOWLEDGEMENTS.md` records material external influences and their licensing/provenance status.

In particular, `shanraisshan/claude-code-best-practice` materially informed the v1.5.0 discussion around conditional Research -> Plan -> Implement gating, fresh-context/cross-model review, context hygiene, progressive disclosure, task-specific workers, and deterministic guardrails. The source repository is MIT-licensed; the workflow-native policies and skill wording in this repository are independently written rather than copied wholesale.

Do not import third-party skill text into this repository unless its license is compatible and attribution/notice obligations are handled explicitly.