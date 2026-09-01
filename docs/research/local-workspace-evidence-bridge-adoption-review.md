# Local Workspace Evidence Bridge — Foundation Research and C2C Adoption Review

Status: Research decision record  
Issue: #21  
Workflow baseline reviewed: v1.6.0 (`3c4d64f7e2a5e6ea1fd6945c8b57c6d87bccd410`)  
Candidate reviewed: `XiaoDuoYa/codex-with-chatgpt`  
Pinned candidate revision: `d6d0dd4e866fd9253572fcf84d8414132838d6f9` (v0.1.1)  
Research date: 2026-09-01  
License: MIT  
Overall concept verdict: **GO WITH CONDITIONS**  
Pinned C2C candidate adoption verdict: **NO-GO at this time**

## 1. Executive decision

A **Local Workspace Evidence Bridge** is a high-value capability for the Engineering Development Workflow.

It can close a real gap between ChatGPT planning/review and Codex local execution by allowing the ChatGPT control plane to inspect current local files, uncommitted Git diff, validation records, and selected execution evidence without asking Codex or the user to paste large bodies of code/logs into chat.

However, the workflow must adopt the **capability abstraction**, not the current C2C product wholesale.

The pinned `codex-with-chatgpt` v0.1.1 implementation is **not approved for installation into a real or sensitive engineering project** because:
- current OpenAI product-plan support is not stable enough to assume from the candidate README;
- the candidate automates ChatGPT Web output consumption in a way whose compatibility with current consumer Terms of Use is unresolved;
- the default public Cloudflare transport creates avoidable Internet-facing attack surface when OpenAI now recommends Secure MCP Tunnel for local/private MCP;
- several material HTTP/OAuth/enrollment/sensitive-data controls are incomplete in the pinned implementation;
- the candidate's daily mutable-branch update path is incompatible with this workflow's supply-chain and explicit-upgrade discipline;
- the candidate test suite is substantial but is not CI-enforced at the pinned commit and could not be independently executed in this research environment.

The correct next step is therefore **not v1.7 implementation and not installation**. The next step is to preserve the bridge abstraction and define the conditions a candidate implementation must satisfy before a low-risk pilot.

## 2. Problem being solved

The current workflow normally observes two evidence surfaces:

```text
ChatGPT control plane
        |
        v
GitHub / PR / CI
        ^
        |
Codex local execution
```

This is strong for accepted/shared state, but it leaves a gap before Codex commits or pushes.

A useful local bridge would add a second **read-only evidence channel**:

```text
                         GitHub
                    authoritative state
                         ^
                         |
ChatGPT control plane ---+--- Local Workspace Evidence Bridge
                         |       current files
                         |       local git status/diff
                         |       validation records
                         |       selected sanitized output
                         |               ^
                         |               |
                         +------------- Codex
                                      edit / shell / test
```

The bridge improves observability. It does not become the source of truth, executor, or acceptance authority.

## 3. Candidate architecture reviewed

C2C implements two conceptual channels:

### Control plane

Codex drives a ChatGPT Web conversation with compact protocol messages:

```text
INIT
-> PLAN
-> EXECUTING
-> EXECUTED
-> REVIEW
-> PLAN | DONE | BLOCKED | ERROR
```

A HANDOFF record supports a replacement conversation.

The intended messages remain small; source files/diffs/logs are not copied into the protocol message.

### Data plane

ChatGPT reads a local workspace through a read-only MCP server.

The pinned tool surface includes:
- `workspace_info`;
- `list_directory`;
- `read_file`;
- `search_workspace`;
- `git_status`;
- `git_diff`;
- `test_status`;
- `execution_summary`;
- `execution_output`.

### Local execution

Codex retains edit, shell, test, Git, package-installation, and repair capabilities.

The MCP server itself contains no write/delete/shell/commit tool.

This separation is architecturally aligned with this workflow's existing principle: ChatGPT reasons/reviews; the coding agent executes.

## 4. OpenAI product compatibility

Official sources checked on 2026-09-01:
- https://help.openai.com/en/articles/12584461
- https://openai.com/policies/terms-of-use/
- https://openai.com/policies/developer-apps-terms/

