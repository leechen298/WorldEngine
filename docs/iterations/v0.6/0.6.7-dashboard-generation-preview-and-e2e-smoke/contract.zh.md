# 合同

状态：review complete

implementation_authorized: yes

## 公共概念

- `GenerationPanel`：dashboard component，用于提交 generic generation preview
  request 并检查 response。
- `GenerationApiClient`：面向现有 `/world/generation/preview`、
  `/world/generation/regenerate` 和 `/world/generation/runtime-readiness` routes 的
  frontend client additions。
- `DashboardGenerationSmoke`：browser E2E smoke，证明 dashboard 可以提交 generic
  preview、显示 metadata/diagnostics，并展示 bounded runtime-readiness status。

## UI 合同

Dashboard generation workflow 必须：

- 位于现有 dashboard application 内，不创建 landing page。
- 使用 generic operator-provided inputs 或 neutral defaults，不引入 concrete
  story/demo-world content。
- 展示 validation status、source kind、generation id、preview summary、diagnostics 和
  runtime-readiness status。
- 保持 raw `WorldSpec` payloads 仅限 inspectable preview output，并避免 raw prompts、
  provider traces、secrets、private oracle details 和 hidden provenance。
- 不改变现有 runtime controls、timeline、world params、agent 和 memory panels。

## 允许修改

Documentation stage：

- 在 `docs/iterations/v0.6/` 下创建和更新本 package。
- 只为 current child state 和 evidence 更新 parent v0.6 status surfaces。
- 记录 subagent/evaluator evidence。

Implementation stage，仅在 `implementation_authorized: yes` 后：

- 更新 `frontend/src/api/client.ts`。
- 更新 `frontend/src/api/client.test.ts`。
- 添加 `frontend/src/components/GenerationPanel.vue`。
- 添加 `frontend/src/components/GenerationPanel.test.ts`。
- 更新 `frontend/src/pages/DashboardPage.vue`。
- 更新 `frontend/src/pages/DashboardPage.test.ts`。
- 仅为 generation panel layout/states 更新 `frontend/src/style.css`。
- 在 `frontend/e2e/` 下新增或更新 focused Playwright E2E spec。
- 更新本 package `review.md` / `review.zh.md`。
- 只为 current child state 和 evidence 更新 parent v0.6 status surfaces。

本 package 不授权 backend implementation files。如果 frontend implementation 暴露 backend
API gap，必须停止并回到 documentation review，之后才可修改 backend code。

## 禁止修改

- 不修改 backend schema、core generation service、API routes、runtime engine、loader、
  runtime-context bridge、memory、Agent loop、archive、params、migrations、fixtures、
  external repositories 或 `backend/worldengine/**`。
- 不 persist、publish、activate generated spec，也不从 generated spec mutate live runtime state。
- 不添加 concrete demo-world data、story content、private validation oracle details、
  provider SDKs、network calls、prompt execution、credentials、generated output artifacts、
  external validation runner behavior 或 projection app behavior。
- 不把 frontend smoke 声明为 product readiness、generation quality、autonomous
  validation、external validation readiness、projection readiness、release readiness 或
  full runtime migration。

## 兼容性要求

- Existing dashboard panels 和 tests 保持兼容。
- Existing backend generation API envelopes 保持兼容。
- Existing E2E runtime、params、timeline、agent 和 memory smoke tests 保持兼容。
- Dashboard preview failures 使用现有 API-client error handling 和 visible error states。
- E2E evidence 仅为 browser smoke，不是 full autonomous 或 quality validation。

## 授权标准

本 package 只有在满足以下条件后才可记录 `implementation_authorized: yes`：

- 所有 package docs 和中文镜像存在。
- Documentation/contract evaluator 报告 PASS，且无 P0/P1、无 blocking unresolved P2。
- Contract/design/test-plan/plan 明确禁止 backend implementation changes、persistence、
  runtime activation、concrete content、live provider behavior、external validation/projection
  behavior 和 broad readiness claims。
- Planned tests 覆盖 frontend API-client behavior、component success/failure states、
  dashboard integration、browser E2E smoke、existing E2E compatibility、build、focused
  backend API compatibility 和 scope guard。

## 范围外后续

- `0.6.8`：evidence and compatibility audit。
- `0.6.9`：release-candidate bundle。
- `0.6.10`：final closeout。
