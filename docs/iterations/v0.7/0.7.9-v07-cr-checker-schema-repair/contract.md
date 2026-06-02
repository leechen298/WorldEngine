# Contract

## Public Concepts

- `ClosedFindingStatus`: a finding status that is genuinely closed for a pass
  report. For this package, only `resolved` is closed for P1/P2 pass blocking.
- `CheckerSemanticAuthority`: Python checker logic is authoritative for
  semantic validation when JSON Schema can only encode shape.
- `GenericLeakPattern`: abstract, non-consumer-specific markers such as local
  absolute paths, `file://` paths, UI selector markers, hidden reset terms,
  oracle terms, transcript terms, seed-data terms, and event-payload terms.
- `PrivateApplicationStateField`: projection read-model field language that
  exposes private or application-state semantics even when the field has an
  otherwise allowed suffix.

## Allowed Changes

- `tools/testing/validate_external_validation_report.py`
- `tools/testing/test_validate_external_validation_report.py`
- `tools/testing/validate_readiness_manifest.py`
- `tools/testing/test_validate_readiness_manifest.py`
- `tools/testing/validate_projection_read_model_contract.py`
- `tools/testing/test_validate_projection_read_model_contract.py`
- `docs/testing/external-validation-report-schema.json`
- `docs/contracts/v0.7-readiness-manifest-schema.json`
- `docs/validation-report-template.md`
- `docs/contracts/projection-read-model-contract.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md`
- files under this package directory.

## Forbidden Changes

- Runtime, API routes, frontend, persistence, migrations, fixture runners,
  generated result artifacts, external repositories, product UI, projection
  application implementation, or `backend/worldengine/`.
- Concrete external validation worlds, concrete world names, characters,
  locations, maps, resources, story rules, seed data, private transcripts,
  private runner paths, hidden reset API details, private oracle internals, UI
  selector dumps, or non-redacted external event payload examples.
- `docs/iterations/v0.8/**`.

## Required Fix Semantics

- V07-CR-01: `pass` external validation reports must reject P1/P2 findings
  with `accepted`, `deferred`, `open`, or any non-closed status.
- V07-CR-02: external validation report checker must reject generic real leak
  patterns, including local absolute paths, `file://` paths, `data-testid`,
  CSS selector-looking text, hidden reset terms, oracle terms, transcript
  terms, seed-data terms, and event-payload terms.
- V07-CR-03: readiness manifest checker must apply public command and
  forbidden-detail checks to `evidence_references[*].command` and all manifest
  text surfaces.
- V07-CR-04: projection read-model checker must reject private/application
  state field terms such as `private_application_state_summary` even with an
  allowed suffix.
- V07-CR-05: public schemas must either be tightened where JSON Schema can
  express the rule, or the docs/tests must explicitly prove checker semantic
  authority with schema-valid/checker-invalid regression cases.
- P3: validation report template field mapping hints and projection
  read-model contract status text must be synchronized.

## Compatibility Requirements

- Existing valid report, manifest, and projection schema inputs must continue
  to pass.
- Existing Agent smoke and Agent autonomous saved-result checkers must continue
  to pass.
- Changes must remain generic and must not require private consumer data.
- Runtime/API/frontend behavior must remain unchanged.

## Review Gates

Implementation may begin only after:

- package docs and Chinese mirrors exist.
- documentation/contract evaluator reports no P0/P1 and no blocking P2.
- `review.md` records `implementation_authorized: yes`.

Closeout may happen only after:

- red tests for V07-CR-01 through V07-CR-05 are observed failing before repair.
- focused checker tests pass after repair.
- adjacent Agent smoke/autonomous checker tests pass.
- final v0.7 validation commands in `test-plan.md` pass.
- subagent/evaluator checkpoints record no blocking P1/P2.
- validation results are updated without overclaiming.

## Out-of-Scope Follow-Ups

- live external suite execution.
- full autonomous runner/full-suite implementation.
- v0.8 projection application readiness.
