# Technical Design

## Current State

0.1.7 completed the prerequisites for this package:

- stable selectors exist for WorldPanel, MemoryPanel, and timeline detail
  surfaces.
- `tools/testing/agent_smoke_evidence.py` can generate deterministic
  `api-summary.json` from real backend state.
- `make validate-agent-smoke-result` supports:
  - `dashboard-basic-runtime`
  - `dashboard-params-flow`
  - `dashboard-invalid-param`
- `dashboard-params-flow` and `dashboard-invalid-param` are
  validator-supported with no live run recorded.

Current Playwright E2E coverage already implements:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`

`dashboard-archive-summary` exists as a scenario contract only. Backend archive
summary behavior exists, and `MemoryPanel.vue` exposes selectors for the latest
summary, but `frontend/e2e/dashboard.spec.ts` does not yet assert that flow.

## Contract Alignment and Invariants

The implementation must preserve these invariants:

- Live Agent smoke evidence is raw evidence, not Codex narration.
- Agent operation logs contain UI and CLI operations only.
- Helper API reads are checker artifact generation, not direct Agent
  operations.
- `api-summary.json` is generated or verified by project tooling.
- Playwright E2E PASS comes from Playwright assertions.
- Playwright API reads are allowed only inside the test script as assertion
  evidence.
- Low archive intervals are scoped to the Playwright backend web server only.
- No backend runtime or API contract changes are allowed.

## Proposed Implementation

### 0.1.8-A: Live `dashboard-params-flow` Agent Smoke

Prepare `test-results/agent-smoke/latest/` as the reviewed live evidence
directory.

Use the 0.1.7 helper around the UI flow:

```bash
tools/testing/agent_smoke_evidence.py baseline \
  --base-url http://127.0.0.1:8000 \
  --out test-results/agent-smoke/latest/api-baseline.json

tools/testing/agent_smoke_evidence.py collect \
  --scenario dashboard-params-flow \
  --base-url http://127.0.0.1:8000 \
  --baseline test-results/agent-smoke/latest/api-baseline.json \
  --out test-results/agent-smoke/latest/api-summary.json
```

Between those commands, Codex operates the dashboard UI to:

1. open the dashboard.
2. set `counter.increment` to numeric value `2`.
3. apply the params patch.
4. step runtime once.
5. capture screenshot evidence.

The operation log must include the scenario-relevant UI targets enforced by
the validator. The result directory must include the required artifacts and
then pass:

```bash
make validate-agent-smoke-result RESULT_DIR=test-results/agent-smoke/latest
```

### 0.1.8-B: `dashboard-archive-summary` E2E

Modify the Playwright backend web-server environment so only E2E backend
startup uses:

```text
WORLD_SUMMARY_INTERVAL_TICKS=2
WORLD_SNAPSHOT_INTERVAL_TICKS=2
```

The intended implementation is in `frontend/playwright.config.ts`, scoped to
the backend web server entry. It must not set global runtime defaults or modify
backend code.

Add a Playwright test in `frontend/e2e/dashboard.spec.ts` that:

1. opens the dashboard.
2. verifies the MemoryPanel starts in empty or non-summary state as
   appropriate for the fresh test server.
3. steps runtime enough times to cross the low summary interval.
4. polls `/world/summaries?limit=1&order=desc` inside the Playwright test.
5. asserts the latest summary has a valid tick range, total events, and
   `tick.advanced` type count.
6. asserts `memory-summary-text` and `memory-summary-stats` show the summary in
   the dashboard.

The test should reuse existing E2E helper patterns in `dashboard.spec.ts` for
API envelope parsing and UI stepping.

## Affected Surfaces

Affected by 0.1.8-A:

- `test-results/agent-smoke/latest/`
- Agent smoke docs and test maps after validation succeeds.
- this package `review.md`.

Affected by 0.1.8-B:

- `frontend/playwright.config.ts`
- `frontend/e2e/dashboard.spec.ts`
- E2E scenario docs and test maps after E2E passes.
- this package `review.md`.

Not affected:

- backend runtime implementation.
- backend API route implementation.
- Agent smoke validator implementation.
- Agent smoke fixtures, unless review evidence requires only docs status
  updates.
- `backend/worldengine/`.

## Data Model / Schema Changes

No runtime, API, or result schema changes are planned.

The live `dashboard-params-flow` `api-summary.json` must conform to the 0.1.7
validator expectations:

- `scenario`: `dashboard-params-flow`
- `health_status`: `ok`
- `param_path`: `counter.increment`
- `expected_value`: `2`
- `observed_value`: `2`
- `before_tick` and `after_tick` prove one runtime step after baseline.
- `counter_event_increment`: `2`

## Runtime / Service Design

No service changes are allowed.

For E2E, the backend process started by Playwright receives lower archive
interval env vars. The service behavior remains the existing archive behavior;
only test startup timing changes.

## Compatibility

Existing users, dev servers, API clients, and runtime defaults continue to use
the existing archive intervals unless they explicitly set env vars.

Existing E2E tests continue to pass under the Playwright environment. If the
lower archive interval affects event timing, the implementation must adjust
assertions without changing runtime semantics.

## Risks

- Codex may accidentally handwrite `api-summary.json`.
  Mitigation: require helper baseline/collect commands and validate the final
  run directory.
- Live smoke may drift into API curl smoke.
  Mitigation: allow API evidence only through the helper artifact and keep
  Agent operation logs UI/CLI-only.
- The archive E2E may become flaky if it relies only on UI timing.
  Mitigation: poll deterministic API state inside Playwright and assert UI
  rendering after summary creation.
- Low interval env vars may leak into normal runtime.
  Mitigation: scope them to the Playwright backend web-server config and
  record the diff in review.
- 0.1.8 may become too broad.
  Mitigation: run only `dashboard-params-flow` live smoke first, then
  implement only `dashboard-archive-summary` E2E.
