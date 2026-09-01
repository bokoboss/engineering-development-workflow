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
    'ENGINEERING_DEV_WORKFLOW.md', 'WORK_MODE_ROUTING.md', 'WORKSPACE_SAFETY.md',
    'CONTEXT_MANAGEMENT.md', 'CONTINUOUS_OPERATIONS.md', 'MODEL_ROUTING_POLICY.md',
    'UX_UI_WORKFLOW.md', 'DEBUGGING_PROTOCOL.md', 'REVIEW_AND_SCRUTINY.md',
    'PARALLEL_EXECUTION.md', 'ACCEPTANCE_AND_EVIDENCE.md',
    'SECURITY_AND_GOVERNANCE.md', 'VERSIONING.md', 'docs/CHEAT_SHEET.md',
    'templates/PROJECT_PROFILE.md', 'templates/EXECUTION_CONTRACT.md',
    'templates/ACCEPTANCE_GATE.md', 'templates/EVIDENCE_PACKAGE.md',
    'templates/HANDOFF.md', 'templates/POSTMORTEM.md', 'templates/CODEX_PROMPT.md',
    'templates/FAST_EXECUTION_PACKET.md', 'templates/LOOP_CONTRACT.md',
    'templates/CHATGPT_PROJECT_INSTRUCTIONS.md',
    '.github/pull_request_template.md', '.github/workflows/validate.yml',
    'scripts/setup_project.py', 'docs/installation.md', 'docs/quick-start.md',
    'docs/chatgpt-project-setup.md', 'docs/skill-system.md', 'patterns/pr-ci-watcher.md',
    'docs/research/loop-engineering-adoption-review.md',
    'docs/research/local-workspace-evidence-bridge-adoption-review.md',
    'tests/test_setup_project.py',
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
        '## Core router', '## Focused skill routing', '## Work mode routing', '## Workspace safety',
        '## Mandatory scrutiny', '## Independent review', '## Continuous operations', '## Progressive disclosure', '## Control-plane rule'
    ],
    'ENGINEERING_DEV_WORKFLOW.md': ['## 3A. Work mode and workspace safety', '## 4. Focused skills', '## 4A. Continuous operations outer layer', '## 5. End-to-end loop'],
    'WORK_MODE_ROUTING.md': [
        '## 1. Common quality floor', '## 2. STRICT triggers', '## 3. FAST eligibility',
        '## 4. STANDARD mode', '## 5. Dynamic escalation', '## 8. Evidence reuse',
        '## 9. Required routing output', '## 11. Safety override'
    ],
    'SECURITY_AND_GOVERNANCE.md': [
        '## Protected changes', '## Secrets and private data',
        '## Licensed and restricted references', '## Tool and remote-agent boundary',
        '## Human approval'
    ],
    'SECURITY_AND_GOVERNANCE.md': [
        '`WORKSPACE_SAFETY.md` is normative for local filesystem/system boundaries and applies to every work mode.',
        'Never commit credentials, tokens, personal secrets, production private data, or temporary debug artifacts containing them.',
        'Default local write authority is the explicit target project root only; external/system writes require explicit human approval under `WORKSPACE_SAFETY.md`.',
        'Human approval is a design control, not a failure of automation.'
    ],
    'WORKSPACE_SAFETY.md': [
        '## 1. Default filesystem authority', '## 2. Forbidden external mutations by default',
        '## 5. Symlink / junction / reparse-point safety', '## 6. External-write approval protocol',
        '## 10. Installer boundary', '## 11. Stop conditions', '## 12. Completion evidence'
    ],
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
    'ACCEPTANCE_AND_EVIDENCE.md': ['## Evidence reuse', '## Deterministic enforcement', '## Independent review rule'],
    'CONTRIBUTING.md': ['## External inspiration and attribution'],
    'ACKNOWLEDGEMENTS.md': [
        '## Attribution principles', '## Current acknowledgements',
        '### thananon/9arm-skills', '### shanraisshan/claude-code-best-practice',
        '### cobusgreyling/loop-engineering', '### XiaoDuoYa/codex-with-chatgpt', '## Future acknowledgements'
    ],
    '.github/pull_request_template.md': ['## Research / decision basis', '## Independent review', '## Review checklist'],
    'templates/EXECUTION_CONTRACT.md': [
        '## Work mode', '## Workspace safety', '## Objective', '## Scope', '## Out of scope', '## Research / decision basis',
        '## Execution routing', '## Context strategy', '## Independent review',
        '## Success gates', '## Evidence reuse', '## Stop conditions', '## Definition of done'
    ],
    'templates/FAST_EXECUTION_PACKET.md': [
        '## Routing', '## Workspace safety', '## Objective', '## Scope',
        '## Evidence reusable without rerun', '## Targeted success gates', '## Stop / escalate'
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
    'MODEL_ROUTING_POLICY.md': ['## 2A. Work mode first', '## 3. Default routing', '## 5. Escalation', '## 8. Recommendation format'],
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
    'WORK_MODE_ROUTING.md': [
        '**FAST**', '**STANDARD**', '**STRICT**',
        'FAST is faster because it omits unnecessary ceremony, not because it accepts weaker work.',
        'at least one concrete proof path exists before mutation',
        '### Looks FAST but is not',
        'How will we prove this exact change is correct?',
        'Evidence is revision-bound.'
    ],
    'WORKSPACE_SAFETY.md': [
        '**the explicit target project root, and only that project root.**',
        'External paths are non-writable by default.',
        'Proceed only after explicit human approval for that exact resource/action.',
        'Prefer a harness-enforced boundary over prompt-only compliance.'
    ],
    'README.md': [
        'Current workflow version: **v1.7.1 baseline**.', 'License: **Apache-2.0**.',
        'WORK_MODE_ROUTING.md', 'WORKSPACE_SAFETY.md', 'CONTEXT_MANAGEMENT.md', 'skills/research-gate/SKILL.md',
        'skills/independent-review/SKILL.md', 'skills/loop-readiness/SKILL.md',
        'CONTINUOUS_OPERATIONS.md', 'patterns/pr-ci-watcher.md', 'ACKNOWLEDGEMENTS.md',
        'Apache License, Version 2.0'
    ],
    'ENGINEERING_DEV_WORKFLOW.md': [
        'Version: 1.7.1', 'WORK_MODE_ROUTING.md', 'WORKSPACE_SAFETY.md', 'skills/research-gate/SKILL.md',
        'skills/scrutinize/SKILL.md', 'skills/independent-review/SKILL.md',
        'CONTEXT_MANAGEMENT.md', 'CONTINUOUS_OPERATIONS.md', 'skills/loop-readiness/SKILL.md'
    ],
    'scripts/setup_project.py': [
        'WORKFLOW_VERSION = "1.7.1"', 'LOCAL_WORKFLOW_DIR = ".engineering-workflow"',
        'WORK_MODE_ROUTING.md', 'WORKSPACE_SAFETY.md', 'templates/FAST_EXECUTION_PACKET.md',
        'def resolve_safe_target', 'def safe_destination', 'refusing filesystem-root target',
        'refusing user-home target', 'refusing target that overlaps workflow-source checkout', 'symlink/junction'
    ],
    'ACKNOWLEDGEMENTS.md': [
        'https://github.com/thananon/9arm-skills', 'conceptual inspiration only',
        'no text, code, or skill implementation',
        'https://github.com/shanraisshan/claude-code-best-practice',
        'MIT License', 'Shayan Rais',
        'https://github.com/cobusgreyling/loop-engineering', 'Cobus Greyling',
        'https://github.com/XiaoDuoYa/codex-with-chatgpt', 'XiaoDuoYa'
    ],
    'CONTINUOUS_OPERATIONS.md': [
        'Operational state is **derived memory/cache/ledger**',
        '**New loop patterns start at A1 unless an explicit adoption record justifies otherwise.**',
        'Default: **silence on no-op**.'
    ],
    'skills/loop-readiness/SKILL.md': ['READY FOR A1', 'READY FOR A2', 'READY FOR A3', 'NOT READY'],
    'patterns/pr-ci-watcher.md': ['Autonomy: **A1 — Observe / report**', 'invoke automatic Codex/coding-agent remediation'],
    'templates/CODEX_PROMPT.md': [
        'Work mode: FAST / STANDARD / STRICT', '.engineering-workflow/WORKSPACE_SAFETY.md',
        'external writes performed (normally none)', 'global/system changes performed (normally none)'
    ],
    'templates/CHATGPT_PROJECT_INSTRUCTIONS.md': [
        'WORK_MODE_ROUTING.md', 'WORKSPACE_SAFETY.md', '.engineering-workflow.json',
        'work mode + rationale', 'workspace write boundary'
    ],
    '.github/workflows/validate.yml': [
        'python scripts/validate_repository.py',
        "python -m unittest discover -s tests -p 'test_*.py' -v"
    ],
    'docs/CHEAT_SHEET.md': [
        'FAST', 'STANDARD', 'STRICT', '.engineering-workflow/', 'WORKSPACE_SAFETY.md'
    ],
    'ACCEPTANCE_AND_EVIDENCE.md': ['Prefer deterministic enforcement over instruction-only compliance', 'Evidence is revision-bound.'],
    'LICENSE': ['Apache License', 'Version 2.0, January 2004'],
    'NOTICE': ['Engineering Development Workflow', 'Copyright 2026 Kittipat Tangittinunt'],
}

