# 测试计划

状态：review complete

## 验证策略

`0.5.4` 是 documentation-only。验证目标是证明 package docs 和 mirrors 存在，worktree
保持在 documentation scope 内，并且没有触及 runtime/code surfaces。

## 必需命令

```bash
git diff --check
```

预期：退出码 `0`，无输出。

```bash
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.4-reflection-relationship-and-drift-contract-followup'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

预期：`missing=0`。

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.5/','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

预期：`out_of_scope=0`。Baseline 允许 inherited reviewed `0.5.2` 和 `0.5.3`
implementation files，因为本 `/goal` campaign 会累积为一个 final commit。

```bash
git status --short -- backend/worldengine frontend backend/app/alembic backend/migrations
```

预期：无输出。

## Backend Tests

`0.5.4` 不要求 backend tests，因为它是 documentation-only，且不改变 runtime、schemas、
APIs、services、tests、migrations 或 frontend behavior。

Review 必须明确记录 backend/frontend/API/E2E/build/Agent smoke/autonomous checks
未运行及原因。

## Evaluator Checkpoint

Docs 和本地检查完成后，运行只读 documentation/contract evaluator。Evaluator 必须报告无
P1 且无 blocking P2，才能 closeout。
