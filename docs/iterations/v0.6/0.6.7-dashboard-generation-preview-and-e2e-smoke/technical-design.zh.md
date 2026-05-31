# 技术设计

状态：review complete

## 设计边界

`0.6.7` 围绕现有 generation APIs 添加 dashboard workflow。它是 frontend 和 E2E
package；不 redesign backend generation contracts、不 activate generated specs，也不添加
persistence。

## Frontend API Client 设计

`frontend/src/api/client.ts` 可以为以下对象添加 TypeScript interfaces 和 functions：

- generation preview request/response。
- regeneration request/response。
- runtime-readiness request/response。

Client 应保持现有 `ApiResponse` envelope handling，并通过 `ApiClientError` 暴露 backend
validation errors。

## Dashboard Component 设计

`frontend/src/components/GenerationPanel.vue` 应：

- 渲染在现有 dashboard page 内。
- 为 request id、root id/label、child id/label 和 seed text 或等价 neutral generic fields
  提供 compact inputs。
- 调用 preview API，并在 successful previews 后调用 runtime-readiness API。
- 展示 status、generation id、summary counts、diagnostics 和 readiness status，并提供稳定
  `data-test` hooks 给 unit 和 E2E tests。
- 保持与现有 Ant Design dashboard panels 一致的 layout。

## Dashboard Integration 设计

`frontend/src/pages/DashboardPage.vue` 可以在现有 panel grid 中挂载该 panel。它不得破坏
runtime controls、timeline、world params、agent 或 memory panel behavior。

## E2E Smoke 设计

Browser smoke 应：

- 打开 dashboard。
- 通过 visible controls 提交 generic preview request。
- 验证 passed preview status、generation metadata、bounded summary 和 readiness pass status。
- 在适用处验证 invalid input 或 backend diagnostics 可见。
- 只声明 dashboard preview smoke。

## 兼容性

Existing frontend unit tests、build、backend generation API focused tests，以及现有
Playwright dashboard/agent-loop tests 必须继续通过。
