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
                  ChatGPT final review
```

GitHub is the bridge. ChatGPT reads the shared workflow and target project through GitHub. Codex reads the same project contracts from its checkout and writes implementation evidence back through commits and PRs.

## 2. Create a ChatGPT Project

Create one ChatGPT Project for the software project you are developing. Keep the project focused on that repository/product so discussions, decisions, and project-specific context remain coherent.

Copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into the ChatGPT Project Instructions. Replace or append only genuinely project-specific context; do not copy the entire workflow policy into Project Instructions.

## 3. Bootstrap the target repository

In parallel with the ChatGPT Project setup, bootstrap the target GitHub repository using `scripts/setup_project.py` or ask Codex to perform the installation using `docs/installation.md`.

The repository bootstrap creates or establishes the contracts both sides can use, including `AGENTS.md`, `PROJECT_PROFILE.md`, a workflow reference, reusable execution templates, and the installation manifest.

## 4. Start work from ChatGPT

The normal starting point is ChatGPT, not Codex. A minimal first instruction is:

```text
Use our Engineering Development Workflow for this project. Inspect the current shared workflow repository and the target project repository, verify the project profile and current GitHub state, then determine the next development step. Complete everything that can be reliably done in ChatGPT before recommending Codex execution.
```

ChatGPT should then research, inspect, scrutinize, scope, define success gates, prepare execution contracts, and perform GitHub-side work before deciding whether an execution-plane agent is required.

## 5. Invoke Codex only when needed

When local code mutation, browser/runtime execution, environment-specific debugging, or other execution capabilities are required, ChatGPT prepares a bounded packet and recommends model + effort according to `MODEL_ROUTING_POLICY.md`.

Codex implements against the project repository and returns evidence through commits, PRs, tests, and CI. ChatGPT then reviews the actual evidence before acceptance.

## 6. Two-sided onboarding checklist

- ChatGPT Project created for the target software project.
- `CHATGPT_PROJECT_INSTRUCTIONS.md` copied into Project Instructions.
- Target repository bootstrapped and validated.
- `PROJECT_PROFILE.md` filled only from verified repository facts plus explicit project context.
- `AGENTS.md` contains project-specific permanent rules.
- Shared workflow repository remains the policy source of truth.
- New development work begins in ChatGPT control plane; Codex is invoked only when execution-plane capabilities are required.
