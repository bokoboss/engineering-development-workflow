# Quick Start

## Recommended adoption path: two-sided setup

A complete adoption has **two sides**:

1. **ChatGPT Project control plane** — where state inspection, research, scrutiny, scoping, model routing, GitHub review, and acceptance decisions begin.
2. **Target repository bootstrap** — where `AGENTS.md`, `PROJECT_PROFILE.md`, reusable templates, and installer-managed workflow references live for ChatGPT and Codex to share through GitHub.

Installing the workflow into a repository does not install anything into ChatGPT. See `docs/chatgpt-project-setup.md` for the architecture and setup instructions.

## 1. Set up the ChatGPT Project

Create a ChatGPT Project for the software project. Copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into Project Instructions.

Keep those instructions concise. Do not copy the entire workflow or skill library into ChatGPT Project Instructions; the shared workflow repository remains the policy source of truth.

## 2. Bootstrap the target repository

Use the safe bootstrap installer from an explicit checkout of this workflow repository:

```bash
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py install /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

See `docs/installation.md` for Windows examples, upgrade behavior, ownership rules, and a ready-to-use Codex installation prompt.

## 3. Verify project-specific contracts

1. Inspect the actual target repository and fill `PROJECT_PROFILE.md` only from verified facts plus explicit project context.
2. Put project-specific permanent instructions in the project's `AGENTS.md`.
3. Identify protected behavior and required human approvals.
4. Verify current GitHub branch, accepted baseline, open Issues/PRs, CI, and known limitations.
5. Keep the active working context focused according to upstream `CONTEXT_MANAGEMENT.md`.

## 4. Start work from ChatGPT and route the situation

A minimal starting instruction is:

```text
Use our Engineering Development Workflow for this project. Inspect the current shared workflow repository and the target project repository, verify the project profile and current GitHub state, apply the upstream context and skill router where relevant, then determine the next development step. Complete everything that can be reliably done in ChatGPT before recommending Codex execution.
```

ChatGPT should read the root `SKILL.md` router and apply focused modules only when materially useful:
- `research-gate` when important feasibility/evidence unknowns block confident planning;
- `scrutinize` for plans, architecture, risk, and important readiness decisions;
- `systematic-debug` for defects and failing validation;
- `independent-review` for risk-based fresh-context/cross-model/human second passes;
- `postmortem` after significant resolved defects/incidents;
- `technical-status` for long or mixed technical evidence;
- `long-task-guard` for multi-step or resumable work.

See `docs/skill-system.md` for routing and progressive-disclosure rules.

## 5. Invoke Codex only when execution-plane capabilities are required

When code/file mutation, local runtime/browser execution, or environment-specific debugging is materially required:

1. Create a GitHub Issue or fill `docs/development/templates/EXECUTION_CONTRACT.md`.
2. Record any research verdict/conditions and independent-review requirement.
3. Translate relevant skill conclusions into scope, constraints, success gates, stop conditions, and the coding-agent prompt.
4. Use upstream `MODEL_ROUTING_POLICY.md` to choose model + effort + chat reuse/new-chat strategy.
5. Execute in an isolated branch/worktree where appropriate.
6. Return implementation evidence through commits, PRs, tests, CI, artifacts, and other required validation.
7. Prefer deterministic enforcement over prompt-only instructions where tests/validators/settings/CI can reliably enforce the requirement.
8. Perform independent review when the acceptance risk justifies it; a fresh context at the same tier may be enough.
9. Have ChatGPT review actual diff + evidence before merge/acceptance.
10. Update `PROJECT_PROFILE.md` and handoff when the accepted baseline changes.

## Context and handoffs

Use the current chat when the objective is continuous and recent reasoning is still useful. Create a concise authoritative handoff and a fresh context when:
- a genuinely new task starts;
- a major phase/responsibility changes;
- failed attempts or irrelevant history are polluting reasoning;
- independent review should be separated from executor reasoning;
- a high-stakes next step benefits from a controlled working set.

Do not use fixed context percentages as universal law; product-specific mechanisms belong in product-specific guidance.

## Upgrading the repository scaffold

Update the workflow checkout to the revision you want, then run:

```bash
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py upgrade /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

The installer refuses to overwrite a managed file that has been modified locally. ChatGPT Project Instructions do not need the full workflow copied again; they continue to point to the shared workflow source of truth.

## Minimal adoption

For a small repository, start with:
- a ChatGPT Project using `templates/CHATGPT_PROJECT_INSTRUCTIONS.md`;
- `AGENTS.md`;
- `PROJECT_PROFILE.md`;
- an Issue with scope/out-of-scope/success gates;
- PR evidence.

Add research, focused skills, independent review, and additional templates only when they reduce real ambiguity, risk, or verification burden. Manual repository adoption remains valid when Python is unavailable.
