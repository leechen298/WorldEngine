# v0.5 发布候选包

状态：prepared for review

本 bundle 由 `0.5.6` 准备，用于 review。它不是 final closeout。

## 纳入 Packages

- `0.5.1-memory-self-continuity-contracts`：review complete。
- `0.5.2-working-and-episodic-memory-substrate`：review complete。
- `0.5.3-memory-context-loop-integration`：review complete。
- `0.5.4-reflection-relationship-and-drift-contract-followup`：review complete。
- `0.5.5-v0.5-evidence-and-compatibility-audit`：review complete。

## 纳入 Implementation Files

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`
- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_api.py`

## 纳入 Behavior

- Generic working-memory 和 episodic-memory schemas。
- Process-local in-memory memory substrate。
- Agent Loop perception 中的 optional bounded read-only memory context。
- 用于 perception context 的 internal app-state memory store wiring。

## 排除 Behavior

- Memory persistence。
- Public memory APIs。
- Loop request memory selectors。
- Loop steps 中写 memory。
- Action semantic changes。
- Relationship behavior。
- Self-summary generation。
- Automatic reflection。
- Personality drift action modifiers。
- Frontend behavior。
- World generation。
- External validation readiness。
- Projection application readiness。

## 证据摘要

来自 `0.5.5` audit：

- `git diff --check`：通过。
- Required docs/mirrors check：`missing=0`。
- Baseline-aware changed-file scope guard：`out_of_scope=0`。
- Forbidden implementation surface sentinel：`backend/worldengine`、frontend、
  alembic 或 migrations 均无输出。
- Focused v0.5 memory/loop/action compatibility：`33 passed`。
- Full backend regression：`145 passed`。
- Evidence/compatibility evaluator：PASS，无 P1/P2/P3 findings。

## Review 问题

- Bundle 是否保持 WorldEngine generic？
- 所有 v0.5 implementation changes 是否 additive？
- Deferred capabilities 是否明确没有实现？
- 当前 evidence 是否足以进入 final closeout review？
- 是否存在 unresolved P1/P2 findings？

## Final Closeout Gate

`0.5.7` 必须运行 final consistency 和 verification checks 后，v0.5 才可标记为 final。
