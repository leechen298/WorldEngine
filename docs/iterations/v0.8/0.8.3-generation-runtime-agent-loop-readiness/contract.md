# Contract

## Public Contract

This package may introduce one generic core-readiness probe after review. The
probe must be additive and must not replace existing preview, regeneration,
runtime-readiness, runtime-step, or Agent-loop APIs.

The probe contract is:

- input: one candidate `WorldSpec` or a reviewed generation preview request.
- process: validate/preview, derive runtime context, run one isolated runtime
  step, and run one default Agent loop `noop`.
- output: bounded generation, runtime-readiness, isolated runtime-step, and
  Agent-loop evidence.
- side effects: none on app runtime, app event log, world params, memory store,
  archive store, external repositories, or provider systems.

## Allowed Code Paths After Review

Implementation may touch only:

- `backend/app/schemas/world_generation.py`
- `backend/app/core/world_generation.py`
- `backend/app/api/routes/world_generation.py`
- focused tests under `backend/app/tests/`

If implementation needs any other file, stop and update this contract before
continuing.

## Required Semantics

- The probe must be read-only relative to the application runtime.
- Runtime execution must be isolated and process-local.
- The isolated runtime may emit bounded events into an isolated in-memory event
  log only.
- The Agent loop action must default to `noop`; `params.patch` is out of scope
  for the probe.
- Returned evidence must be redacted and must not include raw `WorldSpec`
  internals beyond the existing public preview payload.
- Any memory context must remain absent or bounded read-only; no memory read or
  write API may be added.
- Failure paths must return diagnostics without accepted runtime/Agent success
  claims.

## Forbidden Changes

- Do not modify frontend, migrations, fixtures, external repos, product app
  code, or `backend/worldengine/`.
- Do not add write/reset APIs, persistence, live provider behavior, external
  validation execution, product workflow, or generated-world active runtime.
- Do not expose prompt/provider traces, secrets, private transcripts, private
  app data, UI selectors, oracle internals, raw memory, or external event
  payloads.
- Do not claim external validation PASS, product readiness, generation-quality
  PASS, Agent smoke PASS, autonomous PASS, or v0.8 final readiness.

## Evidence Requirements

Implementation evidence must include:

- focused schema/core tests for successful and failed probe paths.
- focused API tests for the read-only route and 422 envelope on forbidden
  fields.
- tests proving app runtime state, app event log, params, and memory store are
  not mutated by the probe.
- tests proving returned evidence excludes raw private payloads.
- adjacent generation runtime-readiness and Agent-loop tests if affected.
- `git diff --check` and changed-file scope guard.

## Authorization

Implementation is not authorized until:

1. this full package document set is reviewed.
2. a documentation/contract evaluator reports no P0/P1 and no blocking P2.
3. `review.md` records `implementation_authorized: yes`.
