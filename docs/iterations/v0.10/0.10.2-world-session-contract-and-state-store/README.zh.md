# 0.10.2 World Session Contract And State Store

英文版本：`README.md`。

状态：`final / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

添加第一版 public world session contract 和 in-memory session state store，使 client
可以创建、列出、读取并检查一个稳定的 MVP session unit。

本包不运行 session。它只创建 session identity 和 status surface，供后续
worldview-to-session creation、bounded runtime、snapshots、dashboard flow 和 validation
handoff 使用。

## Scope

文档评审后允许的 implementation scope：

- Public session schemas for create/list/read/status payloads。
- 挂在 FastAPI app state 上的 in-memory session store。
- Public session routes for create、list、read 和 status。
- Manifest additive updates，将已实现的 session discovery surfaces 标记清楚。
- Focused backend tests 覆盖 session lifecycle、isolation、redaction、manifest
  compatibility 和 existing world/runtime API compatibility。

允许 implementation files：

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/app_factory.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_world_session_api.py`
- `backend/app/tests/test_public_handoff_contract_api.py`
- package 和 parent v0.10 docs/reviews。

禁止范围：

- 不做 worldview-to-session generation flow。
- 不做 session runtime run controls、pause/resume wrappers、snapshot generation、
  diff/replay engine、dashboard flow、durable persistence、migrations、provider live calls、
  checker fixtures、Validation Client implementation、generated results、external validation
  或 `backend/worldengine/` changes。

## Deliverables

- 已评审 package docs and mirrors。
- Public in-memory world session contract and store。
- Session create/list/read/status API。
- Manifest discovery update for implemented session surfaces。
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

当前值：`final / focused verification passed`。

本包仅完成 session create/list/read/status。它不声明 worldview-to-session creation、session
runtime、snapshot generation、dashboard flow、provider live calls、checker output、Validation
Client execution、external validation 或 full v0.10 PASS。
