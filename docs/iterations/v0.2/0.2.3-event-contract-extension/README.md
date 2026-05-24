# 0.2.3 Event Contract Extension

Status: ready for review

Type: code

## Goal

Define the reviewed documentation gate for an additive Event Contract
extension. This package prepares a minimal event-local structured reference
layer without changing current Event construction, payload semantics, API
responses, event log storage, runtime behavior, or frontend behavior.

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
- [ ] Contract reviewed
- [ ] Technical design reviewed
- [ ] Test plan reviewed
- [ ] Documentation gate approved
- [ ] Implementation complete
- [ ] Tests/evidence complete
- [ ] Review complete

## Implementation Boundary

Implementation must not start until this documentation gate is reviewed and
approved. When approved, the implementation stage is limited to:

- `backend/app/schemas/event.py`
- `backend/app/tests/test_event_schema_compat.py`
- this package's `review.md` and `review.zh.md` during closeout

No event log storage, runtime engine, module, API route, frontend,
`backend/worldengine/`, WorldCell runtime connection, reference resolution,
referential integrity, WorldSpec loader, village runtime, agent memory,
pseudo-self, or 0.2.4 work is included in this package.
