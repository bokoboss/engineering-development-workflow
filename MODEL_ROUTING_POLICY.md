# Model Routing Policy

Version: 1.5.0

Current model profile checked: 2026-10-05.

## 1. Objective

Minimize **cost to verified completion**, not token price, model prestige, number of attempts, or raw capability in isolation.

Model tier, reasoning effort, context strategy, and execution parallelism are separate decisions. Use the least expensive combination that is still likely to produce a correct, reviewable, accepted result without avoidable retry or remediation cost.

## 1A. Anti-churn maintenance rule

The durable contract is the routing logic in this file. Model names, effort support, availability, and pricing are a dated operational profile.

Do not rewrite the wider workflow every time a vendor releases or renames a model. Update the dated current profile only when the new information materially changes a routing decision. Change the policy version only when the normative decision rules change, not for a factual profile refresh.

Keep detailed current-model facts centralized here. Other workflow documents should refer to `MODEL_ROUTING_POLICY.md` instead of copying a model ladder or rate card. A new model does not justify a new gate, skill, workflow stage, or worker role by itself.

## 2. Control-plane rule

Before invoking a coding agent, ChatGPT or the human lead should complete as much research, repo inspection, decomposition, architecture/UX reasoning, acceptance design, and prompt preparation as practical.

The control plane should reduce ambiguity before buying more capability, more reasoning effort, or more parallel agents.

## 2A. Work mode first

Apply `WORK_MODE_ROUTING.md` before model selection.

Work mode controls process intensity; model routing controls execution capability and cost. FAST does not require the cheapest model, and STRICT does not require the most expensive model. A STRICT task may still have a mechanical, strongly testable implementation phase suitable for a low-cost executor after the high-risk decision has been resolved.

Do not use a stronger model, higher effort, or multi-agent execution as a substitute for a clear packet, evidence, workspace safety, or scrutiny.

## 3. Default routing

Current profile as of 2026-10-05:

- **GPT-6 Luna** — default low-cost executor for focused, bounded, high-volume work with clear contracts and strong verification. Current API docs expose reasoning efforts from `none` through `max`.
- **GPT-6.1 Sol** — primary stronger workhorse for complex coding, computer use, professional work, broad repository reasoning, nontrivial debugging/integration, and agentic execution that materially exceeds Luna's reliability threshold. OpenAI positions it as near-Astra performance at lower cost. Current API docs expose `low`, `medium`, `high`, `xhigh`, and `max`; `none`/`minimal` are not supported.
- **GPT-6 Sol** — older Sol model. Prefer GPT-6.1 Sol when available unless rollout/access, an already-productive context, or task-specific evidence makes continuity with GPT-6 Sol cheaper to verified completion.
- **GPT-6 Astra** — top-tier route for the hardest end-to-end work where additional capability materially changes feasibility or risk: ambiguous architecture, major migrations, difficult unknown-root-cause work across systems, conflicting evidence/contracts, high-impact cross-system integration, or premium adjudication.
- **Other exposed models** — may be used when current product-surface economics or capability make them preferable, but they are not mandatory rungs in the default route.

This is not an automatic ladder. A bounded task should usually start with Luna. A materially harder coding/agentic task should usually consider GPT-6.1 Sol before Astra. Use Astra only when the task itself has a credible Astra-fit reason.

Do not assume that a higher model tier with lower effort is automatically better or worse than a lower tier with higher effort. Evaluate task shape, verification strength, context-reuse value, likely retry/remediation cost, and current allowance economics together.

## 3A. Dated economic guardrail

As checked against official OpenAI model documentation on 2026-10-05, Standard API short-context pricing per 1M tokens is approximately:

| Model | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |
| GPT-6 Sol | $2.00 | $0.20 | $10.00 |
| GPT-6.1 Sol | $2.00 | $0.10 | $10.00 |
| GPT-6 Astra | $10.00 | $1.00 | $50.00 |

These are **API prices, not Codex subscription allowance/credit prices**. Do not translate them directly into ChatGPT Work/Codex quota consumption.

The earlier user-supplied Codex credit schedule dated 2026-09-05 applied to GPT-5.6-era routes plus GPT-6 Astra. It remains historical evidence only; **do not map those old GPT-5.6 credit rates onto GPT-6 Luna or GPT-6 Sol** or GPT-6.1 Sol.

Under the current API snapshot, GPT-6.1 Sol has the same standard input/output price as GPT-6 Sol and a lower cached-input price, while Astra remains substantially more expensive. That strengthens the default case for trying GPT-6.1 Sol before Astra when the problem is still primarily coding/agentic work.

