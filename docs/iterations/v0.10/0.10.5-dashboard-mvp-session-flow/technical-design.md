# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Affected Files

- `frontend/src/api/client.ts`
- `frontend/src/api/client.test.ts`
- `frontend/src/pages/DashboardPage.vue`
- `frontend/src/pages/DashboardPage.test.ts`
- `frontend/src/components/RuntimeControls.vue`
- `frontend/src/components/RuntimeControls.test.ts`
- `frontend/e2e/dashboard.spec.ts`
- `frontend/src/style.css`
- package and parent v0.10 docs/reviews.

## Design

Extend `frontend/src/api/client.ts` with public session types and methods:

- `createSessionFromWorldview`.
- `runSession`.
- `pauseSession`.
- `resumeSession`.
- `getSessionStatus`.
- `listSessionSnapshots`.

Update `RuntimeControls.vue` to support session-scoped run controls when a
session id is provided while preserving the existing one-step global runtime
behavior where needed by existing tests.

Update `DashboardPage.vue` to add a compact session work area:

- premise textarea/input and create button.
- current session summary.
- bounded tick input and run button.
- pause/resume controls.
- latest run evidence summary.
- snapshot evidence table/list.
- refresh timeline/runtime after create/run.

Keep the layout operational and dense. Avoid landing-page or decorative hero
patterns.

## Redaction

Do not render raw prompts, raw provider responses, provider traces, secrets,
private memory, hidden context, or private evaluator data. Display only public
generation/session summary fields returned by the backend.

## Non-Goals

No backend feature expansion, no Validation Client integration, no provider
key entry UI, no concrete demo assets, and no polished game presentation.
