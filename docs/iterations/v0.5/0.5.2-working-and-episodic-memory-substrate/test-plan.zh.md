# 测试计划

状态：review complete

## TDD 要求

在 production code changes 前，先添加 memory substrate 的 focused failing backend tests，
并运行它们观察预期失败。

## Unit Tests

新增：

- `backend/app/tests/test_agent_memory_substrate.py`

必需覆盖：

- working-memory records validate required semantics。
- working-memory store 按 `agent_id` 和 `world_id` scoped。
- bounded working-memory listing deterministic 且 priority-aware。
- episodic records 保留 event references、tick 和 world time。
- episodic listing scoped 且 deterministic。
- store read results 不暴露 mutable backing state。

## Regression Tests

运行相邻 compatibility tests：

- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_service.py`
- `backend/app/tests/test_agent_loop_api.py`
- `backend/app/tests/test_agent_action_adapter.py`

只有当 implementation 触及 approved new modules 之外的 existing shared schemas、
app factory state、loop/API behavior、runtime、event、params、archive 或其他 shared surfaces 时，
才运行 full backend regression。

## 命令

Documentation 和 scope checks：

```bash
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.5/0.5.2-working-and-episodic-memory-substrate'); docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed=('docs/iterations/v0.5/0.5.0-v0.5-planning-and-continuity-boundary-baseline/','docs/iterations/v0.5/0.5.1-memory-self-continuity-contracts/','docs/iterations/v0.5/0.5.2-working-and-episodic-memory-substrate/','docs/iterations/v0.5/README.md','docs/iterations/v0.5/README.zh.md','docs/iterations/v0.5/CURRENT_STATE.md','docs/iterations/v0.5/CURRENT_STATE.zh.md','docs/iterations/v0.5/v0.5-plan.md','docs/iterations/v0.5/v0.5-plan.zh.md','docs/iterations/v0.5/review.md','docs/iterations/v0.5/review.zh.md','backend/app/schemas/agent_memory.py','backend/app/agent/memory.py','backend/app/tests/test_agent_memory_substrate.py'); out=subprocess.check_output(['git','status','--short'], text=True).splitlines(); bad=[line for line in out if line and not any(line[3:].startswith(prefix) for prefix in allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

预期结果：

- `git diff --check` 退出码为 0，且无输出。
- package docs and mirrors check 输出 `missing=0`。
- changed-file scope guard 输出 `out_of_scope=0`。
- TDD red run 在 production code 前失败，因为 memory substrate module 尚不存在。
- implementation 后 focused memory tests 通过。
- 相邻 compatibility tests 通过，且 existing loop/action behavior 不变。

TDD red command：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py -q
```

Focused 和 adjacent green commands：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_memory_substrate.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_agent_perception.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_agent_action_adapter.py -q
```

如 touched surfaces 需要，可选运行 broader backend regression：

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

## 接受标准

- Production code 前记录 TDD red failure。
- Focused memory tests 通过。
- 相邻 loop/perception/API/action tests 通过。
- Documentation checks 和 changed-file scope guard 通过。
- 必需 evaluators 在 closeout 前没有 unresolved P1/P2。

## 阻塞记录规则

如果任何 documentation、TDD、focused、adjacent compatibility 或 scope check 失败，
在 `review.md` 记录 exact command、exit status 和 failure summary。只在 approved package
scope 内修复，然后在声称进展前重新运行失败命令。

如果 required evaluator 不可用，或返回 P1/blocking P2，记录 `BLOCKED` 或
`NEEDS_USER_INPUT`，不要开始或关闭 implementation。

## 禁止未验证声明规则

不要把 backend tests、compatibility tests、runtime/API behavior、E2E、Agent smoke、
autonomous validation、build、migration 或 release evidence 标记为 passed，除非当前会话已运行
exact command 或 flow，并把结果记录到 `review.md`。

## 未运行项

Frontend、E2E、Agent smoke、autonomous validation、fixture validation、migrations、
external validation runners 和 builds 默认不要求运行，除非 implementation 意外触及这些表面。
任何 skipped check 都必须记录到 `review.md`。
