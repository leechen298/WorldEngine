# Test Plan

Status: review complete

## Documentation-Stage Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "PlanImportSource|PlanImportRequest|PlanImportResult|validate_plan_import|import_generation_plan|implementation_authorized: no" docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import
```

No backend implementation tests are run before `implementation_authorized:
yes`.

## Focused Implementation Tests

After authorization, add or update tests to cover:

- schema construction for `PlanImportSource`, `PlanImportRequest`, and
  `PlanImportResult`.
- accepted import returns the structured plan and redacted provenance.
- invalid imported plans are rejected through `validate_generation_plan`.
- malformed provenance and non-JSON import metadata return deterministic
  diagnostics.
- prompt/free-form fields are rejected instead of ignored.
- no network/provider/credential dependency is introduced.
- structured-plan compiler regression still passes.

Expected focused command after implementation:

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py -q
```

## Adjacent Compatibility Tests

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py -q
```

## Broader Regression

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## Evidence Rules

Record exact command results and all P1/P2/P3 findings in `review.md`.
