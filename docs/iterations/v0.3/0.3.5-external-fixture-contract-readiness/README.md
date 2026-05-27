# 0.3.5 External Fixture Contract Readiness

Status: review complete

Type: documentation-only

## Goal

Define how external fixture runners may consume WorldEngine through public
contracts without creating external repositories, concrete fixture content, or
private validation internals inside the core repository.

## Scope

This package adds the public external fixture runner contract and the
documentation package that explains how external runners may call WorldEngine
and return redacted evidence.

This package does not implement code, create fixtures, add test inputs, add
external repositories, define reset APIs, expose UI selectors, modify schemas,
change runtime behavior, add API routes, or implement a product validation
app.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

`technical-design.md` and `test-plan.md` are included because this
documentation-only package prepares a later external consumer contract and
evidence workflow.

## Deliverables

- `docs/contracts/external-fixture-runner-contract.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/README.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/intent.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/contract.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/technical-design.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/test-plan.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/plan.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.md`
- matching `*.zh.md` mirrors for the package docs.

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [ ] Implementation complete
- [x] Documentation evidence complete
- [x] Review complete

## Handoff

After documentation review approval, future external fixture runners may use
the contract as a public consumption boundary. This package must not be marked
`ready for implementation`; code or mixed implementation requires a later
reviewed package.
