# Security Policy

## Supported versions

Security and filesystem-safety fixes are supported on the **latest stable release** of the Engineering Development Workflow.

Older releases may receive documentation or migration guidance, but users should upgrade to the latest stable release when a security or workspace-safety issue is fixed there.

## What counts as a security issue

Please report issues such as:

- the installer writing, moving, renaming, or deleting content outside the explicit target project root;
- symlink, junction, reparse-point, or path-containment escapes;
- unsafe overwrite/conflict behavior in `scripts/setup_project.py`;
- credential, token, secret, or private-data exposure caused by workflow code/templates;
- a workflow or CI change that materially weakens a protected security/workspace-safety invariant;
- release automation that publishes or retargets an unvalidated or unintended commit;
- an authorization, permissions, or GitHub Actions configuration defect that could allow unsafe repository mutation.

Ordinary documentation disagreements, feature requests, and non-sensitive workflow suggestions can use normal GitHub Issues.

## Reporting a vulnerability

**Do not publish sensitive vulnerability details in a public Issue or Pull Request.**

Preferred path:

1. Open the repository's **Security** tab.
2. Choose **Report a vulnerability** / GitHub Private Vulnerability Reporting when available.
3. Include the affected release/commit, operating system/filesystem, exact reproduction, expected vs actual behavior, affected path/resource, and whether any external/user files were modified.

If GitHub Private Vulnerability Reporting is not enabled or unavailable, open a minimal public Issue that contains **no exploit details, secrets, private paths, or sensitive reproduction data** and ask the maintainer to establish a private reporting channel.

## Useful report details

When safe to provide privately, include:

- affected workflow version/tag and commit SHA;
- target project root used;
- OS and filesystem details;
- whether symlinks/junctions/reparse points were involved;
- exact command or workflow action that triggered the issue;
- paths/resources affected;
- whether the issue modified anything outside the target project;
- minimal reproduction;
- rollback/recovery performed;
- proposed fix, if known.

## Response and disclosure

The maintainer will first confirm whether the report affects:
- the current stable release;
- installer/workspace containment;
- secrets/private-data handling;
- GitHub release/CI integrity;
- another protected workflow contract.

Please allow time for a fix and stable release before public disclosure when the issue could endanger user files, credentials, or repository integrity.

## Security design references

Normative project rules live in:
- `SECURITY_AND_GOVERNANCE.md`;
- `WORKSPACE_SAFETY.md`;
- `ACCEPTANCE_AND_EVIDENCE.md`;
- `WORK_MODE_ROUTING.md`.

The default local write authority remains the explicit target project root only. Human approval is required for external/system mutations as defined by `WORKSPACE_SAFETY.md`.
