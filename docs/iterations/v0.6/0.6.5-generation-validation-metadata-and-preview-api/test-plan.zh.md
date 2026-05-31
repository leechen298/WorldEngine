# 测试计划

状态：review complete

## 文档阶段检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "POST /world/generation/preview|GenerationPreviewRequest|GenerationPreviewResponse|preview_generation|implementation_authorized: no|ApiResponse|ApiErrorResponse" docs/iterations/v0.6/0.6.5-generation-validation-metadata-and-preview-api
```

在 `implementation_authorized: yes` 前，不运行 backend implementation tests。

## 聚焦实现测试

授权后添加或更新测试，覆盖：

- `GenerationPreviewRequest`、`GenerationPreviewMetadata` 和
  `GenerationPreviewResponse` 的 schema construction。
- successful template preview 返回 HTTP 200、`code == 0`、passed status、bounded
  metadata 和 public `WorldSpec` preview。
- successful structured-plan preview 返回 HTTP 200、`code == 0`、passed status、
  bounded metadata 和 public `WorldSpec` preview。
- successful imported-plan preview 先验证 import，并只暴露 redacted provenance
  summary。
- invalid template 或 plan content 返回 HTTP 200、failed status、diagnostics，且不返回
  `worldspec_preview`。
- invalid import provenance 返回 HTTP 200、failed status、diagnostics，且不返回 generated
  preview。
- malformed request shape、unexpected fields、missing source payload 或 mismatched
  source kind 使用现有 422 API error envelope 和 code `30`。
- existing event/Agent loop API envelope tests 仍然通过。
- 不引入 network/provider/credential dependency。

Expected focused command after implementation：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py -q
```

## 相邻兼容测试

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_preview_api.py app/tests/test_agent_loop_api.py app/tests/test_event_api_compat.py -q
```

## 更广回归

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## 静态与范围检查

```bash
git diff --check
```

```bash
python3 -c "import subprocess; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); allowed=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/api/routes/world_generation.py','backend/app/api/routes/__init__.py','backend/app/api/app_factory.py','backend/app/tests/test_generation_preview_api.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py','backend/app/tests/test_generation_plan_schema.py','backend/app/tests/test_structured_generation_plan_compiler.py','backend/app/tests/test_plan_import_schema.py','backend/app/tests/test_plan_import_boundary.py','backend/app/tests/test_agent_loop_api.py','backend/app/tests/test_event_api_compat.py'); bad=[]\nfor line in lines:\n    path=line[3:]\n    if not path.startswith(allowed):\n        bad.append(line)\nprint('out_of_scope=' + str(len(bad)))\n[print(item) for item in bad]\nraise SystemExit(1 if bad else 0)"
```

## 证据规则

在 `review.md` 中记录 exact command results、pass counts、skipped checks、
compatibility review、scope review、evaluator results 和 unresolved P1/P2/P3 findings。
