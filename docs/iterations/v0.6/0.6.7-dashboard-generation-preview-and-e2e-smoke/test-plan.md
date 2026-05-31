# Test Plan

Status: review complete

## Documentation-Stage Checks

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.7-dashboard-generation-preview-and-e2e-smoke'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "GenerationPanel|/world/generation/preview|dashboard generation|implementation_authorized: no" docs/iterations/v0.6/0.6.7-dashboard-generation-preview-and-e2e-smoke
```

No frontend, backend, or E2E implementation tests are run before
`implementation_authorized: yes`.

## Focused Implementation Tests

After authorization, add or update tests to cover:

- frontend API client serializes generation preview, regeneration, and
  runtime-readiness requests and preserves API envelope error handling.
- `GenerationPanel` renders idle, loading, success, diagnostic failure, and
  API-error states.
- successful preview displays validation status, generation id, source kind,
  bounded summary, diagnostics count, and runtime-readiness pass status.
- failed preview displays diagnostics without implying runtime readiness.
- dashboard page mounts the panel without breaking existing dashboard data
  loading.
- browser E2E smoke submits a generic preview and verifies visible metadata and
  readiness status.
- existing dashboard and agent-loop E2E tests remain compatible.

Expected commands after implementation:

```bash
cd frontend && pnpm test
```

```bash
cd frontend && pnpm build
```

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_regeneration_api.py app/tests/test_generation_preview_api.py -q
```

```bash
make test-e2e
```

## Static And Scope Checks

```bash
git diff --check
```

The scope guard below is a cumulative v0.6 worktree guard. It permits backend
generation files already changed by prior reviewed v0.6 packages, but it is not
0.6.7 authorization to modify backend files. Implementation-scope and
code-review evaluators must fail `0.6.7` if this package adds new backend edits
without reopened documentation review.

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/api/client.ts','frontend/src/api/client.test.ts','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/src/pages/DashboardPage.vue','frontend/src/pages/DashboardPage.test.ts','frontend/src/style.css','frontend/e2e/dashboard.spec.ts','frontend/e2e/dashboard-generation.spec.ts'); bad=[]\nfor line in lines:\n    path=line[3:]\n    if not path.startswith(allowed):\n        bad.append(line)\nprint('out_of_scope=' + str(len(bad)))\n[print(item) for item in bad]\nraise SystemExit(1 if bad else 0)"
```

## Evidence Rules

Record exact command results, pass counts, skipped checks, compatibility
review, scope review, evaluator results, exclusions, and unresolved P1/P2/P3
findings in `review.md`.
