# 测试计划

Status: review complete

## 文档阶段检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "PlanImportSource|PlanImportRequest|PlanImportResult|validate_plan_import|import_generation_plan|implementation_authorized: no" docs/iterations/v0.6/0.6.4-ai-assisted-generation-boundary-and-plan-import
```

`implementation_authorized: yes` 前不运行 backend implementation tests。

## 聚焦实现测试

Authorization 后，添加或更新 tests 覆盖：

- `PlanImportSource`、`PlanImportRequest` 和 `PlanImportResult` schema construction。
- accepted import 返回 structured plan 和 redacted provenance。
- invalid imported plans 通过 `validate_generation_plan` 被拒绝。
- malformed provenance 和 non-JSON import metadata 返回 deterministic diagnostics。
- prompt/free-form fields 被拒绝，而不是被忽略。
- 不引入 network/provider/credential dependency。
- structured-plan compiler regression 仍通过。

Implementation 后预期 focused command：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py -q
```

## 相邻兼容性测试

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_plan_import_schema.py app/tests/test_plan_import_boundary.py app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py -q
```

## 更广回归

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## 证据规则

在 `review.md` 记录准确 command results 和所有 P1/P2/P3 findings。
