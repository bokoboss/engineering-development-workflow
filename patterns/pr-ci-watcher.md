# A1 PR/CI Watcher Pattern

## Purpose

Reduce manual PR/CI checking by surfacing **new actionable findings** while preserving human control.

Autonomy: **A1 — Observe / report**

This pattern is the first Continuous Operations reference pilot for v1.6.

It is not a remediation bot.

## Non-goals

The watcher must not:
- edit code or files;
- invoke automatic Codex/coding-agent remediation;
- create speculative fixes;
- merge or enable auto-merge;
- close PRs/issues;
- approve protected/high-impact changes;
- treat missing check information as success;
- widen permissions or watched scope implicitly.

## Watched scope

A project adopting this pattern must explicitly define:
- repository/repositories;
- branch/PR population;
- required-check policy source when available;
- relevant inactivity/aging threshold;
- notification destination;
- trigger/cadence or event source.

Do not hard-code a universal polling interval.

## Authoritative sources

Prefer live GitHub state:
- open PR metadata and head SHA;
- check/CI status;
- repository required-check/branch policy when available;
- review state / changes requested;
- mergeability/conflicts;
- timestamps/activity.

Operational state, if used, is only for dedupe/aging/override memory. Refresh live GitHub before classifying or notifying.

## Observation and classification

For each watched PR, classify into one or more of:

- `HEALTHY_OR_PENDING` — no human action currently justified;
- `NEW_CI_FAILURE` — a required/relevant check newly failed or materially changed;
- `CHECKS_ABSENT_OR_POLICY_UNKNOWN` — readiness cannot be established;
- `BLOCKED_REVIEW` — changes requested or blocking review remains;
- `MERGE_CONFLICT` — branch cannot be cleanly merged;
- `READY_FOR_HUMAN_ACTION` — known required policy appears satisfied and human review/merge/acceptance is the next step;
- `STALE_NEEDS_DECISION` — inactivity exceeds the project-defined threshold and human disposition is useful;
- `PROTECTED_OR_AMBIGUOUS` — finding requires higher judgment and must be escalated rather than interpreted optimistically.

A clean/mergeable PR is not automatically ready if required-check/review policy is absent or unknown.

## Run procedure

1. Load the loop contract and prior operational memory only if needed.
2. Refresh live PR/CI/review/mergeability state.
3. Discard/prune memory for closed/merged/no-longer-watched items.
4. Classify each relevant PR.
5. Compare actionable classifications with the last notified fingerprint.
6. Quiet-exit if there is no new actionable state.
7. Notify only new/changed actionable findings or an explicit aging escalation.
8. Record the observation/notification fingerprint when state is required.
9. Record a concise run outcome according to the project observability rule.

## Notification contract

Default: no message on no-op.

A notification should contain:
- PR identifier and head SHA;
- new actionable classification;
- concise evidence;
- what human action/decision is needed;
- whether the finding is new, changed, or aged;
- any uncertainty such as unknown required-check policy.

Do not repeat an unchanged notification until the project-defined aging/escalation threshold is reached.

## State strategy

Prefer **no extra state** when live GitHub plus the delivery mechanism already prevents duplicate work.

If cross-run memory is needed, keep a lightweight namespaced watcher ledger containing only what is necessary, such as:
- PR identifier;
- last head SHA;
- last actionable classification;
- notification fingerprint/time;
- human override;
- aging baseline.

The ledger is not authoritative. Reconcile it with live GitHub each run.

## Budget / cost behavior

A1 should use a cheap discovery path and early exit.

Do not invoke coding agents, broad repository analysis, or expensive reviewers merely to report that nothing changed.

The adopting project should define a finite run/cost budget appropriate to its platform and expected PR volume.

If cost becomes disproportionate to actionable signal, slow, pause, or redesign the watcher.

## Safety and permissions

Recommended A1 permissions are read-only for repository state plus the minimum write permission needed for the chosen reporting destination, if any.

No merge permission is required.

No code mutation permission is required.

Protected areas are escalated, not acted upon.

## Success metrics

Measure at least:
- actionable findings / notifications;
- false-positive rate;
- duplicate-notification rate;
- mean time from new blocker/failure to human awareness;
- percentage of runs that quiet-exit;
- cost per actionable finding;
- findings that would have produced an unsafe action if A2 had existed.

Do not measure success by notification volume.

## Graduation

Run `skills/loop-readiness/SKILL.md` before considering A2.

A2 is not justified until A1 has demonstrated sufficiently reliable signal over a meaningful project-defined observation period.

If A2 is later approved, it must be a separate bounded work item with explicit failure classes, minimal mutation scope, finite attempts, systematic debugging where needed, independent verification, and human merge.

## Failure modes to watch

- missing checks interpreted as green;
- stale head SHA/state causing duplicate or wrong findings;
- repeated identical notifications;
- noise from non-required checks;
- stale PR threshold producing low-value nagging;
- broad repo scans on every tick;
- watcher scope silently expanding;
- classification narrative becoming speculative implementation advice.

A failure in watcher quality is a reason to tighten or pause A1, not to add more automation.
