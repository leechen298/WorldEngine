# Technical Design

## Current State

0.1.8 leaves these current-code coverage states:

- E2E implemented:
  - `dashboard-basic-runtime`
  - `dashboard-params-flow`
  - `dashboard-invalid-param`
  - `dashboard-archive-summary`
- E2E contract-only:
  - `dashboard-agent-autotune`
  - `dashboard-timeline-navigation`
- Agent smoke live evidence:
  - `dashboard-basic-runtime` has prior live evidence.
  - `dashboard-params-flow` has 0.1.8 live evidence.
  - `dashboard-invalid-param` is validator-supported, with no live run
    recorded.

The current dashboard already exposes required selectors:

- Auto-Tune: `world-agent-goal-input`,
  `world-agent-autotune-button`, `world-agent-success`,
  `world-agent-patches`, `world-agent-error`.
- Timeline: `timeline-page-size`, `timeline-prev-page`,
  `timeline-next-page`, `timeline-row`, `timeline-row-expand`,
  `timeline-event-type`, `timeline-event-payload`,
  `timeline-event-source`.
- Invalid params: `world-params-path-input`,
  `world-params-value-input`, `world-params-apply-button`,
  `world-params-error`.

## Contract Alignment and Invariants

The implementation must preserve these invariants:

- E2E PASS comes from Playwright assertions.
- Live Agent smoke PASS comes from the deterministic validator.
- Agent operation logs contain UI and CLI operations only.
- Helper API reads are checker artifact generation, not direct Agent
  operations.
- `api-summary.json` is helper-generated or helper-verified, not handwritten.
- No backend runtime or API contract changes are allowed.
- No v0.2 schema/spec work is allowed.

## Proposed Implementation

### Auto-Tune E2E

Add `dashboard-agent-autotune` to `frontend/e2e/dashboard.spec.ts`.

The intended test flow:

1. Open the dashboard.
2. Record current world params through Playwright API assertion helper if
   useful.
3. Fill `world-agent-goal-input` with a deterministic goal such as
   `speed up counter`.
4. Click `world-agent-autotune-button`.
5. Assert `world-agent-success` reports applied patches.
6. Assert `world-agent-patches` is visible and includes
   `counter.increment`.
7. Assert `world-params-json` or `/world/params` test-script evidence reflects
   the applied patch.

Current backend startup wires `MockLLMProvider` to return a deterministic
`counter.increment` patch, so this scenario should assert the success path
rather than accepting a generic error as PASS.

### Timeline Navigation E2E

Add `dashboard-timeline-navigation` to `frontend/e2e/dashboard.spec.ts`.

The intended test flow:

1. Open the dashboard.
2. Step runtime enough times through `runtime-step-button` to create more
   event steps than the selected page size.
3. Use `timeline-page-size` to select a deterministic page size.
4. Assert multiple `timeline-row` entries are visible.
5. Assert `timeline-next-page` becomes enabled when enough rows exist.
6. Click `timeline-next-page` and assert the page changes.
7. Click `timeline-prev-page` and assert the page returns.
8. Expand a row through `timeline-row-expand`.
9. Assert `timeline-event-type`, `timeline-event-source`, and
   `timeline-event-payload` are visible and non-empty.

The test should generate its own events and should not depend on prior tests.
If shared serial E2E state already has events, the test may use before/after
counts or deterministic UI state rather than assuming an empty timeline.

### Live Invalid-Param Agent Smoke

Replace `test-results/agent-smoke/latest/` with a reviewed live
`dashboard-invalid-param` run.

The intended helper flow:

```bash
tools/testing/agent_smoke_evidence.py baseline \
  --base-url http://127.0.0.1:8000 \
  --out test-results/agent-smoke/latest/api-baseline.json

tools/testing/agent_smoke_evidence.py collect \
  --scenario dashboard-invalid-param \
  --base-url http://127.0.0.1:8000 \
  --baseline test-results/agent-smoke/latest/api-baseline.json \
  --operation-log test-results/agent-smoke/latest/operation-log.jsonl \
  --out test-results/agent-smoke/latest/api-summary.json

make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
```

Between baseline and collect, Codex operates the dashboard UI to:

1. open the dashboard.
2. set path `system.secret`.
3. set value `blocked`.
4. click Apply.
5. observe `world-params-error`.
6. capture screenshot and transcript evidence.

`result.json.commands` and `operation-log.jsonl` must record helper baseline,
helper collect, and validator commands with `exit_code: 0`.

## Affected Surfaces

Implementation may affect:

- `frontend/e2e/dashboard.spec.ts`
- `test-results/agent-smoke/latest/`
- docs under `docs/testing/`
- this package `review.md`
- v0.1 index and plan docs for status synchronization.

Implementation must not affect:

- `backend/app/`
- `backend/worldengine/`
- Agent smoke validator implementation.
- Agent smoke fixtures.
- autonomous runner or scorecards.

## Data Model / Schema Changes

No runtime, API, or result schema changes are planned.

The live `dashboard-invalid-param` `api-summary.json` must conform to the
existing 0.1.7 validator expectations:

- `scenario`: `dashboard-invalid-param`
- `health_status`: `ok`
- `invalid_path`: `system.secret`
- `params_unchanged`: `true`
- `ui_error_seen`: `true`
- `before_params` and `after_params` are equal objects.

## Runtime / Service Design

No runtime service changes are allowed.

E2E may use existing APIs from inside Playwright tests for deterministic
assertions. Agent smoke may use helper-generated API evidence only as checker
artifact evidence.

## Compatibility

Existing v0.1 tests and docs remain compatible. New E2E scenarios are additive
inside the existing Playwright suite. Replacing `test-results/agent-smoke/latest/`
with invalid-param evidence changes only the latest raw audit directory; the
0.1.8 params-flow live status remains documented.

## Risks

- Auto-Tune E2E may be flaky if it depends on previous params state.
  Mitigation: assert deterministic success patch content and observed params
  after the action, not a hardcoded empty initial state.
- Timeline navigation may be flaky if it depends on prior event count.
  Mitigation: generate enough runtime steps inside the test and use
  before/after or visible UI state assertions.
- Invalid-param live smoke may accidentally become direct API testing.
  Mitigation: keep operation log UI/CLI-only and use API reads only through the
  evidence helper artifact.
- Replacing `latest/` may obscure the 0.1.8 params-flow run.
  Mitigation: record in review that latest now points to invalid-param and
  keep params-flow live status in durable docs.
