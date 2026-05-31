# 计划

状态：review complete

## 目标

创建并评审 `0.6.7` dashboard generation preview and E2E smoke package，然后只在
`implementation_authorized: yes` 后 implementation。

## 已读取输入

- `AGENTS.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.6/CURRENT_STATE.md`
- `docs/iterations/v0.6/v0.6-plan.md`
- `docs/iterations/v0.6/0.6.6-regeneration-and-runtime-readiness-integration/review.md`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/api/client.ts`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/e2e/agent-loop.spec.ts`
- `frontend/package.json`
- `frontend/playwright.config.ts`

## 执行步骤

1. 创建七个 required package docs 和中文镜像。
2. 初始状态保持为 `ready for review`，且 `implementation_authorized: no`。
3. 运行 documentation checks。
4. 请求 documentation/contract evaluator review。
5. Evaluator PASS 后，记录 `implementation_authorized: yes` 并同步 parent status surfaces。
6. 只实现 approved frontend/API-client/E2E files。
7. 运行 focused frontend、build、backend generation API、E2E、diff 和 scope checks。
8. 请求 implementation-scope、code-review、validation-evidence 和 closeout consistency
   evaluators。
9. 如果全部 checks 通过，标记 `0.6.7` review complete，并交接给 `0.6.8`。

## 要创建或更新的文件

Documentation stage：

- `docs/iterations/v0.6/0.6.7-dashboard-generation-preview-and-e2e-smoke/**`
- parent v0.6 status 和 review files。

Implementation stage after authorization：

- `frontend/src/api/client.ts`
- `frontend/src/api/client.test.ts`
- `frontend/src/components/GenerationPanel.vue`
- `frontend/src/components/GenerationPanel.test.ts`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/pages/DashboardPage.test.ts`
- `frontend/src/style.css`
- `frontend/e2e/dashboard-generation.spec.ts`，或对 `frontend/e2e/dashboard.spec.ts`
  做 focused additions。
- 本 package review files 和 parent status surfaces。

## 明确范围外文件

- backend implementation files。
- `backend/worldengine/**`
- persistence/repository modules。
- migrations。
- fixtures。
- generated output artifacts。
- external repositories。
- provider SDKs、prompt libraries、network clients 或 background workers。
- external validation runner 或 projection application files。

## 停止条件

- Authorization 前开始 implementation。
- Dashboard preview 需要 backend API/schema/runtime changes。
- UI store、publish、activate 或 mutate generated specs。
- E2E smoke 变成 external validation、autonomous validation、product readiness 或
  generation-quality validation。
- 引入 concrete demo-world/story data。
- Implementation 需要 approved list 之外的文件。

## 交接

Closeout 后，`0.6.8-v0.6-evidence-and-compatibility-audit` 接收 dashboard generation
preview 和 E2E smoke evidence。
