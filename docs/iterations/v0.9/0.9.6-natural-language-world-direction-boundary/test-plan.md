# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Exact Commands To Run

Focused 0.9.6 tests:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py -q
```

Related public surface regression:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_direction_boundary.py app/tests/test_public_handoff_contract_api.py app/tests/test_runtime_bounded_run.py app/tests/test_world_rule_parameter_schema.py app/tests/test_worldview_fidelity_evaluation.py -q
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
root = Path('docs/iterations/v0.9/0.9.6-natural-language-world-direction-boundary')
combined = '\n'.join(path.read_text() for path in root.glob('*.md'))
required = [
    'implementation_authorized: no',
    'provider_live_call_authorized: no',
    'generated_result_creation_authorized: no',
    'external_validation_authorized: no',
    'WorldDirectionRequest',
    'WorldDirectionQueueItem',
    'direct_final_fact',
    'agent_private_state_mutation',
    'rule_bypass',
]
missing = [term for term in required if term not in combined]
if missing:
    raise SystemExit(f'missing required terms: {missing}')
print('OK')
PY
```

## Expected Focused Coverage

- Benign environmental trend guidance is accepted or queued with a public
  direction item.
- External risk, pressure, event-bias, probability-shift, rule-constraint, and
  future-evaluation guidance classify into allowed public categories.
- Direct final facts such as death, healing, teleportation, forced
  relationship, or forced inventory outcomes are rejected.
- Direct Agent private memory or private goal mutation requests are rejected.
- Rule-bypass language is rejected.
- Private markers are not echoed in public summaries or event payloads.
- Extra request fields are rejected.
- `expires_after_tick < apply_after_tick` is rejected.
- Accepted guidance does not mutate canonical world state or Agent private
  state.
- Existing `/worlds/{world_id}/director-guidance` benign guidance behavior
  remains compatible.

## Expected Results

- Focused tests pass.
- Related public surface regression passes.
- Backend regression passes or records unrelated existing failures with
  evidence.
- `git diff --check` passes.
- Documentation term check passes.

## Commands Not Run And Why

- Live provider smoke: not authorized by `0.9.6`.
- Generated result creation: not authorized by `0.9.6`.
- Checker execution or external validation: not authorized by `0.9.6`.
- Validation Client E2E: out of scope for this package.
- Autonomous validation: out of scope for this package.
- Event legality checker: belongs to `0.9.7+` and is not authorized here.

## Blocker Recording Rule

If any required command fails, record the exact command, exit status, relevant
output, suspected scope, and whether the failure blocks closeout in `review.md`.
Do not replace a failed command with a narrower command and claim package pass.

## No Unverified Claims Rule

Only commands run in the current session may be recorded as passed. Historical
v0.8 or earlier v0.9 evidence may be cited only as handoff context.
