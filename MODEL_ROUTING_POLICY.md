# Model Routing Policy

Version: 1.5.0

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
- FAST often fits GPT-6 Luna Medium, or GPT-6 Luna High for a slightly broader but still low-risk bounded change;
- STANDARD often fits GPT-6 Luna High/Max. Escalate to GPT-6 Sol when the bounded task materially needs stronger coding judgment, cross-module reasoning, debugging reliability, or agentic follow-through. GPT-5.6 Terra may remain an economical middle route where it is exposed and current product-surface economics favor it;
- STRICT does not automatically require GPT-6 Astra, GPT-6 Sol, Max, Ultra, or another premium route. After ChatGPT has completed high-risk reasoning and bounded the implementation, a lower-cost executor may still be appropriate if the execution itself is mechanical and strongly testable.

Do not use a stronger model, higher effort, or multi-agent execution as a substitute for scrutiny, evidence, workspace safety, or a clear packet.

## 3. Default routing

Current profile as of 2026-09-23. OpenAI announced GPT-6 Sol and GPT-6 Luna on 2026-09-22; both are rolling out in Codex and are available in the API. Model availability, effort names, product-surface access, allowance accounting, capability, and economics can change and should be re-verified periodically.

- **GPT-6 Luna Medium** — default for small, direct, patterned work with strong tests and low ambiguity.
- **GPT-6 Luna High** — primary default for multi-file implementation with clear boundaries and established contracts.
- **GPT-6 Luna Max** — difficult or long execution that is still well specified, testable, and bounded; use when deeper reasoning within Luna is likely to cross the reliability threshold without paying for a stronger model tier.
- **GPT-5.6 Terra High/Max, where available** — optional intermediate route when current product-surface pricing/allowance makes it economically attractive and the task needs more judgment than Luna. Do not prefer Terra merely because it occupied the historical middle tier.
- **GPT-6 Sol Medium/High** — primary stronger workhorse for complex coding and agentic workflows: broad repository reasoning, cross-module debugging, nontrivial integration, or implementation that materially exceeds Luna's reliability threshold but does not independently require Astra.
- **GPT-6 Sol XHigh/Max** — use for difficult or high-impact coding/agentic work when Sol likely has the required capability but deeper reasoning or verification is justified. Prefer this before Astra when the remaining problem is still predominantly coding/agentic rather than the hardest ambiguous end-to-end work.
- **GPT-6 Astra Low/Medium, where available** — use when Astra-level capability is materially useful but the task does not require deep reasoning effort.
- **GPT-6 Astra High** — premium route for the hardest end-to-end agentic execution spanning several of the following: code mutation, terminal work, browser/computer use, runtime integration, dependency work, performance investigation, research, and long multi-step follow-through.
- **GPT-6 Astra XHigh/Max** — reserve for the hardest work where additional reasoning/verification materially reduces failure risk: ambiguous architecture, major migrations, difficult unknown-root-cause work, conflicting contracts/evidence, high-impact cross-system integration, or premium independent adjudication.

OpenAI's current model docs list `none`, `low`, `medium`, `high`, `xhigh`, and `max` for GPT-6 Luna and GPT-6 Sol, with Medium as the API default. GPT-6 Astra supports `low` through `max`.

GPT-6 Sol is no longer merely a fallback/continuity route. It is the default stronger workhorse between GPT-6 Luna and GPT-6 Astra when the current execution surface makes it available and economically reasonable.

GPT-6 Astra is not the default for routine implementation. Its higher capability is most valuable when the task shape actually uses its hardest end-to-end strengths.

Do not assume that a higher model tier with lower effort is automatically better or worse than a lower tier with higher effort. Evaluate model tier, effort, context-reuse value, verification burden, likely retry cost, and allowance burn together.

## 3A. Dated economic guardrail

As checked against official OpenAI model documentation on 2026-09-23, Standard API short-context token pricing per 1M tokens is:

| Model | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |
| GPT-5.6 Terra | $2.00 | $0.20 | $12.00 |
| GPT-6 Sol | $2.00 | $0.20 | $10.00 |
| GPT-6 Astra | $10.00 | $1.00 | $50.00 |

These are **API prices, not Codex subscription allowance/credit prices**. Do not translate them directly into Plus/Pro/Business Work or Codex quota consumption.

