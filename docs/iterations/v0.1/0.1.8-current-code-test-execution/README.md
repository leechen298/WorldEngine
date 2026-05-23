# 0.1.8 Current-Code Test Execution

Status: ready for review

Type: mixed

## Goal

Execute the current-code test contracts prepared by 0.1.7 without widening the
runtime scope: first record one live Agent smoke run for
`dashboard-params-flow` using helper-generated API evidence, then implement and
run the `dashboard-archive-summary` Playwright E2E scenario.

This package is an execution package. It must not implement new runtime
features, add API curl smoke, run live `dashboard-invalid-param`, or start
Codex/test-runner autonomous scenarios.

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Status Checklist

- [x] Docs drafted
- [ ] Contract reviewed
- [ ] Technical design reviewed
- [ ] Test plan reviewed
- [ ] Plan reviewed
- [ ] Implementation complete
- [ ] Tests/evidence complete
- [ ] Review complete

## Boundary

0.1.8 has two ordered implementation steps:

1. 0.1.8-A records and validates one live Agent smoke run for
   `dashboard-params-flow` only.
2. 0.1.8-B implements `dashboard-archive-summary` E2E only after 0.1.8-A
   validates successfully.

Implementation must not start until this package is reviewed and approved.
