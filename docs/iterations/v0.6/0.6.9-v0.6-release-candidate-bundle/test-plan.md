# Test Plan

Status: review complete

## Documentation Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.9-v0.6-release-candidate-bundle'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n 'release-candidate|0\.6\.8|0\.6\.10|product readiness|external validation|projection readiness|generation quality|final release' docs/iterations/v0.6/0.6.9-v0.6-release-candidate-bundle
```

## Scope Guard

```bash
python3 -c "import subprocess,sys; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/api/client.ts','frontend/src/api/client.test.ts','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/src/pages/DashboardPage.vue','frontend/src/pages/DashboardPage.test.ts','frontend/src/style.css','frontend/e2e/dashboard-generation.spec.ts'); bad=[line for line in lines if not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); print('\n'.join(bad)); sys.exit(1 if bad else 0)"
```

## Status Consistency

Check that current parent status points to `0.6.9` as ready for review before
evaluator review, and to `0.6.10` only after this package is marked review
complete.

## Runtime Tests

No implementation command is required by this documentation-only package.
Runtime, frontend, E2E, and backend regression evidence is inherited from
review-complete child packages and must be explicitly cited rather than
reclaimed as newly run by `0.6.9`.

## Evaluator Gate

A read-only release-candidate evaluator must review the package before it can
be marked review complete.
