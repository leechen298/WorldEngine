# 0.10.3 Worldview To Runtime Session Creation

英文版本：`README.md`。

状态：`final / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

通过复用现有 redacted worldview generation contract 和 deterministic/mock fallback labels，
从用户 worldview input 创建 public session。

本包把 worldview input 连接到 `0.10.2` session unit。不运行 session、不生成 snapshot、
不构建 dashboard UI，也不发起 live provider call。

## Scope

review 后允许：

- 新增 `POST /sessions/from-worldview`。
- 复用 `generate_worldview_response()` 和 `provider_readiness_from_env()`。
- 创建 `world_id` 和 public metadata 来自 generated public world model 的 session。
- 向 session payload 添加 public generation mode/status 和 redacted generation/session refs。
- 更新 manifest discovery 和 focused backend tests。

允许文件：

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- package 和 parent v0.10 docs/reviews。

禁止：

- 不授权 live provider call。
- 不做 runtime run controls、snapshot generation、dashboard、durable persistence、checker
  fixtures、Validation Client implementation、generated result writing、external validation 或
  `backend/worldengine/` changes。

## Deliverables

- 已评审 package docs and mirrors。
- Worldview-to-session API。
- Session payload 包含 public generation mode/status 和 redacted generation/session refs。
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
