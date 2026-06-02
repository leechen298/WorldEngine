# Contract

## Public Concepts

- `EvidenceMatrix`: a package-local table that records command coverage,
  result, and claim boundary for v0.7 evidence surfaces.
- `SupportedClaim`: a claim backed by a command run in the current session.
- `SkippedCheck`: a command or surface not run, with reason and impact.
- `OutOfScopeCheck`: a surface outside this package contract.

## Allowed Evidence Surfaces

This package may run and record evidence for existing files only:

- external validation report checker tests.
- readiness manifest checker tests.
- projection read-model checker tests.
- Agent smoke saved-result checker tests.
- Agent autonomous saved-result checker tests.
- JSON parsing for v0.7 schema/manifest files.
- CLI validation for existing v0.7 checker entrypoints.
- `git diff --check`.
- changed-file scope guard.

## Required Classification

The evidence matrix must classify these surfaces as passed, failed, blocked,
skipped, or out of scope:

- external validation report schema/checker.
- readiness manifest schema/checker.
- projection read-model schema/checker.
- Agent smoke saved-result checker.
- Agent autonomous saved-result checker.
- backend runtime/API behavior.
- frontend behavior.
- browser E2E.
- live Agent smoke.
- full autonomous runner/full suite.
- external validation suite.
- projection application readiness.
- product readiness.
- generation-quality readiness.
- release readiness.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.5-quality-regression-and-compatibility-evidence/`.
- Create or update package-local `evidence-matrix.md` and Chinese mirror.
- Update parent v0.7 status and route surfaces after review and closeout.

## Forbidden Changes

- Do not modify runtime, API, frontend, backend product code, migrations,
  persistence, fixtures, external repositories, generated result fixtures, or
  `backend/worldengine/`.
- Do not add or change checker behavior, tests, schemas, or contracts in this
  package.
- Do not claim any PASS not backed by a current-session command.
- Do not use v0.6 handoff evidence as current v0.7 PASS evidence.

## Compatibility Requirements

- Existing v0.7 checker behavior remains unchanged.
- Evidence claims must match the exact command surface.
- Historical evidence may be cited only as handoff context.
- Unrun checks must be classified without implying a hidden PASS.

## Review Gates

Evidence execution may begin only after:

- package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- package `review.md` records `evidence_execution_authorized: yes`.

Closeout may happen only after:

- in-scope commands are run or honestly classified.
- `evidence-matrix.md` records exact results and exclusions.
- `git diff --check` passes.
- changed-file scope guard passes.
- validation-evidence and closeout consistency evaluators report no blocking
  findings.
