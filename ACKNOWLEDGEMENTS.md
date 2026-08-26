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

## Future acknowledgements

Add an entry when an external source materially affects a workflow rule, skill, template, architecture decision, validation method, or other reusable project capability.

Do not add routine citations for generic background knowledge unless a specific source materially shaped the implementation. Conversely, do not omit a source merely because only the *idea* rather than literal code or text was reused.

When a change depends on licensed third-party material, also preserve any attribution, notice, copyright, or redistribution requirements imposed by that source's license.
