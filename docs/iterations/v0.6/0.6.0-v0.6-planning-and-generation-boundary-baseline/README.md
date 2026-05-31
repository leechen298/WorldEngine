# 0.6.0 v0.6 Planning And Generation Boundary Baseline

Status: review complete
Type: documentation-only
implementation_authorized: no

## Goal

Create the v0.6 documentation root, `/goal` campaign controls, version plan,
generation boundary, compatibility baseline, and v0.5 handoff mapping without
changing implementation files.

## Scope

Allowed:

- create parent v0.6 campaign docs under `docs/iterations/v0.6/`.
- create this child package under
  `docs/iterations/v0.6/0.6.0-v0.6-planning-and-generation-boundary-baseline/`.
- define the v0.6 capability split across templates, structured generation
  plans, AI-assisted plan import, validation, metadata, preview, regeneration,
  dashboard preview, audit, release candidate, and final closeout.
- define planned child sequence and review gates.
- record v0.5 final closeout as handoff evidence only.

Forbidden:

- do not modify runtime, schema, API, frontend, backend test, fixture,
  migration, generated result, external repository, or `backend/worldengine/`
  implementation files.
- do not implement generation schemas, services, APIs, UI, persistence,
  regeneration, runtime readiness, or tests.
- do not add concrete world data, application-specific backend logic, private
  validation oracle details, live AI-provider dependencies, external
  validation readiness, or projection app readiness.

## Deliverables

- v0.6 parent campaign docs and Chinese mirrors.
- `0.6.0` child package docs and Chinese mirrors.
- Documentation-stage verification plan and review evidence.
- Explicit handoff to
  `0.6.1-world-generation-contracts-and-template-semantics`.

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

## Current Assessment

This documentation-only package is review complete. It hands off to
`0.6.1-world-generation-contracts-and-template-semantics`, with v0.6
implementation authorization still closed until a later implementation-bearing
child package explicitly records `implementation_authorized: yes`.
