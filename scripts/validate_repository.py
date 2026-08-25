from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

SKILL_FILES = [
    'skills/scrutinize/SKILL.md',
    'skills/systematic-debug/SKILL.md',
    'skills/postmortem/SKILL.md',
    'skills/technical-status/SKILL.md',
    'skills/long-task-guard/SKILL.md',
]

REQUIRED_FILES = [
    'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'ACKNOWLEDGEMENTS.md',
    'LICENSE', 'NOTICE', 'AGENTS.md', 'SKILL.md',
    'ENGINEERING_DEV_WORKFLOW.md', 'MODEL_ROUTING_POLICY.md', 'UX_UI_WORKFLOW.md',
    'DEBUGGING_PROTOCOL.md', 'REVIEW_AND_SCRUTINY.md', 'PARALLEL_EXECUTION.md',
    'ACCEPTANCE_AND_EVIDENCE.md', 'SECURITY_AND_GOVERNANCE.md', 'VERSIONING.md',
    'templates/PROJECT_PROFILE.md', 'templates/EXECUTION_CONTRACT.md',
    'templates/ACCEPTANCE_GATE.md', 'templates/EVIDENCE_PACKAGE.md',
    'templates/HANDOFF.md', 'templates/POSTMORTEM.md', 'templates/CODEX_PROMPT.md',
    'templates/CHATGPT_PROJECT_INSTRUCTIONS.md',
    '.github/pull_request_template.md',
    'scripts/setup_project.py', 'docs/installation.md', 'docs/quick-start.md',
    'docs/chatgpt-project-setup.md', 'docs/skill-system.md', 'tests/test_setup_project.py',
    *SKILL_FILES,
]

COMMON_SKILL_HEADINGS = [
    '## Trigger conditions',
    '## Required inputs',
    '## Procedure',
    '## Output',
    '## Gate rules',
    '## Stop / escalation',
]

REQUIRED_HEADINGS = {
    'SKILL.md': ['## Core router', '## Focused skill routing', '## Mandatory scrutiny', '## Control-plane rule'],
    'ENGINEERING_DEV_WORKFLOW.md': ['## 4. Focused skills', '## 5. End-to-end loop'],
    'CONTRIBUTING.md': ['## External inspiration and attribution'],
    'ACKNOWLEDGEMENTS.md': ['## Attribution principles', '## Current acknowledgements', '### thananon/9arm-skills', '## Future acknowledgements'],
    'templates/EXECUTION_CONTRACT.md': [
        '## Objective', '## Scope', '## Out of scope', '## Execution routing',
        '## Success gates', '## Stop conditions', '## Definition of done'
    ],
    'templates/PROJECT_PROFILE.md': [
        '## Current accepted baseline', '## Architecture / invariants',
        '## Protected behavior', '## Validation matrix', '## Current next objective'
    ],
    'templates/CHATGPT_PROJECT_INSTRUCTIONS.md': ['## Control-plane role'],
    'MODEL_ROUTING_POLICY.md': ['## 3. Default routing', '## 5. Escalation', '## 8. Recommendation format'],
    'docs/installation.md': ['## 2. Inspect a target repository', '## 3. Install', '## 4. Validate', '## 5. Upgrade', '## 7. Ask Codex to install it'],
    'docs/chatgpt-project-setup.md': ['## 1. The important distinction', '## 2. Create a ChatGPT Project', '## 3. Bootstrap the target repository', '## 4. Start work from ChatGPT', '## 5. Invoke Codex only when needed'],
    'docs/skill-system.md': ['## 1. Relationship to the core workflow', '## 2. Skill routing', '## 3. Mandatory scrutiny gates', '## 4. Skills and ChatGPT/Codex roles', '## 5. Evidence discipline', '## 6. External inspiration and licensing'],
}
for skill_file in SKILL_FILES:
    REQUIRED_HEADINGS[skill_file] = COMMON_SKILL_HEADINGS

REQUIRED_TEXT = {
    'README.md': ['Current workflow version: **v1.4.1 baseline**.', 'License: **Apache-2.0**.', 'ACKNOWLEDGEMENTS.md', 'Apache License, Version 2.0'],
    'ENGINEERING_DEV_WORKFLOW.md': ['Version: 1.4.1', 'skills/scrutinize/SKILL.md'],
    'scripts/setup_project.py': ['WORKFLOW_VERSION = "1.4.1"'],
    'ACKNOWLEDGEMENTS.md': ['https://github.com/thananon/9arm-skills', 'conceptual inspiration only', 'no text, code, or skill implementation'],
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