Relative to GPT-6 Luna under this API snapshot:
- GPT-5.6 Terra is approximately 20x on input/cached input and 24x on output;
- GPT-6 Sol is approximately 20x on input, cached input, and output;
- GPT-6 Astra is approximately 100x on input, cached input, and output;
- GPT-6 Astra is approximately 5x GPT-6 Sol on those token-price dimensions.

The earlier user-supplied Codex credit schedule dated 2026-09-05 applied to GPT-5.6 Luna/Terra/Sol and GPT-6 Astra. It is historical evidence only; **do not map those old GPT-5.6 credit rates onto GPT-6 Luna or GPT-6 Sol**. OpenAI's 2026-09-22 announcement states that GPT-6 Sol and GPT-6 Luna have 50% lower API prices than their GPT-5.6 promotional counterparts, but that statement does not by itself define current subscription allowance burn. Re-check the current product rate card / usage surface before a cost-sensitive Codex recommendation.

Long-context pricing can also change economics materially. Current GPT-6 Luna/Sol/Astra model pages apply higher rates when prompts exceed 272K input tokens, so lean-context policy remains a cost control rather than merely a latency optimization.

Sources checked 2026-09-23:
- https://developers.openai.com/api/docs/models/gpt-6-luna
- https://developers.openai.com/api/docs/models/gpt-6-sol
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://developers.openai.com/api/docs/models/gpt-5.6-terra
- https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna/1399925

Therefore, fewer retries alone do not justify a stronger-model escalation. Select GPT-6 Sol or GPT-6 Astra only when the expected capability advantage is large enough to change feasibility, materially reduce expensive rework, protect a high-impact decision, or avoid a failure mode that cheaper routes are unlikely to overcome economically.

Do not reason as if two or three avoided GPT-6 Luna retries automatically justify GPT-6 Astra. The real decision must consider whether lower-cost attempts are likely to add useful evidence or merely repeat a capability-limited failure, and must use the current execution surface's actual allowance economics rather than stale model-price assumptions.

## 3B. Effort and Ultra guardrail

Treat reasoning effort as an independent budget decision after selecting a suitable model tier.

Use the **lowest available effort that is still likely to complete the bounded task correctly**. Increasing effort is appropriate when the same model probably has enough capability but needs more time for reasoning, verification, or search. Increasing model tier is appropriate when the capability threshold itself is the problem.

Do not escalate model tier and reasoning effort simultaneously unless both changes have separate task-specific justification. In particular, avoid jumps such as `Luna High -> Astra Max` merely because the task feels difficult.

Treat **Ultra or any equivalent product-level multi-agent premium mode** as a separate parallelism multiplier, not as a model tier or the routine successor to Max. Product behavior, worker inheritance, and allowance accounting can change; re-check the current Codex surface before relying on a specific implementation.

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

## 4. GPT-6 Luna-first principle

For bounded implementation, refactoring with preserved contracts, test creation/repair, UI implementation against a clear UX specification, and debugging with a reliable reproducer, consider GPT-6 Luna first.

The strongest default pattern is often:

`ChatGPT plans -> GPT-6 Luna executes -> tests/CI produce evidence -> ChatGPT reviews`

Use GPT-6 Sol when the bounded work materially needs stronger coding judgment, broad repository reasoning, cross-module debugging, or agentic follow-through than Luna. GPT-5.6 Terra remains an optional middle route only where current product-surface economics and task evidence make it preferable. Use GPT-6 Astra when the task independently meets Astra-fit criteria rather than merely being difficult.

For high-volume implementation such as routine code edits, test generation, repetitive refactoring, documentation boilerplate, fixture creation, and iterative UI adjustments, prefer GPT-6 Luna. Escalate to GPT-6 Sol only when the task's reliability threshold requires it.

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
- GPT-6 Luna has not yet been given a clear bounded packet;
- Astra is expected to be somewhat better or somewhat faster on the same strongly testable implementation task.

When GPT-6 Astra is selected, choose its effort independently. Start at the lowest effort expected to finish reliably; use High/XHigh/Max only when the task specifically benefits from deeper reasoning or verification. When the hard part is still mainly coding/agentic execution, test GPT-6 Sol fit before paying Astra's substantially higher current API price.

