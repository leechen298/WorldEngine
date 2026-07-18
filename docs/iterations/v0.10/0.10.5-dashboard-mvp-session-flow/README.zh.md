# 0.10.5 Dashboard MVP Session Flow

英文版本：`README.md`。

状态：`final / focused verification passed`
类型：mixed implementation package
implementation_authorized: yes
evidence_execution_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## Goal

把现有 dashboard 调整成紧凑 MVP session flow：从 worldview input 创建 session、运行 bounded
session ticks，并检查 timeline/snapshot evidence。

本包让 human 可以通过 dashboard 使用现有 backend session APIs。它不把 dashboard 变成 world
simulation authority，也不增加 provider key management 或 concrete demo assets。

## Scope

review 后允许：

- 增加 frontend API client methods 和 types，覆盖 session create-from-worldview、session
  run、pause、resume、status 和 snapshots。
- 更新 dashboard，展示 MVP session shell，包含 worldview input、session status、bounded run
  controls、timeline refresh 和 snapshot evidence。
- 尽量复用现有 panels；除非明确整合，不移除现有 runtime/world panels。
- 增加 focused frontend unit tests 和 targeted dashboard E2E smoke。
- 运行可用的 frontend unit/build/E2E commands，以及 UI 行为需要的 backend focused tests。

允许文件：

- `frontend/src/api/client.ts`
- `frontend/src/api/client.test.ts`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/pages/DashboardPage.test.ts`
- `frontend/src/components/RuntimeControls.vue`
- `frontend/src/components/RuntimeControls.test.ts`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/src/style.css`
- package 和 parent v0.10 docs/reviews。

禁止：

- 不做 polished game art 或 concrete demo assets。
- 不做 provider key UI 或 live provider execution。
- 不做 Validation Client code。
- 不做 checker fixture implementation。
- 不做 durable persistence 或 migration。
- 不展示 raw prompt/response/provider trace。
- 不改 `backend/worldengine/`。

## Deliverables

- 已评审 package docs and mirrors。
- Dashboard MVP session create/run/inspect flow。
- Frontend API client coverage。
- Unit tests 和 targeted E2E smoke evidence。
- Review evidence and handoff to v0.10 validation。

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
