# 0.6.6 Regeneration And Runtime Readiness Integration

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define and, only after review authorization, implement bounded regeneration
support and runtime-readiness checks for generated `WorldSpec` data. This
package must prove generated specs can pass the existing loader and
runtime-context bridge without changing runtime tick/time behavior, mutating
the live runtime by default, adding persistence, or claiming product/runtime
readiness beyond the checked boundary.

## Scope

Documentation stage:

- create this package and Chinese mirrors.
- define regeneration, lineage, and runtime-readiness public concepts.
- define exact backend files that may be touched after authorization.
- update parent v0.6 status surfaces for the active child state.

Implementation stage, only after authorization:

- extend `backend/app/schemas/world_generation.py` with additive regeneration,
  lineage, and runtime-readiness schemas.
- extend `backend/app/core/world_generation.py` with deterministic
  regeneration and runtime-readiness helpers that reuse the existing preview,
  loader, and runtime-context bridge.
- extend `backend/app/api/routes/world_generation.py` with approved
  generation routes, without changing existing route envelopes.
- add focused backend tests for regeneration, lineage, runtime-readiness
  success/failure, request validation, and runtime event non-leakage.
- update this package review evidence and parent status surfaces.

Forbidden:

- no runtime tick/time/event semantic changes.
- no automatic mutation of the live runtime from generated specs.
- no persistence, repositories, migrations, fixtures, generated output files,
  external repositories, or `backend/worldengine/**`.
- no frontend UI, dashboard workflow, E2E, external validation runner, or
  projection app behavior.
- no live AI calls, provider SDKs, network calls, credentials, prompt
  execution, raw prompts, provider traces, private validation oracle details,
  secrets, external application data, or concrete world/story content.

## Deliverables

- complete package docs and Chinese mirrors.
- reviewed regeneration and runtime-readiness contract.
- after authorization, focused backend API/service tests plus adjacent loader,
  runtime-context, runtime-step, and full backend regression evidence.
- review evidence that distinguishes loader/context readiness from runtime
  mutation, regeneration quality, external validation readiness, projection
  readiness, product readiness, and release readiness.

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

Implementation and validation are complete for the approved 0.6.6 backend
schema/core/existing-route/test scope. Focused and full backend regression
evidence passed, and evaluator checkpoints report no P1/P2/P3 findings.
