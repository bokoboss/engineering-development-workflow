# Quick Start

For a one-page operational summary, see `docs/CHEAT_SHEET.md`.

## Recommended adoption path: two-sided setup

A complete adoption has **two sides**:

1. **ChatGPT Project control plane** — where state inspection, research, scrutiny, scoping, model routing, GitHub review, and acceptance decisions begin.
2. **Target repository bootstrap** — where `AGENTS.md`, `PROJECT_PROFILE.md`, reusable templates, and the installer-managed pinned `.engineering-workflow/` router/policy/skill snapshot live for Codex execution.

Installing the workflow into a repository does not install anything into ChatGPT. See `docs/chatgpt-project-setup.md` for the architecture and setup instructions.

## 1. Set up the ChatGPT Project

Create a ChatGPT Project for the software project. Copy `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into Project Instructions.

Keep those instructions concise. Do not copy the entire workflow or skill library into ChatGPT Project Instructions; the shared workflow repository remains the policy source of truth.

## 2. Bootstrap the target repository before Codex feature work

Use the safe bootstrap installer from an explicit checkout of this workflow repository:

```bash
python scripts/setup_project.py inspect /path/to/target-repo
python scripts/setup_project.py install /path/to/target-repo
python scripts/setup_project.py validate /path/to/target-repo
```

See `docs/installation.md` for Windows examples, upgrade behavior, ownership rules, workspace-safety guarantees, and a ready-to-use Codex installation prompt.

After installation, Codex can read `.engineering-workflow/SKILL.md`, `.engineering-workflow/WORK_MODE_ROUTING.md`, `.engineering-workflow/WORKSPACE_SAFETY.md`, and focused skills locally without network access.

## 3. Verify project-specific contracts

1. Inspect the actual target repository and fill `PROJECT_PROFILE.md` only from verified facts plus explicit project context.
2. Put project-specific permanent instructions in the project's `AGENTS.md`.
3. Identify protected behavior and required human approvals.
4. Verify current GitHub branch, accepted baseline, open Issues/PRs, CI, and known limitations.
5. Keep the active working context focused according to upstream `CONTEXT_MANAGEMENT.md`.

## 4. Start work from ChatGPT and choose the work mode

A minimal starting instruction is:

```text
Use our Engineering Development Workflow for this project. Inspect the current shared workflow repository and target project state, verify the installed local workflow snapshot, classify the next coding work as FAST / STANDARD / STRICT using WORK_MODE_ROUTING.md, enforce the target-project-root write boundary from WORKSPACE_SAFETY.md, then complete everything that can be reliably done in ChatGPT before recommending Codex execution. When Codex is needed, state the work mode, rationale, model, effort, chat choice, required local policies/skills, success gates, evidence that can be reused, and stop/escalation conditions.
```

ChatGPT should apply `WORK_MODE_ROUTING.md` before loading focused modules. FAST should normally load no focused skill unless a trigger emerges; STANDARD/STRICT load only those materially justified:
- `research-gate` when important feasibility/evidence unknowns block confident planning;
- `scrutinize` for plans, architecture, risk, and important readiness decisions;
- `systematic-debug` for defects and failing validation;
- `independent-review` for risk-based fresh-context/cross-model/human second passes;
- `postmortem` after significant resolved defects/incidents;
- `technical-status` for long or mixed technical evidence;
- `long-task-guard` for multi-step or resumable work;
- `loop-readiness` when a recurring/event-driven loop is being activated or its autonomy is increasing.

See `docs/skill-system.md` for routing and progressive-disclosure rules.

## Optional: continuous operations

Most projects do **not** need recurring automation on day one. When a project benefits from scheduled/event-driven observation, read `CONTINUOUS_OPERATIONS.md` and create a `templates/LOOP_CONTRACT.md` only for that loop.

Start new loop patterns at **A1 observe/report** unless a reviewed readiness record supports otherwise. Use `skills/loop-readiness/SKILL.md` before activation or autonomy increases. GitHub/project evidence remains authoritative; operational state is optional derived memory, not a second source of truth.

The v1.6 reference pilot is `patterns/pr-ci-watcher.md`, intentionally A1/report-only with no code mutation, automatic Codex remediation, close, or merge.

## 5. Invoke Codex only when execution-plane capabilities are required

When code/file mutation, local runtime/browser execution, or environment-specific debugging is materially required:

1. Verify `.engineering-workflow.json` and the local pinned snapshot. Install/upgrade/validate first if missing or materially incompatible.
2. State FAST / STANDARD / STRICT and the target project root write boundary.
3. Use `docs/development/templates/FAST_EXECUTION_PACKET.md` for eligible FAST work; otherwise create a GitHub Issue or fill `docs/development/templates/EXECUTION_CONTRACT.md`.
4. Record any research verdict/conditions and independent-review requirement.
5. Translate relevant conclusions into scope, constraints, success gates, stop conditions, evidence reuse, and the coding-agent prompt.
6. Use upstream `MODEL_ROUTING_POLICY.md` to choose model + effort + chat reuse/new-chat strategy.
7. Tell Codex to begin from `.engineering-workflow/SKILL.md` and obey `.engineering-workflow/WORKSPACE_SAFETY.md`.
8. Execute in an isolated branch/worktree where appropriate, without writes outside the approved project root.
9. Return implementation evidence through commits, PRs, tests, CI, artifacts, and other required validation.
10. Prefer deterministic enforcement over prompt-only instructions where tests/validators/settings/CI can reliably enforce the requirement.
11. Reuse valid revision-bound evidence rather than rerunning broad checks mechanically.
12. Perform independent review when the acceptance risk justifies it; FAST does not require it by default.
13. Have ChatGPT review actual diff + evidence before merge/acceptance.
14. Update `PROJECT_PROFILE.md` and handoff when the accepted baseline changes.

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

The installer refuses to overwrite a managed file that has been modified locally. It also rejects dangerous targets and managed symlink/junction escape paths. ChatGPT Project Instructions do not need the full workflow copied into the Project Instructions; Codex uses the pinned `.engineering-workflow/` snapshot inside the target repo.

## Minimal adoption

For a small repository, FAST mode keeps day-to-day work lightweight, but bootstrap/validate the local workflow first when Codex will execute changes. Start with:
- a ChatGPT Project using `templates/CHATGPT_PROJECT_INSTRUCTIONS.md`;
- `AGENTS.md`;
- `PROJECT_PROFILE.md`;
- an Issue with scope/out-of-scope/success gates;
- PR evidence.

Add research, focused skills, independent review, and additional templates only when they reduce real ambiguity, risk, or verification burden. Manual repository adoption remains valid when Python is unavailable.
