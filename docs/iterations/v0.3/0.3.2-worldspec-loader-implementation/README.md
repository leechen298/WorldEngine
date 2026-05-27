# 0.3.2 WorldSpec Loader Implementation

Status: ready for review

Type: mixed or code

## Goal

Implement the minimal generic `WorldSpec` loader from the reviewed
`0.3.1-worldspec-loader-contract` without connecting loaded data to runtime.

## Scope

This package may add a small loader module and focused backend tests that
prove generic `WorldSpec` input can be parsed, validated, and rejected with
structured errors.

This package must not connect the loader to `RuntimeEngine`, API routes,
persistence, events, archive snapshots, params, frontend behavior, external
fixture repositories, or concrete validation worlds.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

Chinese mirrors are included for the full package.

## Deliverables

Implementation stage:

- `backend/app/core/worldspec_loader.py`
- `backend/app/tests/test_worldspec_loader.py`
- documentation review evidence in this package.

Documentation stage:

- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.md`
- matching `*.zh.md` mirrors.

## Status Checklist

- [x] Docs drafted
- [ ] Contract reviewed
- [ ] Technical design reviewed
- [ ] Test plan reviewed
- [ ] Implementation complete
- [x] Documentation evidence complete
- [ ] Review complete

## Handoff

After documentation review approval, this package may be marked ready for
implementation. Implementation must use `worldengine-iteration-dev`, follow
this package, and update `review.md` with current-session implementation and
test evidence.
