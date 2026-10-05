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

Each worker receives only what it needs to act safely:
- objective and owned files/modules or decision surface;
- interfaces/contracts it may rely on and areas it must not modify;
- relevant research/scrutiny findings;
- success gates and validation commands;
- stop conditions and handoff format.

## Cost-aware worker model routing

Do not assume that a worker/subagent should inherit the orchestrator's model tier, reasoning effort, or parallel mode.

Route every worker through the current profile in `MODEL_ROUTING_POLICY.md`. Use the least expensive model/effort likely to finish that worker's bounded packet correctly. Do not duplicate the current model catalog here; model names, availability, effort support, and dated economics belong in the model-routing policy.

Default role pattern:
- use the current low-cost/default executor for narrow reconnaissance, patterned edits, fixtures, targeted tests, straightforward documentation, and other strongly verifiable work;
- use the current stronger workhorse when the worker itself needs materially more repository reasoning, debugging, integration judgment, or agentic follow-through;
- use the current top-tier/premium model only when that worker's own task independently meets the premium-routing criteria.

A stronger orchestrator should retain high-leverage reasoning, decomposition, ambiguity resolution, coordination, and adjudication while delegating routine execution downward only when that improves expected verified completion cost, time, quality, or risk. Do not retain a premium worker after the task has become routine or strongly testable.

## Delegation gate

Delegation must justify itself against a credible single-agent baseline. Do not assume that a cheaper worker makes the overall run cheaper.

Before spawning a worker, account for:
- worker execution/allowance cost;
- duplicated context/read cost;
- parent coordination and integration cost;
- verification/review cost;
- expected retries or remediation if the worker is below the reliability threshold;
- wall-clock benefit from genuinely useful parallelism.

If the expected benefit is unclear and the parent can complete the work reliably, prefer the single-agent path.

Do not delegate merely to create activity or parallelism. Minimize context transfer, and avoid recursive worker spawning by default. A worker should create more workers only when its packet explicitly permits it and the extra fan-out has a concrete cost/time/quality justification.

If the product surface cannot select a cheaper model for workers and effectively inherits the parent route, count that inherited allowance cost before spawning the worker.

Where runtime/session evidence exposes the effective worker model or effort, verify it when routing economics materially depend on that setting. Do not infer the serving model solely from an agent's natural-language self-identification.

## Fresh-context reviewers

Parallelism can also be used for **test-time review**, not only implementation. A fresh worker may review a plan, diff, or artifact without inheriting the executor's reasoning trail.

Use `skills/independent-review/SKILL.md` when this independence materially reduces acceptance risk. The reviewer may use the same model tier as the executor if that tier can reliably challenge the material risk; a stronger model is not automatically required.

Do not run multiple redundant reviewers by default. Add reviewers only when the incremental chance of catching a material problem justifies the extra context/read/reconciliation cost.

## Worktree / isolation

When supported and appropriate, isolate parallel implementation workers in separate branches/worktrees so file ownership and rollback remain clear. Isolation does not remove the need for explicit interface contracts or final integration testing.

## Integration

One owner is responsible for contract reconciliation, merge conflicts, cross-worker tests, and final integration evidence. For complex execution this can be a stronger coding-agent orchestrator; otherwise the primary worker or human/ChatGPT control plane is sufficient.

The integration owner must review the actual combined result. Passing worker-level gates independently does not prove that the integrated system passes its cross-module contracts.
