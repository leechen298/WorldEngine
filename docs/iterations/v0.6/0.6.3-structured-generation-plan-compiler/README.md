# 0.6.3 Structured Generation Plan Compiler

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define and, only after review authorization, implement the structured
generation plan compiler that turns validated plan data into valid
`WorldSpec` output through the generic generation semantics reviewed in
`0.6.1` and the deterministic generator evidence from `0.6.2`.

This package must keep plan compilation provider-independent. A structured
plan may later be produced by an AI system, but this package treats every plan
as untrusted data and does not execute free-form prompt text or call external
providers.

## Scope

Documentation stage:

- create this package and Chinese mirrors.
- define plan schema, compiler semantics, deterministic diagnostics, and
  metadata requirements.
- define exact backend files that may be touched after authorization.
- define verification commands and compatibility gates.

Implementation stage, only after authorization:

- extend `backend/app/schemas/world_generation.py` with additive structured
  plan schema and metadata fields.
- extend `backend/app/core/world_generation.py` with plan validation and
  compiler functions.
- add focused backend tests for structured plan schema and compiler behavior.
- update existing generation tests only where needed to protect compatibility.

Forbidden:

- do not add public API routes, frontend, persistence, migrations, fixtures,
  generated seed files, external validation readiness, projection readiness,
  Agent/memory changes, runtime tick/event changes, or `backend/worldengine/`
  runtime features.
- do not accept free-form prompt text as executable generation behavior.
- do not call external AI providers or read credentials/secrets.
- do not add concrete world names, maps, characters, locations, resources,
  story rules, private validation oracle details, or application-specific
  backend behavior.

## Deliverables

- complete package docs and Chinese mirrors.
- reviewed implementation authorization criteria.
- structured plan schema and deterministic compiler after authorization.
- focused tests and adjacent template-generator / loader / runtime-context
  compatibility evidence after implementation.

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
off reviewed structured plan compiler evidence to
`0.6.4-ai-assisted-generation-boundary-and-plan-import`.
