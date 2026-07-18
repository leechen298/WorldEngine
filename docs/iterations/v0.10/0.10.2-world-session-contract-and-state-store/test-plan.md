# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.2-world-session-contract-and-state-store')
required = {
    'README.md', 'README.zh.md', 'intent.md', 'intent.zh.md',
    'contract.md', 'contract.zh.md', 'technical-design.md',
    'technical-design.zh.md', 'test-plan.md', 'test-plan.zh.md',
    'plan.md', 'plan.zh.md', 'review.md', 'review.zh.md',
}
missing = sorted(name for name in required if not (pkg / name).exists())
print({'files': len(list(pkg.glob('*.md'))), 'missing': missing})
raise SystemExit(1 if missing else 0)
PY
```

Focused backend verification from `backend`:

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py
```

Expected result: focused session, manifest compatibility, and runtime
compatibility tests pass.

## Commands Not Run And Why

Full backend regression, frontend unit/build, E2E, Agent smoke, autonomous
validation, provider live calls, checker result generation, Validation Client
execution, generated-result creation, and external validation are not required
unless focused tests or review reveal broader impact.

## Blocker Recording Rule

If session create/list/read/status cannot be implemented without runtime
execution, dashboard, persistence, provider, checker, or external client work,
stop and record `BLOCKED` or revise the package.

## No Unverified Claims Rule

This package can only claim focused session contract/state-store behavior when
the listed focused tests pass.
