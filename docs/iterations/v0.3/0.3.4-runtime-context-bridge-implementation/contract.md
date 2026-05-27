# Contract

## Public Concepts

- `RuntimeContextBridge`: implementation boundary that derives context from a
  successful loader result.
- `RuntimeContextInput`: accepted input, limited to successful
  `LoadedWorldSpec` or a reviewed equivalent.
- `RuntimeContext`: optional inert context derived from generic
  `WorldSpec` data.
- `RuntimeContextSummary`: deterministic diagnostic view for tests and review
  evidence, not product UI.
- `RuntimeContextBridgeError`: structured bridge error for unsupported input,
  incomplete loader output, or derivation failures.

The normative public contract remains
`docs/contracts/runtime-context-bridge-contract.md`.

## Compatibility Constraints

- Existing `RuntimeEngine` construction without context must remain
  compatible.
- Existing tick, `world_time_seconds`, `step_seconds`, and `updated_at`
  behavior must remain compatible.
- Existing API envelopes and response shapes for runtime and world event
  endpoints must remain compatible.
- Existing event payloads, params behavior, archive behavior,
  frontend-facing shapes, fixtures, migrations, tests, and legacy
  `backend/worldengine/` behavior must remain compatible.
- Existing `WorldSpec`, `WorldCell`, loader, and event schemas must not
  change.
- Runtime context must remain optional and inert.

## Allowed Changes

- Add `backend/app/core/runtime_context.py`.
- Add focused bridge tests in `backend/app/tests/test_runtime_context_bridge.py`.
- Add an optional `runtime_context` constructor argument or equivalent
  read-only holder to `RuntimeEngine` only if default behavior remains
  unchanged.
- Add a read-only summary helper for tests and review evidence.
- Add narrow imports needed by the bridge and focused tests.
- Update this package `review.md` and `review.zh.md` with implementation
  evidence after implementation.

## Forbidden Changes

- Do not change default runtime scaffold behavior.
- Do not change `/runtime/state`, `/runtime/step`, `/world/events`,
  `/world/event-steps`, or legacy `/world/step` response shapes.
- Do not emit new bridge events or place raw `WorldSpec` data in event
  payloads.
- Do not make runtime context drive tick advancement, module execution,
  params reads or writes, archive snapshots, or API responses.
- Do not modify schemas, migrations, fixtures, frontend code, persistence
  models, or legacy `backend/worldengine/` code.
- Do not convert `WorldCell` into `WorldModule` semantics.
- Do not implement generation, Agent-in-World loop, memory, self-continuity,
  projection, story generation, NPC chat, external repositories, or concrete
  demo-world behavior.

## Acceptance Requirements

- Bridge derives `RuntimeContext` from a successful `LoadedWorldSpec`.
- Derived context includes only `worldspec_id`, `schema_version`,
  `root_cell_id`, `root_cell_type`, `source_type`, optional `source_label`,
  and reviewed neutral metadata.
- Bridge rejects unsupported input with `unsupported_input`.
- Bridge rejects incomplete or internally inconsistent loaded output with
  `invalid_loaded_worldspec`.
- Bridge reports `context_derivation_error` for derivation failures not
  covered by loader schema validation.
- `RuntimeEngine()` and `RuntimeEngine.from_env()` work unchanged when no
  context is supplied.
- Supplying context, if supported by `RuntimeEngine`, does not change
  `step()` state advancement or event output.
- Focused tests prove no raw `WorldSpec` event payloads are emitted.
- Compatibility tests prove runtime, event API, params, archive, and
  frontend-facing response shapes remain compatible for touched surfaces.
- English and Chinese package and milestone mirrors keep 0.3.4 status
  synchronized as `ready for review` / `待评审`.

## North Star Check

This package keeps WorldEngine generic. It implements only a bounded bridge
from validated world specification data to optional runtime context and
explicitly forbids concrete world behavior, external validation internals,
Agent behavior, memory, generation, and projection.

## Out-of-Scope Follow-ups

- `0.3.5` may define external fixture runner contract readiness.
- `0.3.6` may audit loader and bridge compatibility evidence.
- Later milestones may define runtime module mapping, Agent loops, memory,
  self-continuity, generation, projection, and external product validation.
