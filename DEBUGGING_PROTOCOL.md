# Debugging Protocol

## 1. Reproduce first

Do not begin with speculative edits. Establish a reliable reproducer or state clearly why reproduction is impossible.

Capture:
- exact failing behavior;
- environment/runtime;
- input/fixture;
- expected vs actual;
- earliest known good/bad baseline where available.

## 2. Localize

Reduce the problem to the smallest subsystem or contract that explains the failure. Inspect logs, tests, state transitions, data provenance, and recent diffs before broad refactoring.

## 3. Form and test hypotheses

Prefer falsifiable hypotheses. Change one explanatory variable at a time when practical.

## 4. Fix root cause

Avoid masking symptoms with UI suppression, retries, broad dependency changes, or hard-coded special cases unless those are the intended design.

## 5. Regression proof

Add the smallest durable regression check that would have caught the defect before the fix. Run broader regression gates appropriate to blast radius.

## 6. Escalation

If a worker fails, classify whether the blocker is specification, environment, scope discovery, integration, missing evidence, or model capability before escalating model tier.

## 7. Postmortem threshold

Use `templates/POSTMORTEM.md` for defects that were high-impact, escaped prior gates, revealed a systemic weakness, or are likely to recur. Do not create ceremony for trivial one-off mistakes.
