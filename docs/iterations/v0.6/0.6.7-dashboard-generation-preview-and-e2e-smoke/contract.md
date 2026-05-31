# Contract

Status: review complete

implementation_authorized: yes

## Public Concepts

- `GenerationPanel`: dashboard component for submitting a generic generation
  preview request and inspecting the response.
- `GenerationApiClient`: frontend client additions for existing
  `/world/generation/preview`, `/world/generation/regenerate`, and
  `/world/generation/runtime-readiness` routes.
- `DashboardGenerationSmoke`: browser E2E smoke proving the dashboard can
  submit a generic preview, display metadata/diagnostics, and surface bounded
  runtime-readiness status.

## UI Contract

The dashboard generation workflow must:

- live inside the existing dashboard application, not a landing page.
- use generic operator-provided inputs or neutral defaults, not concrete
  story/demo-world content.
- display validation status, source kind, generation id, preview summary,
  diagnostics, and runtime-readiness status.
- keep raw `WorldSpec` payloads bounded to inspectable preview output and avoid
  raw prompts, provider traces, secrets, private oracle details, and hidden
  provenance.
- avoid changing existing runtime controls, timeline, world params, agent, and
  memory panels.

## Allowed Changes

Documentation stage:

- create and update this package under `docs/iterations/v0.6/`.
- update parent v0.6 status surfaces only for current child state and
  evidence.
- record subagent/evaluator evidence.

Implementation stage, only after `implementation_authorized: yes`:

- update `frontend/src/api/client.ts`.
- update `frontend/src/api/client.test.ts`.
- add `frontend/src/components/GenerationPanel.vue`.
- add `frontend/src/components/GenerationPanel.test.ts`.
- update `frontend/src/pages/DashboardPage.vue`.
- update `frontend/src/pages/DashboardPage.test.ts`.
- update `frontend/src/style.css` only for generation panel layout/states.
- add or update a focused Playwright E2E spec under `frontend/e2e/`.
- update this package `review.md` / `review.zh.md`.
- update parent v0.6 status surfaces only for current child state and
  evidence.

Backend implementation files are not authorized by this package. If frontend
implementation reveals a backend API gap, stop and return to documentation
review before changing backend code.

## Forbidden Changes

- Do not change backend schema, core generation service, API routes, runtime
  engine, loader, runtime-context bridge, memory, Agent loop, archive, params,
  migrations, fixtures, external repositories, or `backend/worldengine/**`.
- Do not persist, publish, activate, or mutate live runtime state from a
  generated spec.
- Do not add concrete demo-world data, story content, private validation oracle
  details, provider SDKs, network calls, prompt execution, credentials,
  generated output artifacts, external validation runner behavior, or
  projection app behavior.
- Do not claim frontend smoke as product readiness, generation quality,
  autonomous validation, external validation readiness, projection readiness,
  release readiness, or full runtime migration.

## Compatibility Requirements

- Existing dashboard panels and tests remain compatible.
- Existing backend generation API envelopes remain compatible.
- Existing E2E runtime, params, timeline, agent, and memory smoke tests remain
  compatible.
- Dashboard preview failures use existing API-client error handling and visible
  error states.
- E2E evidence is browser smoke only, not full autonomous or quality
  validation.

## Authorization Criteria

This package may record `implementation_authorized: yes` only after:

- all package docs and Chinese mirrors exist.
- documentation/contract evaluator reports PASS with no P0/P1 and no blocking
  unresolved P2.
- contract/design/test-plan/plan explicitly forbid backend implementation
  changes, persistence, runtime activation, concrete content, live provider
  behavior, external validation/projection behavior, and broad readiness
  claims.
- planned tests cover frontend API-client behavior, component success/failure
  states, dashboard integration, browser E2E smoke, existing E2E compatibility,
  build, focused backend API compatibility, and scope guard.

## Out-of-Scope Follow-ups

- `0.6.8`: evidence and compatibility audit.
- `0.6.9`: release-candidate bundle.
- `0.6.10`: final closeout.
