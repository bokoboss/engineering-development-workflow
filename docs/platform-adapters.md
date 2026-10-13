# Platform Adapters

The workflow defines two roles, not two products:

- **Control plane** — research, scoping, work-mode routing, packet preparation, diff/CI review, and acceptance.
- **Execution plane** — bounded changes in the real repository, tests, runtime/browser checks, and evidence.

Any capable assistant can fill either role. The policies say "ChatGPT" and "Codex" because that was the first supported pairing; read them as *control plane* and *executor* respectively. The rules, gates, and stop conditions are identical on every platform.

## Role mapping

| Role | OpenAI | Anthropic |
|---|---|---|
| Control plane | ChatGPT Project | Claude Project (claude.ai) |
| Control-plane instructions | `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` | same template (see below) |
| Executor | Codex | Claude Code |
| Executor entry file | `AGENTS.md` | `CLAUDE.md` → imports `AGENTS.md` |
| Executor skills | `.engineering-workflow/skills/` via the router | `.claude/skills/` wrappers → `.engineering-workflow/skills/` |
| Model profile | `MODEL_ROUTING_POLICY.md` §3 | `MODEL_ROUTING_POLICY.md` §3C |

Mixed pairings are allowed (for example a Claude Project control plane reviewing Codex output, or a ChatGPT control plane handing off to Claude Code). Independent review across vendors is a valid way to obtain independence under `skills/independent-review/SKILL.md`.

## Claude Project control plane

Paste `templates/CHATGPT_PROJECT_INSTRUCTIONS.md` into the Claude Project's instructions unchanged. Where it says ChatGPT, the Claude Project is the control plane; where it says Codex, read "the selected coding agent". The control plane must state the executor (Codex or Claude Code) in the routing output so the model profile and entry files match.

## Claude Code executor

`scripts/setup_project.py install|upgrade` adds the Claude Code entry points alongside the existing scaffold:

- **`CLAUDE.md`** (project-owned, created only when missing). Its first line, `@AGENTS.md`, imports the shared agent instructions so there is one instruction source for every coding agent. Claude Code reads `CLAUDE.md` instead of `AGENTS.md` when both exist, so a pre-existing `CLAUDE.md` without that import hides the workflow; `inspect`, `install`, `upgrade`, and `validate` print a warning in that case. The installer never edits an existing `CLAUDE.md`.
- **`.claude/skills/<name>/SKILL.md`** (installer-managed, hash-tracked). Each wrapper carries the focused skill's `name` and `description` so Claude Code can discover and trigger it, and points to the canonical procedure in `.engineering-workflow/skills/<name>/SKILL.md`. Procedure text is not duplicated, so the pinned snapshot remains the only authority. An unmanaged skill already at the same path blocks installation rather than being overwritten.

The root router is not wrapped as a skill; `AGENTS.md` already directs every executor to `.engineering-workflow/SKILL.md` before changing code.

### Deterministic enforcement (optional, project-owned)

`CLAUDE.md` and `AGENTS.md` are context, not enforcement. Where a rule can be mechanically blocked, `ACCEPTANCE_AND_EVIDENCE.md` prefers that. In Claude Code the relevant mechanisms are permission rules and `PreToolUse` hooks in `.claude/settings.json`, for example to deny writes outside the project root. The installer does not create or modify `.claude/settings.json`: those settings are project- and machine-specific, and changing an agent's permission configuration is a STRICT action under `WORKSPACE_SAFETY.md`.

## Adding another platform

Add a row to the mapping table, an entry-file or wrapper rule in the installer only when the platform cannot read the existing files, and a dated profile section in `MODEL_ROUTING_POLICY.md`. Do not fork the policies per platform.
