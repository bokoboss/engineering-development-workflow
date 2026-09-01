# Acknowledgements and External Inspiration

This project is built from practical use, iteration, and research across software-development workflows, engineering practice, AI-assisted development, and public prior art.

The purpose of this file is to give meaningful credit where external work materially influenced this repository, while clearly distinguishing **inspiration** from **adaptation** or **copied material**.

## Attribution principles

For any external source that materially influences this repository, record:

1. **Source** — project, author, article, documentation, talk, standard, or other identifiable origin.
2. **Relevant influence** — the concept or part of this workflow that the source helped shape.
3. **Relationship** — one of:
   - `conceptual inspiration` — an idea or pattern was studied, then independently re-expressed for this workflow;
   - `adapted` — source material was transformed or modified under a license that permits it;
   - `copied/embedded` — source material is included substantially as-is under a compatible license and with required notices.
4. **License/status** — the source license when known, or an explicit note when no license is declared.
5. **What is original here** — enough context to avoid implying that the external source authored this repository's implementation or wording.

A public source being viewable does not by itself grant permission to copy its text or code. If licensing is unclear, use the source only for high-level research or conceptual inspiration and write original material.

## Current acknowledgements

### thananon/9arm-skills

- **Source:** https://github.com/thananon/9arm-skills
- **Author/maintainer:** `thananon`
- **Relationship:** conceptual inspiration only.
- **Relevant influence:** helped prompt discussion of focused, reusable reasoning modes around scrutiny/review, debugging discipline, postmortem learning, and management/status communication. Those discussions contributed to the decision to organize recurring reasoning procedures as focused skills in this repository.
- **License/status when reviewed:** the repository did not declare a repository license when reviewed on 2026-08-25.
- **Use in this project:** no text, code, or skill implementation from `9arm-skills` was copied into this repository. The focused skills under `skills/` are independently written, workflow-native definitions developed for the Engineering Development Workflow and licensed here under Apache-2.0.

Credit is given because the external project materially influenced the direction of the skill-layer discussion even though the resulting implementation and wording are original to this repository.

### shanraisshan/claude-code-best-practice

- **Source:** https://github.com/shanraisshan/claude-code-best-practice
- **Author/maintainer:** Shayan Rais (`shanraisshan`).
- **Relationship:** conceptual inspiration; no source file is embedded wholesale in this repository.
- **License/status when reviewed:** MIT License, copyright 2025-2026 Shayan Rais; reviewed on 2026-08-26.
- **Relevant influence:** the repository's documented practices materially informed the v1.5.0 design discussion in several areas:
  - conditional Research -> Plan -> Implement gating before committing to uncertain feature directions;
  - cross-model/fresh-context plan and implementation review;
  - context hygiene, deliberate fresh sessions, isolated subagents, and progressive disclosure;
  - separating workflow/orchestration, autonomous workers, and reusable skills;
  - feature/task-specific workers rather than relying only on generic agent roles;
  - using independent context as additional review/test-time compute;
  - preferring deterministic settings/hooks/verification mechanisms over instruction-only rules when the harness can enforce behavior.
- **Relevant source areas reviewed:** `development-workflows/rpi/`, `development-workflows/cross-model-workflow/`, `orchestration-workflow/`, `best-practice/`, `reports/claude-agent-command-skill.md`, and the sourced tips collected in the repository README.
- **Use in this project:** v1.5.0 introduces original workflow-native `research-gate` and `independent-review` skills, `CONTEXT_MANAGEMENT.md`, progressive-disclosure/Gotchas conventions, task-specific worker guidance, and deterministic-enforcement guidance. These are independently written and integrated with this repository's existing ChatGPT-control-plane, cost-aware model-routing, engineering-governance, and evidence/acceptance contracts rather than copying the Claude-specific harness or wording wholesale.

The source repository focuses heavily on Claude Code mechanics and best practices; this project generalizes selected ideas into a tool-independent engineering-development workflow. Product-specific Claude commands, fixed context heuristics, mandatory plan mode, per-file commit rules, and wholesale `.claude/` configuration are intentionally not adopted as universal rules here.


### cobusgreyling/loop-engineering

