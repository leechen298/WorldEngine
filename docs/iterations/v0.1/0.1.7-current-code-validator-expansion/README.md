# 0.1.7 Current-Code Validator Expansion

Status: ready for implementation

Type: mixed

## Goal

Make the current-code Agent smoke contracts executable by adding the missing
dashboard selectors, validator support, result-schema support, deterministic
API evidence helper, fixtures, and tests needed for `dashboard-params-flow` and
`dashboard-invalid-param`.

This package prepares execution capability only. It must not run live Agent
smoke and must not implement archive-summary E2E.

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

0.1.7 builds the selector and validator infrastructure for future live Agent
smoke execution. 0.1.8 or later must own live smoke execution evidence and
`dashboard-archive-summary` E2E implementation after its own package documents
are drafted and reviewed.
