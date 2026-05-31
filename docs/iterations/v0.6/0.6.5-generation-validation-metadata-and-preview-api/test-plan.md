# Test Plan

Status: review complete

## Documentation-Stage Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "POST /world/generation/preview|GenerationPreviewRequest|GenerationPreviewResponse|preview_generation|implementation_authorized: no|ApiResponse|ApiErrorResponse" docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api
```

No backend implementation tests are run before `implementation_authorized:
yes`.

## Focused Implementation Tests

After authorization, add or update tests to cover:

- schema construction for `GenerationPreviewRequest`,
  `GenerationPreviewMetadata`, and `GenerationPreviewResponse`.
- successful template preview returns HTTP 200, `code == 0`, passed status,
  bounded metadata, and public `WorldSpec` preview.
- successful structured-plan preview returns HTTP 200, `code == 0`, passed
  status, bounded metadata, and public `WorldSpec` preview.
- successful imported-plan preview validates the import first and exposes only
  redacted provenance summary.
- invalid template or plan content returns HTTP 200 with failed status,
  diagnostics, and no `worldspec_preview`.
- invalid import provenance returns HTTP 200 with failed status, diagnostics,
  and no generated preview.
- malformed request shape, unexpected fields, missing source payload, or
  mismatched source kind uses the existing 422 API error envelope and code
  `30`.
- existing event/Agent loop API envelope tests still pass.
- no network/provider/credential dependency is introduced.

Expected focused command after implementation:

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py -q
```

## Adjacent Compatibility Tests

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py app/tests/test_agent_loop_api.py app/tests/test_event_api_compat.py -q
```

## Broader Regression

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## Static And Scope Checks

```bash
git diff --check
```

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','backend/app/tests/test_agent_loop_api.py','backend/app/tests/test_event_api_compat.py'); bad=[]\nfor line in lines:\n    path=line[3:]\n    if not path.startswith(allowed):\n        bad.append(line)\nprint('out_of_scope=' + str(len(bad)))\n[print(item) for item in bad]\nraise SystemExit(1 if bad else 0)"
```

## Evidence Rules

Record exact command results, pass counts, skipped checks, compatibility
review, scope review, evaluator results, and unresolved P1/P2/P3 findings in
`review.md`.
