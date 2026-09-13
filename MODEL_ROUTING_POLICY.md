# Model Routing Policy

Version: 1.4.0

## 1. Objective

Minimize **cost to verified completion**, not merely token count, model price, number of attempts, or raw model capability.

Model capability, reasoning effort, and execution parallelism are separate routing axes.

The routing goal is to use the least expensive route that is still likely to produce a correct, reviewable, accepted result without avoidable retry or remediation cost. Product-surface quota/allowance burn is part of that cost when it constrains sustained work.

Do not maximize model tier or effort by default. A stronger setting is justified only when its expected improvement in completion probability, decision quality, or avoided rework is worth its incremental cost and allowance consumption.

## 2. Control-plane rule

Before invoking a coding agent, ChatGPT or the human lead should complete as much research, repo inspection, decomposition, architecture/UX reasoning, acceptance design, and prompt preparation as practical. This converts ambiguous work into bounded execution packets and increases the share of work that lower-cost models can complete reliably.

The control plane should reduce ambiguity before buying more model capability, more reasoning effort, or more parallel agents.

## 2A. Work mode first

Apply `WORK_MODE_ROUTING.md` before model selection.

Work mode and execution resources are separate axes:
- FAST often fits Luna Medium, or Luna High for a slightly broader but still low-risk bounded change;
- STANDARD often fits Luna High/Max, with Terra when materially more judgment is needed;
- STRICT does not automatically require Astra, Max, Ultra, or another premium route. After ChatGPT has completed high-risk reasoning and bounded the implementation, a lower-cost executor may still be appropriate if the execution itself is mechanical and strongly testable.

Do not use a stronger model, higher effort, or multi-agent execution as a substitute for scrutiny, evidence, workspace safety, or a clear packet.

## 3. Default routing

Current profile as of 2026-09-13; model availability, effort names, product-surface access, allowance accounting, capability, and economics can change and should be re-verified periodically.

- **Luna Medium** — small, direct, patterned work with strong tests and low ambiguity.
- **Luna High** — primary default for multi-file implementation with clear boundaries and established contracts.
- **Luna Max** — difficult or long execution that is well specified, testable, and bounded; use when deeper reasoning within Luna is likely to cross the reliability threshold without paying for a higher model tier.
- **Terra High/Max** — balanced escalation when a bounded task needs materially more judgment or cross-module synthesis than Luna, but does not justify the most capable premium route.
- **Astra Low/Medium, where available** — use when Astra-level capability is materially useful but the task does not require deep reasoning effort. This can be preferable to combining a premium model with unnecessarily high effort.
- **Astra High** — premium route for difficult end-to-end agentic execution spanning several of the following: code mutation, terminal work, browser/computer use, runtime integration, dependency work, performance investigation, and long multi-step follow-through.
- **Astra XHigh/Max** — reserve for the hardest end-to-end tasks where additional reasoning/verification materially reduces failure risk: ambiguous architecture, major migrations, difficult unknown-root-cause work, conflicting contracts/evidence, high-impact cross-system integration, or premium independent adjudication.
- **Sol** — valid premium fallback or continuity route when Astra is unavailable or usage-constrained, when preserving an existing productive Sol context materially lowers verified completion cost, or when task-specific evidence favors Sol. Choose Sol effort independently rather than automatically pairing a premium tier with Max.

Astra is not the default for routine implementation. Its higher capability is most valuable when the task shape actually uses its end-to-end strengths.

Do not assume that a higher model tier with lower effort is automatically better or worse than a lower tier with higher effort. Evaluate model tier, effort, context-reuse value, verification burden, likely retry cost, and allowance burn together.

## 3A. Dated economic guardrail

A user-supplied Codex credit schedule dated 2026-09-05 reported these per-1M-token rates:

| Model | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GPT-5.6 Luna | 5 credits | 0.5 credits | 30 credits |
| GPT-5.6 Terra | 50 credits | 5 credits | 300 credits |
| GPT-5.6 Sol | 100 credits | 10 credits | 500 credits |
| GPT-6 Astra | 250 credits | 25 credits | 1,250 credits |

Treat this table as a **dated economic snapshot, not timeless pricing**. Re-check the user's current product-surface pricing before making a cost-sensitive routing decision when rates may have changed.

Under this snapshot, relative to Luna:
- Terra is approximately 10x on input, cached input, and output;
- Sol is approximately 20x on input/cached input and 16.7x on output;
- Astra is approximately 50x on input/cached input and 41.7x on output.

Therefore, fewer retries alone do not justify a premium-model escalation. A premium route should be selected only when its expected capability advantage is large enough to change feasibility, materially reduce expensive rework, protect a high-impact decision, or avoid a failure mode that lower-cost routes are unlikely to overcome economically.

Do not reason as if two or three avoided Luna retries automatically justify Astra. With a large price ratio, many lower-cost attempts can still be cheaper in raw credits; the real decision must consider whether those attempts are likely to add useful evidence or merely repeat a capability-limited failure.

