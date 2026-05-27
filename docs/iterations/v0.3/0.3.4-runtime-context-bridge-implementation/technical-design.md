# Technical Design

## Current State

`backend/app/core/worldspec_loader.py` exposes `LoadedWorldSpec` and
`load_worldspec()`. `docs/contracts/runtime-context-bridge-contract.md`
defines accepted bridge input, context shape, error categories, and
compatibility requirements.

`RuntimeEngine` is still the v0.1 in-memory runtime scaffold. It owns
`RuntimeState`, advances tick and `world_time_seconds`, emits `tick.advanced`,
runs the default module tree when supplied, calls archive callbacks, and
returns copied runtime state.

## Contract Alignment and Invariants

Implementation must preserve these invariants:

- only successful loader output or a reviewed equivalent may enter the bridge.
- derived context is bounded and does not expose raw `WorldSpec` payloads.
- context is optional and inert.
- `WorldCell` remains schema structure, not `WorldModule`.
- existing runtime, API, event, params, archive, frontend-facing, fixture,
  migration, and legacy behavior are compatibility surfaces.
- examples and tests use domain-neutral identifiers only.

## Proposed Implementation

Add `backend/app/core/runtime_context.py` with small structured types and a
pure derivation function. The exact names may follow local Python style, but
the module should expose:

- `RuntimeContext`.
- `RuntimeContextSummary`.
- `RuntimeContextBridgeError`.
- a result wrapper or clear success/error return.
- a single obvious derivation function, such as `build_runtime_context()`.

The derivation function should:

1. receive one candidate input.
2. confirm it is a successful `LoadedWorldSpec` or reviewed equivalent.
3. read only validated identity, schema version, root cell identity/type, and
   neutral loader source metadata.
4. return either `RuntimeContext` or structured bridge errors.
5. perform no runtime side effects.

If `RuntimeEngine` stores context, use an additive optional constructor
argument with a default of `None`. Existing constructor call sites and
`RuntimeEngine.from_env()` must not need changes unless they only pass
through the optional value without changing defaults. Any context accessor
must be read-only and must not alter `get_state()` or `step()` response
semantics unless review explicitly approves an additive diagnostic helper.

## Affected Surfaces

Implementation surfaces:

- `backend/app/core/runtime_context.py`
- `backend/app/core/runtime_engine.py`, only for optional inert storage if
  required.
- `backend/app/tests/test_runtime_context_bridge.py`

Read-only compatibility surfaces:

- `backend/app/core/worldspec_loader.py`
- `backend/app/core/event_bus.py`
- `backend/app/world/modules/*`
- runtime, event API, params, archive, schema, frontend-facing, and legacy
  tests needed for compatibility evidence.

Documentation surfaces:

- `docs/iterations/v0.3/0.3.4-runtime-context-bridge-implementation/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

## Data Model / Schema Changes

No schema changes are allowed. `RuntimeContext`, `RuntimeContextSummary`, and
`RuntimeContextBridgeError` are internal bridge boundary structures, not
persisted schemas and not API response models.

The allowed runtime context fields are:

- `worldspec_id`
- `schema_version`
- `root_cell_id`
- `root_cell_type`
- `source_type`
- `source_label`
- `metadata`

Metadata must stay domain-neutral and bounded. If the implementation cannot
prove metadata neutrality, omit metadata for this package.

## Error Model

Bridge errors must use stable codes:

- `unsupported_input`
- `invalid_loaded_worldspec`
- `context_derivation_error`

Errors should include a concise message, optional path, and neutral source
metadata when available. Bridge errors must not reinterpret schema validation
errors that belong to the loader.

## Runtime / Service Design

The bridge is a pure local boundary. It must not:

- start or mutate runtime services.
- emit events.
- apply params.
- create archive snapshots.
- write persistence records.
- call API route handlers.
- import frontend or legacy runtime modules.

If runtime storage is added, `step()` must continue to increment tick and
world time exactly as before, emit the same event shapes under the same
conditions, and call existing callbacks with the same arguments.

## Compatibility

Implementation must provide current-session evidence for:

- default `RuntimeEngine` construction.
- `RuntimeEngine.from_env()`.
- `RuntimeEngine.step()` state advancement.
- event API compatibility for `/world/events` and `/world/event-steps`.
- runtime API compatibility for `/runtime/state` and `/runtime/step`.
- params and params apply behavior.
- archive snapshot and summary behavior.
- optional `Event.refs` compatibility.
- frontend-facing response shapes.
- legacy `backend/worldengine/` boundary.

## Risks

- Runtime context storage could accidentally become serialized public state.
- A convenience summary could be mistaken for product UI or projection API.
- Tests could prove the pure bridge but miss default runtime constructor
  compatibility.
- Metadata could become application-specific unless kept out or tightly
  bounded.
