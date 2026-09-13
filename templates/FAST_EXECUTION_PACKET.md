# FAST Execution Packet

Use only when `WORK_MODE_ROUTING.md` FAST eligibility is satisfied.

## Routing
- Work mode: FAST
- Mode rationale:
- Mode confidence: high / medium
- Model:
- Reasoning effort:
- Ultra / multi-agent mode: Off
- Cost / quota rationale:
- Existing/new chat:

FAST should normally use a single lower-cost worker at the lowest effort expected to finish reliably. If Ultra, broad parallel-agent exploration, or a premium/high-effort route appears necessary, reassess FAST eligibility before execution rather than silently spending more compute.

## Workspace safety
- Target project root:
- Writable boundary: target project root only
- External writes approved: No
- Project-local workflow version:
- Required local policies: `.engineering-workflow/SKILL.md`, `.engineering-workflow/WORK_MODE_ROUTING.md`, `.engineering-workflow/WORKSPACE_SAFETY.md`

## Objective

## Scope
-

## Out of scope / protected behavior
-

## Relevant files / state to inspect
-

## Evidence reusable without rerun
-

## Targeted success gates
-

## Stop / escalate
Escalate to STANDARD/STRICT or reroute model/effort before continuing if:
- scope becomes materially cross-module;
- protected/security/safety/legal/destructive/system behavior appears;
- validation becomes weak or ambiguous;
- an external write/global change is required;
- root cause is not as bounded as expected;
- the selected model/effort is demonstrably insufficient;
- Ultra/multi-agent execution appears necessary.

## Completion report
- changed behavior/files;
- targeted validation;
- actual diff review result;
- required CI result if applicable;
- work-mode or model/effort escalation, if any;
- external writes: expected `none`;
- global/system changes: expected `none`.
