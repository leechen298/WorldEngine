# Contract

## Public Semantics

This package defines current-code test scenario contracts for v0.1. It may
change testing documentation and iteration indexes only.

Scenario documents must distinguish implemented, executable, blocked, pending,
and contract-only states so a future agent cannot treat a documented scenario
as runnable evidence unless a deterministic checker or Playwright assertion
exists.

## Allowed Changes

- Add `docs/testing/e2e-scenarios/` scenario documentation.
- Add or update Agent smoke scenario documentation under
  `docs/testing/agent-smoke/scenarios/`.
- Add Codex/test-runner autonomous test protocol, scorecard, and scenario
  documentation under `docs/testing/agent-autonomous/`.
- Add `docs/testing/test-implementation-prerequisites.md`.
- Update English and Chinese high-level testing and v0.1 iteration indexes.
- Add this 0.1.6 iteration package.

## Forbidden Changes

- Do not modify backend code.
- Do not modify frontend code.
- Do not modify Playwright E2E implementation.
- Do not modify Agent smoke validator behavior.
- Do not modify fixtures.
- Do not modify runtime behavior.
- Do not add API curl smoke.
- Do not run live Agent smoke.
- Do not run Codex autonomous tests.
- Do not report new tests as passed.
- Do not treat Agent smoke as full Agent autonomous testing.
- Do not modify `backend/worldengine/`.

## Status Rules

E2E scenario documents may use these statuses:

- `implemented`
- `scenario-contract-only / blocked-by-selector`
- `scenario-contract-only / partially-blocked-by-selector`
- `scenario-contract-only / blocked-by-selector-and-test-env`

Agent smoke scenario documents may use these statuses:

- `executable`
- `defined-not-executable-until-validator-supports-scenario`
- `contract-only`

Codex/test-runner autonomous scenario documents must use:

- `contract-only-do-not-execute`

## Verdict Rules

- E2E PASS comes from Playwright assertion.
- Agent smoke PASS comes from
  `make validate-agent-smoke-result RESULT_DIR=<run-dir>`.
- Agent smoke `verdict_source` must be `deterministic_checker`.
- Codex/test-runner autonomous PASS cannot be claimed until a scorecard checker
  exists and returns PASS.
- Codex natural language observation is never a final PASS source.

## Agent Operation Rules

Agent smoke and Codex/test-runner autonomous operation logs may record UI and
CLI operations only. Direct API calls must not be recorded as Agent operations.

API evidence may appear in `api-summary.json` or future checker artifacts only
as deterministic checker evidence.

## Compatibility

This package is documentation-only. Existing runtime, API, schema, dashboard,
E2E, validator, fixture, and skill behavior must remain unchanged.

## Chinese Mirrors

High-level Chinese mirrors must stay aligned for this package:

- `docs/testing/README.zh.md`
- `docs/testing/v0.1-test-map.zh.md`
- `docs/iterations/v0.1/README.zh.md`
- `docs/iterations/v0.1/v0.1-plan.zh.md`
