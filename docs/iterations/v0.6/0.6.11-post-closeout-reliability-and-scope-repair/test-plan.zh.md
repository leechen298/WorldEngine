# 测试计划

状态：review complete

## Focused 测试

```bash
cd backend && PYTHONPATH=. .venv/bin/pytest app/tests/test_deterministic_world_generation.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_generation_preview_api.py app/tests/test_plan_import_boundary.py -q
```

预期：所有 focused v0.6 generation、plan import 和 preview API tests 通过。

## 回归检查

```bash
cd backend && PYTHONPATH=. .venv/bin/pytest app/tests tests -q
```

预期：full backend regression 通过。

```bash
cd frontend && pnpm test
```

预期：frontend unit suite 通过。

```bash
cd frontend && pnpm build
```

预期：production build 通过。既有 Vite large-chunk warning 可以保留。

```bash
make test-e2e
```

预期：browser E2E suite 通过。如果 sandbox bind permissions 失败，则用已批准的提权重跑并记录两次尝试。

## 既有 saved-result 检查器

```bash
make validate-agent-smoke-fixtures
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260531T122230+0800
```

预期：deterministic saved-result checkers 通过。这些不是新的 live Agent smoke，也不是 full
autonomous runner execution。

## Scope 与证据检查

```bash
git diff --check
```

```bash
python3 -c "import subprocess,sys; allowed=('docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/','backend/app/core/world_generation.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/e2e/dashboard-generation.spec.ts','docs/backend-implementation.md','docs/backend-implementation.zh.md','docs/current-implementation.md','docs/current-implementation.zh.md','docs/frontend-implementation.md','docs/frontend-implementation.zh.md','docs/iterations/v0.6/README.md','docs/iterations/v0.6/README.zh.md','docs/iterations/v0.6/CURRENT_STATE.md','docs/iterations/v0.6/CURRENT_STATE.zh.md','docs/iterations/v0.6/review.md','docs/iterations/v0.6/review.zh.md','docs/testing/results/2026-06-01-v0.6-reliability-validation.md'); lines=subprocess.check_output(['git','status','--short','--untracked-files=all'], text=True).splitlines(); bad=[line for line in lines if not any(line[3:]==path or line[3:].startswith(path) for path in allowed)]; print('out_of_scope=' + str(len(bad))); print('\\n'.join(bad)); sys.exit(1 if bad else 0)"
```

```bash
git status --short -- backend/worldengine backend/app/alembic backend/migrations
```

预期：whitespace check 通过，package scope guard 输出 `out_of_scope=0`，forbidden surfaces
无输出。

## 不运行 / 不声明

除非在当前 session 中通过已授权 package 单独运行，否则不得声明 live Agent smoke、
full autonomous runner/full-suite、external validation readiness、projection readiness、
live provider behavior、generation quality 或 product readiness 已通过。