## 4B. Premium-model leverage pattern

When the premium model is valuable for only part of the task, use it surgically rather than assigning the entire execution volume to it.

Preferred pattern:

`ChatGPT control plane -> premium diagnosis/architecture/orchestration -> bounded GPT-6 Luna/GPT-6 Sol execution -> tests/CI -> ChatGPT review`

Examples of high-leverage premium work:
- resolving contradictory architecture constraints before implementation;
- diagnosing an unknown-root-cause failure after lower-cost evidence gathering has stalled;
- defining a migration sequence where a wrong decision would create broad rework;
- coordinating a long cross-tool integration where state coherence is itself the hard part;
- independently adjudicating a high-impact design or remediation decision.

Examples of work that should normally return to GPT-6 Sol or GPT-6 Luna after the Astra-level reasoning step:
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
4. Can the remaining execution be handed down to GPT-6 Sol or GPT-6 Luna (or GPT-5.6 Terra where it is economically preferable) without losing critical context or correctness?

If yes, downgrade model tier, effort, parallelism, or a combination of them for the remaining work.

If premium/high-effort execution is consuming allowance rapidly without proportional progress, stop at a safe evidence checkpoint and reroute rather than continuing by inertia.

## 5. Escalation

Escalation is not a single linear ladder.

After a lower-tier failure, diagnose the failure class first:

- weak specification -> improve the packet;
- environment/tooling failure -> repair the environment/tooling;
- missing research/dependency evidence -> return to the research gate;
- same model likely sufficient but reasoning depth inadequate -> raise effort one justified step;
- bounded task exceeds GPT-6 Luna's reliability threshold -> consider GPT-6 Sol; GPT-5.6 Terra is an optional intermediate only when current surface economics and task evidence favor it;
- difficult coding/agentic work likely remains within GPT-6 Sol capability -> raise Sol effort before jumping to Astra when justified;
- long, ambiguous, cross-tool/end-to-end work exceeds GPT-6 Sol reliability or independently matches Astra-fit criteria -> consider GPT-6 Astra at the lowest sufficient effort;
- architecture/evidence remains materially contradictory or the hardest end-to-end reasoning is required -> consider GPT-6 Astra High/XHigh/Max and/or independent review;
- parallel exploration itself is the bottleneck -> consider Ultra/multi-agent mode only with explicit cost justification;
- GPT-6 Astra is unavailable, quota-constrained, or economically unjustified -> remain on GPT-6 Sol or return to a lower-cost bounded route rather than treating a prior-generation model as an automatic fallback.

Do **not** use:

`GPT-6 Luna failed -> GPT-6 Astra Max/Ultra`

as an automatic rule.

Escalate only after determining that the problem is a capability/effort/parallelism mismatch rather than a weak specification, broken environment, undiscovered dependency, integration mistake, or context pollution.

A repeated lower-tier attempt should either test a new hypothesis, use a materially improved packet, or gather new evidence. Do not spend cheap-model credits on blind repetition merely because they are inexpensive.

## 6. Orchestrated execution

Use a premium orchestrator only when in-repository coordination itself is complex enough to justify it.

A useful pattern for large parallelizable work is:

`ChatGPT control plane -> GPT-6 Sol technical orchestrator when justified -> bounded GPT-6 Luna workers -> GPT-6 Astra only for independently Astra-fit orchestration/adjudication -> CI/evidence -> ChatGPT final review`

Use GPT-6 Sol as the normal stronger orchestrator before GPT-6 Astra when coordination is complex but still primarily software-engineering work. Use GPT-6 Astra as orchestrator/adjudicator only when the coordination problem itself meets Astra-fit criteria.

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
1. Can ChatGPT/control-plane work reduce ambiguity enough for GPT-6 Luna?
2. What is the cheapest model tier likely to cross the capability threshold?
3. Within that tier, what is the lowest effort likely to finish reliably?
4. Does parallelism add real value, or would a single agent be sufficient?
5. What is the expected quota/allowance burn relative to the importance and duration of the task?
6. If a premium/high-effort route is justified, where is the earliest safe downgrade checkpoint?
7. After the high-leverage step, can GPT-6 Sol or GPT-6 Luna perform the bulk execution?

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
