# Technical Design

英文版本：`technical-design.md`。

## Affected Files

- `frontend/src/api/client.ts`
- `frontend/src/api/client.test.ts`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/pages/DashboardPage.test.ts`
- `frontend/src/components/RuntimeControls.vue`
- `frontend/src/components/RuntimeControls.test.ts`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/src/style.css`
- package 和 parent v0.10 docs/reviews。

## Design

扩展 `frontend/src/api/client.ts`，新增 public session types and methods：

- `createSessionFromWorldview`。
- `runSession`。
- `pauseSession`。
- `resumeSession`。
- `getSessionStatus`。
- `listSessionSnapshots`。

更新 `RuntimeControls.vue`：当提供 session id 时支持 session-scoped run controls，同时在需要时
保留现有 one-step global runtime behavior，以兼容 existing tests。

更新 `DashboardPage.vue`，增加紧凑 session work area：

- premise textarea/input 和 create button。
- current session summary。
- bounded tick input 和 run button。
- pause/resume controls。
- latest run evidence summary。
- snapshot evidence table/list。
- create/run 后刷新 timeline/runtime。

Layout 应保持 operational and dense，避免 landing-page 或 decorative hero patterns。

## Redaction

不渲染 raw prompts、raw provider responses、provider traces、secrets、private memory、
hidden context 或 private evaluator data。只展示 backend 返回的 public generation/session
summary fields。

## Non-Goals

不扩展 backend features，不集成 Validation Client，不做 provider key entry UI，不加 concrete
demo assets，不做 polished game presentation。
