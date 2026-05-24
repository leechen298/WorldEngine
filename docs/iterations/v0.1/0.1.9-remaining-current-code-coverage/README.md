# 0.1.9 Remaining Current-Code Coverage

Status: ready for implementation

Type: mixed

## Goal

Close the remaining v0.1 current-code test coverage gaps before moving to
v0.2: implement the Auto-Tune and timeline-navigation dashboard E2E scenarios,
then record one live Agent smoke run for `dashboard-invalid-param`.

This package is a final v0.1 testing closeout package. It must not add new
runtime capability, start v0.2 work, add API curl smoke, or run full
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
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Plan reviewed
- [ ] Implementation complete
- [ ] Tests/evidence complete
- [ ] Review complete

## Boundary

0.1.9 may only close remaining test coverage for current v0.1 behavior:

1. `dashboard-agent-autotune` E2E.
2. `dashboard-timeline-navigation` E2E.
3. Live `dashboard-invalid-param` Agent smoke evidence.

Implementation may start after this documentation approval gate. Implementation
must still follow `contract.md`, `technical-design.md`, `test-plan.md`, and
`plan.md`.
