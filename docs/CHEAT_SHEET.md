# Engineering Development Workflow Cheat Sheet

Use this page when you need the shortest safe path through the workflow.

## New project

1. Create the ChatGPT Project and use `templates/CHATGPT_PROJECT_INSTRUCTIONS.md`.
2. Bootstrap the target repository **before first Codex feature/fix work**:
   ```bash
   python scripts/setup_project.py inspect /path/to/project
   python scripts/setup_project.py install /path/to/project
   python scripts/setup_project.py validate /path/to/project
   ```
3. Fill `PROJECT_PROFILE.md` from verified repository facts.
4. Put permanent project-specific rules in `AGENTS.md`.
5. Start the task from ChatGPT.
6. ChatGPT chooses **FAST / STANDARD / STRICT**.
7. Codex reads the local pinned workflow beginning at `.engineering-workflow/SKILL.md`.
8. Codex obeys `.engineering-workflow/WORKSPACE_SAFETY.md`.
9. Validate, review the actual diff/evidence, then accept or remediate.

## Which work mode?

| Situation | Mode |
|---|---|
| Typo, tiny UI polish, bounded low-risk fix with a reliable proof path | **FAST** |
| Ordinary feature, multi-file bug, moderate refactor/integration | **STANDARD** |
| Engineering formula/methodology, security/auth/privacy, migration, architecture/schema/public contract, legal/regulatory, system/global/external write, high-impact uncertainty | **STRICT** |

### FAST requires proof

Before choosing FAST, answer:

> **How will we prove this exact change is correct?**

FAST needs at least one concrete proof path before mutation:
- reliable reproducer;
- existing test directly exercising the behavior; or
- deterministic before/after check.

If confidence is low, use STANDARD.

Do not classify by line count. A one-line engineering/security/schema change may still be STRICT.

## Codex handoff minimum

Before Codex execution, state:

```text
Work mode:
Mode rationale:
Mode confidence:
Target project root:
Workspace write boundary: target project root only
External writes approved: No, unless explicitly approved
Required local policies/skills:
Model:
Reasoning effort:
Existing/new chat:
Scope:
Evidence that can be reused:
Success gates:
Stop/escalation conditions:
```

## Workspace safety

Default writable boundary:

> **the target project root only**

Without explicit human approval, do not:
- write into another repository or directory;
- alter the workflow source checkout;
- change user/system/global configuration;
- install packages/tools globally;
- create persistent external staging/work folders;
- use destructive cleanup/reset commands that may remove user work.

If an external/system write appears necessary, stop first and report the exact resource, mutation, reason, safer project-local alternative, and rollback.

## FAST path

```text
focused inspect
-> compact FAST packet
-> bounded change
-> targeted validation
-> actual diff review
-> required CI
-> accept / remediate
```

Do not add research, scrutiny, broad regression, or independent review unless a trigger emerges.

## STANDARD path

```text
inspect
-> scope
-> conditional research/scrutiny
-> execute
-> targeted + relevant regression validation
-> PR/CI
-> ChatGPT review
-> accept / remediate
```

## STRICT path

Use the full evidence-first workflow with the risk controls justified by the task:
- research where material unknowns remain;
- scrutiny;
- explicit execution contract;
- protected/human approval gates;
- stronger validation;
- risk-appropriate independent review.

STRICT does not automatically mean the most expensive model.

## Evidence reuse

Reuse valid evidence when:
- the relevant revision/input is unchanged;
- the environment/toolchain is materially unchanged;
- the evidence still covers the risk.

Re-run when evidence is stale, invalidated, incomplete, or repository policy requires a fresh run.

## Optional efficiency sampling

For workflow tuning or postmortems, optionally record:
- work mode;
- executor model/effort;
- execution attempts;
- validation reruns;
- mode escalation;
- approximate execution duration when available;
- blocked/wasted attempt and reason.

Do **not** make these metrics mandatory for routine FAST work.
