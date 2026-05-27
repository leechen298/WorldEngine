# Contract

## Public Concepts

- `WorldSpecLoader`: implementation component that loads one supported generic
  input source into a validated loader result.
- `WorldSpecInput`: supported domain-neutral input, limited to a parsed mapping,
  JSON string or bytes, and optionally a caller-supplied JSON file path.
- `LoadedWorldSpec`: successful result containing the validated `WorldSpec`,
  `source_type`, optional neutral `source_label`, and `schema_version`.
- `WorldSpecLoaderError`: stable structured error with `code`, `message`,
  optional `path`, `source_type`, and optional `source_label`.
- `WorldSpecLoaderResult`: success or failure wrapper returned by the loader.

The normative public contract remains
`docs/contracts/worldspec-loader-contract.md`.

## Compatibility Constraints

- Existing runtime behavior must stay compatible.
- Existing API response shapes must stay compatible.
- Existing event, archive, params, frontend-facing, and legacy path behavior
  must stay compatible.
- Existing `WorldSpec`, `WorldCell`, and `EntityRef` schema behavior must be
  preserved.
- Schema changes are forbidden in this package.
- Loader implementation must not become runtime context.

## Allowed Changes

- Add `backend/app/core/worldspec_loader.py`.
- Add `backend/app/tests/test_worldspec_loader.py`.
- Add or update imports needed only for the focused loader tests.
- Create this package documentation and Chinese mirrors.
- Update v0.3 milestone index and plan status for 0.3.2 review readiness.
- Update `review.md` and `review.zh.md` with documentation-stage and later
  implementation-stage evidence.

## Forbidden Changes

- Do not modify `RuntimeEngine` or change `RuntimeEngine.step` behavior.
- Do not import `RuntimeEngine` from the loader.
- Do not connect the loader to API routes or response envelopes.
- Do not emit events, create archive snapshots, apply params, write
  persistence records, or mutate runtime state.
- Do not modify schemas, migrations, frontend files, fixtures, or legacy
  `backend/worldengine/` runtime code.
- Do not add concrete demo-world names, maps, characters, locations,
  resources, story rules, external validation-world data, or private oracle
  details.
- Do not implement runtime bridge, world generation, Agent-in-World loop,
  memory, self-continuity, projection, story generation, or NPC chat behavior.

## Acceptance Requirements

- Loader accepts a valid minimal mapping and returns a successful
  `LoadedWorldSpec`.
- Loader accepts valid JSON string or bytes input and returns the same semantic
  result as mapping input.
- If file-backed loading is implemented, loader accepts one JSON document path
  and reports `io_error` for unreadable input.
- Loader returns `unsupported_input` for unsupported input types or source
  forms.
- Loader returns `parse_error` for malformed JSON input.
- Loader returns `schema_validation_error` for invalid `WorldSpec` schema data,
  including unsupported `schema_version` and invalid root cell data.
- Loader error `path` values use the JSON Pointer-style convention defined in
  `technical-design.md`, including `/schema_version` for unsupported schema
  versions when that field is the failing location.
- Successful output includes neutral `source_type`, optional `source_label`,
  and validated `schema_version`.
- Tests prove no runtime, API, event, archive, params, persistence, frontend,
  fixture, migration, or legacy implementation behavior changed.
- English and Chinese package and milestone mirrors keep 0.3.2 status
  synchronized as `ready for review` / `待评审`.

## North Star Check

This package keeps WorldEngine generic. It implements only a reusable
engine-level loader for structured world specifications and explicitly forbids
demo-specific backend behavior, external validation-world internals, and
runtime execution semantics.

## Out-of-Scope Follow-ups

- `0.3.3` may define how validated loaded data may become runtime context.
- `0.3.4` may implement the minimal optional runtime context bridge after its
  contract is reviewed.
- Later milestones may implement Agent loops, memory, self-continuity,
  generation, projection, and external product validation.
