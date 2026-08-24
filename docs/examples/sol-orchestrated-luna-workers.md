# Example — Sol Orchestrator with Luna Workers

Scenario: a large feature has independent backend, frontend, and browser-test workstreams, while integration touches several contracts.

Control plane:
1. ChatGPT/human lead defines architecture, interfaces, ownership, and success gates.
2. Sol is used only if in-repo orchestration and integration judgment are materially complex.
3. Luna workers receive bounded ownership:
   - Worker A: backend module and backend tests.
   - Worker B: frontend module and component tests.
   - Worker C: browser/E2E coverage only after interface fixtures are fixed.
4. Sol reconciles integration and runs cross-workstream gates.
5. ChatGPT/human lead reviews PR, CI, and evidence.

Do not use this pattern when one Luna worker could finish the entire bounded change reliably; orchestration itself has cost.
