# 0.3.1 WorldSpec Loader Contract

Status: review complete

Type: documentation-only

## Goal

Define the WorldSpec loader contract before implementing loader code.

## Scope

This package adds the documentation contract for how generic `WorldSpec` input
may be accepted, parsed, validated, returned, or rejected by a future loader.

This package does not implement the loader, connect anything to runtime,
change schemas, add API routes, create fixtures, or touch frontend behavior.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

`technical-design.md` and `test-plan.md` are included because this
documentation-only package prepares a later code package.

## Deliverables

- `docs/contracts/worldspec-loader-contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/intent.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/technical-design.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/test-plan.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/plan.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/review.md`

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [ ] Implementation complete
- [x] Documentation evidence complete
- [x] Review complete

## Handoff

After review approval, `0.3.2-worldspec-loader-implementation` may implement
the minimal loader from the reviewed contract. This package must not be marked
ready for implementation; implementation readiness belongs to the next code or
mixed package after documentation review passes.
