# 0.6.7 Dashboard Generation Preview And E2E Smoke

Status: review complete
Type: mixed
implementation_authorized: yes

## Goal

Define and, only after review authorization, implement a dashboard-facing
generation preview workflow backed by the existing v0.6 generation API. The
workflow should let an operator submit a generic template preview request,
inspect validation metadata, view bounded runtime-readiness output, and verify
the flow through focused frontend and browser E2E smoke tests.

## Scope

Documentation stage:

- create this package and Chinese mirrors.
- define dashboard generation preview UI, API-client, and E2E-smoke
  boundaries.
- update parent v0.6 status surfaces for the active child state.

Implementation stage, only after authorization:

- add frontend API client types and functions for existing generation preview,
  regeneration, and runtime-readiness routes.
- add a focused dashboard generation preview component and mount it in the
  existing dashboard page.
- add focused component/API-client tests and a browser E2E smoke for the
  dashboard generation flow.
- update this package review evidence and parent status surfaces.

Forbidden:

- no backend schema/API/runtime implementation changes unless documentation
  review is reopened.
- no runtime tick/time/event semantic changes.
- no automatic mutation, activation, persistence, migration, or repository
  storage of generated specs.
- no concrete demo-world, story, private validation oracle, external
  validation runner, projection app, live provider/network/prompt execution,
  credential, or `backend/worldengine/**` work.
- no claim that dashboard preview, E2E smoke, generation quality, product
  readiness, projection readiness, external validation readiness, autonomous
  validation, release readiness, or full runtime migration is complete.

## Deliverables

- complete package docs and Chinese mirrors.
- reviewed dashboard generation preview contract.
- after authorization, frontend API-client/component tests, browser E2E smoke,
  focused backend generation API compatibility evidence, build evidence, static
  checks, scope checks, and evaluator checkpoints.
- review evidence that distinguishes dashboard preview smoke from product,
  generation-quality, external validation, projection, autonomous, and release
  readiness.

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

This package is review complete. Documentation/contract, implementation-scope,
code-review, validation, E2E, build, backend compatibility, browser smoke, and
scope checks passed after the readiness-diagnostics P2 was fixed. It hands
dashboard preview and E2E smoke evidence to
`0.6.8-v0.6-evidence-and-compatibility-audit`.