### 4.1 Custom MCP support

Current OpenAI documentation states:
- ChatGPT Pro users can connect MCPs with read/fetch permissions in developer mode;
- full MCP support, including modify/write actions, is currently for Business and Enterprise/Edu;
- ChatGPT does not connect directly to a local MCP server;
- OpenAI recommends **Secure MCP Tunnel** for private/on-prem/developer-machine MCP servers so the local server need not be exposed to the public Internet;
- MCP apps are currently web-only;
- agent mode does not use custom apps;
- deep research can use custom apps only for read/fetch.

### 4.2 Plus is not a reliable deployment assumption

The candidate README promotes a Plus/Pro use case.

Current official documentation does **not** establish Plus as a supported custom read/fetch MCP plan.

Candidate issues contain anecdotal Plus reports that conflict with each other:
- some Plus sessions reported `FORBIDDEN` or no visible developer-MCP path;
- at least one Plus user/maintainer report says a hidden/direct plugins path worked after developer mode was toggled.

These observations do not override the current official support matrix.

**Decision:** a workflow contract must never promise Plus compatibility unless current OpenAI documentation explicitly supports it or a separately documented product experiment confirms it for the exact account/surface without relying on hidden or unsupported UI.

### 4.3 Web-only and surface limitations

The C2C design depends on ChatGPT Web plus a custom MCP connector.

Do not assume:
- mobile parity;
- ChatGPT agent mode support;
- ChatGPT Work/custom-app compatibility;
- stable settings URLs or UI automation behavior.

These are product-level dependencies and may change independently from C2C.

## 5. Terms and policy compatibility

This is a distinct gate from MCP technical compatibility.

The OpenAI Terms of Use effective 2026-01-01 for consumer/individual services prohibit automatically or programmatically extracting data or Output and prohibit circumventing rate limits/restrictions or protective measures.

C2C does not appear to steal cookies, proxy private APIs, or technically bypass product rate limits. Its maintainer explicitly states that this is not the intent.

Nevertheless, the candidate Skill directs Codex to:
- automate the ChatGPT Web UI;
- send INIT/EXECUTED messages;
- poll/read the ChatGPT response;
- parse PLAN/DONE/BLOCKED back into an external coding-agent loop.

That automated consumption of ChatGPT Web output is materially different from a human manually using a custom MCP app inside ChatGPT.

The App Developer Terms establish that custom MCP apps/connectors are supported concepts, but they do not by themselves grant permission for an external agent to programmatically consume consumer ChatGPT Web output.

### Policy decision

**Consumer-plan C2C automation is not approved for our workflow until this use pattern is clearly permitted by current OpenAI product documentation/terms or a supported first-party integration provides the same orchestration path.**

This decision is deliberately conservative. It is not a legal conclusion that C2C violates the Terms; it is a statement that the evidence reviewed is insufficient to treat the pattern as policy-safe.

Business/Enterprise/Edu use is governed by different agreements, but any real deployment still requires checking the applicable agreement and supported product surface rather than assuming the consumer analysis transfers unchanged.

## 6. Connectivity architecture

### Candidate default

The pinned C2C bridge:
1. binds a local Express server to loopback;
2. starts Cloudflare Quick Tunnel by default, or Named Tunnel when configured;
3. exposes the OAuth/MCP HTTP surface through the public hostname;
4. connects ChatGPT to that remote MCP URL.

The public MCP endpoint is bearer-protected, but several OAuth/discovery/health surfaces are intentionally unauthenticated.

### OpenAI current recommendation

Current OpenAI documentation recommends Secure MCP Tunnel for a developer-machine/private MCP server so the server does not need to be exposed to the public Internet.

### Decision

The workflow-level abstraction must not mandate Cloudflare.

Preferred order for any future pilot:

```text
1. OpenAI-supported private outbound / Secure MCP Tunnel
2. another reviewed private outbound transport
3. stable public tunnel only as an explicitly accepted compatibility fallback
4. ephemeral public Quick Tunnel only for disposable development/test, not normal engineering use
```

