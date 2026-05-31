# Technical Design

Status: review complete

## Design Boundary

`0.6.7` adds a dashboard workflow around existing generation APIs. It is a
frontend and E2E package; it does not redesign backend generation contracts,
activate generated specs, or add persistence.

## Frontend API Client

`frontend/src/api/client.ts` may add TypeScript interfaces and functions for:

- generation preview request/response.
- regeneration request/response.
- runtime-readiness request/response.

The client should preserve the existing `ApiResponse` envelope handling and
surface backend validation errors through `ApiClientError`.

## Dashboard Component

`frontend/src/components/GenerationPanel.vue` should:

- render inside the existing dashboard page.
- provide compact inputs for request id, root id/label, child id/label, and
  seed text or equivalent neutral generic fields.
- call the preview API, then runtime-readiness API for successful previews.
- display status, generation id, summary counts, diagnostics, and readiness
  status with predictable `data-test` hooks for unit and E2E tests.
- keep layout consistent with existing Ant Design dashboard panels.

## Dashboard Integration

`frontend/src/pages/DashboardPage.vue` may mount the panel in the existing
panel grid. It must not disrupt runtime controls, timeline, world params,
agent, or memory panel behavior.

## E2E Smoke

The browser smoke should:

- open the dashboard.
- submit a generic preview request through visible controls.
- verify a passed preview status, generation metadata, bounded summary, and
  readiness pass status.
- verify invalid input or backend diagnostics are visible where applicable.
- keep the claim to dashboard preview smoke only.

## Compatibility

Existing frontend unit tests, build, backend generation API focused tests, and
existing Playwright dashboard/agent-loop tests must continue to pass.
