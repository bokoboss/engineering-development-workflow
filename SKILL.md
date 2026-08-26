---
name: engineering-development-workflow
description: Research, scrutinize, plan, route, execute, verify, independently review, accept, and hand off engineering-software development using explicit contracts, lean context, cost-aware model routing, focused skills, and evidence-first GitHub workflows.
---

# Engineering Development Workflow Skill

Use this skill for software-development planning, feasibility research, implementation handoff, repo review, UX/UI remediation, debugging, release qualification, technical-status review, long multi-step work, independent verification, or agent orchestration where engineering correctness and auditability matter.

This file is the **router**. The core workflow remains authoritative; focused modules under `skills/` add procedures for recurring situations without creating separate competing workflows.

## Core router

1. Establish the authoritative project state from the repository and `PROJECT_PROFILE.md` if present.
2. Apply `ENGINEERING_DEV_WORKFLOW.md`.
3. Apply `CONTEXT_MANAGEMENT.md` to keep the working set relevant and decide when fresh context or isolation is useful.
4. Apply `MODEL_ROUTING_POLICY.md` before recommending a coding model or reasoning effort.
5. Route focused situations through the skill modules below.
6. Apply `UX_UI_WORKFLOW.md` when UX/UI changes are involved.
7. Apply `PARALLEL_EXECUTION.md` when multiple workers are proposed.
8. Define gates using `ACCEPTANCE_AND_EVIDENCE.md` and `templates/ACCEPTANCE_GATE.md`.
9. Produce or update an execution packet using `templates/EXECUTION_CONTRACT.md`.
10. Do not claim completion without the required evidence, review, and approvals.

## Focused skill routing

- **Material unknown / feasibility / new dependency / methodology / external evidence needed before planning** -> `skills/research-gate/SKILL.md`.
- **Plan / concept / architecture / risky change / pre-merge challenge** -> `skills/scrutinize/SKILL.md`.
- **Bug / regression / failing CI / runtime or browser defect** -> `skills/systematic-debug/SKILL.md`, together with `DEBUGGING_PROTOCOL.md` where relevant.
- **Material plan/implementation needs a fresh-context or cross-model second pass** -> `skills/independent-review/SKILL.md`.
- **Significant fixed defect or incident with reusable lessons** -> `skills/postmortem/SKILL.md`.
- **Long agent report / mixed gates / "what is actually done?"** -> `skills/technical-status/SKILL.md`.
- **Long, multi-step, resumable, or multi-worker execution** -> `skills/long-task-guard/SKILL.md`.

Multiple modules may apply to one work item. Use the smallest set that materially improves correctness or control.

## Mandatory scrutiny

Apply `skills/scrutinize/SKILL.md` as a required gate unless explicitly documented as not applicable for:
- material architecture/interface/schema changes;
- protected engineering, safety-critical, security-sensitive, or similarly high-impact logic;
- major work packages where a wrong direction has material cost;
- high-risk PRs before merge;
- important acceptance decisions based on incomplete or contradictory evidence.

Do not turn scrutiny into ceremony for trivial edits.

## Independent review

Use `skills/independent-review/SKILL.md` when a materially independent second pass is justified by risk. High-risk acceptance should not rely solely on the executor's own narrative or review.

Independence may be provided by a fresh context using the same model tier, a different model/agent, deterministic recomputation or end-to-end verification, a human specialist, or an appropriate combination. Do not escalate to a premium model merely to satisfy the word "independent"; choose the cheapest reviewer that can reliably challenge the material risk.

## Progressive disclosure

Load only the policies, skills, references, examples, scripts, and evidence needed for the current decision or task. A focused skill may grow through `references/`, `examples/`, `scripts/`, or `templates/` beside its `SKILL.md`; do not inflate the root router or every working context with optional material.

Use `## Gotchas` in focused skills for recurring, high-signal failure modes learned from real use. Keep project-specific one-off lessons in the target project instead.

## Control-plane rule

ChatGPT or the human lead should execute as much of these skills as can be completed reliably from repository/GitHub/docs/evidence before invoking Codex. Send only the remaining bounded execution work to the coding agent, with relevant research, scrutiny, context, and review conclusions translated into scope, constraints, gates, and stop conditions.

Keep project-specific facts and protected engineering methodology in the target project, not in this shared skill.