# 0.2.2 Recursive World Contract

Status: review complete

Type: code

## Goal

Define the reviewed implementation contract for the first recursive world
schema package. This package prepares EntityRef, WorldCell, and minimal
WorldSpec schemas without changing runtime behavior.

## Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

Chinese mirror documents are included as `.zh.md` files and must remain
synchronized with the English package documents.

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Implementation Boundary

Implementation must not start until this documentation gate is reviewed and
approved. When approved, the implementation stage is limited to:

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/tests/test_world_cell_schema.py`

No runtime, API route, frontend, fixture, loader, generator, or legacy backend
changes are included in this package.
