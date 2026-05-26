# 0.2.8 Event Reference Contract Hardening

Status: ready for review

Type: mixed

## Goal

Prepare a reviewed implementation contract for hardening `EventRef` and
optional `Event.refs` as additive event reference structures while preserving
existing event compatibility.

## Scope

This package may add EventRef contract documentation and update focused,
domain-neutral event schema compatibility tests after documentation review
passes. It must keep refs event-schema-local and must not implement a
referential integrity resolver, causality engine, runtime bridge, memory link,
projection behavior, frontend behavior, fixture data, migration, or external
repository.

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
- [ ] Contract reviewed
- [ ] Technical design reviewed
- [ ] Test plan reviewed
- [ ] Documentation gate approved
- [ ] Implementation complete
- [x] Documentation-stage evidence complete
- [ ] Review complete

## Planned Deliverables After Review

- `docs/contracts/event-ref-contract.md`
- focused updates to `backend/app/tests/test_event_schema_compat.py` if the
  approved acceptance requirements are not already covered.
- implementation evidence in this package's `review.md`.

## Assumptions

- The current event schema source of truth is
  `backend/app/schemas/event.py`.
- The current focused compatibility coverage starts in
  `backend/app/tests/test_event_schema_compat.py`.
- `Event.refs` remains a list with default `[]` and remains optional for
  existing event dictionaries.
- `EventRef.kind` and `EventRef.role` are generic strings in v0.2, not
  enumerated runtime semantics.

## Open Risks

- The current tests already cover many compatibility cases, so
  implementation must avoid duplicative low-value tests.
- Contract wording could accidentally imply resolver, causality, memory, or
  projection behavior. The implementation contract must keep those as
  explicit non-goals.
- If implementation discovers a non-additive schema behavior change is needed,
  the package must return to documentation review before code changes
  continue.
