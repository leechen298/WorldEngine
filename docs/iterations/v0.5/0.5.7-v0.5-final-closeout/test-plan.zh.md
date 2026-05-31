# 测试计划

状态：final / closeout complete

## 验证策略

Final closeout 必须刷新 core backend evidence，并在应用 final status 前证明 documentation 和 status surfaces 一致。

## 必需命令

```bash
git diff --check
```

预期：退出码 `0`，无输出。

```bash
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.5'); parent_docs=['README','v0.5-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; child_extra={'0.5.6-v0.5-release-candidate-bundle':['release-candidate-bundle'],'0.5.7-v0.5-final-closeout':['final-closeout']}; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()];\nfor child in [p for p in parent.iterdir() if p.is_dir() and p.name.startswith('0.5.')]:\n    docs=child_docs + child_extra.get(child.name, [])\n    missing += [str(child/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]\nprint('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
```

预期：`missing=0`。

```bash
python3 -c "import subprocess; allowed=('docs/iterations/v0.5/','docs/roadmap.md','docs/roadmap.zh.md','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
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

Frontend、browser E2E、Agent smoke、autonomous、migrations、fixture 和 external validation checks 对 final v0.5 非必需，因为最终 implementation surface 是 backend memory/loop code。必须记录未运行原因，且不得转换为 pass claims。

## Evaluator Checkpoint

Final verification commands 后运行 closeout consistency evaluator。只有 evaluator PASS 后才可应用 final status。
