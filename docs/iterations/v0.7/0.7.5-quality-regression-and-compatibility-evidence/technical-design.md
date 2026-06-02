# Technical Design

## Current State

`0.7.2`, `0.7.3`, and `0.7.4` added or reviewed checker surfaces for redacted
reports, readiness manifests, and projection read models. This package does
not add new implementation. It turns those surfaces into a current-session
evidence matrix.

## Evidence Matrix Shape

`evidence-matrix.md` should include:

- command table with exact command, exit status, result, and claim supported.
- coverage table for required classifications.
- skipped/out-of-scope table with reason and residual risk.
- compatibility notes for v0.7 public contract surfaces.
- unresolved findings table.

## Command Groups

Focused checker regression:

- external validation report checker tests.
- readiness manifest checker tests.
- projection read-model checker tests.

Saved-result checker regression:

- Agent smoke saved-result checker tests.
- Agent autonomous saved-result checker tests.

Schema and CLI validation:

- JSON parsing for report schema, readiness manifest schema/json, and
  projection read-model schema.
- CLI validation for readiness manifest and projection read-model contract.

Scope and formatting:

- `git diff --check`.
- changed-file scope guard.

## Classification Rules

- A checker test PASS supports only that checker surface.
- Saved-result checker PASS supports only saved-result schema/checker
  compatibility, not live Agent smoke or autonomous runner PASS.
- JSON parse PASS supports syntax only, not semantic runtime behavior.
- Scope guard PASS supports changed-file boundary only.
- Runtime/API/frontend/E2E/live Agent/full autonomous/external/projection app
  checks are out of scope unless this package is explicitly widened.

## Anti-Drift Rules

- Parent and child route/status surfaces must agree before closeout.
- `evidence matrix complete` is not v0.7 final closeout.
- Do not turn skipped/out-of-scope checks into implicit PASS claims.
- Do not modify implementation files to make evidence pass.