## 3B. Effort and Ultra guardrail

Treat reasoning effort as an independent budget decision after selecting a suitable model tier.

Use the **lowest available effort that is still likely to complete the bounded task correctly**. Increasing effort is appropriate when the same model probably has enough capability but needs more time for reasoning, verification, or search. Increasing model tier is appropriate when the capability threshold itself is the problem.

Do not escalate model tier and reasoning effort simultaneously unless both changes have separate task-specific justification. In particular, avoid jumps such as `Luna High -> Astra Max` merely because the task feels difficult.

As checked against OpenAI's GPT-5.6 product documentation on 2026-09-13, **Ultra is not just another ordinary single-agent reasoning notch**: it is described as a highest-capability mode that coordinates multiple agents in parallel by default and trades higher token use for stronger results and faster time-to-result on demanding tasks. Treat Ultra or any equivalent multi-agent premium mode as a separate parallelism multiplier, not as the routine successor to Max. Product behavior and availability may change; re-check the current surface before relying on this description.

Default rule for Ultra/multi-agent premium modes: **off unless explicitly justified**.

Use Ultra only when parallel exploration itself is valuable, for example:
- several materially different hypotheses or solution paths should be investigated concurrently;
- independent workstreams can be explored in parallel and synthesized into one high-impact decision;
- the task is research-grade or unusually ambiguous and a single-agent path is likely to miss important alternatives;
- faster wall-clock convergence has material value and the expected quality gain outweighs the higher allowance/token burn.

Do not use Ultra for:
- routine implementation, boilerplate, repetitive refactoring, fixture/test generation, or straightforward documentation;
- ordinary multi-file work that is already well specified;
- compensating for a vague execution packet;
- merely obtaining a slightly more polished answer;
- FAST work. If FAST appears to need Ultra, reassess the work-mode classification first.

## 4. Luna-first principle

For bounded implementation, refactoring with preserved contracts, test creation/repair, UI implementation against a clear UX specification, and debugging with a reliable reproducer, consider Luna first.

The strongest default pattern is often:

`ChatGPT plans -> Luna executes -> tests/CI produce evidence -> ChatGPT reviews`

Use Terra when the bounded work mainly needs more judgment. Use Astra when the work is materially end-to-end/agentic rather than simply difficult.

For high-volume implementation such as routine code edits, test generation, repetitive refactoring, documentation boilerplate, fixture creation, and iterative UI adjustments, prefer Luna or Terra unless there is task-specific evidence that a premium model is necessary.

## 4A. Astra-fit principle

Prefer Astra over repeated lower-tier retries when several of these are true:

- the task spans code mutation plus terminal/runtime/browser/computer interaction;
- execution is long and multi-step, with important state that must remain coherent across many tool calls;
- success requires integrating several technology stacks or environments;
- the agent must gather evidence, adapt to intermediate results, and continue to a verified end state;
- task-boundary adherence is important because adjacent future scope must remain blocked;
- runtime/performance/packaging/security evidence is part of the implementation itself rather than a separate simple test.

Do not use Astra merely because:
- the work mode is STRICT;
- the repository is large;
- the prompt is long;
- the task is routine but tedious;
- Luna has not yet been given a clear bounded packet;
- Astra is expected to be somewhat better or somewhat faster on the same strongly testable implementation task.

When Astra is selected, choose its effort independently. Start at the lowest effort expected to finish reliably; use High/XHigh/Max only when the task specifically benefits from deeper reasoning or verification.

## 4B. Premium-model leverage pattern

When the premium model is valuable for only part of the task, use it surgically rather than assigning the entire execution volume to it.

Preferred pattern:

`ChatGPT control plane -> premium diagnosis/architecture/orchestration -> bounded Luna/Terra execution -> tests/CI -> ChatGPT review`

Examples of high-leverage premium work:
- resolving contradictory architecture constraints before implementation;
- diagnosing an unknown-root-cause failure after lower-cost evidence gathering has stalled;
- defining a migration sequence where a wrong decision would create broad rework;
- coordinating a long cross-tool integration where state coherence is itself the hard part;
- independently adjudicating a high-impact design or remediation decision.

Examples of work that should normally return to Luna/Terra after the premium reasoning step:
- routine edits across already-identified files;
- bulk test or fixture implementation;
- repetitive API/client/schema updates with a fixed contract;
- ordinary documentation updates;
- straightforward UI implementation from an accepted specification.

This is the default **premium-as-surgeon** rule: spend premium capability on the narrow part where additional intelligence changes the outcome, then move execution volume back to the least expensive reliable worker.

## 4C. Allowance stop-loss and downgrade checkpoint

For premium or unusually high-effort execution, define a checkpoint before the run when practical. Good checkpoints include completion of diagnosis, architecture choice, migration plan, first bounded milestone, or proof that the premium capability is actually needed for the remaining work.

