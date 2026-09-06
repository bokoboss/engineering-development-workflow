# Agent Instructions

This repository defines a reusable engineering-development workflow. Do not treat it as a product repository.

## Before changing anything

1. Read `WORK_MODE_ROUTING.md` and classify the change.
2. Read `WORKSPACE_SAFETY.md` and keep writes inside this repository.
3. Read `ENGINEERING_DEV_WORKFLOW.md`.
4. Read the issue or change request completely.
5. Read the specific policy file affected by the change.
6. Inspect existing templates and cross-references before editing.

## Action-oriented execution

When the user's intent is reasonably clear that work should be performed, carry it out within the currently approved scope. Do not stop at acknowledging capability, proposing a plan, offering to continue, or suggesting a next step that can be completed now.

When the required information, tools, and permissions are already available, proceed through understanding, execution, verification, and completion reporting. If tests, review, documentation, commit, push, or PR creation are part of the approved execution contract, complete those available steps before claiming completion.

Do not use this rule to expand permission. Stop when a material unresolved decision, workspace-boundary crossing, protected/destructive/external action, required human approval, or material risk of doing the wrong work is encountered. Clearly informational or exploratory questions remain questions, not mutation requests.

## Invariants

- Keep project-specific facts out of the shared workflow.
- Do not create/modify/delete files outside this repository or alter user/system/global configuration without explicit human approval.
- Do not weaken evidence, approval, protected-change, or stop-condition semantics without explicit human review.
- Do not hard-code transient model pricing as timeless policy; date cost-specific guidance.
- Prefer small coherent policy changes over broad rewrites.
- Update linked templates when a normative contract changes.
- Run `python scripts/validate_repository.py` before claiming completion.

## Completion

A documentation edit is not complete merely because Markdown renders. Check consistency across normative docs, templates, examples, and README; report unresolved policy conflicts explicitly.
