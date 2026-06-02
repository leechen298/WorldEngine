# Plan

## Ordered Execution Steps

1. Create the full `0.7.9` package document set and Chinese mirrors.
2. Run documentation gate checks.
3. Dispatch read-only documentation/contract and mirror/scope evaluators.
4. If review passes, update `review.md` to
   `implementation_authorized: yes`.
5. Read package docs in implementation order.
6. Add red regression tests for V07-CR-01 through V07-CR-05.
7. Run focused tests and record the expected red failures.
8. Implement minimal checker/schema/template/status fixes.
9. Rerun focused and adjacent checker tests.
10. Run final v0.7 validation checks from `test-plan.md`.
11. Dispatch implementation-scope, code-review, validation-evidence, and
    closeout consistency evaluators.
12. Update `review.md` and validation result docs with current-session
    evidence and final verdict.

## Phase Boundaries

- Documentation phase ends only after evaluator review and
  `implementation_authorized: yes`.
- Implementation phase starts only after reading this package's approved docs.
- Validation result update happens only after command evidence exists.

## Stop Conditions

- Required package docs or mirrors are missing.
- Evaluator reports P0/P1 or blocking P2.
- Red tests do not reproduce the V07-CR blockers.
- A fix requires runtime/API/frontend/v0.8 work.
- Scope guard finds unrelated or v0.8 changes in the repair package.
- Clean pass would require unsupported external suite, projection readiness,
  product readiness, live Agent smoke, full autonomous runner, or v0.8 claims.

## Review Update Step

`review.md` must record changed files, commands run, red/green test evidence,
compatibility review, scope review, subagent/evaluator findings, unresolved
P1/P2/P3, and final assessment.
