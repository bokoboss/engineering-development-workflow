# Review and Scrutiny

## Pre-implementation scrutiny

Required for architectural changes, major UX/workflow changes, engineering methodology, safety/security-sensitive behavior, migrations, broad refactors, or expensive long-running work.

Ask:
- Is the problem correctly framed?
- What assumptions are unproven?
- What contracts/invariants can be broken?
- Is the proposed scope minimal but sufficient?
- Are there simpler alternatives?
- Are success gates capable of detecting the important failure modes?
- Does the proposed model/effort match risk and ambiguity?

## Pre-merge review

Review the actual diff and evidence against the work order.

Order:
1. scope and intent;
2. behavior/correctness;
3. protected engineering logic and data contracts;
4. regression risk;
5. tests and evidence quality;
6. UX/error recovery/accessibility when relevant;
7. security/privacy/secrets;
8. maintainability and documentation;
9. cosmetic polish.

A passing CI run is necessary when required but not sufficient if the tests do not cover the acceptance contract.

## Fresh-context review

Use a fresh reviewer when confirmation bias or long-context contamination is a material risk. This is particularly valuable for methodology changes, release qualification, and contentious root-cause conclusions.