There must be no silent downgrade from private transport to a public transport.

## 7. Security audit — strengths

The following controls are present in the pinned implementation and are worth preserving conceptually.

### 7.1 Read-only MCP capability boundary

The registered MCP tools are read/search/evidence tools.

There is no MCP tool for:
- write;
- delete;
- shell;
- package install;
- Git commit/push.

This is a strong deterministic boundary and is preferable to a prompt-only rule saying "do not edit."

### 7.2 Workspace containment

`Workspace.resolve()`:
- normalizes Windows-style separators;
- rejects null bytes;
- canonicalizes the deepest existing ancestor using `realpath`;
- compares against the canonical workspace root;
- blocks `../`, outside absolute paths, and symlink escapes.

The repository contains tests for normal traversal and symlink escape where the OS permits symlink creation.

### 7.3 Common sensitive-path filtering

The hard-sensitive rules cover common:
- `.env*` files except `.env.example`;
- private key/certificate extensions;
- SSH/GPG/cloud credential directories;
- npm/netrc/git-credential/keychain-style paths;
- Cloudflare credentials;
- common credentials/service-account/secrets files;
- browser cookie files;
- C2C-local secrets.

Custom `.c2cignore` can further restrict the visible surface.

### 7.4 Git-diff filtering

The Git diff implementation includes tests for:
- unstaged/staged/head modes;
- custom ignored files;
- sensitive files;
- rename provenance where either source or destination is sensitive.

This is more careful than a simple post-diff path filter.

### 7.5 OAuth mechanics

The pinned implementation includes:
- authorization-code flow;
- mandatory PKCE S256;
- one-time authorization codes;
- access-token expiry;
- refresh-token rotation;
- token revocation;
- token hashes rather than raw tokens in persisted auth state;
- workspace binding on bearer validation;
- scope checks per MCP tool.

### 7.6 Pairing basics

Pairing codes are:
- generated from CSPRNG bytes;
- short-lived;
- single-use;
- attempt-limited;
- rate-limited per observed IP.

### 7.7 Admin boundary

The local bridge refuses a normal non-loopback bind.

Admin routes require:
- loopback socket origin;
- absence of proxy-forwarding headers;
- random admin bearer token.

### 7.8 Execution-output sanitizer

Released execution output:
- rejects private-key blocks;
- redacts several common credential/token patterns;
- redacts user home paths;
- caps lines and bytes;
- stores restricted items without releasing the body.

These controls are useful but should be treated as best-effort leakage reduction, not perfect DLP.

## 8. Security audit — material gaps

### F1 — MCP request body parsed before bearer auth — HIGH

Pinned route order:

```text
/mcp
-> express.json(limit 8 MB)
-> bearerAuth
-> MCP handler
```

An unauthenticated Internet client can therefore consume JSON parsing memory/CPU before authentication.

Required future condition:
- authenticate/cheap-validate before expensive body parsing;
- lower/bounded body limits;
- request deadline/concurrency control.

### F2 — Broad proxy trust affects rate-limit identity — HIGH

The app globally enables `trust proxy = true`, while pairing verification uses `req.ip`.

Without provider-specific trusted-proxy handling, attacker-controlled forwarding headers can make IP-based controls unreliable.

Required future condition:
- explicit trusted proxy policy;
- security decisions must not trust arbitrary forwarded headers.

### F3 — Public health endpoint leaks stable workspace identifier — MEDIUM

The security documentation describes a salted workspace hash.

The implementation derives:

```text
workspaceId = SHA-256(canonical local path).slice(0, 12)
```

without a salt, and returns that identifier on public `/health`.

This is a documentation/privacy mismatch and may permit guessing common path identities.

Required future condition:
- public readiness must not reveal stable workspace identity;
- or keep health local/private.

### F4 — Dynamic Client Registration permanently open — HIGH

The public server accepts OAuth Dynamic Client Registration without a local short-lived enrollment window.

There is no tight intended-client lifecycle around setup.

Required future condition:
- local-admin-controlled enrollment window;
- default one intended client;
- bounded client/pending-request/token stores.

### F5 — Pairing not bound to intended OAuth transaction — HIGH