At that checkpoint, ask:
1. Has the hard reasoning/uncertainty been resolved?
2. Is the remaining work mostly mechanical, repetitive, or strongly testable?
3. Is observed quota/allowance burn materially higher than the value of continuing at the current setting?
4. Can the remaining execution be handed to Luna/Terra without losing critical context or correctness?

If yes, downgrade model tier, effort, parallelism, or a combination of them for the remaining work.

If premium/high-effort execution is consuming allowance rapidly without proportional progress, stop at a safe evidence checkpoint and reroute rather than continuing by inertia.

## 5. Escalation

Escalation is not a single linear ladder.

After a lower-tier failure, diagnose the failure class first:

- weak specification -> improve the packet;
- environment/tooling failure -> repair the environment/tooling;
- missing research/dependency evidence -> return to the research gate;
- same model likely sufficient but reasoning depth inadequate -> raise effort one justified step;
- bounded task needs materially more judgment -> consider Terra;
- long cross-tool/end-to-end agentic task exceeds Luna/Terra reliability -> consider Astra at the lowest sufficient effort;
- architecture/evidence remains materially contradictory or the hardest end-to-end reasoning is required -> consider Astra High/XHigh/Max and/or independent review;
- parallel exploration itself is the bottleneck -> consider Ultra/multi-agent mode only with explicit cost justification;
- Astra unavailable, quota-constrained, economically unjustified, or task-specific evidence favors prior-model continuity -> consider Sol or return to a lower-cost bounded route.

Do **not** use:

`Luna failed -> Astra Max/Ultra`

as an automatic rule.

Escalate only after determining that the problem is a capability/effort/parallelism mismatch rather than a weak specification, broken environment, undiscovered dependency, integration mistake, or context pollution.

A repeated lower-tier attempt should either test a new hypothesis, use a materially improved packet, or gather new evidence. Do not spend cheap-model credits on blind repetition merely because they are inexpensive.

## 6. Orchestrated execution

Use a premium orchestrator only when in-repository coordination itself is complex enough to justify it.

A useful pattern for large parallelizable work is:

`ChatGPT control plane -> premium technical orchestrator -> bounded Luna/Terra workers -> premium integration verification only when justified -> CI/evidence -> ChatGPT final review`

If Astra is unavailable or task-specific continuity favors Sol, Sol may serve the same orchestrator/adjudicator role.

The premium orchestrator should coordinate and adjudicate rather than spend premium capacity on routine edits that bounded workers can complete reliably.

Do not automatically bring a premium model back for integration verification if deterministic tests, CI, or a lower-cost reviewer already provide sufficient evidence.

Do not conflate an orchestrated execution plan with Ultra. Explicit worker orchestration can be bounded and selective; Ultra may multiply parallel agent usage at the product level. Choose each deliberately.

## 7. Retry and quota economics

Choose the route expected to minimize total verified cost including:
- initial execution;
- reasoning effort;
- parallel-agent/subagent usage where applicable;
- context rereads;
- retries;
- failed CI;
- merge conflict/reconciliation;
- human review;
- remediation;
- downstream rework caused by an incorrect architecture or implementation decision;
- loss of productive capacity caused by exhausting a product-surface quota/allowance window.

A cheaper worker that requires many retries can be more expensive than a stronger worker used once. Conversely, a premium worker or Ultra run on routine, strongly testable work can consume scarce allowance without improving verified completion.

For long work, include the value of context continuity in the routing decision. Preserving useful execution state can be cheaper than switching models and reconstructing the task, but continuity must not override the need for a fresh independent reviewer when independence is required.

Use the following decision order:
1. Can ChatGPT/control-plane work reduce ambiguity enough for Luna?
2. What is the cheapest model tier likely to cross the capability threshold?
3. Within that tier, what is the lowest effort likely to finish reliably?
4. Does parallelism add real value, or would a single agent be sufficient?
5. What is the expected quota/allowance burn relative to the importance and duration of the task?
6. If a premium/high-effort route is justified, where is the earliest safe downgrade checkpoint?
7. After the high-leverage step, can Luna/Terra perform the bulk execution?

## 8. Recommendation format

Whenever recommending Codex/coding-agent execution, state:
- work mode (FAST / STANDARD / STRICT) and rationale;
- workspace write boundary and whether any external write is explicitly approved;
- model;
- reasoning effort;
- Ultra/multi-agent/parallel mode: on or off, with explicit justification if on;
- existing chat or new chat;
- why this model tier is sufficient;
- why a higher tier is not currently required;
- why this effort level is sufficient and why a higher effort is not currently required;
- expected cost/allowance rationale when recommending Terra, Sol, Astra, Max, Ultra, or other materially expensive settings;
- if a premium model is selected, what property justifies it and whether its role can be narrowed to a high-leverage phase;
- downgrade checkpoint/trigger for premium or high-effort execution when practical;
- explicit escalation trigger, including whether the next escalation should change effort, model tier, parallelism, or work mode;
- fallback route if the preferred model/effort is unavailable or economically unattractive on the user's current product surface.
