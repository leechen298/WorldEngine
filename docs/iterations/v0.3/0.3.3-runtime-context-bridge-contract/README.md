# 0.3.3 Runtime Context Bridge Contract

Status: ready for review

Type: documentation-only

## Goal

Define how validated `WorldSpec`-derived data may become optional runtime
context without implementing the bridge or changing runtime behavior.

## Scope

This package adds the documentation contract for the runtime context bridge.
It defines accepted bridge input, derived context shape, compatibility rules,
forbidden behavior, and required implementation evidence for `0.3.4`.

This package does not implement the bridge, change `RuntimeEngine`, modify
schemas, add API routes, emit events, alter archive or params behavior, create
fixtures, or touch frontend behavior.

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

- `docs/contracts/runtime-context-bridge-contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.md`
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

After documentation review approval, `0.3.4-runtime-context-bridge-implementation`
may implement the minimal optional bridge. This package must not be marked
ready for implementation; implementation readiness belongs to the next code or
mixed package after review passes.
