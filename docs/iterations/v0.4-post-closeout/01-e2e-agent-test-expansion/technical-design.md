# Technical Design

## Current State

Browser E2E currently lives in `frontend/e2e/dashboard.spec.ts` and covers the
dashboard runtime, params, invalid params, old params-agent Auto-Tune, timeline
navigation, and archive summary flows. Playwright starts backend and frontend
web servers through `frontend/playwright.config.ts`.

v0.4 adds backend/API behavior for:

- `PerceptionFrame`
- `ActionIntent`
- `ActionResult`
- `AgentLoopService`
- `POST /world/agent/loop/step`

Agent smoke currently has:

- scenario docs under `docs/testing/agent-smoke/scenarios/`
- evidence helper `tools/testing/agent_smoke_evidence.py`
- checker `tools/testing/validate_agent_smoke_result.py`
- checker tests in `tools/testing/test_validate_agent_smoke_result.py`
- fixture coverage for basic runtime, params flow, and invalid param.

## Proposed Implementation

### E2E Expansion

Create `frontend/e2e/agent-loop.spec.ts` for v0.4 Agent Loop API scenarios.
Use Playwright `request` so the tests run under the existing E2E harness while
avoiding a non-existent UI dependency.

The spec should cover:

- default empty-body loop step returns deterministic `noop` and no mutation.
- valid `params.patch` updates `/world/params` and emits `params.applied` with
  `source="agent.loop"`.
- reserved-path `params.patch` returns HTTP 200 rejected result, does not
  mutate params, and emits no `params.applied`.
- unsupported action returns HTTP 200 rejected result with
  `unsupported_action`.
- schema errors such as `event_limit=0` or unknown fields return the existing
  HTTP 422 envelope with `code=30` and no mutation.
- existing `/world/agent/params/propose-and-apply` remains compatible.

Update `frontend/e2e/dashboard.spec.ts` to strengthen
`dashboard-agent-autotune` as the compatibility path for the existing
dashboard params-agent UI. The test should verify that the resulting
`params.applied` event has `source="agent.params"` and should not expect
`source="agent.loop"`.

### Agent Smoke Expansion

Add `dashboard-agent-autotune` as an executable Agent smoke scenario.

The Agent operation path is UI/CLI only:

- UI opens dashboard.
- UI sets `counter.increment` to `2`.
- CLI records baseline helper command after the baseline value is visible.
- UI enters an Auto-Tune goal.
- UI clicks the Auto-Tune button.
- UI records success and patch evidence.
- CLI records collect helper command.
- CLI records validator command.

The checker evidence in `api-summary.json` should prove:

- `health_status == "ok"`
- scenario is `dashboard-agent-autotune`
- baseline counter increment was `2`
- observed counter increment changed from `2`
- patch count is at least one
- patch paths include `counter.increment`
- at least one `params.applied` event exists after the baseline
- Auto-Tune UI success target was observed
- Auto-Tune UI patches target was observed

The checker must require the stable UI targets:

- `dashboard`
- `world-params-path-input`
- `world-params-type-select`
- `world-params-value-input`
- `world-params-apply-button`
- `world-agent-goal-input`
- `world-agent-autotune-button`
- `world-agent-success`
- `world-agent-patches`
- `world-params-json`

## Affected Surfaces

- E2E tests and scenario docs.
- Agent smoke scenario docs, helper, checker, tests, and fixture.
- Optional raw latest Agent smoke evidence if a live run is mirrored.
- Durable result summaries.

## Data Model / Schema Changes

No product schema changes are allowed.

Agent smoke checker support extends `api-summary.json` for
`dashboard-agent-autotune` with scenario-specific fields:

- `baseline_counter_increment`
- `observed_counter_increment`
- `counter_changed`
- `patches_count`
- `patch_paths`
- `params_applied_event_seen`
- `ui_success_seen`
- `ui_patches_seen`

## Compatibility

Existing Agent smoke result shape remains valid. Existing supported scenarios
must still validate without changes to their artifacts.

## Risks

- E2E API tests can share backend process state with existing dashboard specs.
  Mitigation: assertions compare before/after state and do not require a fresh
  empty backend.
- Agent smoke live evidence can be invalid if operation logs record API calls
  directly. Mitigation: keep API evidence in helper outputs and record helper
  invocations as CLI operations.
- Auto-Tune deterministic provider may set the same value as baseline if the
  baseline is not controlled. Mitigation: the scenario sets
  `counter.increment` to `2` before Auto-Tune; current mock provider applies
  `1`.
