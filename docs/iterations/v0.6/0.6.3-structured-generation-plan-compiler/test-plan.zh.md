# 测试计划

Status: review complete

## 文档阶段检查

```bash
git diff --check
```

```bash
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.3-structured-generation-plan-compiler'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

```bash
rg -n "GenerationPlan|PlanCell|PlanGenerationRequest|generate_worldspec_from_plan|validate_generation_plan|implementation_authorized: yes" docs/iterations/v0.6/0.6.3-structured-generation-plan-compiler
```

```bash
python3 -c "import subprocess, re, sys; allowed=[re.compile(r'^ M docs/iterations/v0\\.6/'), re.compile(r'^\\?\\? docs/iterations/v0\\.6/0\\.6\\.3-structured-generation-plan-compiler/')]; lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); unexpected=[line for line in lines if not any(p.search(line) for p in allowed)]; print('unexpected_status=' + str(len(unexpected))); [print(line) for line in unexpected]; sys.exit(1 if unexpected else 0)"
```

`implementation_authorized: yes` 前不运行 backend implementation tests，因为本 package 仍处于
documentation review。

## 聚焦实现测试

Authorization 后，添加或更新 tests 覆盖：

- `PlanCell`、`GenerationPlan` 和 `PlanGenerationRequest` schema construction。
- valid plan compilation 到 deterministic `WorldSpec`。
- 相同 input 输出 deterministic，seed material 改变时 digest 变化。
- invalid plan diagnostics 有 stable codes 和 paths。
- duplicate cell ids 和 duplicate entity refs。
- min/max child-cell constraints 与 entity-kind allowlist violations。
- unsupported plan versions。
- strict JSON seed/material failures，包括 set、tuple、`NaN`、`Infinity` 和 non-string
  dict keys。
- no input mutation。
- generated content 保持 generic，不包含 concrete world/story 或 application terms。

Implementation 后预期 focused command：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py -q
```

## 相邻兼容性测试

Implementation 后运行：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests/test_generation_plan_schema.py app/tests/test_structured_generation_plan_compiler.py app/tests/test_world_generation_schema.py app/tests/test_deterministic_world_generation.py app/tests/test_worldspec_loader.py app/tests/test_runtime_context_bridge.py app/tests/test_world_cell_schema.py -q
```

## 更广回归

Closeout 前运行 full backend app tests：

```bash
PYTHONPATH=. .venv/bin/pytest app/tests -q
```

## 证据规则

在 `review.md` 记录每条 command、exit status、pass/fail count 和 failure summary。
P1 会阻塞 implementation 或 closeout。未解决 P2 会阻塞 closeout，除非本 package contract
明确接受。
