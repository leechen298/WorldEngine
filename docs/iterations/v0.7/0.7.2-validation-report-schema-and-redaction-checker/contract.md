# Contract

## Public Concepts

- `ExternalValidationReport`: a machine-readable, redacted report describing
  public behavior against a reviewed WorldEngine contract surface.
- `ReportStatus`: one of `pass`, `fail`, `blocked`, `skipped`, or
  `out_of_scope`.
- `RedactionConfirmation`: a required boolean confirmation that forbidden
  external consumer details were removed.
- `ForbiddenDetailReview`: a required object whose listed forbidden detail
  flags must be false for an accepted report.
- `RedactionRiskScan`: generic checker logic that rejects obvious private
  paths, UI-selector markers, hidden reset markers, oracle-internal markers,
  seed-data markers, transcript markers, and non-redacted external event
  payload markers without needing private fixture data.

## Report Semantics

The schema/checker must preserve these fields:

- report id.
- engine commit or version reference.
- public contract surface exercised.
- external suite id.
- redacted target id.
- capability area.
- abstract scenario id.
- high-level public goal.
- status: `pass`, `fail`, `blocked`, `skipped`, or `out_of_scope`.
- observed public behavior.
- redacted evidence summary.
- compatibility notes.
- unresolved P1/P2/P3 findings.
- redaction confirmation.
- forbidden detail review.
- scope review.

`pass` is valid only when redaction confirmation is true, forbidden detail
flags are false, required public-behavior evidence is present, and no
unresolved P1/P2 finding remains. `blocked`, `skipped`, and `out_of_scope`
are not pass equivalents and must include explicit reasons.

## Allowed Changes

- Create or update files under
  `docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/`.
- Create or update Chinese mirrors for this child package.
- Create `docs/testing/external-validation-report-schema.json`.
- Create `tools/testing/validate_external_validation_report.py`.
- Create `tools/testing/test_validate_external_validation_report.py`.
- Additively update `docs/validation-report-template.md`.
- Update parent v0.7 status and route surfaces after review and closeout:
  - `docs/iterations/v0.7/README.md`
  - `docs/iterations/v0.7/README.zh.md`
  - `docs/iterations/v0.7/v0.7-plan.md`
  - `docs/iterations/v0.7/v0.7-plan.zh.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.md`
  - `docs/iterations/v0.7/GOAL_RUNNER.zh.md`
  - `docs/iterations/v0.7/CURRENT_STATE.md`
  - `docs/iterations/v0.7/CURRENT_STATE.zh.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.md`
  - `docs/iterations/v0.7/CAMPAIGN_PLAN.zh.md`
  - `docs/iterations/v0.7/review.md`
  - `docs/iterations/v0.7/review.zh.md`

## Forbidden Changes

- Do not modify runtime, core schemas, API routes, frontend, persistence,
  migrations, fixture runners, generated result artifacts, external
  repositories, or `backend/worldengine/`.
- Do not add concrete external validation world data, concrete world names,
  character names, location names, story rules, seed data, private
  transcripts, UI selectors, hidden reset API details, private fixture paths,
  oracle internals, or non-redacted external event payloads.
- Do not create consumer-specific example reports. Tests may use only abstract
  identifiers such as `external-suite-001`, `target-redacted-001`, and
  `scenario-001`.
- Do not weaken `docs/contracts/external-validation-readiness-contract.md` or
  `docs/contracts/external-fixture-runner-contract.md`.
- Do not claim external suite PASS, projection application readiness, product
  readiness, release readiness, runtime PASS, API PASS, frontend PASS, E2E
  PASS, Agent smoke PASS, or autonomous PASS.

## Compatibility Requirements

- Existing Agent smoke and Agent autonomous saved-result schemas and checkers
  must remain unchanged unless a shared-tooling dependency is intentionally
  touched. This package should avoid shared-tooling changes.
- `docs/validation-report-template.md` changes must be additive and align with
  `0.7.1` readiness semantics.
- The checker must use only Python standard-library behavior unless the
  package review explicitly expands dependencies.
- Runtime/API/frontend behavior must remain unchanged.
- The schema/checker must not require private consumer details to validate a
  report.

## Review Gates

Implementation may begin only after:

- package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- package `review.md` records `implementation_authorized: yes`.

Closeout may happen only after:

- focused checker tests pass.
- `git diff --check` passes.
- changed-file scope guard passes.
- implementation-scope evaluator reports no blocking findings.
- code-review evaluator reports no blocking findings.
- validation-evidence evaluator confirms command evidence is recorded without
  overclaiming.
- closeout consistency review finds parent and child status surfaces aligned.

## Out-of-Scope Follow-ups

- `0.7.3`: contract bundle and readiness manifest.
- `0.7.4`: projection read-model contracts and any approved implementation.
- `0.7.5`: current-core compatibility evidence package.
- `0.7.6`: release-candidate bundle.
- `v0.8`: projection application readiness.
