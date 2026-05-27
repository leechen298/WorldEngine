# Technical Design

## Current State

`WorldSpec` is defined in `backend/app/schemas/world_cell.py` and is already
covered by schema smoke tests. `0.3.1` added the loader contract in
`docs/contracts/worldspec-loader-contract.md` but did not implement loader
code. No runtime bridge exists yet.

## Contract Alignment and Invariants

Implementation must preserve these invariants:

- use the existing `WorldSpec` schema, or a reviewed wrapper around it, for
  validation.
- normalize input dispatch, parsing, and validation failures into stable loader
  result objects.
- keep loaded data as specification data only.
- avoid imports from `RuntimeEngine`, API route modules, persistence, archive,
  params, event writers, frontend, fixtures, and legacy runtime code.
- keep test data domain-neutral.

## Proposed Implementation

Add `backend/app/core/worldspec_loader.py` with a small, synchronous API. The
exact names may follow local Python style, but the module should expose a
single obvious load function and structured result types matching the reviewed
contract.

Suggested shape:

- immutable or plain structured result objects for success and errors.
- input dispatch for mapping, JSON text, JSON bytes, and optional JSON file
  path.
- JSON parsing through the standard library.
- schema validation through `WorldSpec`.
- error normalization that maps exceptions to `unsupported_input`,
  `parse_error`, `schema_validation_error`, or `io_error`.

The loader should not perform deep semantic checks beyond existing schema
validation. It should not resolve references or derive runtime context.

## Affected Surfaces

Implementation surfaces:

- `backend/app/core/worldspec_loader.py`
- `backend/app/tests/test_worldspec_loader.py`

Documentation surfaces:

- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`

Read-only compatibility surfaces:

- `backend/app/schemas/world_cell.py`
- existing schema smoke tests.
- runtime, API, event, archive, params, frontend-facing, fixture, migration,
  and legacy-path tests.

## Data Model / Schema Changes

No schema changes are allowed. `LoadedWorldSpec`, `WorldSpecLoaderError`, and
`WorldSpecLoaderResult` are loader boundary structures, not persisted schema
objects and not API response models in this package.

## Runtime / Service Design

The loader is a pure data-boundary utility:

1. receive one input value.
2. classify the input source.
3. parse JSON only when needed.
4. validate the resulting mapping with `WorldSpec`.
5. return a success or failure result.

It must not start, mutate, wrap, or configure runtime services.

## Compatibility

Existing runtime ticks, `world_time_seconds`, API envelopes, `/runtime/step`,
`/world/events`, `/world/event-steps`, params behavior, archive behavior,
optional `Event.refs`, frontend-facing shapes, and legacy
`backend/worldengine/` behavior must remain unchanged.

The implementation should prove this mainly by scope, import, and focused
regression checks because the loader is not wired into those surfaces.

## Risks

- Error normalization could hide too much validation detail. Focused tests must
  assert stable codes and enough path/detail to locate invalid fields.
- File input could imply fixture policy. If implemented, tests must use a
  temporary single JSON document with neutral content.
- A convenience API could drift into runtime bridge behavior. Import checks and
  forbidden-change review must catch runtime/API/event/persistence coupling.
- Validation may change existing schema expectations if code modifies
  `world_cell.py`; this package forbids that and requires existing schema
  smoke tests to keep passing.
