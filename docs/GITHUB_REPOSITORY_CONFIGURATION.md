# GitHub Repository Configuration

This document records **desired GitHub-level state** that is not established merely by committing files to this repository.

Repository files and GitHub repository configuration are separate control planes. Do not claim a GitHub-level control is active until the GitHub API/UI confirms it.

## 1. Main branch protection / ruleset

Desired rule for `main`:

- require changes through a pull request;
- require the `Validate workflow repository / validate` status check before merge;
- block force pushes;
- block branch deletion;
- allow repository-owner/admin emergency bypass only when necessary for recovery;
- do not require auto-merge.

Rationale:
- pull-request + CI acceptance becomes deterministic rather than instruction-only;
- a direct push to `main` currently triggers validation, but that is detection **after mutation**, not prevention.

### Verification

Verify through GitHub Settings -> Rules / Branches, or the GitHub rulesets/branch-protection API.

A Markdown statement in this repository is not proof that protection is enabled.

## 2. Repository About metadata

Recommended description:

> Evidence-first, risk-adaptive workflow for safe AI-assisted engineering software development with ChatGPT, Codex, GitHub, verification gates, and workspace safety.

Recommended topics:

- `ai-agents`
- `chatgpt`
- `codex`
- `engineering-software`
- `software-engineering`
- `development-workflow`
- `ai-assisted-development`
- `coding-agents`
- `github-actions`
- `software-quality`

## 3. Vulnerability reporting

Enable GitHub **Private Vulnerability Reporting** for this public repository when available.

The committed `SECURITY.md` defines the reporting policy, but the private-reporting UI is a separate GitHub repository setting and must be verified independently.

## 4. Release discipline

Stable versions use:
- semantic version in repository contracts;
- exact accepted commit;
- Git tag `vX.Y.Z`;
- GitHub Release for the same tag;
- green repository validation before release publication.

The post-validation release workflow in `.github/workflows/release.yml` enforces the tag/release side after a successful main validation.

## 5. Scheduled validation

Monthly scheduled validation is a **platform/toolchain drift safety net**, not a substitute for branch protection.

It can detect problems such as:
- GitHub Actions/runtime changes;
- action-version deprecation;
- unexpected environment drift.

It does not prevent an unsafe direct push. Branch/ruleset enforcement addresses that risk.

## Current configuration evidence

Update this section only from verified GitHub API/UI state.

At the v1.7.2 preparation baseline:
- repository rulesets visible to the connected integration: none;
- branch-protection endpoint: not readable by the connected integration (403);
- releases: none;
- tag refs: none;
- About description/topics: not established through the connected mutation toolset.

Release/tag state is expected to change automatically after v1.7.2 merges and the post-validation release workflow succeeds.
