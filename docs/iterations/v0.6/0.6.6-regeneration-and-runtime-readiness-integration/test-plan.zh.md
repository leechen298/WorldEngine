# 测试计划

状态：review complete

## 文档阶段检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "POST /world/generation/regenerate|POST /world/generation/runtime-readiness|GenerationRegenerationRequest|RuntimeReadinessResult|implementation_authorized: no" docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration
```

在 `implementation_authorized: yes` 前，不运行 backend implementation tests。

## 聚焦实现测试

授权后添加或更新测试，覆盖：

- regeneration success 返回 deterministic lineage 和 regenerated preview。
- changed seed 或 constraints 会改变 lineage/output metadata，但不 mutate source request
  data。
- invalid regeneration request 使用现有 422 API error envelope。
- regeneration generation failure 返回 failed status 和 diagnostics。
- runtime-readiness success 将 generated `WorldSpec` 通过 `load_worldspec` 和
  `build_runtime_context`。
- runtime-readiness failure 返回 loader 或 context diagnostics。
- readiness result 包含 bounded context summary 和 `does_not_mutate_runtime: true`。
- runtime step/event payloads 不包含 raw `WorldSpec` 或 root payloads。
- existing preview API 保持兼容。

Expected focused command after implementation：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_regeneration_api.py app/tests/test_generation_preview_api.py app/tests/test_worldspec_loader.py app/tests/test_runtime_context_bridge.py app/tests/test_runtime_step.py -q
```

## 更广回归

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## 静态与范围检查

```bash
git diff --check
```

下面的 scope guard 是 cumulative v0.6 worktree guard。它允许 prior reviewed v0.6
packages 已经修改的文件，包括 `0.6.5` 的 route registry 和 app factory changes。它不是
授权 0.6.6 修改 `backend/app/api/routes/__init__.py` 或
`backend/app/api/app_factory.py`。Implementation-scope 和 code-review evaluators 必须在
0.6.6 未重新打开 documentation review 的情况下，对这两个文件的新增编辑判为失败。

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_generation_regeneration_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','backend/app/tests/test_worldspec_loader.py','backend/app/tests/test_runtime_context_bridge.py','backend/app/tests/test_runtime_step.py','backend/app/tests/test_agent_loop_api.py','backend/app/tests/test_event_api_compat.py'); bad=[]\nfor line in lines:\n    path=line[3:]\n    if not path.startswith(allowed):\n        bad.append(line)\nprint('out_of_scope=' + str(len(bad)))\n[print(item) for item in bad]\nraise SystemExit(1 if bad else 0)"
```

## 证据规则

在 `review.md` 中记录 exact command results、pass counts、skipped checks、
compatibility review、scope review、evaluator results、exclusions 和 unresolved
P1/P2/P3 findings。
