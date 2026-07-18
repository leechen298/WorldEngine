# Test Plan

## Exact Commands To Run

```bash
git status --short --branch
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
pkg = Path('docs/iterations/v0.10/0.10.3-worldview-to-runtime-session-creation')
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

From `backend`:

```bash
python3 -m pytest app/tests/test_world_session_api.py app/tests/test_llm_worldview_generation_api.py app/tests/test_public_handoff_contract_api.py
```

## Commands Not Run And Why

Full backend regression, frontend, E2E, provider live calls, checker result
generation, Validation Client execution, generated-result creation, and
external validation are not required unless focused tests show broader impact.

## Blocker Recording Rule

If the flow requires live provider execution, runtime run, snapshots,
dashboard, checker fixtures, persistence, or external client work, stop and
record `BLOCKED` or revise the package.

## No Unverified Claims Rule

Only worldview-to-session creation can be claimed after focused tests pass.
