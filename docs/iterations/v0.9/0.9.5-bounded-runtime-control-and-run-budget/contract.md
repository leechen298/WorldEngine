# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

`RuntimeRunRequest`

- Public request for bounded runtime advancement.
- Supports one of:
  - `ticks`: run a finite number of ticks.
  - `duration_seconds`: run until at least that much world time is advanced.
- Includes `max_ticks`, `max_duration_seconds`, `max_provider_calls`, and
  `max_estimated_cost_units` guards.

`RuntimeControlState`

- Public runtime-control state with `status` values `running`, `paused`, and
  `idle`.
- Does not create durable scheduling.

`RuntimeRunSummary`

- Public summary of a bounded run.
- Includes start/end tick, start/end world time, ticks requested, ticks
  executed, stop reason, guard summary, provider/cost counters, and redaction
  status.

## Allowed Changes

- Additive runtime-control schemas in active backend schema files.
- RuntimeEngine methods or adjacent active-backend helper code for bounded
  run, pause, resume, and control state.
- Runtime API endpoints in `backend/app/api/routes/runtime.py`.
- Manifest/OpenAPI exposure only if needed by existing app route registration.
- Focused backend/API tests.
- Package-local review documentation and parent v0.9 status updates after
  closeout.

## Forbidden Changes

- No live provider calls.
- No generated-result creation.
- No checker execution or checker fixture changes.
- No external validation or autonomous validation.
- No frontend UI or Validation Client changes.
- No durable scheduler, background worker, queue, deployment infrastructure, or
  cron-like behavior.
- No event legality implementation or rule-linked parameter evolution.
- No Agent continuity, memory consolidation, narrative projection, or
  diagnostic dialogue behavior.
- No concrete demo-world fixtures or application-specific logic.
- No `backend/worldengine/` changes.

## Compatibility Requirements

- Existing `/runtime/step` must continue to advance exactly one tick.
- Existing `/runtime/state` response fields must remain compatible.
- Existing event, snapshot, archive, world params, Agent loop, and world
  generation tests must continue to pass.
- New request schemas must reject unbounded requests and extra fields.
- Pause must block multi-tick bounded runs but must not make existing
  `/runtime/step` incompatible unless the implementation contract explicitly
  records that behavior and tests it.
- Provider-call and cost counters must remain zero in this package.

## Out-of-scope Follow-ups

- `0.9.6`: natural-language world direction boundary.
- `0.9.7`: rule-linked evolution and event legality.
- `0.9.8`: brain-inspired Agent continuity and consolidation evidence.
- `0.9.10`: checker fixtures and scorecard support.
- `0.9.12`: live or blocked full lifecycle validation execution.

## Exit Criteria

This package may close only when:

- required package docs and mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- implementation authorization is recorded before code changes.
- focused tests prove bounded tick runs, bounded duration runs, pause/resume,
  max guard rejection, zero provider/cost counters, public run summary, and
  single-step compatibility.
- relevant backend regressions pass in the current session.
- `review.md` records exact commands, changed files, subagent findings,
  compatibility review, scope review, unresolved findings, and final route.

