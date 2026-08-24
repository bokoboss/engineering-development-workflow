# Example — Bounded Feature

Scenario: add a new export column without changing calculation logic.

Recommended route:
- ChatGPT inspects current export contract, tests, and downstream compatibility.
- Define exact column name/order, null semantics, and regression tests.
- Use Luna Medium or High depending on file spread.
- Required gates: targeted export test, regression suite, artifact comparison, CI.
- Escalate only if implementation reveals unexpected schema coupling or ambiguous compatibility requirements.

Why: the problem is bounded, objectively testable, and does not require premium architecture reasoning.
