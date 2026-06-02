# Intent

## Problem

v0.7 has added public contracts, report schemas, manifest validation, and
projection read-model checker surfaces. Before the evidence/audit packages can
prepare release-candidate review, the campaign needs one current-session
evidence matrix that proves the existing checker surfaces pass and clearly
classifies surfaces that were not run.

## Desired Outcome

Create a narrow, evidence-only checkpoint for v0.7 that records:

- which existing checker/test/JSON/scope commands passed.
- which runtime/API/frontend/E2E/Agent/autonomous/external/projection/product
  checks were skipped or out of scope.
- which compatibility claims are supported by current-session evidence.
- which claims remain unavailable for later packages.

## Non-Goals

- Do not repair implementation code.
- Do not add new checker logic.
- Do not run external validation suites.
- Do not build or validate a projection application.
- Do not claim runtime/API/frontend/product/generation readiness from checker
  tests.

## Handoff

`0.7.6-v0.7-evidence-and-compatibility-audit` receives the completed evidence
matrix and any unresolved findings.
