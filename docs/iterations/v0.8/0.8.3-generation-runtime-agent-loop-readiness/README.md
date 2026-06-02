# 0.8.3 Generation Runtime Agent Loop Readiness

Status: review complete
Type: mixed/code candidate
implementation_authorized: yes
evidence_execution_authorized: yes

## Purpose

This package prepares the minimum generic core loop that v0.8 needs before a
future external validation function can judge WorldEngine from public engine
surfaces:

```text
candidate WorldSpec
  -> runtime context readiness
  -> isolated runtime step evidence
  -> default Agent loop perception/action evidence
```

The package is not an external validator and does not implement a product
application. Documentation/contract review and implementation review are
complete for the generic, read-only, isolated core-readiness probe described
below.

## Current State

Current implementation already has:

- generation preview and regeneration APIs under `/world/generation`.
- runtime-readiness checks that validate a candidate `WorldSpec` and derive a
  bounded runtime context summary.
- process-local `RuntimeEngine` that can carry inert runtime context.
- `AgentLoopService` with bounded perception, default deterministic `noop`, and
  reviewed `params.patch` action boundary.
- bounded memory context in perception, but no public memory API.

The missing v0.8 slice is a single generic evidence path that proves a
candidate `WorldSpec` can be inspected, used as an inert runtime context,
advanced in an isolated runtime, and observed by a default Agent loop without
mutating app runtime state or exposing private detail.

## Allowed Implementation After Review

If this package review records `implementation_authorized: yes`, implementation
may add:

- additive schemas in `backend/app/schemas/world_generation.py`.
- generic helper logic in `backend/app/core/world_generation.py`.
- one read-only API route under `backend/app/api/routes/world_generation.py`.
- focused backend/API tests under `backend/app/tests/`.

The intended route is a core-side readiness probe, for example
`POST /world/generation/core-readiness`, returning bounded preview,
runtime-readiness, isolated runtime-step, and default Agent-loop probe
evidence.

## Forbidden Scope

- No frontend changes.
- No external validator, external app, product UI, app routing, packaging, or
  deployment.
- No concrete validation world, seed data, character, location, resource, story
  rule, UI selector, private transcript, private repo path, oracle detail,
  provider trace, prompt, secret, or external event payload.
- No durable persistence, migration, live provider behavior, public memory API,
  reset API, or write API.
- No new runtime feature under `backend/worldengine/`.
- No generated-world active runtime execution in the app's live runtime state.
- No claim of external validation PASS, product readiness, generation quality,
  Agent smoke PASS, autonomous PASS, or v0.8 final readiness.

## Handoff

This package hands bounded core readiness evidence to
`0.8.4-external-validation-handoff-contract`. It does not claim external
validation PASS, product readiness, generation quality, Agent smoke PASS,
autonomous PASS, frontend/E2E PASS, or final v0.8 readiness.
