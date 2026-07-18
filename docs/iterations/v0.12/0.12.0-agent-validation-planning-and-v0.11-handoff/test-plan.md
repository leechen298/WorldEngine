# Test Plan

Chinese mirror: `test-plan.zh.md`.

This package is documentation-only. It does not run runtime, API, frontend,
provider, checker, Validation Client, or Agent behavior tests.

## Documentation Checks

Run:

```bash
git status --short --branch
git diff --check
python3 - <<'PY'
from pathlib import Path

pkg = Path('docs/iterations/v0.12/0.12.0-agent-validation-planning-and-v0.11-handoff')
required = [
    'README.md', 'README.zh.md',
    'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md',
    'technical-design.md', 'technical-design.zh.md',
    'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md',
    'review.md', 'review.zh.md',
]
missing = [name for name in required if not (pkg / name).exists()]
empty = [name for name in required if (pkg / name).exists() and not (pkg / name).read_text().strip()]
print({'missing': missing, 'empty': empty})
PY
rg -n "implementation_authorized: yes|evidence_execution_authorized: yes|provider_live_call_authorized: yes|external_validation_authorized: yes" docs/iterations/v0.12/0.12.0-agent-validation-planning-and-v0.11-handoff docs/iterations/v0.12/CURRENT_STATE.md docs/iterations/v0.12/README.md docs/iterations/v0.12/review.md
```

## Expected Results

- Package file check returns no missing or empty files.
- `git diff --check` has no output.
- Authorization scan finds no active yes authorization fields.
- Review records no runtime tests were run because this is docs-only.

## Commands Not Run

- Backend tests: not run; this package does not change runtime code.
- Frontend/E2E: not run; this package does not change frontend code.
- Provider live call: not authorized and not run.
- External Validation Client automation: not authorized and not run.
- Agent smoke/autonomous validation: not in scope and not run.
