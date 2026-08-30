from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

SKILL_FILES = [
    'skills/research-gate/SKILL.md',
    'skills/scrutinize/SKILL.md',
    'skills/systematic-debug/SKILL.md',
    'skills/independent-review/SKILL.md',
    'skills/postmortem/SKILL.md',
    'skills/technical-status/SKILL.md',
    'skills/long-task-guard/SKILL.md',
    'skills/loop-readiness/SKILL.md',
]

REQUIRED_FILES = [
    'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'ACKNOWLEDGEMENTS.md',
    'LICENSE', 'NOTICE', 'AGENTS.md', 'SKILL.md',
    'ENGINEERING_DEV_WORKFLOW.md', 'CONTEXT_MANAGEMENT.md', 'CONTINUOUS_OPERATIONS.md', 'MODEL_ROUTING_POLICY.md',
    'UX_UI_WORKFLOW.md', 'DEBUGGING_PROTOCOL.md', 'REVIEW_AND_SCRUTINY.md',
    'PARALLEL_EXECUTION.md', 'ACCEPTANCE_AND_EVIDENCE.md',
    'SECURITY_AND_GOVERNANCE.md', 'VERSIONING.md',
    'templates/PROJECT_PROFILE.md', 'templates/EXECUTION_CONTRACT.md',
    'templates/ACCEPTANCE_GATE.md', 'templates/EVIDENCE_PACKAGE.md',
    'templates/HANDOFF.md', 'templates/POSTMORTEM.md', 'templates/CODEX_PROMPT.md',
    'templates/LOOP_CONTRACT.md',
    'templates/CHATGPT_PROJECT_INSTRUCTIONS.md',
    '.github/pull_request_template.md',
    'scripts/setup_project.py', 'docs/installation.md', 'docs/quick-start.md',
    'docs/chatgpt-project-setup.md', 'docs/skill-system.md', 'patterns/pr-ci-watcher.md',
    'docs/research/loop-engineering-adoption-review.md', 'tests/test_setup_project.py',
    *SKILL_FILES,
]

COMMON_SKILL_HEADINGS = [
    '## Trigger conditions',
    '## Required inputs',
    '## Procedure',
    '## Output',
    '## Gate rules',
    '## Gotchas',
    '## Stop / escalation',
]

REQUIRED_HEADINGS = {
    'SKILL.md': [
        '## Core router', '## Focused skill routing', '## Mandatory scrutiny',
        '## Independent review', '## Continuous operations', '## Progressive disclosure', '## Control-plane rule'
    ],
    'ENGINEERING_DEV_WORKFLOW.md': ['## 4. Focused skills', '## 4A. Continuous operations outer layer', '## 5. End-to-end loop'],
    'CONTINUOUS_OPERATIONS.md': [
        '## 2. Autonomy levels', '## 4. Source of truth and operational state',
        '## 5. Budget and circuit breaker', '## 6. Notification policy',
        '## 7. Multi-loop coordination', '## 10. Graduation and rollback',
        '## 12. First v1.6 pilot'
    ],
    'CONTEXT_MANAGEMENT.md': [
        '## 1. Authoritative context hierarchy', '## 2. Load only what is relevant',
        '## 3. Choose continue vs fresh context deliberately', '## 4. Context isolation',
        '## 5. Checkpoints and handoffs', '## 6. Recover from context pollution',
        '## 7. Skill progressive disclosure', '## 8. Gotchas as learned context'
    ],
    'PARALLEL_EXECUTION.md': ['## Task-specific workers', '## Fresh-context reviewers', '## Integration'],
    'ACCEPTANCE_AND_EVIDENCE.md': ['## Deterministic enforcement', '## Independent review rule'],
    'CONTRIBUTING.md': ['## External inspiration and attribution'],
    'ACKNOWLEDGEMENTS.md': [
        '## Attribution principles', '## Current acknowledgements',
        '### thananon/9arm-skills', '### shanraisshan/claude-code-best-practice',
        '### cobusgreyling/loop-engineering', '## Future acknowledgements'
    ],
    '.github/pull_request_template.md': ['## Research / decision basis', '## Independent review', '## Review checklist'],
    'templates/EXECUTION_CONTRACT.md': [
        '## Objective', '## Scope', '## Out of scope', '## Research / decision basis',
        '## Execution routing', '## Context strategy', '## Independent review',
        '## Success gates', '## Stop conditions', '## Definition of done'
    ],
    'templates/ACCEPTANCE_GATE.md': ['## Research conditions', '## Gates', '## Independent review', '## Decision'],
    'templates/LOOP_CONTRACT.md': [
        '## Identity', '## Purpose', '## Autonomy', '## Authoritative source of truth',
        '## Operational state', '## Action boundary', '## Budget and circuit breaker',
        '## Notification', '## Pause / kill / recovery', '## Graduation criteria'
    ],
    'patterns/pr-ci-watcher.md': [
        '## Purpose', '## Non-goals', '## Authoritative sources',
        '## Observation and classification', '## Notification contract',
        '## Safety and permissions', '## Graduation'
    ],
    'templates/PROJECT_PROFILE.md': [
        '## Current accepted baseline', '## Architecture / invariants',
        '## Protected behavior', '## Validation matrix', '## Current next objective'
    ],
    'templates/CHATGPT_PROJECT_INSTRUCTIONS.md': ['## Control-plane role'],
    'MODEL_ROUTING_POLICY.md': ['## 3. Default routing', '## 5. Escalation', '## 8. Recommendation format'],
    'docs/installation.md': ['## 2. Inspect a target repository', '## 3. Install', '## 4. Validate', '## 5. Upgrade', '## 7. Ask Codex to install it'],
    'docs/chatgpt-project-setup.md': ['## 1. The important distinction', '## 2. Create a ChatGPT Project', '## 3. Bootstrap the target repository', '## 4. Start work from ChatGPT', '## 5. Invoke Codex only when needed'],
    'docs/skill-system.md': [
        '## 1. Relationship to the core workflow', '## 2. Skill routing',
        '## 3. Mandatory scrutiny gates', '## 4. Skills and ChatGPT/Codex roles',
        '## 5. Evidence discipline', '## 6. Progressive disclosure and skill structure',
        '## 7. External inspiration and licensing'
    ],
}
for skill_file in SKILL_FILES:
    REQUIRED_HEADINGS[skill_file] = COMMON_SKILL_HEADINGS

