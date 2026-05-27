# Technical Design

## Current State

`RuntimeEngine` is a v0.1 in-memory runtime scaffold. It owns tick state,
advances `world_time_seconds`, emits `tick.advanced`, runs the default module
tree, and calls archive callbacks.

`WorldSpec` and the 0.3.2 loader remain data boundaries. Loaded data is not
runtime context yet. No runtime bridge exists.

## Contract Alignment and Invariants

The bridge contract must preserve these invariants:

- only successful loader output may enter the bridge.
- runtime context is derived and bounded, not raw `WorldSpec`.
- context storage, if later implemented, is optional and inert by default.
- `WorldCell` is schema/world structure, not a `WorldModule`.
- tick, event, params, archive, API, frontend, and legacy behavior remain
  read-only compatibility surfaces for this package.
- examples and diagnostics remain domain-neutral.

## Proposed Future Implementation Shape

The later implementation package should add a small bridge module, most likely
under `backend/app/core/`, that:

1. receives one successful loader result.
2. checks that the loader result is complete enough for bridge derivation.
3. derives a narrow `RuntimeContext`.
4. returns success or structured bridge errors.
5. performs no runtime side effects.

If `RuntimeEngine` later stores context, the constructor change must be
additive and default to no context. Existing calls without context must behave
exactly as they do now.

This package does not create that module.

## Affected Surfaces

Documentation surfaces affected by this package:

- `docs/contracts/runtime-context-bridge-contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

Implementation surfaces intentionally unaffected:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- tests, fixtures, migrations, API routes, schemas, runtime services, archive,
  params, event, or persistence code.

## Data Model / Schema Changes

No schema changes are made. `RuntimeContext`, `RuntimeContextSummary`, and
`RuntimeContextBridgeError` are conceptual bridge boundary structures until
`0.3.4` implements them.

The proposed context shape is intentionally small:

- validated WorldSpec identity.
- validated schema version.
- validated root cell identity and type.
- neutral source metadata.
- optional reviewed metadata.

It is not a persisted schema and not an API response model in this package.

## Runtime / Service Design

No runtime or service behavior changes in this package. The future bridge is a
pure derivation boundary until a reviewed implementation adds optional storage
or access paths.

Runtime context must not drive:

- tick advancement.
- event emission.
- module execution.
- params validation or application.
- archive snapshot or summary creation.
- API response shape.
- frontend behavior.

## Compatibility

Existing runtime ticks, `world_time_seconds`, API envelopes, `/runtime/state`,
`/runtime/step`, `/world/events`, `/world/event-steps`, params behavior,
archive behavior, optional `Event.refs`, frontend-facing shapes, and legacy
`backend/worldengine/` behavior must remain unchanged.

The later implementation must prove old behavior with focused tests and scope
checks before claiming compatibility.

## Verification Design

Documentation verification should prove:

- required package files exist in English and Chinese.
- the bridge contract contains required concepts, context fields, error
  categories, compatibility surfaces, and forbidden inferences.
- 0.3.3 status is synchronized in English and Chinese milestone docs.
- touched docs do not introduce concrete demo-world anchors.
- no implementation files were modified.
- `git diff --check` passes.

## Risks

- Context shape could be too broad and become an API or event payload by
  accident. The contract mitigates this by defining a small derived shape and
  forbidding raw `WorldSpec` payload exposure.
- RuntimeEngine constructor changes in 0.3.4 could affect existing tests. The
  test plan requires compatibility evidence for existing default behavior.
- `WorldCell` could be mistaken for `WorldModule`. The contract explicitly
  forbids direct equivalence.
- Metadata may become domain-specific. The bridge limits metadata to neutral
  diagnostics unless reviewed.
