from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'AGENTS.md', 'SKILL.md',
    'ENGINEERING_DEV_WORKFLOW.md', 'MODEL_ROUTING_POLICY.md', 'UX_UI_WORKFLOW.md',
    'DEBUGGING_PROTOCOL.md', 'REVIEW_AND_SCRUTINY.md', 'PARALLEL_EXECUTION.md',
    'ACCEPTANCE_AND_EVIDENCE.md', 'SECURITY_AND_GOVERNANCE.md', 'VERSIONING.md',
    'templates/PROJECT_PROFILE.md', 'templates/EXECUTION_CONTRACT.md',
    'templates/ACCEPTANCE_GATE.md', 'templates/EVIDENCE_PACKAGE.md',
    'templates/HANDOFF.md', 'templates/POSTMORTEM.md', 'templates/CODEX_PROMPT.md',
    '.github/pull_request_template.md',
]

REQUIRED_HEADINGS = {
    'templates/EXECUTION_CONTRACT.md': [
        '## Objective', '## Scope', '## Out of scope', '## Execution routing',
        '## Success gates', '## Stop conditions', '## Definition of done'
    ],
    'templates/PROJECT_PROFILE.md': [
        '## Current accepted baseline', '## Architecture / invariants',
        '## Protected behavior', '## Validation matrix', '## Current next objective'
    ],
    'MODEL_ROUTING_POLICY.md': ['## 3. Default routing', '## 5. Escalation', '## 8. Recommendation format'],
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

if errors:
    print('Repository validation FAILED')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'Repository validation PASS ({len(REQUIRED_FILES)} required files checked)')
