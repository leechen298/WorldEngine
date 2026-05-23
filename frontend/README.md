# Frontend

Status: v0.1 active dashboard

This folder contains the Vue 3 + TypeScript dashboard used by the current
WorldEngine v0.1 scaffold.

## Quick Start

```bash
cd frontend
pnpm install
pnpm dev
```

The app runs at `http://localhost:5173` by default.

## Environment

Set `VITE_API_BASE_URL` (default: `http://localhost:8000`) to point at the backend API.

## Stack

- Vue 3
- TypeScript
- Vite
- Ant Design Vue
- Vitest
- Vue Test Utils

## Current Surface

`src/App.vue` renders `DashboardPage`, the only v0.1 page.

The dashboard currently loads and renders:

- backend health.
- runtime state.
- grouped event steps.
- current world params.
- latest archive summary.

User-facing controls include:

- manual runtime stepping.
- cursor-paginated timeline inspection.
- expanded event details.
- manual world param patching.
- params-agent auto-tune flow.
- placeholder agent state panel.
- archive summary display.

The dashboard does not currently expose snapshot detail APIs, routing,
authentication, recursive world editing, or a game surface.

## Structure

- `src/api/client.ts` - API envelope handling and backend client functions.
- `src/pages/DashboardPage.vue` - dashboard data loading and coordination.
- `src/components/RuntimeControls.vue` - runtime step action.
- `src/components/TimelinePanel.vue` - grouped timeline table and pagination.
- `src/components/WorldPanel.vue` - params display, manual patches, and
  params-agent flow.
- `src/components/AgentPanel.vue` - placeholder agent state panel.
- `src/components/MemoryPanel.vue` - latest archive summary display.
- `src/style.css` - global dashboard styling.

## Verification

```bash
cd frontend
pnpm test
pnpm build
```

Latest recorded closeout results:

- unit tests: `24 passed`.
- production build: passed with a Vite chunk-size warning.

See `../docs/testing/v0.1-test-map.md` and
`../docs/testing/results/2026-05-23-v0.1-closeout.md`.
