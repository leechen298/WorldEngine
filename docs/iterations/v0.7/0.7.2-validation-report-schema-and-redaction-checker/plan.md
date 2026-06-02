# Plan

## Phase 1: Documentation Gate

1. Read parent v0.7 state, `0.7.1` reviewed contracts, the validation report
   template, external fixture runner contract, and existing saved-result
   checker patterns.
2. Draft this package document set and Chinese mirrors.
3. Run documentation-gate checks from `test-plan.md`.
4. Use read-only subagent/evaluator review for documentation, contract,
   mirror, and scope consistency.
5. Fix P0/P1/P2 findings or stop.
6. Record evaluator findings and set `implementation_authorized: yes` only
   after the documentation/contract gate passes.

## Phase 2: Implementation

1. Add `docs/testing/external-validation-report-schema.json`.
2. Add `tools/testing/validate_external_validation_report.py`.
3. Add `tools/testing/test_validate_external_validation_report.py`.
4. Additively update `docs/validation-report-template.md`.
5. Keep implementation isolated to the approved files.

## Phase 3: Verification

1. Run focused checker tests.
2. Run existing Agent smoke/autonomous checker tests if shared assumptions are
   touched or to prove no saved-result checker regression.
3. Run `git diff --check`.
4. Run the changed-file scope guard.
5. Use implementation-scope evaluator, code-review evaluator, and
   validation-evidence evaluator.
6. Fix or explicitly resolve every P0/P1/P2 finding.

## Phase 4: Closeout

1. Update `review.md` and `review.zh.md` with exact command evidence,
   compatibility review, scope review, evaluator evidence, unresolved
   findings, and final assessment.
2. Update parent v0.7 route/status surfaces to hand off to
   `0.7.3-contract-bundle-and-readiness-manifest`.
3. Run closeout consistency review.
4. Stop if parent and child status surfaces disagree.

## Stop Conditions

- The checker needs private fixture data, concrete external world details, UI
  selectors, oracle internals, private paths, transcripts, or non-redacted
  event payloads to validate a report.
- `blocked`, `skipped`, or `out_of_scope` cannot be distinguished from
  `pass`.
- Redaction rules become weaker than `0.7.1` or the report template.
- A required evaluator returns an unresolved P0/P1 or blocking P2.
- Scope guard reports out-of-scope changed files.

## Review Update Step

Every phase that changes files must update package review evidence before
claiming completion. Tests not run must be recorded explicitly with reason.
