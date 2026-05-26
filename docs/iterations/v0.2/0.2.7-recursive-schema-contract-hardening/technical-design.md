# Technical Design

## Current State

`backend/app/schemas/entity.py` defines EntityRef as a Pydantic model with
non-empty `id`, non-empty `kind`, optional `label`, and default empty
metadata.

`backend/app/schemas/world_cell.py` defines WorldCell as a recursive Pydantic
model with non-empty `id`, optional `label`, literal `kind = "world"`,
default empty `entity_refs`, default empty `child_cells`, and default empty
metadata. It defines WorldSpec with literal `schema_version = "0.2"`,
non-empty `id`, optional `label`, required `root`, and default empty metadata.

`backend/app/tests/test_world_cell_schema.py` already covers imports,
defaults, nested child cells, entity references, required root WorldCell,
empty-id rejection, non-world kind rejection, unsupported schema version
rejection, invalid child/entity input rejection, model_dump serialization, and
model_validate reconstruction.

`backend/app/tests/test_worldspec_schema_smoke.py` already covers a
domain-neutral in-memory schema smoke payload, recursive children, EntityRef
integration, WorldSpec validation, and round trips.

## Contract Alignment and Invariants

- Keep EntityRef generic. `kind` identifies a reference category but does not
  bind to runtime registries or resolver behavior in this package.
- Keep WorldCell recursive at the schema layer only.
- Keep WorldSpec as a validated specification object, not a runtime loader
  input path.
- Keep examples domain-neutral.
- Preserve current valid payload compatibility.
- Preserve runtime, API, frontend, fixture, migration, and legacy directory
  behavior.

## Proposed Implementation

After documentation review approval, implement the smallest scoped hardening
pass:

1. Add `docs/contracts/entity-ref-contract.md` describing EntityRef fields,
   accepted generic semantics, metadata boundary, compatibility guarantees,
   validation behavior, and non-goals.
2. Add `docs/contracts/worldcell-contract.md` describing recursive WorldCell
   structure, child cell semantics, entity reference semantics, metadata
   boundary, and non-runtime status.
3. Add `docs/contracts/worldspec-contract.md` describing WorldSpec versioning,
   root semantics, serialization expectations, compatibility behavior, and
   v0.3 handoff boundary.
4. Compare existing schema tests against the accepted coverage list in
   `test-plan.md`.
5. Add only missing domain-neutral tests. Prefer extending existing schema test
   files instead of adding new test files unless a separate file improves
   clarity.
6. Update `review.md` and `review.zh.md` with actual changed files, commands,
   results, compatibility review, scope review, and unresolved findings.

## Affected Surfaces

Documentation:

- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`
- `docs/iterations/v0.2/0.2.7-recursive-schema-contract-hardening/**`

Possible tests:

- `backend/app/tests/test_world_cell_schema.py`
- `backend/app/tests/test_worldspec_schema_smoke.py`

Possible schemas, only if additive clarification is required:

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`

## Data Model / Schema Changes

No schema change is required by default. The expected implementation is
contract documentation plus any missing generic tests.

If implementation finds a real schema ambiguity, allowed schema changes are
limited to additive validation clarifications approved by `contract.md`.
Breaking changes require returning to documentation review.

## Runtime / Service Design

None. This package must not add a loader, resolver, runtime bridge, service
flow, background task, persistence behavior, API route, or frontend behavior.

## Compatibility

Existing v0.1 runtime behavior, event behavior, API response shapes, frontend
behavior, and legacy `backend/worldengine/` behavior remain unchanged.

Existing valid EntityRef, WorldCell, and WorldSpec payloads covered by current
tests must continue to validate. Existing invalid payloads covered by current
tests must continue to fail validation.

## Assumptions

- Pydantic remains the schema validation layer for this package.
- Contract docs can clarify semantics without requiring schema code changes.
- The current generic tests are a baseline and may be reused as evidence where
  they already cover acceptance criteria.

## Risks

- Risk: tests duplicate existing coverage instead of hardening meaningful
  gaps. Mitigation: implementation must first map current tests to acceptance
  criteria and add only missing tests.
- Risk: contract docs accidentally imply runtime loader behavior. Mitigation:
  each contract doc must include explicit non-runtime boundaries.
- Risk: generic examples drift into external validation world details.
  Mitigation: use neutral identifiers and run a concrete demo anchor sweep on
  touched docs and tests.
- Risk: additive schema clarification could affect existing payloads.
  Mitigation: run focused schema tests and `make check-backend`, then record
  compatibility evidence.
