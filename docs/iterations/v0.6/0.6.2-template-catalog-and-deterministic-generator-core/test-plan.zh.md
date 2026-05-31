# 测试计划

Status: review complete

## 文档阶段检查

Implementation authorization 前运行：

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; child=Path('docs/iterations/v0.6/0.6.2-template-catalog-and-deterministic-generator-core'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/',); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]; [bad.append(line) for line in lines if line and not line[3:].startswith(allowed_prefixes)]; print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

预期：

- `git diff --check` exit `0`。
- required docs/mirrors check 输出 `missing=0`。
- documentation-stage scope guard 输出 `unexpected_status=0`。

## Focused 实现测试

实现后运行：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_generation_schema.py app/tests/test_template_catalog.py app/tests/test_deterministic_world_generation.py
```

预期：所有 focused generation tests pass。

Focused tests 必须覆盖：

- generation schema defaults 和 required fields。
- 相同 input 产生 stable `WorldSpec.model_dump()` output。
- 不同 seed material 改变已评审 deterministic ids 或 metadata，同时保持 `WorldSpec`
  validity。
- generated output 只包含 generic ids/labels，不含 concrete world、story、oracle 或
  application data。
- invalid templates 为 duplicate cell ids、duplicate entity refs、invalid bounds、
  unsupported entity kinds、empty ids 和 unknown/unsupported template versions 产生
  deterministic diagnostics。
- diagnostics 包含 stable code、severity、message、optional path 和 source context。
- generator 不 mutate template input objects。

## 兼容性回归测试

实现后运行：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py app/tests/test_worldspec_loader.py app/tests/test_runtime_context_bridge.py
```

预期：现有 schema、loader 和 runtime-context bridge tests pass。

Focused 和 adjacent tests 通过后，运行 full backend regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests
```

预期：full backend regression passes；如果失败，必须准确记录并在 closeout 前分类。

## 实现后的 scope guard

从 repo root 运行：

```bash
python3 -c "import subprocess; allowed_prefixes=('docs/iterations/v0.6/','backend/app/schemas/world_generation.py','backend/app/core/world_generation.py','backend/app/tests/test_world_generation_schema.py','backend/app/tests/test_template_catalog.py','backend/app/tests/test_deterministic_world_generation.py'); lines=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[]; [bad.append(line) for line in lines if line and not any(line[3:].startswith(prefix) for prefix in allowed_prefixes)]; print('unexpected_status=' + str(len(bad))); [print(item) for item in bad]; raise SystemExit(1 if bad else 0)"
```

预期：`unexpected_status=0`。

## 授权前不运行的命令

在 `implementation_authorized: yes` 前，不运行 backend implementation tests，因为
implementation files 尚不存在，本 package 仍处于 documentation review。

Frontend、API smoke、E2E、Agent smoke、autonomous validation、migration、external
validation、projection 和 release commands 均不属于本 package 范围，除非后续已评审
package 授权。

## Blocker 记录规则

任何 failed command 都必须在 `review.md` 中记录 exact command、exit status 和 failure
summary。P1 阻断 implementation 或 closeout。除非 contract 和 review 明确接受，否则
unresolved P2 阻断最终 package handoff。
