---
name: engineering-development-workflow
description: Plan, route, execute, verify, review, and hand off engineering-software development using explicit contracts, cost-aware model routing, focused reasoning skills, success gates, and evidence-first GitHub workflows.
---

# Engineering Development Workflow Skill

Use this skill for software-development planning, implementation handoff, repo review, UX/UI remediation, debugging, release qualification, technical-status review, long multi-step work, or agent orchestration where engineering correctness and auditability matter.

This file is the **router**. The core workflow remains authoritative; focused modules under `skills/` add procedures for recurring situations without creating separate competing workflows.

## Core router

1. Establish the authoritative project state from the repository and `PROJECT_PROFILE.md` if present.
2. Apply `ENGINEERING_DEV_WORKFLOW.md`.
3. Apply `MODEL_ROUTING_POLICY.md` before recommending a coding model or reasoning effort.
4. Route focused situations through the skill modules below.
5. Apply `UX_UI_WORKFLOW.md` when UX/UI changes are involved.
6. Apply `PARALLEL_EXECUTION.md` when multiple workers are proposed.
7. Define gates using `ACCEPTANCE_AND_EVIDENCE.md` and `templates/ACCEPTANCE_GATE.md`.
8. Produce or update an execution packet using `templates/EXECUTION_CONTRACT.md`.
9. Do not claim completion without the required evidence and approvals.

## Focused skill routing

- **Plan / concept / architecture / risky change / pre-merge challenge** -> `skills/scrutinize/SKILL.md`.
- **Bug / regression / failing CI / runtime or browser defect** -> `skills/systematic-debug/SKILL.md`, together with `DEBUGGING_PROTOCOL.md` where relevant.
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

## Control-plane rule

ChatGPT or the human lead should execute as much of these skills as can be completed reliably from repository/GitHub/docs/evidence before invoking Codex. Send only the remaining bounded execution work to the coding agent, with the relevant skill conclusions translated into scope, constraints, gates, and stop conditions.

Keep project-specific facts and protected engineering methodology in the target project, not in this shared skill.