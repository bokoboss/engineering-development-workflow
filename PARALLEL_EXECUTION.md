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

## Worker packet

Each worker receives:
- objective;
- owned files/modules;
- interfaces it may rely on;
- files/areas it must not modify;
- success gates;
- validation commands;
- stop conditions;
- handoff format.

## Integration

One owner is responsible for contract reconciliation, merge conflicts, cross-worker tests, and final integration evidence. For complex execution this can be a stronger coding-agent orchestrator; otherwise the primary worker or human/ChatGPT control plane is sufficient.