- **Source:** https://github.com/cobusgreyling/loop-engineering
- **Author/maintainer:** Cobus Greyling (`cobusgreyling`) and contributors.
- **Relationship:** conceptual inspiration and prior-art research; no source file, CLI, skill, or harness is embedded wholesale in this repository.
- **License/status when reviewed:** MIT License, copyright 2026 Cobus Greyling and contributors; reviewed at revision `ffeb5a37d0a0d397bb7438609b1713da1c69f204` on 2026-08-30.
- **Relevant influence:** materially informed the foundation research for a possible v1.6 Continuous Operations Layer, especially recurring work discovery/triage, phased autonomy, operational state, maker/checker separation, finite retry/circuit-breaker controls, recurring-operation budgets, selective notifications, run observability, multi-loop collision control, and human escalation.
- **Relevant source areas reviewed:** `LOOP.md`, `STATE.md`, `docs/concepts.md`, `docs/primitives.md`, `docs/loop-design-checklist.md`, `docs/operating-loops.md`, `docs/failure-modes.md`, `docs/anti-patterns.md`, `docs/safety.md`, `docs/multi-loop.md`, `docs/refactor.md`, `docs/architecture-diagrams.md`, `tools/loop-audit/README.md`, `starters/thin-loop/README.md`, and the Daily Triage / PR Babysitter / CI Sweeper / Issue Triage patterns.
- **Use in this project:** the adoption review at `docs/research/loop-engineering-adoption-review.md` independently re-expresses selected concepts for this workflow's existing ChatGPT-control-plane, GitHub-source-of-truth, cost-aware model-routing, independent-review, engineering-governance, and human-approval architecture. It explicitly rejects wholesale harness adoption, mandatory `STATE.md`, product-specific loop commands, fixed budgets/attempt counts, broad unattended refactoring, and initial auto-merge.

Credit is given because this source materially shaped the proposed continuous-operations architecture and risk controls even though the resulting recommendation and wording are original to this repository.

### XiaoDuoYa/codex-with-chatgpt

- **Source:** https://github.com/XiaoDuoYa/codex-with-chatgpt
- **Author/maintainer:** `XiaoDuoYa` and contributors.
- **Relationship:** conceptual and implementation prior-art research; no source file, Skill, bridge implementation, protocol text, or code is embedded wholesale in this repository.
- **License/status when reviewed:** MIT License; candidate LICENSE states copyright 2026 codex-with-chatgpt contributors. Foundation review pinned revision `d6d0dd4e866fd9253572fcf84d8414132838d6f9` (v0.1.1) on 2026-09-01.
- **Relevant influence:** materially informed research into a possible tool-independent **Local Workspace Evidence Bridge**: a narrow read-only evidence/data plane allowing the ChatGPT control plane to inspect local workspace files, Git status/diff, validation records, and selected sanitized execution evidence while Codex retains mutation/execution ownership.
- **Relevant source areas reviewed:** `README.md`, `docs/architecture.md`, `docs/protocol.md`, `docs/security.md`, `skill/SKILL.md`, MCP/workspace/Git/auth/pairing/bridge/tunnel/execution/session implementation, package/lock metadata, tests, and relevant public issues.
- **Use in this project:** the decision record at `docs/research/local-workspace-evidence-bridge-adoption-review.md` independently evaluates and re-expresses the capability for this workflow's existing ChatGPT-control-plane, GitHub-source-of-truth, Codex-execution-plane, security, model-routing, independent-review, continuous-operations, and human-approval contracts.
- **Explicit non-adoption:** the pinned C2C v0.1.1 implementation is not approved for direct installation by this research. The workflow does not adopt its public Cloudflare Quick Tunnel default, mutable-branch daily auto-update, fail-open scope behavior, always-open OAuth client registration, denylist-only sensitive-data model, or C2C PLAN as an authority over the workflow's Issue/execution contract.

Credit is given because the project's read-only MCP data-plane architecture and plan/execute/review separation materially shaped the Local Workspace Evidence Bridge research direction even though the resulting workflow recommendation and wording are original to this repository.

## Future acknowledgements

Add an entry when an external source materially affects a workflow rule, skill, template, architecture decision, validation method, or other reusable project capability.

Do not add routine citations for generic background knowledge unless a specific source materially shaped the implementation. Conversely, do not omit a source merely because only the *idea* rather than literal code or text was reused.

When a change depends on licensed third-party material, also preserve any attribution, notice, copyright, or redistribution requirements imposed by that source's license.
