# 0.6.5 Generation Validation Metadata And Preview API

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define and, only after review authorization, implement the backend API surface
for generation validation, bounded metadata, and preview. The API must expose
reviewed `0.6.2`, `0.6.3`, and `0.6.4` generation behavior through the
existing `ApiResponse` / `ApiErrorResponse` envelope without changing runtime,
persistence, frontend UI, or live AI-provider behavior.

## Scope

Documentation stage:

- create this package and Chinese mirrors.
- define the preview API contract, metadata boundary, route wiring, tests, and
  forbidden leak surfaces.
- define exact backend files that may be touched after authorization.
- update parent v0.6 status surfaces for the active child state.

Implementation stage, only after authorization:

- extend `backend/app/schemas/world_generation.py` with additive preview API
  request/response schemas.
- extend `backend/app/core/world_generation.py` with a preview helper that
  reuses existing template, plan, and import validation/generation functions.
- add `backend/app/api/routes/world_generation.py`.
- update `backend/app/api/routes/__init__.py` and
  `backend/app/api/app_factory.py` only to export/include the route.
- add focused API tests for successful preview, generation validation failure,
  import validation failure, request-envelope validation, preview payload
  shape, and existing envelope compatibility.
- update this package review evidence and parent status surfaces.

Forbidden:

- no frontend UI or dashboard workflow.
- no persistence, repositories, migrations, fixtures, generated output files,
  or external repositories.
- no live AI calls, provider SDKs, network calls, credentials, prompt
  execution, hidden retries, or background jobs.
- no raw prompts, unredacted provider traces, private validation oracle
  details, secrets, external application data, concrete maps, characters,
  locations, resources, story rules, or seed content.
- no changes to existing route response envelopes, existing error handler
  behavior, runtime tick/event behavior, Agent/memory behavior, loader/runtime
  behavior, or `backend/worldengine/**`.

## Deliverables

- complete package docs and Chinese mirrors.
- reviewed preview API contract and bounded metadata semantics.
- after authorization, focused backend API/service tests plus full backend
  regression evidence.
- review evidence that distinguishes structural preview validity from runtime
  readiness, generation quality, external validation readiness, projection
  readiness, and product readiness.

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

Documentation/contract evaluator review passed with no P1/P2/P3 findings.
Implementation and validation evidence are recorded in `review.md`, and the
package hands preview/API metadata semantics to `0.6.6`.
