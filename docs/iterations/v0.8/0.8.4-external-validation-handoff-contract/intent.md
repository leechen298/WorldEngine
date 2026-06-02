# Intent

## Problem

v0.8 needs to prepare WorldEngine for external validation without absorbing the
external validator. After `0.8.3`, the core has a bounded readiness probe, but
later packages still need a clear vocabulary for what may be handed off to an
external validator as public evidence.

Without this package, later smoke/evidence work could accidentally mix:

- core-side evidence and external validation PASS.
- public evidence references and private validator artifacts.
- blocked/skipped/out-of-scope classifications and PASS.
- v0.7 checker/docs clean-pass evidence and v0.8 readiness.

## Objective

Create a reviewed documentation-only contract that defines the external
validation handoff boundary for v0.8.

The contract must state:

- which public handoff facts WorldEngine may expose or record.
- which status values and evidence classes are allowed.
- how redaction and forbidden-detail confirmation must be represented.
- how unresolved findings, blockers, skipped checks, and out-of-scope surfaces
  must be classified.
- which private external validator details remain forbidden.

## Non-Goals

- Do not implement the external validator.
- Do not implement schema/checker/template files in this package.
- Do not add API, runtime, frontend, backend test, fixture, migration,
  generated artifact, external repository, or `backend/worldengine/` changes.
- Do not run or claim external validation.
- Do not claim product readiness, projection app readiness, frontend/E2E PASS,
  Agent smoke PASS, autonomous PASS, generation quality PASS, or final v0.8
  readiness.

## Handoff Outcome

If this package is reviewed, `0.8.5` may use the contract to decide how to
record core-side smoke evidence and non-claims without needing private
external validation details.
