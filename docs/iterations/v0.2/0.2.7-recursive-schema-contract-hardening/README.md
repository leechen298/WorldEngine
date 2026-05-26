# 0.2.7 Recursive Schema Contract Hardening

Status: review complete

Type: mixed

## Goal

Prepare a reviewed implementation contract for hardening the generic
EntityRef, WorldCell, and WorldSpec schema contracts and schema tests without
connecting WorldSpec to runtime loading.

## Scope

This package may add generic schema contract documentation and update
domain-neutral schema tests after documentation review passes. It must keep the
engine core generic, preserve v0.1 runtime behavior, and avoid loader,
runtime-bridge, generation, projection, frontend, fixture, migration, or
external-repository work.

The current documentation-stage pass creates the package documents only.
Implementation starts only after the package documents are reviewed and
approved.

## Documents

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Planned Deliverables After Review

- `docs/contracts/entity-ref-contract.md`
- `docs/contracts/worldcell-contract.md`
- `docs/contracts/worldspec-contract.md`
- focused updates to generic schema tests if the approved contract requires
  more coverage.
- implementation evidence in this package's `review.md`.

## Assumptions

- The current recursive schema source of truth is
  `backend/app/schemas/entity.py` and `backend/app/schemas/world_cell.py`.
- The current generic schema coverage starts in
  `backend/app/tests/test_world_cell_schema.py` and
  `backend/app/tests/test_worldspec_schema_smoke.py`.
- Pydantic model behavior remains the validation mechanism for this package.

## Open Risks

- Existing tests already cover some recursive and round-trip behavior, so
  implementation must avoid duplicative low-value tests.
- Contract docs may reveal ambiguity in `EntityRef.kind` semantics; resolving
  that ambiguity must remain additive and domain-neutral.
- If implementation finds schema behavior must change in a non-additive way,
  the package must return to documentation review before code changes continue.
