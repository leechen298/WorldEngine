# 0.6.4 AI-Assisted Generation Boundary And Plan Import

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define and, only after review authorization, implement the provider-independent
AI-assisted plan import boundary. This package imports structured plans that
may have been produced by an AI system, records redacted provenance, validates
the imported plan through the `0.6.3` compiler contract, and never calls live
providers.

## Scope

Documentation stage:

- create this package and Chinese mirrors.
- define import envelope, provenance, diagnostics, tests, and forbidden
  provider behavior.
- define exact backend files that may be touched after authorization.

Implementation stage, only after authorization:

- extend `backend/app/schemas/world_generation.py` with additive import and
  provenance schemas.
- extend `backend/app/core/world_generation.py` with import validation and
  conversion helpers.
- add focused backend tests for plan import schema and boundary behavior.
- update existing generation-plan tests only where needed for compatibility.

Forbidden:

- no live provider credentials, network calls, model orchestration, background
  jobs, hidden retry loops, prompt libraries, or prompt execution.
- no public API routes, frontend, persistence, migrations, fixtures, external
  repositories, `backend/worldengine/`, runtime tick/event, Agent/memory, or
  projection/external-validation readiness.
- no concrete world/story/application content, private validation oracle
  details, secrets, prompts, or external application data.

## Deliverables

- complete package docs and Chinese mirrors.
- provider-independent import/provenance contract.
- focused import tests and structured compiler compatibility evidence after
  authorization.
- review evidence that distinguishes import of structured plans from live AI
  generation.

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

Review complete. Implementation and validation evidence are recorded in
`review.md`, and the package hands import/provenance semantics to `0.6.5`.
