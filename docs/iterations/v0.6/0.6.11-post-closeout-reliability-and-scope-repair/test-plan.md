# Test Plan

Status: review complete

## Focused Tests

```bash
cd backend && PYTHONPATH=. .venv/bin/pytest app/tests/test_deterministic_world_generation.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_generation_preview_api.py app/tests/test_plan_import_boundary.py -q
```

Expected: all focused v0.6 generation, plan import, and preview API tests pass.

## Regression Checks

```bash
cd backend && PYTHONPATH=. .venv/bin/pytest app/tests tests -q
```

Expected: full backend regression passes.

```bash
cd frontend && pnpm test
```

Expected: frontend unit suite passes.

```bash
cd frontend && pnpm build
```

Expected: production build passes. Existing Vite large-chunk warning may remain.

```bash
make test-e2e
```

Expected: browser E2E suite passes. If sandbox bind permissions fail, rerun
with approved escalation and record both attempts.

## Existing Saved-Result Checkers

```bash
make validate-agent-smoke-fixtures
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260531T122230+0800
```

Expected: deterministic saved-result checkers pass. These are not new live Agent
smoke or full autonomous runner executions.

## Scope And Evidence Checks

```bash
git diff --check
```

```bash
python3 -c "import subprocess,sys; allowed=('docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/','backend/app/core/world_generation.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/e2e/dashboard-generation.spec.ts','docs/backend-implementation.md','docs/backend-implementation.zh.md','docs/current-implementation.md','docs/current-implementation.zh.md','docs/frontend-implementation.md','docs/frontend-implementation.zh.md','docs/iterations/v0.6/README.md','docs/iterations/v0.6/README.zh.md','docs/iterations/v0.6/CURRENT_STATE.md','docs/iterations/v0.6/CURRENT_STATE.zh.md','docs/iterations/v0.6/review.md','docs/iterations/v0.6/review.zh.md','docs/testing/results/2026-06-01-v0.6-reliability-validation.md'); lines=subprocess.check_output(['git','status','--short','--untracked-files=all'], text=True).splitlines(); bad=[line for line in lines if not any(line[3:]==path or line[3:].startswith(path) for path in allowed)]; print('out_of_scope=' + str(len(bad))); print('\\n'.join(bad)); sys.exit(1 if bad else 0)"
```

```bash
git status --short -- backend/worldengine backend/app/alembic backend/migrations
```

Expected: whitespace check passes, package scope guard reports
`out_of_scope=0`, and forbidden surfaces produce no output.

## Not-Run / Non-Claims

Do not claim live Agent smoke, full autonomous runner/full-suite, external
validation readiness, projection readiness, live provider behavior, generation
quality, or product readiness passed unless separately run in the current
session under an authorized package.