A pairing session is workspace-wide rather than bound to:
- intended client id;
- exact redirect URI;
- scope set;
- pending authorization request.

A remote actor reaching the public surface during setup can at minimum consume the active pairing attempt budget with wrong codes, causing denial of service.

Required future condition:
- bind pairing to the intended authorization transaction and close enrollment after success/expiry.

### F6 — Invalid/missing scope falls back broad — HIGH

If scope input is missing or contains no recognized scope, the current helper falls back to all supported scopes, including `offline_access`.

Fail-open scope broadening conflicts with least privilege.

Required future condition:
- reject unknown/unsupported scopes;
- grant only explicit intersection;
- do not implicitly add persistent/offline access.

### F7 — Denylist-based secret protection is incomplete — HIGH for sensitive repos

Common filename patterns are blocked, but secret data can live in:
- ordinary source files;
- renamed credential files;
- customer documents/data;
- test fixtures;
- arbitrary text;
- generated logs.

The README wording that sensitive files "never leave" is therefore too categorical for the pinned implementation.

Required future condition for sensitive repos:
- strict allowlist mode;
- hard machine/admin policy that project files cannot weaken;
- bounded content secret scanning/redaction;
- explicit project-root approval.

### F8 — Noise-hidden VCS metadata is not a hard direct-read denial — MEDIUM/HIGH

`.git/` is hidden as noise for normal listing/search.

However, direct `read_file` resolution blocks `isSensitive`, not all `isHidden` noise paths.

Therefore hiding `.git/` is not equivalent to deterministically denying direct reads of VCS metadata.

Potential exposure includes internal remote URLs and repository metadata.

Required future condition:
- hard-deny VCS/agent/browser/credential metadata where appropriate, independently from UI/noise filtering.

### F9 — Broad workspace roots are allowed — HIGH for accidental exposure

The bridge accepts an arbitrary existing root and does not require that it equal a recognized project/Git root.

Accidentally selecting a home directory or broad parent could expose far more data than intended.

Required future condition:
- reject or explicitly approve broad roots;
- strict profiles should require an approved project root and path allowlist.

### F10 — Output sanitization is best effort — MEDIUM

The execution-output sanitizer is useful, but regex coverage cannot guarantee all secrets are removed.

Required future condition:
- never treat sanitizer success as proof an output is safe;
- strict mode may need structured allowlisted diagnostics rather than arbitrary command output.

### F11 — Node fallback regex can consume local CPU — LOW/MEDIUM

When ripgrep is unavailable, user/model-provided regex is evaluated by JavaScript RegExp across file lines without a regex complexity guard or request cancellation.

A prompt-injected tool call could therefore create avoidable local compute pressure.

Required future condition:
- bounded regex policy or safe engine;
- cancellation/deadlines for long search/Git work.

## 9. Supply-chain and update audit

### 9.1 Daily mutable-branch update is rejected

The Skill checks `origin/HEAD` daily.

When an update is available, the documented path may:
- `git pull --ff-only`;
- automatically stash local edits on failure;
- `pnpm install`;
- build;
- reinstall the Skill;
- restart the bridge.

This makes:
- the mutable upstream branch;
- local Git remote configuration;
- dependency resolution;
- the fetched Skill instructions

part of a recurring code-execution path on the developer workstation.

This is incompatible with our workflow.

### Required adoption policy

Any candidate bridge used by us must:
- pin an exact release/tag/commit;
- disable automatic update/application;
- use an explicit reviewed upgrade work item;
- use a frozen lockfile;
- verify repository identity;
- prefer signed/checksummed immutable release artifacts when available;
- preserve rollback;
- never auto-stash the installed product as an update mechanism.

### 9.2 `latest` dependency declaration

The pinned `package.json` declares:

```text
@modelcontextprotocol/sdk: latest
```

The pinned `pnpm-lock.yaml` resolves it to 1.30.0 with integrity data, so the exact pinned source plus frozen lock is more reproducible than the manifest alone suggests.

Nevertheless, `latest` is not an acceptable long-term dependency policy for a security-sensitive bridge.

