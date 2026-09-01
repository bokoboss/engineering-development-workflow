# ChatGPT Project Control-Plane Setup

## 1. The important distinction

Installing this workflow into a project repository does **not** install anything into ChatGPT. ChatGPT and Codex are separate execution contexts.

The intended architecture is:

```text
                    Shared Workflow Repo
        bokoboss/engineering-development-workflow
                  /                    \
                 /                      \
                v                        v
       ChatGPT Project             Target GitHub Repo
        control plane              shared project state
             |                           |
             |                           v
             |                         Codex
             |                    execution plane
             |                           |
             +--------- GitHub ----------+
                         |
                    PR / CI / Evidence
                         |
                         v
            Independent review when needed
                         |
                         v
                  ChatGPT final review
```

GitHub is the bridge and accepted shared source of truth. ChatGPT reads current upstream workflow policy and target project state through GitHub. Codex reads the project's **pinned local workflow snapshot** under `.engineering-workflow/` plus project contracts from its checkout, then writes implementation evidence back through commits and PRs.

## 2. Create a ChatGPT Project

Create one ChatGPT Project for the software project you are developing. Keep the project focused on that repository/product so discussions, decisions, and project-specific context remain coherent.

Copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into the ChatGPT Project Instructions. Replace or append only genuinely project-specific context; do not copy the entire workflow policy into Project Instructions.

The Project Instructions intentionally point back to the shared workflow. `CONTEXT_MANAGEMENT.md` and the root `SKILL.md` router should be read when relevant rather than duplicated permanently into the Project Instructions.

## 3. Bootstrap the target repository

In parallel with the ChatGPT Project setup, bootstrap the target GitHub repository using `scripts/setup_project.py` or ask Codex to perform the installation using `docs/installation.md`.

The repository bootstrap creates or establishes the contracts both sides can use, including `AGENTS.md`, `PROJECT_PROFILE.md`, reusable execution templates, the installation manifest, and an installer-managed `.engineering-workflow/` snapshot containing the root router, risk-mode policy, workspace-safety policy, core execution policies, templates, and focused skills.

## 4. Start work from ChatGPT and route FAST / STANDARD / STRICT

The normal starting point is ChatGPT, not Codex. A minimal first instruction is:

```text
Use our Engineering Development Workflow for this project. Inspect the current shared workflow repository and target project state, verify `.engineering-workflow.json` and the installed local workflow version, classify the next coding work as FAST / STANDARD / STRICT, enforce the project-root write boundary, and complete everything that can be reliably done in ChatGPT before recommending Codex execution. When Codex is needed, provide the work mode, rationale, model/effort/chat choice, required local policies/skills, success gates, evidence reuse, and stop/escalation conditions.
```

ChatGPT should then:
- apply `WORK_MODE_ROUTING.md` first and state FAST / STANDARD / STRICT;
- apply `WORKSPACE_SAFETY.md` and state the target project root as the default writable boundary;
- verify the project-local workflow snapshot before first Codex execution;
- establish a lean authoritative working context;
- apply the research gate when material feasibility/evidence unknowns remain;
- scrutinize high-impact plans and decisions;
- scope the work and define success gates;
- record whether independent review will be required for acceptance;
- when the request is recurring/event-driven, apply `CONTINUOUS_OPERATIONS.md` and assess loop readiness before enabling automation;
- prepare execution contracts and perform GitHub-side work before deciding whether an execution-plane agent is required.

## 5. Invoke Codex only when needed

When local code mutation, browser/runtime execution, environment-specific debugging, or other execution capabilities are required, ChatGPT prepares a mode-appropriate bounded packet and recommends model + effort according to `MODEL_ROUTING_POLICY.md`. Eligible FAST work uses the compact FAST packet; STANDARD/STRICT use the full contract when appropriate.

Codex must begin from `.engineering-workflow/SKILL.md`, read the local mode/workspace-safety policy, load only additional skills required by the selected mode, implement within the target project root, and return evidence through commits, PRs, tests, and CI. ChatGPT then reviews the actual evidence before acceptance.

For material risk, use `skills/independent-review/SKILL.md` to determine whether a fresh-context, different-model/agent, deterministic, or human second pass is warranted. Independent review does not automatically require a stronger model.

When the current conversation has become polluted by failed attempts, when a genuinely new task begins, or when a reviewer should not inherit executor anchoring, create a concise authoritative handoff and continue in fresh context according to `CONTEXT_MANAGEMENT.md`.

## 5A. Optional continuous operations

Continuous operations are optional and should not be configured merely because a scheduler exists. When recurring observation/triage is valuable, use the upstream `CONTINUOUS_OPERATIONS.md` contract and `skills/loop-readiness/SKILL.md`.

New loops default to A1 observe/report. Keep GitHub/project evidence authoritative, add operational state only when cross-run memory is actually needed, and define budget/circuit-breaker, notification, human handoff, observability, and pause/kill behavior before action-capable autonomy is considered.

## 6. Two-sided onboarding checklist

- ChatGPT Project created for the target software project.
- `CHATGPT_PROJECT_INSTRUCTIONS.md` copied into Project Instructions.
- Target repository bootstrapped and validated **before first Codex feature execution**.
- `.engineering-workflow/` local pinned router/policies/skills present and version recorded in `.engineering-workflow.json`.
- ChatGPT explicitly selects FAST / STANDARD / STRICT before coding-agent execution.
- Project-root-only write boundary is stated in Codex packets; any external/system mutation requires explicit human approval.
- `PROJECT_PROFILE.md` filled only from verified repository facts plus explicit project context.
- `AGENTS.md` contains project-specific permanent rules.
- Shared workflow repository remains the current control-plane policy source; the project-local snapshot is the pinned execution policy for Codex.
- Context is loaded progressively rather than copying the full workflow/skill library into every prompt.
- Material unknowns are researched before being converted into assumptions.
- High-risk acceptance records independent-review requirements when applicable.
- New development work begins in ChatGPT control plane; Codex is invoked only when execution-plane capabilities are required.
