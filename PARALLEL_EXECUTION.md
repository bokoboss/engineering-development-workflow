# Parallel Execution

Parallel agents primarily reduce elapsed time; they do not automatically reduce credits or total work.

## Parallelize only when

- workstreams are genuinely independent;
- file/module ownership can be separated;
- interfaces/contracts are already defined;
- each worker has its own success gate;
- integration order and owner are explicit;
- duplicated repository reading/reasoning is outweighed by the benefit.

## Avoid

Do not spawn multiple agents to independently solve the same vaguely defined problem by default. This duplicates context, creates conflicting implementations, and increases reconciliation cost.

Do not use generic role names as a substitute for task definition. `backend engineer`, `QA agent`, or `reviewer` is weaker than a worker packet that names the concrete outcome, owned surface, preserved contracts, and evidence required.

## Task-specific workers

Prefer workers shaped around the actual bounded task or feature slice, for example:
- `excel-direction-mapping-investigator` rather than generic `data engineer`;
- `checkout-flow-verifier` rather than generic `QA`;
- `schema-migration-reviewer` rather than generic `reviewer`.

The name itself is not important; the principle is that the worker's context and tools should be optimized for one explicit objective rather than a broad job title.

Where the execution environment supports it, preload only the focused skills/domain references relevant to that worker. Apply `CONTEXT_MANAGEMENT.md` so unrelated project history does not occupy the worker's context.

## Worker packet

Each worker receives:
- objective;
- owned files/modules or decision surface;
- interfaces it may rely on;
- files/areas it must not modify;
- relevant research/scrutiny findings;
- success gates;
- validation commands;
- stop conditions;
- handoff format.

## Cost-aware worker model routing

Do not assume that a worker/subagent should inherit the orchestrator's model tier, reasoning effort, or parallel mode.

Where the execution surface supports per-worker model selection, route each worker independently using `MODEL_ROUTING_POLICY.md` and choose the least expensive model/effort likely to finish that bounded packet correctly. Specify both the worker model and reasoning effort explicitly when the surface allows it; omitted settings may inherit from the parent/orchestrator.

Default worker pattern:
- **Luna** for narrow or targeted reconnaissance against known files/symbols, targeted code reading, mechanical or patterned edits, fixtures, targeted tests, straightforward documentation, and other well-specified work with strong verification;
- **Terra** for broad or initially unknown repository exploration, read-heavy scans across many files, cross-module synthesis, or bounded debugging where materially more judgment/reliability is needed than Luna;
- **Sol/Astra or another premium model** only when that worker's own task independently meets the premium-routing criteria. Do not use a premium worker merely because the parent/orchestrator is premium.

A premium orchestrator should retain high-leverage reasoning, decomposition, ambiguity resolution, cross-worker coordination, and adjudication while delegating routine execution volume downward only when doing so improves expected verified completion cost, time, quality, or risk.

## Delegation gate

Delegation must justify itself against a credible single-agent baseline. Do not assume that a cheaper worker makes the overall run cheaper.

Before spawning a worker, account for:
- worker execution cost and allowance burn;
- duplicated context/read cost;
- parent/orchestrator coordination and integration cost;
- verification and review cost;
- expected retries, regressions, and remediation if the worker is below the reliability threshold;
- wall-clock benefit from genuinely useful parallelism.

If the expected benefit is unclear and the parent can complete the work reliably, prefer the single-agent path. A cheap worker that causes the parent to reread, repair, or redo substantial work is not a saving.

Do not delegate merely to create activity or parallelism. A worker should have a bounded objective, a useful evidence return, and coordination overhead low enough to justify the delegation.

Minimize context transfer. Send the worker the smallest packet that contains the contracts, files, evidence, and success gates it actually needs instead of copying the entire parent context. Large duplicated context can erase the quota savings from using a cheaper worker.

Avoid recursive worker spawning by default. A worker should not create additional workers unless its packet explicitly permits it and the extra fan-out has a concrete cost/time/quality justification.

If the product surface cannot select a cheaper model for workers and would effectively inherit the premium parent route, include that inherited allowance cost in the decision whether to spawn the worker at all.

Where runtime/session evidence exposes the effective worker model or effort, verify it when routing economics materially depend on that setting. Do not infer the actual serving model solely from an agent's natural-language self-identification.

## Fresh-context reviewers

Parallelism can also be used for **test-time review**, not only implementation. A fresh worker may review a plan, diff, or artifact without inheriting the executor's reasoning trail.

Use `skills/independent-review/SKILL.md` when this independence materially reduces acceptance risk. The reviewer may use the same model tier as the executor if the task is within that tier's capability; a stronger model is not automatically required.

Do not run multiple redundant reviewers by default. Add reviewers only when the incremental chance of catching a material problem justifies the extra context/read/reconciliation cost.

## Worktree / isolation

When supported and appropriate, isolate parallel implementation workers in separate branches/worktrees so file ownership and rollback remain clear. Isolation does not remove the need for explicit interface contracts or final integration testing.

## Integration

One owner is responsible for contract reconciliation, merge conflicts, cross-worker tests, and final integration evidence. For complex execution this can be a stronger coding-agent orchestrator; otherwise the primary worker or human/ChatGPT control plane is sufficient.

The integration owner must review the actual combined result. Passing worker-level gates independently does not prove that the integrated system passes its cross-module contracts.
