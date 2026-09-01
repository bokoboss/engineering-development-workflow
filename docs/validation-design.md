# Repository Validation Design and Limitations

## Purpose

`scripts/validate_repository.py` is a deterministic repository-contract guard.

It is intentionally:
- stdlib-only;
- fast;
- offline;
- reproducible;
- suitable for local execution and GitHub Actions.

## What it validates

The validator checks:
- required files;
- required headings;
- critical invariant text;
- selected cross-contract references;
- CI commands that must remain present;
- release/security/workspace-safety contract anchors.

Negative regression tests in `tests/test_validate_repository.py` also prove that selected invalid states actually cause validation to fail.

## What it does not validate

The validator is **not a semantic parser or AI reviewer**.

It cannot prove that:
- two policies are logically consistent merely because required phrases are present;
- a paragraph has not been rewritten to contradict a preserved keyword elsewhere;
- an engineering/security decision is correct;
- a GitHub ruleset or repository setting is active;
- runtime behavior matches documentation unless a separate executable test covers it.

Substring/presence checks are therefore a bounded deterministic guard, not semantic proof.

## Why this trade-off is intentional

A semantic/LLM validator in mandatory CI would add:
- nondeterminism;
- external service dependency;
- cost and latency;
- false-positive/false-negative review behavior;
- a new security and availability dependency.

The shared workflow instead uses layered assurance:

```text
deterministic contract validator
        +
negative validator tests
        +
installer/runtime tests
        +
GitHub CI
        +
actual diff review
        +
risk-appropriate independent/human review
```

## Maintenance rule

When a policy adds or changes a non-negotiable invariant:

1. decide whether deterministic enforcement is practical;
2. if practical, add a required heading/text/cross-contract check;
3. add or update a negative test when losing that invariant would be materially unsafe;
4. do not claim semantic coverage beyond what the validator actually enforces.

A validator PASS means the encoded repository contract is structurally intact. It does not replace engineering judgment or acceptance review.