## 10. Test and CI maturity

### Repository evidence

The pinned repository contains a non-trivial Vitest suite covering areas such as:
- workspace containment;
- sensitive paths;
- Git diff;
- OAuth;
- pairing;
- MCP integration;
- execution output;
- runtime/daemon behavior;
- sandbox allowlist;
- sessions and configuration.

This is a positive maturity signal.

### CI evidence

At the pinned commit:
- GitHub combined status has zero statuses;
- GitHub check-runs count is zero;
- no `.github/workflows` directory is visible at the pinned baseline.

Therefore the repository does not provide CI evidence that the pinned commit passed its tests.

### Independent execution limitation

The research environment used for this review could inspect the repository through GitHub but could not clone/materialize the source into the execution container because outbound container network resolution for GitHub was unavailable.

Consequently:
- `pnpm install` was not independently run;
- `pnpm build` was not independently run;
- `pnpm typecheck` was not independently run;
- `pnpm test` was not independently run.

Candidate README/self-reported pass counts remain **claims**, not accepted evidence.

A future pilot is blocked until these commands pass on the actual pilot machine from the exact pinned revision with a frozen lockfile.

## 11. Performance and operational maturity

The pinned implementation uses synchronous Git subprocesses for several operations.

A large/paginated review can re-run or recompute expensive Git work.

There is no accepted evidence in this research that large engineering repositories have bounded:
- review latency;
- memory;
- cancellation;
- concurrent request load;
- repeated diff cost.

This is not a blocker for a tiny disposable pilot, but it is a blocker to assuming the bridge scales to large workspaces.

## 12. Protocol fit with our workflow

### Concepts worth adopting

The following C2C concepts fit well:
- keep control messages compact;
- let the reviewer fetch evidence itself;
- do not trust the executor narrative;
- separate planner/reviewer from local mutation;
- keep local workspace identity isolated per connector;
- use concise handoff/checkpoint records instead of replaying large logs;
- expose validation/execution evidence read-only.

### Concepts that must be subordinate to our workflow

C2C's `PLAN` is not our execution authority.

Our ordering remains:

```text
Research / Scrutiny
-> Issue / Execution Contract
-> approved scope + gates
-> Codex execution
-> Local evidence review (optional bridge)
-> commit / PR
-> GitHub CI / review
-> Acceptance
```

A C2C PLAN may help create or refine an execution packet, but it cannot silently supersede:
- Issue scope;
- protected behavior;
- approved engineering methodology;
- model-routing/stop conditions;
- human approval;
- current GitHub acceptance state.

### Missing plan-to-execution binding

The pinned protocol does not immutably bind:
- the exact plan;
- the exact workspace snapshot reviewed;
- the action Codex executed;
- the evidence later reviewed.

A future bridge should include evidence identifiers, not only natural-language state.

## 13. Evidence hierarchy

A Local Workspace Evidence Bridge introduces **ephemeral evidence**, not a new source of truth.

Recommended hierarchy:

1. **Accepted repository/GitHub state**
   - accepted commit;
   - project contracts;
   - Issues/PRs;
   - CI/checks;
   - accepted decision records.

2. **Verified local evidence**
   - exact workspace identity;
   - current Git HEAD;
   - dirty/staged/unstaged state;
   - local diff bound to HEAD;
   - validation record bound to task/iteration/revision;
   - sanitized/allowlisted execution evidence.

3. **Handoff/checkpoint**
   - task progress and current expected next action.

4. **Executor narrative**
   - Codex statement such as "tests passed."

If local and GitHub state conflict, do not merge them mentally. State the mismatch and resolve which revision is being reviewed.

Local bridge evidence expires when the workspace revision changes.

## 14. Proposed tool-independent Local Workspace Evidence Bridge contract

Do not name C2C in the normative core capability.

A future abstraction should provide a minimal read-only contract such as:

```text
EvidenceBridge
  identity()
  list()
  read()
  search()
  git_status()
  git_diff()
  validation_records()
  released_execution_evidence()
  health()
```

### Mandatory invariants

