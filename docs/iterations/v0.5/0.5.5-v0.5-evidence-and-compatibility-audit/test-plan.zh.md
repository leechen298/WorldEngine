# 测试计划

状态：review complete

## 验证策略

`0.5.5` 是 documentation-only，但它审计 implementation evidence。因此必须运行
documentation checks，并刷新已实现 v0.5 surfaces 的核心 backend regression evidence。

## 必需命令

```bash
git diff --check
```

预期：退出码 `0`，无输出。

```bash
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.5-v0.5-evidence-and-compatibility-audit'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

预期：`missing=0`。

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.5/','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

预期：`out_of_scope=0`。

```bash
git status --short -- backend/worldengine frontend backend/app/alembic backend/migrations
```

预期：无输出。

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py app/tests/test_agent_perception.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_agent_action_adapter.py -q
```

预期：退出码 `0`。

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

预期：退出码 `0`。

## 跳过检查

Frontend、browser E2E、Agent smoke、autonomous、migrations、fixture 和 external
validation checks 对 `0.5.5` 非必需，因为本 package 不改变这些 surfaces。Review 必须记录
它们未运行的原因。

## Evaluator Checkpoint

本地检查后运行只读 evidence/compatibility evaluator。
