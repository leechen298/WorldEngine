# Technical Design

## Current State

WorldEngine currently has:

- `docs/contracts/external-fixture-runner-contract.md`.
- `docs/contracts/external-validation-readiness-contract.md`.
- `docs/contracts/projection-consumer-contract.md`.
- `docs/validation-report-template.md`.
- Agent smoke and Agent autonomous saved-result checkers under
  `tools/testing/`.

It does not yet have a machine-readable external validation report schema or
checker. The template still needs additive alignment with the `0.7.1`
readiness status taxonomy.

## Implementation Structure

Planned implementation files:

```text
docs/testing/external-validation-report-schema.json
tools/testing/validate_external_validation_report.py
tools/testing/test_validate_external_validation_report.py
```

Planned documentation/template update:

```text
docs/validation-report-template.md
```

Package evidence files:

```text
docs/iterations/v0.7/0.7.2-validation-report-schema-and-redaction-checker/
```

## Schema Shape

The schema should define one generic report object with required fields:

```text
report_id
engine_reference
public_contract_surface
external_suite_id
redacted_target_id
capability_area
scenario_id
high_level_goal
status
observed_public_behavior
redacted_evidence_summary
compatibility_notes
unresolved_findings
redaction_confirmed
forbidden_detail_review
scope_review
```

`status` must enumerate `pass`, `fail`, `blocked`, `skipped`, and
`out_of_scope`. The schema should be public documentation; the checker owns
semantic validation that JSON Schema cannot express cleanly without new
dependencies.

## Checker Flow

The checker should:

1. Load a JSON report file.
2. Validate that the top-level value is an object.
3. Validate required fields and simple field types.
4. Validate `status` is one of the allowed values.
5. Validate `redaction_confirmed` is true.
6. Validate every `forbidden_detail_review` flag is false.
7. Validate `pass` reports include public behavior and evidence summary and
   have no unresolved P1/P2 findings.
8. Validate `blocked`, `skipped`, and `out_of_scope` reports include an
   explicit reason and are not treated as pass.
9. Scan report strings for generic redaction-risk markers such as absolute
   private paths, UI-selector markers, hidden reset markers, oracle-internal
   markers, seed-data markers, transcript markers, and external event payload
   markers.
10. Print deterministic `FAIL:` lines for each error or one deterministic
    `PASS:` line on success.

The checker must not import private fixture data or evaluate external suite
truth. It checks report shape and redaction safety only.

## Test Strategy

Focused tests should build report dictionaries in memory and write them to
temporary JSON files. They must use only abstract identifiers.

Required cases:

- valid `pass` report passes.
- missing required field fails.
- unsupported status fails.
- `pass` with `redaction_confirmed: false` fails.
- `pass` with unresolved P1/P2 fails.
- `blocked` without reason fails.
- valid `blocked`, `skipped`, and `out_of_scope` reports pass as non-pass
  statuses.
- report containing forbidden detail review flag set to true fails.
- report containing private path, UI selector, hidden reset, oracle internal,
  seed-data, transcript, or event payload marker fails.
- CLI returns `0` on valid input and `1` on invalid input.

## Compatibility Strategy

- Keep implementation isolated to the new checker and schema.
- Do not modify Agent smoke/autonomous checkers or their schemas.
- Use Python standard library only.
- Update `docs/validation-report-template.md` additively so existing human
  report structure remains recognizable.
- Keep all examples abstract and redacted.

## Anti-Drift Rules

- Parent and child status surfaces must agree before closeout.
- `implementation_authorized: yes` must appear only after evaluator approval.
- The checker must not use private consumer knowledge.
- `blocked`, `skipped`, and `out_of_scope` must never be accepted as pass.
- Tests must not contain concrete external validation world details.
- Review evidence must distinguish focused checker tests from broader
  runtime/API/frontend/E2E/Agent/autonomous checks that were not run.
