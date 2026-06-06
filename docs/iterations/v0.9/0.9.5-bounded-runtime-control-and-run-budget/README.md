# 0.9.5 Bounded Runtime Control And Run Budget

Chinese mirror: `README.zh.md`.

Status: implementation complete / focused verification passed
Type: mixed implementation package

## Goal

Add bounded runtime control for current in-memory WorldEngine execution so a
caller can run a finite number of ticks or a finite world-time duration, pause,
resume, and receive a public run summary with explicit guard limits.

## Scope

This package may extend the active backend runtime path under `backend/app/`
with:

- bounded run request and response schemas.
- deterministic in-memory runtime helper behavior.
- API endpoints for bounded run, pause, and resume.
- maximum tick and world-time duration guards.
- public provider-call and cost guard counters that remain zero because this
  package does not authorize provider calls.
- focused backend and API tests.

It must preserve the existing `/runtime/step` behavior and must not introduce
durable scheduling, background workers, deployment infrastructure, frontend UI,
checker execution, external validation, or Validation Client changes.

## Deliverables

- Public runtime-control schemas.
- Bounded run helper in the active runtime code path.
- Runtime API surface for bounded run, pause, and resume.
- Public run summary evidence.
- Focused tests for tick limits, duration limits, pause/resume, max guards,
  provider/cost counters, and compatibility with single-step runtime behavior.

## Current Authorization

Documentation/contract review passed. Implementation is authorized only for the
scoped active-backend in-memory runtime-control work recorded in this package.

Provider live calls, generated-result creation, checker execution, external
validation, Validation Client changes, durable scheduling, and frontend UI work
remain unauthorized.

## Final Assessment State

Implementation complete for the scoped active-backend in-memory
runtime-control work. Focused, related runtime, and backend regression
verification passed. Read-only implementation re-review reported no unresolved
P1/P2/P3 findings.

Provider live calls, generated-result creation, checker execution, external
validation, Validation Client changes, durable scheduling, frontend UI,
event legality, Agent continuity, and `backend/worldengine/` changes remain
unauthorized and unclaimed.
