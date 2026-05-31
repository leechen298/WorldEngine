# 测试计划

状态：review complete

## 验证策略

`0.5.6` 是 documentation-only。它打包已审计 evidence，必须证明 bundle docs 存在、
status wording 有边界，且没有改变 implementation surfaces。

## 必需命令

```bash
git diff --check
```

预期：退出码 `0`，无输出。

```bash
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.6-v0.5-release-candidate-bundle'); docs=['README','intent','contract','technical-design','test-plan','plan','release-candidate-bundle','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
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
rg -n "final / closeout complete|final release|released|Status: final|状态：final" docs/iterations/v0.5/0.5.6-v0.5-release-candidate-bundle
```

预期：只出现 forbidden-scope descriptions，不作为 status declaration。

## Backend Tests

`0.5.6` 不要求 backend tests，因为它只打包当前 `0.5.5` audit evidence。Review 必须引用
`0.5.5` fresh backend evidence，并记录为何本 package 不重跑 tests。

## Evaluator Checkpoint

运行只读 release-candidate bundle evaluator。
