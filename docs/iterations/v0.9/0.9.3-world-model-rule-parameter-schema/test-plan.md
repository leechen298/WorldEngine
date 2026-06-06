# Test Plan

Chinese mirror: `test-plan.zh.md`.

## Unit Tests

Add or update focused tests after implementation authorization:

- `backend/app/tests/test_world_rule_parameter_schema.py`
  - accepts a valid generated rule parameter set.
  - rejects duplicate parameter ids.
  - rejects duplicate rule ids.
  - rejects unresolved target parameter refs.
  - rejects unresolved rule refs.
  - rejects `initial_value` that does not match `value_type`.
  - rejects prose-only rules without structured triggers/effects.
  - rejects private/raw/provider/secret markers in ids, paths, descriptions,
    evidence, diagnostics, and summary fields.
  - returns a public `RuleParameterValidationResult` and
    `PublicWorldRuleSummary`.
- `backend/app/tests/test_world_generation_schema.py`
  - verifies new schema models serialize and round-trip without private fields.
  - verifies `PublicGeneratedWorldModel` remains backward-compatible.
- `backend/app/tests/test_llm_worldview_generation_api.py`
  - verifies `/world/generation/worldview` remains compatible.
  - if the implementation adds a rule summary field, verifies it is additive
    and redacted.
- `backend/app/tests/test_param_validator.py` or `test_world_params.py`
  - verifies existing `/world/params` registered paths still pass/reject as
    before.
  - verifies generated-only parameter definitions do not silently become
    writable runtime paths unless explicitly bridged in a later package.

## Regression Tests

Run focused compatibility tests:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_rule_parameter_schema.py app/tests/test_world_generation_schema.py app/tests/test_llm_worldview_generation_api.py app/tests/test_param_validator.py app/tests/test_world_params.py -q
```

Run backend regression:

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

Run diff/format checks:

```bash
git diff --check
```

Run package documentation checks:

```bash
python3 - <<'PY'
from pathlib import Path
root = Path('docs/iterations/v0.9/0.9.3-world-model-rule-parameter-schema')
docs = ['README', 'intent', 'contract', 'technical-design', 'test-plan', 'plan', 'review']
missing = [str(root / f'{name}{suffix}') for name in docs for suffix in ['.md', '.zh.md'] if not (root / f'{name}{suffix}').exists()]
print('missing_child_docs', len(missing))
if missing:
    print('\n'.join(missing))
    raise SystemExit(1)
PY
```

## Acceptance Criteria

- Full package docs and mirrors exist.
- Documentation review records no P0/P1/P2 findings before implementation.
- Implementation adds only additive schema/API/helper behavior.
- Valid generated rule parameter set is accepted and summarized.
- Invalid ids, refs, value types, unstructured rules, and private markers are
  rejected with public diagnostics.
- Existing `/world/params` behavior remains compatible.
- Existing `0.9.2` worldview generation behavior remains compatible.
- No live provider calls, external validation, generated-result directories,
  Validation Client changes, frontend changes, migrations, or
  `backend/worldengine/` changes occur.

## Not Run

Until implementation is authorized, backend tests are not run for this package
except optional baseline checks. Live provider calls, checker execution,
external validation, generated-result creation, and Validation Client tests
remain unauthorized for this package.
