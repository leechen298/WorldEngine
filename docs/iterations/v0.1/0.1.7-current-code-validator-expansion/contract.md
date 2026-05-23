# Contract

## Public Concepts

### Validator-supported Agent smoke scenario

An Agent smoke scenario is validator-supported when
`make validate-agent-smoke-result RESULT_DIR=<run-dir>` can validate its
required artifacts, operation log, deterministic verdict source, scenario
specific UI targets, and checker artifact evidence.

Validator-supported does not mean a live run has been recorded.

### Deterministic API evidence helper

`tools/testing/agent_smoke_evidence.py` is a project-owned helper that reads
real backend state and writes API checker artifacts for Agent smoke. Live
`api-summary.json` must be generated or verified by project tooling, not
manually authored by Codex.

Helper API reads are checker artifact generation. They are not Agent
operations and must not be recorded as direct API operations in
`operation-log.jsonl`.

## Compatibility Constraints

- Existing runtime behavior must stay compatible.
- Existing API response shapes must stay compatible.
- Existing dashboard user-visible behavior must stay compatible.
- Existing implemented E2E scenarios must keep passing.
- Existing `dashboard-basic-runtime` Agent smoke fixture must keep validating.
- Result-schema changes may only widen supported scenario names from one to
  three.

## Allowed Changes

- Add `data-test` selectors to existing dashboard components:
  - `frontend/src/components/WorldPanel.vue`
  - `frontend/src/components/MemoryPanel.vue`
  - `frontend/src/components/TimelinePanel.vue`
- Update existing frontend unit tests only to verify selector presence or keep
  component behavior stable.
- Add `tools/testing/agent_smoke_evidence.py`.
- Extend `tools/testing/validate_agent_smoke_result.py`.
- Extend `tools/testing/test_validate_agent_smoke_result.py`.
- Add or update Agent smoke fixtures under
  `tools/testing/fixtures/agent-smoke/`.
- Update `docs/testing/agent-smoke/result-schema.json`.
- Update Agent smoke scenario docs and testing indexes to reflect
  validator-supported status after implementation passes.
- Update this 0.1.7 package `review.md` with actual implementation evidence.

## Forbidden Changes

- Do not run live Agent smoke in this package.
- Do not create or replace `test-results/agent-smoke/latest/` evidence.
- Do not implement `dashboard-archive-summary` E2E.
- Do not add API curl smoke.
- Do not record direct API calls as Agent operations.
- Do not allow `verdict_source: agent`.
- Do not change backend runtime behavior.
- Do not change API contracts.
- Do not change dashboard user-visible behavior.
- Do not modify `backend/worldengine/`.
- Do not run Codex/test-runner autonomous scenarios.
- Do not create the 0.1.8 package as part of this implementation.

## Scenario Rules

The Agent smoke validator must support exactly these scenarios in 0.1.7:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`

`result.json.scenario` must match `api-summary.json.scenario`.

`operation-log.jsonl` may contain UI and CLI operations only. The validator
must reject direct API operation records.

## Required UI Targets

| Scenario | Required UI operation targets |
|---|---|
| `dashboard-basic-runtime` | `dashboard`, `runtime-tick-id`, `runtime-step-button` |
| `dashboard-params-flow` | `dashboard`, `world-params-path-input`, `world-params-type-select`, `world-params-value-input`, `world-params-apply-button`, `runtime-step-button` |
| `dashboard-invalid-param` | `dashboard`, `world-params-path-input`, `world-params-value-input`, `world-params-apply-button`, `world-params-error` |

Optional evidence targets such as `world-params-json` and `timeline-panel` may
appear, but validator success must not depend on Codex narration.

## Checker Artifact Rules

For live Agent smoke in 0.1.8 or later, `api-summary.json` must be produced or
verified by a deterministic helper/checker, not manually authored by Codex.

For `dashboard-params-flow`, checker evidence must prove:

- scenario is `dashboard-params-flow`.
- `counter.increment` is the target path.
- expected value is `2`.
- observed value is `2`.
- a runtime step happened after baseline collection.
- a counter event records increment `2`.

For `dashboard-invalid-param`, checker evidence must prove:

- scenario is `dashboard-invalid-param`.
- invalid path is `system.secret`.
- params are unchanged compared with baseline.
- the required UI error target appears in the operation log.

## North Star Check

This package improves evidence integrity for the current dashboard projection.
It does not add village-specific runtime behavior, WorldSpec behavior, world
generation, agent memory, or pseudo-self continuity.

## Out-of-Scope Follow-ups

- 0.1.8 must write its own package before running live `dashboard-params-flow`
  Agent smoke.
- A later package may run live `dashboard-invalid-param` Agent smoke.
- A later package may implement full Codex/test-runner autonomous checker and
  scorecard support.
