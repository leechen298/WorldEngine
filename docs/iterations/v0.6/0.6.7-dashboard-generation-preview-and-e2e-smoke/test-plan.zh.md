# 测试计划

状态：review complete

## Documentation-Stage 检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.7-dashboard-generation-preview-and-e2e-smoke'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "GenerationPanel|/world/generation/preview|dashboard generation|implementation_authorized: no" docs/iterations/v0.6/0.6.7-dashboard-generation-preview-and-e2e-smoke
```

在 `implementation_authorized: yes` 前，不运行 frontend、backend 或 E2E implementation tests。

## Focused Implementation 测试

Authorization 后添加或更新 tests，覆盖：

- frontend API client 序列化 generation preview、regeneration 和 runtime-readiness requests，
  并保留 API envelope error handling。
- `GenerationPanel` 渲染 idle、loading、success、diagnostic failure 和 API-error states。
- successful preview 展示 validation status、generation id、source kind、bounded summary、
  diagnostics count 和 runtime-readiness pass status。
- failed preview 展示 diagnostics，且不暗示 runtime readiness。
- dashboard page 挂载 panel 且不破坏现有 dashboard data loading。
- browser E2E smoke 提交 generic preview，并验证 visible metadata 和 readiness status。
- existing dashboard 和 agent-loop E2E tests 保持兼容。

Implementation 后预期命令：

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

## Static And Scope 检查

```bash
git diff --check
```

下面的 scope guard 是 cumulative v0.6 worktree guard。它允许 prior reviewed v0.6 packages
已经修改的 backend generation files，但不授权 0.6.7 修改 backend files。如果本 package 在未
重新打开 documentation review 的情况下新增 backend edits，implementation-scope 和 code-review
evaluators 必须判定失败。

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','frontend/src/api/client.ts','frontend/src/api/client.test.ts','frontend/src/components/GenerationPanel.vue','frontend/src/components/GenerationPanel.test.ts','frontend/src/pages/DashboardPage.vue','frontend/src/pages/DashboardPage.test.ts','frontend/src/style.css','frontend/e2e/dashboard.spec.ts','frontend/e2e/dashboard-generation.spec.ts'); bad=[]\nfor line in lines:\n    path=line[3:]\n    if not path.startswith(allowed):\n        bad.append(line)\nprint('out_of_scope=' + str(len(bad)))\n[print(item) for item in bad]\nraise SystemExit(1 if bad else 0)"
```

## Evidence 规则

在 `review.md` 中记录 exact command results、pass counts、skipped checks、compatibility
review、scope review、evaluator results、exclusions 和 unresolved P1/P2/P3 findings。
