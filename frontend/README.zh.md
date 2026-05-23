# Frontend

Status: v0.1 active dashboard

英文版本：`README.md`。

本目录包含当前 WorldEngine v0.1 scaffold 使用的 Vue 3 + TypeScript dashboard。

## Quick Start

```bash
cd frontend
pnpm install
pnpm dev
```

应用默认运行在 `http://localhost:5173`。

## Environment

设置 `VITE_API_BASE_URL`（默认：`http://localhost:8000`）即可指向 backend API。

## Stack

- Vue 3
- TypeScript
- Vite
- Ant Design Vue
- Vitest
- Vue Test Utils

## Current Surface

`src/App.vue` 渲染 `DashboardPage`，这是 v0.1 唯一页面。

dashboard 当前加载和渲染：

- backend health。
- runtime state。
- grouped event steps。
- current world params。
- latest archive summary。

用户可见 controls 包括：

- manual runtime stepping。
- cursor-paginated timeline inspection。
- expanded event details。
- manual world param patching。
- params-agent auto-tune flow。
- placeholder agent state panel。
- archive summary display。

dashboard 当前不暴露 snapshot detail APIs、routing、authentication、recursive world editing 或 game
surface。

## Structure

- `src/api/client.ts` - API envelope handling 与 backend client functions。
- `src/pages/DashboardPage.vue` - dashboard data loading 与 coordination。
- `src/components/RuntimeControls.vue` - runtime step action。
- `src/components/TimelinePanel.vue` - grouped timeline table 与 pagination。
- `src/components/WorldPanel.vue` - params display、manual patches 和 params-agent flow。
- `src/components/AgentPanel.vue` - placeholder agent state panel。
- `src/components/MemoryPanel.vue` - latest archive summary display。
- `src/style.css` - global dashboard styling。

## Verification

```bash
cd frontend
pnpm test
pnpm build
```

最新记录的 closeout results：

- unit tests: `24 passed`。
- production build: passed with a Vite chunk-size warning。

见 `../docs/testing/v0.1-test-map.md` 和
`../docs/testing/results/2026-05-23-v0.1-closeout.md`。