#### Capability
- read-only by construction;
- no write/delete/shell/commit/package-install tool;
- no privilege expansion from workspace content;
- explicit scope per tool.

#### Workspace boundary
- one approved project/workspace boundary;
- canonical realpath containment;
- broad-root rejection/approval;
- strict allowlist mode for sensitive projects;
- machine/admin restrictions cannot be weakened by repository configuration.

#### Evidence binding
Every evidence response should be able to identify enough context to detect staleness:
- workspace identifier that does not leak the local path publicly;
- current HEAD/revision where applicable;
- dirty-state/snapshot identifier;
- timestamp;
- policy revision;
- task/iteration for execution evidence.

#### Transport
- transport-neutral core;
- private outbound transport preferred;
- public exposure explicit and visible;
- no silent fallback to weaker transport.

#### Authentication
- short-lived enrollment;
- intended-client binding;
- least scopes;
- bounded client/token lifecycle;
- revocation;
- no implicit offline access.

#### Data loss prevention
- hard-sensitive deny policy;
- optional/required allowlist;
- content-aware redaction for outbound data;
- user/project rights and confidentiality must permit the content to be sent to ChatGPT.

#### Supply chain
- immutable/pinned implementation;
- frozen dependencies;
- controlled upgrade;
- no mutable-branch auto-execution.

#### Observability
- local exposure status;
- authorized client summary;
- recent metadata-only access log;
- kill/revoke path;
- no secrets in audit logs.

## 15. Adopt / adapt / reject / defer matrix

| Candidate concept | Decision | Reason |
|---|---|---|
| ChatGPT planner/reviewer + Codex executor split | **Adopt** | Direct fit with existing architecture |
| Read-only local MCP evidence surface | **Adopt** | Closes pre-PR visibility gap |
| Reviewer independently fetches diff/evidence | **Adopt** | Stronger than executor self-report |
| Compact control messages | **Adopt** | Reduces context transfer/noise |
| Workspace-scoped connector identity | **Adapt** | Keep concept, strengthen policy/root binding |
| Checkpoint/HANDOFF | **Adapt** | Integrate with our existing context/handoff contract |
| Execution summary/output | **Adapt** | Prefer structured, allowlisted diagnostics with evidence binding |
| C2C PLAN as execution authority | **Reject** | Our Issue/execution contract remains authoritative |
| Public Cloudflare Quick Tunnel default | **Reject** | Prefer OpenAI Secure MCP Tunnel/private transport |
| Cloudflare Named Tunnel as universal requirement | **Reject** | Transport must remain swappable |
| Daily auto-update from origin/main | **Reject** | Supply-chain risk; explicit pinned upgrades only |
| `git stash` during updater repair | **Reject** | May alter installed checkout state unexpectedly |
| `@modelcontextprotocol/sdk: latest` policy | **Reject** for adoption | Pin security-sensitive dependencies |
| Denylist-only sensitive policy for client/customer repos | **Reject** | Need strict allowlist/monotonic policy |
| Always-open DCR | **Reject** | Enrollment must be short-lived/bounded |
| Implicit full scopes/offline_access | **Reject** | Fail closed / least privilege |
| ChatGPT Web automation loop | **Defer / blocked** | Consumer Terms compatibility unresolved |
| C2C v0.1.1 direct installation | **Reject now** | Material gates unresolved |
| Future hardened C2C release/fork | **Defer** | Re-evaluate against this contract |
| Local Workspace Evidence Bridge as workflow capability | **Adopt with conditions** | High value, implementation-independent |

## 16. Low-risk pilot design

A pilot is **designed but not authorized yet**.

### Mandatory prerequisites before pilot

All must be satisfied:

1. Product plan/surface explicitly supports the required read-only MCP connection.
2. ChatGPT Web automation/output-consumption policy is clarified as permitted for the intended account/use, **or** the pilot uses a supported first-party orchestration path that removes this ambiguity.
3. Use Secure MCP Tunnel/private outbound transport where available; no default Quick Tunnel.
4. Candidate implementation is an exact pinned revision/release.
5. Candidate automatic update application is disabled.
6. Frozen dependency install/build/typecheck/test pass independently on the pilot machine.
7. Public-boundary/auth/enrollment/scope blockers F1-F6 are fixed or avoided by the private transport architecture.
8. Workspace policy prevents broad-root exposure and uses a strict allowlist for any non-toy repository.
9. Bridge remains read-only with no write/shell/commit tools.
10. Revoke/stop/uninstall path is tested before exposing project data.

