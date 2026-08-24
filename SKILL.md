---
name: engineering-development-workflow
description: Plan, route, execute, verify, review, and hand off engineering-software development using explicit contracts, cost-aware model routing, success gates, and evidence-first GitHub workflows.
---

# Engineering Development Workflow Skill

Use this skill for software-development planning, implementation handoff, repo review, UX/UI remediation, debugging, release qualification, or agent orchestration where engineering correctness and auditability matter.

## Router

1. Establish the authoritative project state from the repository and `PROJECT_PROFILE.md` if present.
2. Apply `ENGINEERING_DEV_WORKFLOW.md`.
3. Apply `MODEL_ROUTING_POLICY.md` before recommending a coding model or reasoning effort.
4. If UX/UI changes are involved, apply `UX_UI_WORKFLOW.md`.
5. If a defect is involved, apply `DEBUGGING_PROTOCOL.md`.
6. For large or risky work, apply `REVIEW_AND_SCRUTINY.md` before implementation.
7. If multiple workers are proposed, apply `PARALLEL_EXECUTION.md`.
8. Define gates using `ACCEPTANCE_AND_EVIDENCE.md` and `templates/ACCEPTANCE_GATE.md`.
9. Produce or update an execution packet using `templates/EXECUTION_CONTRACT.md`.
10. Do not claim completion without the required evidence.

Keep project-specific facts and protected engineering methodology in the target project, not in this shared skill.
