# Frontend Implementation

Status: current frontend map through v0.6

This document describes the current `frontend/src/` implementation after the
v0.6 final closeout and 0.6.11 post-closeout reliability/scope repair.

## Stack

- Vue 3
- TypeScript
- Vite
- Ant Design Vue
- Vitest
- Vue Test Utils

Scripts:

```bash
pnpm dev
pnpm test
pnpm build
```

`VITE_API_BASE_URL` controls the backend URL. If unset, the frontend uses
`http://localhost:8000`.

## App Structure

`frontend/src/App.vue` renders `DashboardPage`.

`DashboardPage` is the main dashboard surface. It loads and coordinates:

- backend health.
- runtime state.
- grouped event steps.
- world params.
- latest summary.
- generation preview state.

## API Client

File: `frontend/src/api/client.ts`

The API client wraps fetch and expects the backend envelope:

```text
{ code, data, msg }
```

If the HTTP response is not OK or the response code is not `0`, it throws
`ApiClientError` with:

- `status`
- `code`
- `data`

Implemented client functions:

- `fetchHealth()`
- `getRuntimeState()`
- `stepRuntime()`
- `getWorldEvents()`
- `getWorldEventSteps()`
- `getWorldParams()`
- `applyWorldParams()`
- `proposeAndApplyWorldParams()`
- `getWorldSummaries()`
- `previewGeneration()`
- `checkGenerationRuntimeReadiness()`
- `regenerateWorld()`

The frontend does not currently call snapshot APIs.

The frontend client also does not expose the v0.4/v0.5 Agent Loop endpoint as
a dashboard workflow. Agent Loop behavior is covered by browser E2E through
direct API calls.

## Dashboard Page

File: `frontend/src/pages/DashboardPage.vue`

Responsibilities:

- render health and runtime status cards.
- load initial data on mount.
- coordinate event pagination.
- reload runtime, timeline, and latest summary after a runtime step.
- update local world params after manual or agent-applied patch.
- mount the generation preview panel.

Data loading functions:

- `loadRuntimeState()`
- `loadEvents()`
- `loadWorldParams()`
- `loadLatestSummary()`

Event pagination is cursor-based and newest-first.

## Runtime Controls

File: `frontend/src/components/RuntimeControls.vue`

The component renders one primary `Step` button. On click it calls
`stepRuntime()` and emits `stepped` so the dashboard can refresh runtime state,
timeline, and summary.

## Timeline Panel

File: `frontend/src/components/TimelinePanel.vue`

The panel renders grouped event steps from `/world/event-steps`.

Features:

- table grouped by tick.
- event count per tick.
- type-count summary per step.
- expandable event details.
- page size selection.
- previous/next cursor pagination.
- newest-first display.

Details are formatted from event payload fields such as `module_path`,
`summary`, `counter`, `patches`, and `params`.

## World Panel

File: `frontend/src/components/WorldPanel.vue`

The panel renders current params as JSON and provides two modification flows.

Manual patch flow:

1. user enters a dot path.
2. user selects value type.
3. component builds a structured value:
   `{ "value": <value>, "type": "<type>", "unit": "<optional>" }`.
4. component sends `POST /world/params/apply`.
5. validation or dry-run errors are shown from `ApiClientError.data.errors`.

Agent flow:

1. user optionally enters a goal.
2. component sends `POST /world/agent/params/propose-and-apply`.
3. on success, component fetches current params.
4. applied patches are shown in expandable details.

## Agent Panel

File: `frontend/src/components/AgentPanel.vue`

The Agent Panel is a placeholder. It does not show persistent agent state,
memory, identity, goals, or actions.

## Memory Panel

File: `frontend/src/components/MemoryPanel.vue`

The Memory Panel displays the latest archive summary:

- tick range.
- total events.
- created time.
- summary text.
- event type counts.

This is archive-summary display, not agent memory.

## Generation Panel

File: `frontend/src/components/GenerationPanel.vue`

The v0.6 dashboard includes a generic generation preview workflow. The panel:

- builds a generic template preview request from operator-provided request,
  root, child, and seed fields.
- calls `POST /world/generation/preview` through `previewGeneration()`.
- renders validation status, generation id, source kind, and preview summary.
- renders generation diagnostics for failed previews.
- calls `POST /world/generation/runtime-readiness` only after a passed preview
  returns a `worldspec_preview`.
- renders runtime-readiness status and diagnostics.

The panel is a preview and readiness surface. It does not expose live-provider
generation, prompt execution, subjective generation-quality approval, external
validation readiness, or projection application readiness.

Current evidence includes frontend unit `36 passed`, production build passed
with the existing Vite large-chunk warning, and E2E `17 passed` including
generation preview success and diagnostics failure-path rendering.

## Styling

File: `frontend/src/style.css`

The dashboard uses a centered max-width layout with a responsive grid for
panels. Component-specific styles live inside scoped style blocks.

## Frontend Limits

- No routing; the dashboard is the only page.
- No authenticated user model.
- No persistent client-side store.
- Snapshot APIs are not exposed in the dashboard.
- Agent and memory panels are placeholders or archive displays, not full agent
  cognition surfaces.
- No frontend product behavior exposes v0.5 memory records or memory-context
  management.
- Agent Loop is covered by E2E API/browser baseline tests, not by a dashboard
  product control.
- Generation preview is available, but no live-provider workflow, external
  validation UI, projection readiness UI, product packaging flow, or
  generation-quality approval UI is present.
- Production build currently emits a chunk-size warning.
