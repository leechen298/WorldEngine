# Test Plan

Status: review complete

## Documentation Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.8-v0.6-evidence-and-compatibility-audit'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "frontend unit `36 passed`|E2E `16 passed`|full backend `220 passed`|release-candidate" docs/iterations/v0.6/0.6.8-v0.6-evidence-and-compatibility-audit
```

## Scope Guard

This package is documentation-only. The guard permits v0.6 documentation and
previously reviewed cumulative v0.6 implementation files, but it does not
authorize new implementation changes for `0.6.8`.

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/api/client.ts','frontend/src/api/client.test.ts','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/src/pages/DashboardPage.vue','frontend/src/pages/DashboardPage.test.ts','frontend/src/style.css','frontend/e2e/dashboard-generation.spec.ts'); bad=[line for line in lines if not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

## Implementation Commands

No new implementation commands are required by this documentation-only package
because it touches no implementation files. It records current-session
evidence already produced by `0.6.7`: frontend unit `36 passed`, build passed,
backend focused `21 passed`, E2E `16 passed`, and full backend `220 passed`.

## Evidence Rules

Record exact command results, evaluator findings, skipped checks, scope review,
compatibility review, and release-candidate recommendation in `review.md`.
