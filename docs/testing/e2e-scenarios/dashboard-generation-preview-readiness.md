# E2E Scenario: dashboard-generation-preview-readiness

Status: implemented

## Purpose

Verify the dashboard GenerationPanel path for a generic world preview and the
runtime-readiness check that follows a valid preview. This scenario is v0.7
compatibility coverage for the v0.6 generation surface; it does not judge
subjective world quality and does not use an external validation world.

## Coverage

Implemented in `frontend/e2e/dashboard-generation.spec.ts`.

The scenario covers:

- a valid generic template preview submitted through the dashboard.
- visible validation status for the preview result.
- visible generated `generation-...` id.
- visible source kind `template`.
- visible preview summary containing public count metadata.
- runtime-readiness status displayed only after a valid preview.
- an invalid duplicate-cell preview submitted through the dashboard.
- visible diagnostic code `duplicate_cell_id`.
- no visible readiness status for the invalid preview.

## Preconditions

- Backend and frontend can start through the Playwright web server config.
- Dashboard is reachable at the configured E2E app URL.
- GenerationPanel selectors are stable:
  - `generation-panel`
  - `generation-request-id-input`
  - `generation-root-id-input`
  - `generation-root-label-input`
  - `generation-child-id-input`
  - `generation-child-label-input`
  - `generation-seed-input`
  - `generation-preview-submit`
  - `generation-validation-status`
  - `generation-id`
  - `generation-source-kind`
  - `generation-summary`
  - `generation-readiness-status`
  - `generation-diagnostics`
- Test data uses generic ids and labels only, such as `e2e-root`,
  `e2e-child`, `E2E Root`, and `E2E Child`.

## Valid Preview Steps

1. Open the dashboard.
2. Verify GenerationPanel is visible.
3. Fill request id `e2e-generation-preview`.
4. Fill root id `e2e-root` and root label `E2E Root`.
5. Fill child id `e2e-child` and child label `E2E Child`.
6. Fill seed `e2e-seed`.
7. Click `generation-preview-submit`.
8. Wait for validation, generation metadata, summary, and readiness UI.

## Valid Preview Assertions

- `generation-validation-status` is `passed`.
- `generation-id` contains `generation-`.
- `generation-source-kind` is `template`.
- `generation-summary` contains `total_cell_count`.
- `generation-readiness-status` is `passed`.

## Invalid Diagnostics Steps

1. Open the dashboard.
2. Verify GenerationPanel is visible.
3. Fill request id `e2e-generation-diagnostics`.
4. Fill root id `duplicate-cell`.
5. Fill child id `duplicate-cell`.
6. Fill generic labels for both cells.
7. Click `generation-preview-submit`.
8. Wait for validation diagnostics.

## Invalid Diagnostics Assertions

- `generation-validation-status` is `failed`.
- `generation-source-kind` is `template`.
- `generation-diagnostics` contains `duplicate_cell_id`.
- `generation-readiness-status` is not visible.

## API Evidence Boundary

The implemented Playwright spec currently asserts dashboard UI produced by
GenerationPanel after it calls the public generation APIs. It does not yet make
separate Playwright `request` assertions against
`/world/generation/preview` or `/world/generation/runtime-readiness`.

Public API metadata and redaction boundaries are covered by backend API tests,
including:

- `backend/app/tests/test_generation_preview_api.py`
- `backend/app/tests/test_generation_regeneration_api.py`
- `backend/app/tests/test_plan_import_boundary.py`

If a future package wants E2E-level API response assertions for this scenario,
it should add request-level checks to `frontend/e2e/dashboard-generation.spec.ts`
or a sibling spec and keep this scenario contract updated.

## Failure-Path Assertions

- Invalid duplicate cell ids must not show readiness as passed.
- Diagnostics must be visible and must include the public diagnostic code.
- Output must stay generic and must not expose external validation world
  content, private provider details, private fixture paths, hidden reset hooks,
  or oracle/transcript content.

## Artifact Expectations

PASS comes only from Playwright assertion exit status:

```bash
cd frontend && pnpm exec playwright test e2e/dashboard-generation.spec.ts
```

For full E2E validation runs, artifacts should be retained under:

- `test-results/e2e/html-report/index.html`
- `test-results/e2e/artifacts/`
- failure screenshots and traces when Playwright retains them.

## Non-Goals

- This scenario does not prove subjective generation quality.
- This scenario does not prove external validation suite PASS.
- This scenario does not prove projection application readiness.
- This scenario does not replace backend schema/import/generation unit tests.
