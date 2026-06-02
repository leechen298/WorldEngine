# Technical Design

## Documentation And Implementation Structure

This package repairs existing checker and documentation surfaces; it does not
create new runtime behavior.

Affected implementation files:

- `tools/testing/validate_external_validation_report.py`
- `tools/testing/test_validate_external_validation_report.py`
- `tools/testing/validate_readiness_manifest.py`
- `tools/testing/test_validate_readiness_manifest.py`
- `tools/testing/validate_projection_read_model_contract.py`
- `tools/testing/test_validate_projection_read_model_contract.py`

Affected public docs/schema files:

- `docs/testing/external-validation-report-schema.json`
- `docs/contracts/v0.7-readiness-manifest-schema.json`
- `docs/validation-report-template.md`
- `docs/contracts/projection-read-model-contract.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.md`
- `docs/testing/results/2026-06-02-v0.7-overall-validation.zh.md`

## Repair Design

### External validation report checker

- Replace accepted-as-resolved P1/P2 semantics with closed-only semantics.
- Add generic forbidden text scanning over every string in the report.
- Keep synthetic sentinels for existing fixtures, but add real generic
  patterns for private paths, UI selector markers, hidden reset markers,
  oracle terms, transcript terms, seed-data terms, and event payload terms.
- Keep valid abstract identifiers accepted.

### Readiness manifest checker

- Reuse the same style of generic leak scanning over all manifest strings.
- Validate command strings as public commands: no absolute local paths, no
  parent traversal, no private runner terms, no UI selector text, no oracle or
  transcript/event payload terms.
- Preserve current public repository-relative path checks.

### Projection read-model checker

- Extend forbidden allowed-field terms for `private`, `application_state`, and
  equivalent app/private state language.
- Preserve allowed bounded suffix semantics for safe public summaries.

### JSON schema and authority

- Tighten JSON Schema where it can express safe enum narrowing.
- Where JSON Schema cannot express semantic text scans, add regression tests
  showing schema-valid/checker-invalid inputs and document checker semantic
  authority.

### Template/status drift

- Add concise field mapping hints to `docs/validation-report-template.md`.
- Update projection read-model contract status to match reviewed/repair
  context without claiming projection readiness PASS.

## Compatibility Strategy

- Start with failing tests for each V07-CR issue.
- Make minimal checker changes to pass those tests.
- Rerun all `tools/testing` tests and existing Agent smoke/autonomous checker
  tests.
- Do not change valid public contract payloads except where schema tightening
  is intentionally needed.

## Anti-Drift Rules

- Do not add concrete external-world examples.
- Do not change or stage known unrelated v0.8 boundary worktree items:
  `docs/roadmap.md`, `docs/scope-boundaries.md`, the v0.7 root planning docs,
  v0.7 handoff/final-closeout boundary docs, or `docs/iterations/v0.8/**`.
- Do not turn checker/schema PASS into external suite or product readiness
  PASS.
- Do not claim clean pass until the V07-CR blocker gate no longer finds
  unresolved P1/P2 blockers or the validation result records them repaired with
  current-session evidence.
