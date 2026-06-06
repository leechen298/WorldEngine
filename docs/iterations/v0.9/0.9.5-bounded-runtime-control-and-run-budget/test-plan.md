# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Exact Commands To Run

Focused 0.9.5 tests:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py -q
```

Related runtime regression:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_bounded_run.py app/tests/test_runtime_step.py app/tests/test_archive_snapshot_summary.py app/tests/test_dry_run_validation.py app/tests/test_agent_loop_api.py -q
```

Backend regression:

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Documentation and whitespace checks:

```bash
git diff --check
```

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.5-bounded-runtime-control-and-run-budget')
combined = '\n'.join(path.read_text() for path in root.glob('*.md'))
required = [
    'provider_live_call_authorized: no',
    'generated_result_creation_authorized: no',
    'external_validation_authorized: no',
    'RuntimeRunRequest',
    'RuntimeRunSummary',
    'pause',
    'resume',
    'bounded runtime',
]
missing = [term for term in required if term not in combined]
if missing:
    raise SystemExit(f'missing required terms: {missing}')
print('OK')
PY
```

## Expected Results

- Focused tests pass for bounded tick runs, duration runs, pause/resume,
  invalid unbounded requests, max guard rejection, public run summary fields,
  provider/cost counters, and single-step compatibility.
- Related runtime regression passes.
- Backend regression passes or records unrelated existing failures with
  evidence.
- `git diff --check` passes.
- Documentation term check passes.

## Commands Not Run And Why

- Live provider smoke: not authorized by `0.9.5`.
- Generated result creation: not authorized by `0.9.5`.
- Checker execution or external validation: not authorized by `0.9.5`.
- Validation Client E2E: out of scope for this package.
- Autonomous validation: out of scope for this package.

## Blocker Recording Rule

If any required command fails, record the exact command, exit status, relevant
output, suspected scope, and whether the failure blocks closeout in `review.md`.
Do not replace a failed command with a narrower command and claim package pass.

## No Unverified Claims Rule

Only commands run in the current session may be recorded as passed. Historical
v0.8 or earlier v0.9 evidence may be cited only as handoff context.
