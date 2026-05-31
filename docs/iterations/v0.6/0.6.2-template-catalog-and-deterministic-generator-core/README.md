# 0.6.2 Template Catalog And Deterministic Generator Core

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define and, after review authorization, implement only the generic template
catalog and deterministic template-to-`WorldSpec` generator core for v0.6.

The implementation phase may start only after this package's contract,
technical design, test plan, and execution plan pass documentation/contract
review and `review.md` records `implementation_authorized: yes`.

## Scope

Documentation stage:

- create this package and Chinese mirrors.
- define exact backend schema/service/test files that the implementation phase
  may touch.
- define deterministic generation semantics and diagnostics.
- define verification commands and compatibility gates.

Implementation stage, only after authorization:

- create `backend/app/schemas/world_generation.py`.
- create `backend/app/core/world_generation.py`.
- create focused backend tests under `backend/app/tests/`:
  - `test_world_generation_schema.py`
  - `test_template_catalog.py`
  - `test_deterministic_world_generation.py`

Forbidden:

- do not add public API routes, API envelope changes, frontend code,
  persistence, migrations, archive/params changes, Agent loop or memory
  changes, runtime tick/event behavior changes, live AI-provider behavior,
  external validation readiness, projection readiness, generated seed files, or
  `backend/worldengine/` runtime features.
- do not add concrete demo-world names, maps, characters, locations,
  resources, story rules, private validation oracle details, or
  application-specific backend behavior.

## Deliverables

- complete package docs and Chinese mirrors.
- reviewed implementation authorization criteria.
- generic generation schema and deterministic generator core after
  authorization.
- focused tests and adjacent schema/loader/runtime-context compatibility
  evidence after implementation.

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

Documentation/contract review, implementation, code review, and validation
evidence are complete with evaluator PASS and no P1/P2/P3. This package hands
off the reviewed deterministic template generator core to
`0.6.3-structured-generation-plan-compiler`.
