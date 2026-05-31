# 测试计划

状态：review complete

## TDD 要求

Production code changes 前，先为 perception 或 loop API 中的 memory context 添加 focused
failing test，并运行它观察预期失败。

## 单元测试

更新或新增 focused tests，覆盖：

- `PerceptionBuilder` 包含 bounded working 和 episodic memory context。
- memory context 被 copy，不能 mutate store backing state。
- 没有 memory store 时，旧 `PerceptionBuilder` callers 仍可用。
- loop API 只 additive 地包含 memory context，并保持旧 request compatibility。
- action result behavior 保持不变。

## 回归测试

运行：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py app/tests/test_agent_perception.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_agent_action_adapter.py -q
```

如果 app factory wiring 触及 shared state，运行更广的相邻 compatibility：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_params.py app/tests/test_event_api_compat.py app/tests/test_event_schema_compat.py app/tests/test_runtime_step.py -q
```

只有当 implementation 触及 approved loop/perception/app-factory memory wiring 之外的 behavior 时，
才运行 full backend regression。

## 命令

Documentation 和 scope checks：

```bash
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.3-memory-context-loop-integration'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed=('docs/iterations/v0.5/','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py','backend/app/schemas/agent_loop.py','backend/app/agent/perception.py','backend/app/api/app_factory.py','backend/app/tests/test_agent_perception.py','backend/app/tests/test_agent_loop_api.py','backend/app/tests/test_agent_loop_service.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

## 预期结果

- Documentation checks 输出 `missing=0` 和 `out_of_scope=0`。
- Scope guard 将已评审的 `0.5.2` memory substrate files 作为本 single-commit
  `/goal` campaign 的 inherited baseline 接受。
- TDD red 在 production code 前失败，因为 `PerceptionFrame` 尚无 memory context。
- Implementation 后 focused/adjacent backend tests 通过。
- Existing strict request validation 和 action behavior tests 继续通过。

## 阻塞记录规则

在 `review.md` 记录任何 failed command、exit status 和 failure summary。只在 approved scope
内修复，并在声称进展前重新运行失败命令。

## 禁止未验证声明规则

不要声称 API、loop、runtime、frontend、E2E、Agent smoke、autonomous、fixture、
migration、build 或 release behavior passed，除非记录了当前会话的 exact command 或 flow。

## 未运行项

Frontend、E2E、Agent smoke、autonomous validation、fixture validation、migrations、
external validation runners 和 builds 默认不要求运行，除非 implementation 触及这些表面。
