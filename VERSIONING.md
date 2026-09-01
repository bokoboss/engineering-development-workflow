# Workflow Versioning

This repository versions the workflow contract using Semantic Versioning.

- PATCH — wording, examples, clarifications, typo fixes, or non-behavioral validation improvements.
- MINOR — backward-compatible new workflow capabilities, templates, gate types, or routing guidance.
- MAJOR — breaking changes to required contracts, core philosophy, acceptance semantics, or project integration expectations.

Model names, prices, and product capabilities are time-sensitive operational guidance. Updating them does not automatically require a major version unless the normative routing contract changes incompatibly.

Stable releases should record the accepted commit and avoid claiming a version until repository validation and human review are complete.


## Stable release discipline

A stable workflow version is not complete merely because version strings exist in repository files.

Before publication:
1. the version must match across `README.md`, `ENGINEERING_DEV_WORKFLOW.md`, and `scripts/setup_project.py`;
2. `CHANGELOG.md` must contain a stable release section for that version;
3. repository validation, release-metadata validation, and regression tests must pass on the accepted `main` commit;
4. the accepted commit must be immutable enough to identify by exact SHA;
5. the repository must publish a Git tag `vX.Y.Z` and a GitHub Release for that same accepted commit.

The release workflow in `.github/workflows/release.yml` runs only after the named validation workflow completes successfully on `main`.

Release automation is fail-closed:
- it never moves or overwrites an existing tag;
- if an existing tag points to a different commit than the expected accepted SHA, publication fails;
- an existing GitHub Release is left unchanged;
- historical release backfill is limited to explicitly verified accepted SHAs;
- current release metadata must pass `scripts/release_metadata.py verify`.

## Historical backfill policy

v1.7.2 release automation is authorized to backfill only:

- `v1.7.0` -> `21437f848beaa04d7684d396a07993b40c0dbcd1`;
- `v1.7.1` -> `02553e582a81a8d0ec120f30c5fa08bfd0def576`.

Do not infer or recreate older tags from version names alone. An older release may be backfilled only after its accepted commit is reconstructed and verified from repository history/evidence.

## Repository configuration is separate

Git tags/releases are repository state, while branch rulesets, About metadata, and Private Vulnerability Reporting are GitHub-level configuration.

See `docs/GITHUB_REPOSITORY_CONFIGURATION.md`.

A committed document describing desired GitHub configuration is not evidence that the setting is active.
