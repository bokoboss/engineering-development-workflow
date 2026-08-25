# Contributing

Contributions should improve verified engineering-development outcomes rather than add process for its own sake.

## Change process

1. Open an issue describing the problem, evidence, proposed change, compatibility impact, and success gates.
2. Keep changes scoped. Separate policy changes from examples when practical.
3. Update affected templates and cross-references together.
4. Record material external inspiration or reused material in `ACKNOWLEDGEMENTS.md` when applicable.
5. Run `python scripts/validate_repository.py`.
6. Open a pull request with rationale, validation evidence, compatibility notes, unresolved risks, and any required attribution/licensing notes.
7. Treat changes to the normative workflow, model-routing rules, protected-change policy, and acceptance semantics as human-review gates.

## External inspiration and attribution

Give credit when a specific external project, article, standard, talk, documentation set, or other identifiable source materially shapes a reusable rule, skill, template, architecture decision, or validation method in this repository.

For each material source, record in `ACKNOWLEDGEMENTS.md`:
- source name, author/maintainer when known, and URL;
- the idea or component it influenced;
- whether the relationship is `conceptual inspiration`, `adapted`, or `copied/embedded`;
- source license or licensing status when known;
- what was independently designed or written in this repository.

Do not treat publicly viewable material as automatically reusable. If a source has no declared compatible license, do not copy its text or code. Use it only as high-level research or conceptual inspiration and write original material.

When source material is adapted or embedded under a license, preserve all required attribution, copyright, notice, and redistribution terms in addition to the acknowledgement entry.

## Design principles

- Optimize for cost to verified completion, not raw token count or agent count.
- Prefer explicit contracts, evidence, and reproducible validation.
- Keep project-specific facts in project repositories, not in this shared workflow.
- Give meaningful credit for material external influence and keep provenance explicit.
- Do not encode transient model pricing as timeless truth. Date any cost-specific guidance.
- Add complexity only when it reduces ambiguity, risk, rework, or verification burden.

## Versioning

See `VERSIONING.md`. Behavioral changes to required contracts or gates may require a minor or major version increment depending on compatibility.
