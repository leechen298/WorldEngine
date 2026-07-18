# Test Plan

## Exact Commands To Run

Documentation and status checks:

```bash
git status --short --branch
git diff --check
```

Package document completeness:

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.1-mvp-public-manifest-and-debug-handoff')
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

Focused backend verification:

```bash
../../.venv/bin/pytest backend/app/tests/test_public_handoff_contract_api.py
```

Expected result: all focused manifest/debug handoff tests pass.

Optional compatibility check if focused changes touch shared manifest/provider
readiness behavior:

```bash
../../.venv/bin/pytest backend/app/tests/test_public_handoff_contract_api.py backend/app/tests/test_provider_live_smoke_api.py
```

Expected result: both focused files pass.

## Commands Not Run And Why

Full backend regression, frontend unit, frontend build, E2E, Agent smoke,
autonomous validation, live provider calls, checker saved-result generation,
Validation Client execution, generated-result creation, and external
validation are not required for this package unless focused verification or
review finds broader breakage. This package changes only `/manifest` schema
and route construction plus focused tests.

## Blocker Recording Rule

If focused backend tests fail, fix inside the approved file scope. If the fix
requires session runtime, checker fixture, frontend, provider live-call,
Validation Client, migration, generated-result, or external repository work,
record the package as `BLOCKED` or update the contract for review before
continuing.

## No Unverified Claims Rule

Do not claim v0.10 runnable session, dashboard flow, provider readiness PASS,
external validation, autonomous validation, checker PASS, or full MVP PASS
from this package. Only focused manifest/debug handoff behavior may be claimed
when the listed commands pass in the current session.