### Pilot repository

Use a deliberately non-sensitive test repository containing:
- no client data;
- no licensed confidential references;
- no credentials;
- no proprietary engineering methodology;
- synthetic test fixtures only.

Do not begin with an active production project.

### Pilot workflow

```text
ChatGPT
  inspect local evidence
  -> produce bounded plan/review
Codex
  execute locally
ChatGPT
  inspect local diff + validation evidence
  -> READY FOR PR / REMEDIATE
Codex
  commit/push
GitHub
  PR + CI
ChatGPT
  final GitHub acceptance
```

GitHub remains the final shared/accepted evidence surface.

### Pilot measurements

Collect:
- setup/reconnect failures;
- time spent repairing connector/tunnel;
- MCP calls per planning/review cycle;
- local review latency;
- percentage of Codex summaries independently confirmed;
- defects caught before PR;
- Codex reasoning/quota reduction, if measurable without violating product policy;
- ChatGPT usage/cost impact;
- false/stale evidence incidents;
- data-redaction/blocked-read events;
- duplicate context transfer avoided;
- human interventions;
- any security/policy incident.

## 17. Licensing and provenance

Source:
https://github.com/XiaoDuoYa/codex-with-chatgpt

Maintainer:
`XiaoDuoYa` and contributors.

Reviewed revision:
`d6d0dd4e866fd9253572fcf84d8414132838d6f9`.

License:
MIT License; candidate LICENSE states copyright 2026 codex-with-chatgpt contributors.

Relationship:
**conceptual and implementation prior-art research**.

No candidate source file, Skill, bridge implementation, protocol text, or code is embedded wholesale in the Engineering Development Workflow by this research change.

If future work copies or materially adapts source code/text, preserve the MIT copyright and permission notice as required.

## 18. Conditions attached to GO

The overall concept verdict is **GO WITH CONDITIONS**.

Before a Local Workspace Evidence Bridge can become a normative workflow capability or pilot:

- the bridge must remain read-only and optional;
- GitHub/project state remains authoritative;
- local evidence must be revision-bound and treated as ephemeral;
- current product-plan support must be verified against official OpenAI documentation;
- consumer ChatGPT Web automation must not be assumed policy-safe;
- private/first-party connectivity is preferred over public tunnel exposure;
- authentication/enrollment/scope handling must fail closed;
- sensitive-repo use requires strict allowlist and machine/admin policy;
- broad workspace roots must be rejected or explicitly approved;
- implementation and dependencies are pinned and upgrades are controlled;
- build/typecheck/tests must be independently executed;
- no protected engineering approval is delegated to the bridge;
- final acceptance still requires the existing GitHub/CI/human gates.

## 19. Research verdict

### Local Workspace Evidence Bridge concept

**GO WITH CONDITIONS**

The capability directly addresses a real workflow gap and can materially improve independent review before a PR exists.

### `codex-with-chatgpt` v0.1.1 at the pinned revision

**NO-GO AT THIS TIME**

Do not install it into an active engineering/customer/sensitive project and do not integrate it into v1.7 as a dependency.

Re-evaluate a future candidate release or a minimal hardened adapter only after the product/policy and security conditions above are satisfied.

## 20. Recommended next decision

Do **not** start v1.7 implementation yet.

Create a future readiness checkpoint rather than an implementation issue. Revisit when either:
- OpenAI provides a clearly supported orchestration path for this pattern; or
- a candidate bridge satisfies the security/supply-chain contract and the applicable account terms clearly permit the intended automation.

The main reusable lesson should be preserved now:

> Give the ChatGPT control plane a narrow, read-only, revision-bound way to inspect local execution evidence — but never turn that evidence bridge into the executor, source of truth, or a shortcut around product/security/human-approval boundaries.
