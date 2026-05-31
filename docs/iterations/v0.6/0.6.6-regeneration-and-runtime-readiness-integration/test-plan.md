# Test Plan

Status: review complete

## Documentation-Stage Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "POST /world/generation/regenerate|POST /world/generation/runtime-readiness|GenerationRegenerationRequest|RuntimeReadinessResult|implementation_authorized: no" docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration
```

No backend implementation tests are run before `implementation_authorized:
yes`.

## Focused Implementation Tests

After authorization, add or update tests to cover:

- regeneration success returns deterministic lineage and regenerated preview.
- changed seed or constraints changes lineage/output metadata without mutating
  source request data.
- invalid regeneration request uses existing 422 API error envelope.
- regeneration generation failure returns failed status and diagnostics.
- runtime-readiness success validates a generated `WorldSpec` through
  `load_worldspec` and `build_runtime_context`.
- runtime-readiness failure returns loader or context diagnostics.
- readiness result contains bounded context summary and
  `does_not_mutate_runtime: true`.
- runtime step/event payloads do not include raw `WorldSpec` or root payloads.
- existing preview API remains compatible.

Expected focused command after implementation:

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_regeneration_api.py app/tests/test_generation_preview_api.py app/tests/test_worldspec_loader.py app/tests/test_runtime_context_bridge.py app/tests/test_runtime_step.py -q
```

## Broader Regression

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## Static And Scope Checks

```bash
git diff --check
```

The scope guard below is a cumulative v0.6 worktree guard. It permits files
already changed by prior reviewed v0.6 packages, including the route registry
and app factory changes from `0.6.5`. It is not 0.6.6 authorization to modify
`backend/app/api/routes/__init__.py` or `backend/app/api/app_factory.py`.
Implementation-scope and code-review evaluators must fail `0.6.6` if this
package adds new edits to those two files without reopened documentation
review.

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','backend/app/tests/test_worldspec_loader.py','backend/app/tests/test_runtime_context_bridge.py','backend/app/tests/test_runtime_step.py','backend/app/tests/test_agent_loop_api.py','backend/app/tests/test_event_api_compat.py'); bad=[]\nfor line in lines:\n    path=line[3:]\n    if not path.startswith(allowed):\n        bad.append(line)\nprint('out_of_scope=' + str(len(bad)))\n[print(item) for item in bad]\nraise SystemExit(1 if bad else 0)"
```

## Evidence Rules

Record exact command results, pass counts, skipped checks, compatibility
review, scope review, evaluator results, exclusions, and unresolved P1/P2/P3
findings in `review.md`.