REQUIRED_TEXT = {
    'README.md': [
        'Current workflow version: **v1.6.0 baseline**.', 'License: **Apache-2.0**.',
        'CONTEXT_MANAGEMENT.md', 'skills/research-gate/SKILL.md',
        'skills/independent-review/SKILL.md', 'skills/loop-readiness/SKILL.md',
        'CONTINUOUS_OPERATIONS.md', 'patterns/pr-ci-watcher.md', 'ACKNOWLEDGEMENTS.md',
        'Apache License, Version 2.0'
    ],
    'ENGINEERING_DEV_WORKFLOW.md': [
        'Version: 1.6.0', 'skills/research-gate/SKILL.md',
        'skills/scrutinize/SKILL.md', 'skills/independent-review/SKILL.md',
        'CONTEXT_MANAGEMENT.md', 'CONTINUOUS_OPERATIONS.md', 'skills/loop-readiness/SKILL.md'
    ],
    'scripts/setup_project.py': ['WORKFLOW_VERSION = "1.6.0"', 'templates/LOOP_CONTRACT.md'],
    'ACKNOWLEDGEMENTS.md': [
        'https://github.com/thananon/9arm-skills', 'conceptual inspiration only',
        'no text, code, or skill implementation',
        'https://github.com/shanraisshan/claude-code-best-practice',
        'MIT License', 'Shayan Rais',
        'https://github.com/cobusgreyling/loop-engineering', 'Cobus Greyling'
    ],
    'CONTINUOUS_OPERATIONS.md': [
        'Operational state is **derived memory/cache/ledger**',
        '**New loop patterns start at A1 unless an explicit adoption record justifies otherwise.**',
        'Default: **silence on no-op**.'
    ],
    'skills/loop-readiness/SKILL.md': ['READY FOR A1', 'READY FOR A2', 'READY FOR A3', 'NOT READY'],
    'patterns/pr-ci-watcher.md': ['Autonomy: **A1 — Observe / report**', 'invoke automatic Codex/coding-agent remediation'],
    'ACCEPTANCE_AND_EVIDENCE.md': ['Prefer deterministic enforcement over instruction-only compliance'],
    'LICENSE': ['Apache License', 'Version 2.0, January 2004'],
    'NOTICE': ['Engineering Development Workflow', 'Copyright 2026 Kittipat Tangittinunt'],
}

errors = []
for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        errors.append(f'missing required file: {rel}')

for rel, headings in REQUIRED_HEADINGS.items():
    path = ROOT / rel
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8')
    for heading in headings:
        if heading not in text:
            errors.append(f'{rel}: missing heading {heading!r}')

for rel, snippets in REQUIRED_TEXT.items():
    path = ROOT / rel
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8')
    for snippet in snippets:
        if snippet not in text:
            errors.append(f'{rel}: missing required text {snippet!r}')

if errors:
    print('Repository validation FAILED')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'Repository validation PASS ({len(REQUIRED_FILES)} required files checked, {len(SKILL_FILES)} focused skills)')