CROSS_CONTRACT_REQUIREMENTS = [
    (
        'SECURITY_AND_GOVERNANCE.md',
        [
            'WORKSPACE_SAFETY.md',
            'explicit target project root only',
            'Human approval is a design control'
        ],
    ),
    (
        'WORK_MODE_ROUTING.md',
        [
            'WORKSPACE_SAFETY.md',
            'If mode confidence is low, do not choose FAST.',
            'at least one concrete proof path exists before mutation'
        ],
    ),
    (
        'templates/CODEX_PROMPT.md',
        [
            '.engineering-workflow/WORK_MODE_ROUTING.md',
            '.engineering-workflow/WORKSPACE_SAFETY.md',
            'Work mode: FAST / STANDARD / STRICT'
        ],
    ),
    (
        'templates/CHATGPT_PROJECT_INSTRUCTIONS.md',
        [
            'WORK_MODE_ROUTING.md',
            'WORKSPACE_SAFETY.md',
            'workspace write boundary'
        ],
    ),
    (
        '.github/workflows/validate.yml',
        [
            'python scripts/validate_repository.py',
            "python -m unittest discover -s tests -p 'test_*.py' -v"
        ],
    ),
]

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

for rel, snippets in CROSS_CONTRACT_REQUIREMENTS:
    path = ROOT / rel
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8')
    for snippet in snippets:
        if snippet not in text:
            errors.append(f'{rel}: cross-contract invariant missing {snippet!r}')

if errors:
    print('Repository validation FAILED')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'Repository validation PASS ({len(REQUIRED_FILES)} required files checked, {len(SKILL_FILES)} focused skills)')
