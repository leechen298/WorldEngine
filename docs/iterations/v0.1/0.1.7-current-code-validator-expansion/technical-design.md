# Technical Design

## Current State

`frontend/e2e/dashboard.spec.ts` already implements these Playwright
scenarios:

- `dashboard-basic-runtime`
- `dashboard-params-flow`
- `dashboard-invalid-param`

The Agent smoke validator currently accepts only
`dashboard-basic-runtime`. It requires `verdict_source:
deterministic_checker`, validates required artifact paths, rejects direct API
operation records, and checks a basic runtime `api-summary.json`.

The result schema under `docs/testing/agent-smoke/result-schema.json` also
pins `scenario` to `dashboard-basic-runtime`.

0.1.6 recorded selector prerequisites for:

- params-agent Auto-Tune controls and feedback.
- MemoryPanel summary content.
- timeline rows and expanded event details.

## Contract Alignment and Invariants

The implementation must preserve these invariants:

- selectors are non-user-visible test hooks only.
- Agent smoke operation logs remain UI/CLI-only.
- API reads used by the evidence helper are checker artifact generation, not
  Agent operations.
- `api-summary.json` must match the scenario in `result.json`.
- `verdict_source` stays `deterministic_checker`.
- CLI commands and operation-log CLI records must have exit code `0`.
- `dashboard-basic-runtime` fixture compatibility must be preserved.

## Proposed Implementation

### Selector Additions

Add stable `data-test` attributes to existing UI elements:

| Component | Selectors |
|---|---|
| `WorldPanel.vue` | `world-agent-goal-input`, `world-agent-autotune-button`, `world-agent-success`, `world-agent-patches`, `world-agent-error` |
| `MemoryPanel.vue` | `memory-panel`, `memory-summary-text`, `memory-summary-stats`, `memory-summary-empty` |
| `TimelinePanel.vue` | `timeline-row`, `timeline-row-expand`, `timeline-event-type`, `timeline-event-payload`, `timeline-event-source` |

For `TimelinePanel.vue`, use Ant Design Vue table extension points rather than
rewriting the table. The intended shape is:

- `customRow` returns `data-test="timeline-row"` for each row.
- `expandIcon` wraps the existing expand trigger in a button with
  `data-test="timeline-row-expand"`.
- expanded-row render output exposes event type, source, and payload/detail
  text through stable selectors.

### Evidence Helper

Add `tools/testing/agent_smoke_evidence.py` with two commands:

```bash
tools/testing/agent_smoke_evidence.py baseline \
  --base-url http://127.0.0.1:8000 \
  --out <run-dir>/api-baseline.json

tools/testing/agent_smoke_evidence.py collect \
  --scenario <scenario> \
  --base-url http://127.0.0.1:8000 \
  --baseline <run-dir>/api-baseline.json \
  --out <run-dir>/api-summary.json
```

`baseline` records deterministic pre-action backend state:

- health status.
- runtime tick.
- world params.

`collect` reads current backend state and writes scenario-specific
`api-summary.json`:

- `dashboard-basic-runtime`: health status, before tick, after tick.
- `dashboard-params-flow`: target path, expected value, observed value,
  before/after tick, and counter event increment evidence.
- `dashboard-invalid-param`: invalid path, before/after params comparison, and
  unchanged status.

The helper may derive UI-error presence from sibling `operation-log.jsonl` when
available, but the validator must still enforce the required raw UI target
directly.

### Validator Expansion

Extend `validate_agent_smoke_result.py` with:

- `SUPPORTED_SCENARIOS` containing the three supported scenarios.
- a required UI target table keyed by scenario.
- scenario-specific `api-summary.json` validation.
- clearer unsupported-scenario error text listing supported scenarios.

The validator must reject:

- unsupported scenario names.
- `result.json.scenario` / `api-summary.json.scenario` mismatch.
- missing scenario-required UI targets.
- direct API operation log records.
- blank commands, artifacts, assertions, or evidence.
- incorrect or incomplete checker evidence.

### Fixtures and Tests

Add valid fixture directories for:

- `valid-params-flow`
- `valid-invalid-param`

Extend validator tests with negative coverage for:

- missing required UI target.
- scenario mismatch.
- missing checker evidence.
- incorrect params-flow evidence.
- incorrect invalid-param unchanged evidence.

## Affected Surfaces

Affected:

- frontend component selectors.
- frontend unit tests for selector stability.
- Agent smoke validator.
- Agent smoke result schema.
- Agent smoke fixtures.
- Agent smoke scenario docs and high-level test indexes after implementation.
- this iteration package review evidence.

Not affected:

- backend runtime behavior.
- backend API contracts.
- Playwright scenario behavior.
- live Agent smoke result artifacts.
- Codex/test-runner autonomous checker.
- `backend/worldengine/`.

## Data Model / Schema Changes

`docs/testing/agent-smoke/result-schema.json` must widen:

```json
{
  "scenario": {
    "enum": [
      "dashboard-basic-runtime",
      "dashboard-params-flow",
      "dashboard-invalid-param"
    ]
  }
}
```

All other result schema requirements remain compatible:

- `status` is `pass`.
- `verdict_source` is `deterministic_checker`.
- `commands`, `artifacts`, `assertions`, and `failures` remain required.

## Runtime / Service Design

No runtime service changes are allowed.

The evidence helper is a test tool. It performs deterministic backend reads to
generate checker artifacts. It must not mutate runtime state and must not
replace UI operation evidence.

## Compatibility

Existing `dashboard-basic-runtime` Agent smoke fixture and validator behavior
must continue to pass. New support is additive.

Dashboard selectors must not alter visual layout, labels, form behavior, API
calls, or runtime state.

## Risks

- Codex may hand-author `api-summary.json`.
  Mitigation: document and implement the helper as the required artifact source
  for future live smoke, and make validator checks strict enough to catch
  inconsistent evidence.
- UI-only operation logs may pass without relevant flow evidence.
  Mitigation: require scenario-specific UI operation targets.
- Selector changes may accidentally affect rendering.
  Mitigation: run frontend unit tests and E2E regression.
- 0.1.7 may be mistaken for live smoke coverage.
  Mitigation: docs and review state that no live Agent smoke is run or claimed.
