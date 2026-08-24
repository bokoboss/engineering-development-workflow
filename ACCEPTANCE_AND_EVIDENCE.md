# Acceptance and Evidence

## Principle

Agent confidence is not evidence. Completion must be supported by the gates appropriate to the change.

## Gate classes

Possible gates include:
- G1 Functional / targeted tests
- G2 Regression
- G3 Contract / schema / compatibility
- G4 Engineering reference / numerical equivalence
- G5 UX / browser / accessibility / localization
- G6 Package / runtime / artifact
- G7 Performance / reliability
- G8 Security / privacy
- G9 CI
- G10 Human approval / UAT
- G11 Evidence completeness

Use only gates relevant to the change, but explicitly justify omitted high-risk gates.

## Gate record

Each non-trivial gate should identify:
- criterion;
- validation method or command;
- expected result;
- actual result;
- evidence/provenance;
- PASS / FAIL / BLOCKED / NOT APPLICABLE.

## Acceptance rule

A change is accepted only when all mandatory gates are PASS and mandatory approvals are present. BLOCKED is a valid outcome when required evidence cannot yet be obtained.

## Evidence hierarchy

Prefer reproducible evidence over prose summaries:
- test output and CI conclusions;
- deterministic fixtures/reference cases;
- browser/E2E results and screenshots where visual state matters;
- artifact hashes/diffs or export comparisons;
- real-data/UAT results;
- explicit engineering source references and decision records;
- exact commit/PR identifiers.
