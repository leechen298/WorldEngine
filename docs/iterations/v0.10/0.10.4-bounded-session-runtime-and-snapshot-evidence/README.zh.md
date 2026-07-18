# 0.10.4 Bounded Session Runtime And Snapshot Evidence

英文版本：`README.md`。

状态：`final / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

为 0.10.2 和 0.10.3 创建的 in-memory MVP session unit 增加 bounded session runtime
controls 和 public snapshot evidence。

本包允许 client 对已知 session 执行 bounded ticks 或 duration、pause/resume session
runtime，并检查 public snapshot evidence。不创建 autonomous Agent behavior、dashboard UI、
Validation Client behavior 或 durable persistence。

## Scope

review 后允许：

- 新增 session-scoped run、pause、resume 和 snapshot-list APIs。
- 复用现有 bounded `RuntimeRunRequest` 和 runtime engine guards。
- 增加 public session run summary fields，引用 session id、runtime deltas、event counts、
  snapshot counts 和 branch-ready timeline labels。
- 更新 manifest discovery，暴露 session runtime 和 snapshot surfaces。
- 增加 focused backend tests，覆盖 bounds、pause/resume、snapshot evidence、redaction
  和 existing runtime compatibility。

允许文件：

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- `backend/app/tests/test_runtime_bounded_run.py`
- package 和 parent v0.10 docs/reviews。

禁止：

- 不做 infinite default run。
- 不做 live provider calls 或 provider-cost execution。
- 不做 dashboard UI。
- 不做 checker fixtures 或 Validation Client implementation。
- 不写 generated result files 或 external validation。
- 不做 durable persistence 或 migration。
- 不改 `backend/worldengine/`。
- replay/worldline wording 不得暗示 parent/child worlds 或 source worlds。

## Deliverables

- 已评审 package docs and mirrors。
- Session run/pause/resume APIs。
- Session snapshot list API。
- Public session run summary and evidence references。
- Manifest discovery update。
- Focused backend tests and review evidence。

## Status Checklist

- [x] Package documents drafted。
- [x] Documentation / contract evaluator complete。
- [x] Implementation authorized。
- [x] Implementation complete。
- [x] Focused verification complete。
- [x] Evaluator closeout complete。
- [x] Review evidence updated。

## Final Assessment State

当前值：`PASS`。
