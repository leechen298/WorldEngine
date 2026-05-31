# Frontend Implementation

状态：当前前端地图，覆盖到 v0.5

英文版本：`frontend-implementation.md`。

本文档描述当前 `frontend/src/` implementation。

## Stack

- Vue 3
- TypeScript
- Vite
- Ant Design Vue
- Vitest
- Vue Test Utils

Scripts：

```bash
pnpm dev
pnpm test
pnpm build
```

`VITE_API_BASE_URL` 控制 backend URL。未设置时，frontend 使用 `http://localhost:8000`。

## App Structure

`frontend/src/App.vue` 渲染 `DashboardPage`。

`DashboardPage` 是 main dashboard surface。它加载并协调：

- backend health。
- runtime state。
- grouped event steps。
- world params。
- latest summary。

## API Client

File: `frontend/src/api/client.ts`

API client 封装 fetch，并期望 backend envelope：

```text
{ code, data, msg }
```

如果 HTTP response 不是 OK，或 response code 不是 `0`，它会抛出 `ApiClientError`，包含：

- `status`
- `code`
- `data`

已实现 client functions：

- `fetchHealth()`
- `getRuntimeState()`
- `stepRuntime()`
- `getWorldEvents()`
- `getWorldEventSteps()`
- `getWorldParams()`
- `applyWorldParams()`
- `proposeAndApplyWorldParams()`
- `getWorldSummaries()`

Frontend 当前不调用 snapshot APIs。

Frontend client 也没有把 v0.4/v0.5 Agent Loop endpoint 暴露为 dashboard workflow。
Agent Loop behavior 通过 browser E2E 中的 direct API calls 覆盖。

## Dashboard Page

File: `frontend/src/pages/DashboardPage.vue`

Responsibilities：

- 渲染 health 和 runtime status cards。
- mount 时加载 initial data。
- 协调 event pagination。
- runtime step 后 reload runtime、timeline 和 latest summary。
- manual 或 agent-applied patch 后更新 local world params。

Data loading functions：

- `loadRuntimeState()`
- `loadEvents()`
- `loadWorldParams()`
- `loadLatestSummary()`

Event pagination 是 cursor-based 和 newest-first。

## Runtime Controls

File: `frontend/src/components/RuntimeControls.vue`

组件渲染一个 primary `Step` button。点击后调用 `stepRuntime()` 并 emit `stepped`，让 dashboard
刷新 runtime state、timeline 和 summary。

## Timeline Panel

File: `frontend/src/components/TimelinePanel.vue`

该 panel 渲染来自 `/world/event-steps` 的 grouped event steps。

Features：

- 按 tick 分组的 table。
- 每个 tick 的 event count。
- 每个 step 的 type-count summary。
- expandable event details。
- page size selection。
- previous/next cursor pagination。
- newest-first display。

Details 会从 `module_path`、`summary`、`counter`、`patches` 和 `params` 等 event payload fields 格式化。

## World Panel

File: `frontend/src/components/WorldPanel.vue`

该 panel 把 current params 渲染为 JSON，并提供两个 modification flows。

Manual patch flow：

1. 用户输入 dot path。
2. 用户选择 value type。
3. 组件构造 structured value：
   `{ "value": <value>, "type": "<type>", "unit": "<optional>" }`。
4. 组件发送 `POST /world/params/apply`。
5. 从 `ApiClientError.data.errors` 展示 validation 或 dry-run errors。

Agent flow：

1. 用户可选输入 goal。
2. 组件发送 `POST /world/agent/params/propose-and-apply`。
3. 成功后，组件拉取 current params。
4. 在 expandable details 中展示 applied patches。

## Agent Panel

File: `frontend/src/components/AgentPanel.vue`

Agent Panel 是 placeholder。它不展示 persistent agent state、memory、identity、goals 或 actions。

## Memory Panel

File: `frontend/src/components/MemoryPanel.vue`

Memory Panel 展示 latest archive summary：

- tick range。
- total events。
- created time。
- summary text。
- event type counts。

这是 archive-summary display，不是 Agent memory。

## Styling

File: `frontend/src/style.css`

dashboard 使用 centered max-width layout，并用 responsive grid 布局 panels。Component-specific styles
位于 scoped style blocks。

## Frontend Limits

- 没有 routing；dashboard 是唯一页面。
- 没有 authenticated user model。
- 没有 persistent client-side store。
- dashboard 不暴露 Snapshot APIs。
- Agent 和 memory panels 是 placeholders 或 archive displays，不是完整 Agent cognition surfaces。
- 没有 frontend product behavior 暴露 v0.5 memory records 或 memory-context management。
- Agent Loop 由 E2E API/browser baseline tests 覆盖，不是 dashboard product control。
- Production build 当前会输出 chunk-size warning。