Long-context and product-surface pricing can change the economics. Re-check the current rate card / usage surface before a cost-sensitive recommendation.

Sources checked 2026-10-05:
- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/models/gpt-6-sol
- https://developers.openai.com/api/docs/models/gpt-6-luna
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- https://developers.openai.com/api/docs/changelog

## 3B. Effort, parallelism, and service modes

Select model tier first, then use the lowest reasoning effort likely to finish the bounded task correctly.

Raise effort when the same model probably has enough capability but needs deeper reasoning/verification. Raise model tier when the capability threshold itself is the problem. Do not escalate tier and effort together without separate reasons.

Treat parallelism and service tiers as separate axes:
- multi-agent/subagent execution is off by default unless independent workstreams or hypothesis exploration justify the coordination cost;
- GPT-6.1 Sol Multi-agent is currently an API beta capability; do not assume identical behavior or allowance accounting in every Codex/Work surface;
- GPT-6 Astra `ultrafast` is an API service tier for latency, not a reasoning tier or a reason to select Astra for work that does not otherwise need it.

Do not add product-specific parallel/service modes to the core workflow unless they change the actual routing or safety contract.

## 4. Default execution pattern

For bounded implementation, refactoring with preserved contracts, test creation/repair, straightforward UI implementation, and debugging with a reliable reproducer, prefer the current low-cost/default executor.

A common pattern is:

`ChatGPT plans -> cheapest reliable executor -> tests/CI -> ChatGPT review`

Use the stronger workhorse when broader repository reasoning, cross-module debugging, integration judgment, or agentic follow-through materially improves completion probability. Use the top-tier model surgically for the high-leverage part when its additional capability changes the outcome, then return routine execution to a cheaper route.

Do not use a premium model merely because the repo is large, the prompt is long, the task is STRICT, or the work is tedious.

## 5. Escalation

Escalation is diagnosis-driven, not a fixed ladder.

After a failed attempt, classify the failure first:

- weak specification -> improve the packet;
- environment/tooling failure -> repair the environment/tooling;
- missing research/dependency evidence -> return to the research gate;
- same model likely sufficient but reasoning depth inadequate -> raise effort one justified step;
- bounded task exceeds the current low-cost model's reliability threshold -> consider the current stronger workhorse;
- difficult coding/agentic work still appears within GPT-6.1 Sol capability -> raise Sol effort before jumping to Astra when justified;
- long, ambiguous, cross-tool/end-to-end work exceeds the stronger workhorse or independently matches Astra-fit criteria -> consider Astra at the lowest sufficient effort;
- parallel exploration itself is the bottleneck -> consider multi-agent execution only with explicit benefit and cost justification.

Do not use `cheap model failed -> Astra Max` as an automatic rule. A repeated attempt must test a new hypothesis, use a materially improved packet, or gather new evidence.

## 6. Orchestration and workers

Use a stronger orchestrator only when coordination itself is hard enough to justify it. Route each worker independently through this policy rather than automatically inheriting the parent model/effort.

Delegate routine volume only when the worker packet is bounded, independently verifiable, and cheap enough to offset coordination/context duplication. Prefer a single agent when delegation creates more rereading, integration, or repair than it saves.

Do not recursively spawn workers by default. `PARALLEL_EXECUTION.md` contains the worker/delegation contract; this file remains the authoritative source for current model choice.

## 7. Cost, downgrade, and closure

Choose the route expected to minimize total verified cost including execution, context rereads, retries, failed CI, reconciliation, human review, remediation, downstream rework, and quota/allowance exhaustion.

For expensive/high-effort execution, define one practical downgrade checkpoint when useful: after diagnosis, architecture choice, migration plan, or the first bounded milestone. If the hard uncertainty is resolved and the remaining work is mechanical or strongly testable, step down model tier, effort, parallelism, or a combination of them.

Do not keep reviewing or escalating after the selected work mode's mandatory gates are satisfied. Once the requested outcome is verified and no BLOCKER/REQUIRED finding remains, close the task. Optional polish becomes follow-up work.

## 8. Recommendation format

Whenever recommending Codex/coding-agent execution, state:
- work mode and workspace write boundary;
- model and reasoning effort;
- parallel/multi-agent mode on or off;
- existing or fresh context when that choice matters;
- why this route is sufficient and why a higher route is not currently required;
- success gates and stop conditions;
- escalation trigger if the route fails;
- downgrade checkpoint when using a materially expensive/high-effort route.

Do not include a long model-comparison essay when the routing decision is obvious. The recommendation should be just detailed enough to explain and execute the choice.
