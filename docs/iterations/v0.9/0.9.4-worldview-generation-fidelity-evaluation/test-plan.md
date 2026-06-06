# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Exact Commands To Run

Focused 0.9.4 tests:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_worldview_fidelity_evaluation.py -q
```

Related v0.9 regression set:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_worldview_fidelity_evaluation.py app/tests/test_world_rule_parameter_schema.py app/tests/test_world_generation_schema.py app/tests/test_llm_worldview_generation_api.py app/tests/test_provider_live_smoke_api.py app/tests/test_public_handoff_contract_api.py -q
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
paths = list(Path('docs/iterations/v0.9/0.9.4-worldview-generation-fidelity-evaluation').glob('*.md'))
required = [
    'implementation_authorized: no',
    'provider_live_call_authorized: no',
    'generated_result_creation_authorized: no',
    'external_validation_authorized: no',
    'Validation Client',
    'bounded runtime',
    'WorldviewFidelityScorecard',
    'ImmediateWorldviewFidelityArtifact',
    'BoundedRunWorldviewFidelityArtifact',
]
missing = []
combined = '\n'.join(path.read_text() for path in paths)
for term in required:
    if term not in combined:
        missing.append(term)
if missing:
    raise SystemExit(f'missing required terms: {missing}')
print('OK')
PY
```

## Expected Results

- Focused tests pass and cover faithful immediate output, missing premise
  output, deterministic generic fallback, contradictory runtime summaries,
  missing bounded-run evidence, and redaction failures.
- Related v0.9 regression passes.
- Backend regression passes or records an unrelated existing failure with
  evidence.
- `git diff --check` passes.
- Documentation term check passes.

## Commands Not Run And Why

- Live provider smoke: not authorized by `0.9.4`.
- Generated result creation: not authorized by `0.9.4`.
- Checker execution or external validation: not authorized by `0.9.4`.
- Validation Client E2E: out of scope for this package.
- Bounded runtime control verification: owned by `0.9.5`.

## Blocker Recording Rule

If any required command fails, record the exact command, exit status, relevant
output, suspected scope, and whether the failure blocks closeout in `review.md`.
Do not replace a failed command with a narrower command and claim package pass.

## No Unverified Claims Rule

Only commands run in the current session may be recorded as passed. Historical
v0.8 or earlier v0.9 evidence may be cited only as handoff context.
