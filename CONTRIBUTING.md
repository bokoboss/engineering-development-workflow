# Contributing

Contributions should improve verified engineering-development outcomes rather than add process for its own sake.

## Change process

1. Open an issue describing the problem, evidence, proposed change, compatibility impact, and success gates.
2. Keep changes scoped. Separate policy changes from examples when practical.
3. Update affected templates and cross-references together.
4. Run `python scripts/validate_repository.py`.
5. Open a pull request with rationale, validation evidence, compatibility notes, and unresolved risks.
6. Treat changes to the normative workflow, model-routing rules, protected-change policy, and acceptance semantics as human-review gates.

## Design principles

- Optimize for cost to verified completion, not raw token count or agent count.
- Prefer explicit contracts, evidence, and reproducible validation.
- Keep project-specific facts in project repositories, not in this shared workflow.
- Do not encode transient model pricing as timeless truth. Date any cost-specific guidance.
- Add complexity only when it reduces ambiguity, risk, rework, or verification burden.

## Versioning

See `VERSIONING.md`. Behavioral changes to required contracts or gates may require a minor or major version increment depending on compatibility.
