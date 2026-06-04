# Plan

Chinese mirror: `plan.zh.md`.

## Objective

Prepare and, after review approval, execute a narrow repair for the public
director guidance redaction failure that blocked the full lifecycle autonomous
validation checker.

## Phase 1: Documentation Gate

1. Read root and iteration agent rules.
2. Read v0.8 current state and 0.8.9 handoff documents.
3. Read the failed full lifecycle validation result and scenario contract.
4. Draft this package's full document set and mirrors.
5. Keep `implementation_authorized: no`.
6. Run documentation-stage checks.
7. Dispatch a read-only documentation/contract evaluator.
8. Stop before runtime or test implementation until review approval is
   recorded.

## Phase 2: Implementation Authorization

Implementation may start only after:

1. documentation/contract evaluator returns no P0/P1 and no blocking P2.
2. package review records `implementation_authorized: yes`.
3. working tree dirty scope is inspected.

## Phase 3: RED Test

1. Update the focused director guidance test to reject forbidden public
   evidence markers.
2. Run the focused test.
3. Record the expected failure against current code.

## Phase 4: Runtime Repair

1. Change only the public director guidance explanation wording.
2. Preserve response schema, operation id, event type, and event payload safety.
3. Do not add private marker terms to public output.

## Phase 5: Checker Coverage

1. Inspect current checker behavior for direct API operation-log rejection.
2. Add focused checker regression only if current coverage is insufficient.
3. Do not relax any checker rule.

## Phase 6: Verification

Run the commands in `test-plan.md` in this order:

1. focused backend test.
2. related 0.8.9.1 regression set.
3. full backend regression.
4. historical saved-result checker, expected to remain FAIL.
5. optional runtime probe.
6. new full lifecycle rerun and checker only if review records
   `evidence_execution_authorized: yes`; otherwise record the rerun as not
   authorized.
7. `git diff --check`.

## Phase 7: Required Evaluators

Use the `/goal` subagent checkpoints:

1. documentation/contract evaluator before implementation authorization.
2. implementation-scope evaluator after files are changed and before broad
   verification.
3. code-review evaluator after focused tests and before broad regression or
   autonomous validation claims.
4. validation-evidence evaluator before recording checker, API smoke, or
   autonomous validation claims.
5. closeout consistency evaluator before final assessment.

## Stop Conditions

- Stop if implementation needs Validation Client changes.
- Stop if implementation needs concrete validation-world content.
- Stop if public output still contains forbidden private/internal markers.
- Stop if any P1 remains.
- Stop if any P2 remains without explicit accepted rationale.
- Stop if full lifecycle PASS would depend on rewriting the old failed result.
- Stop before any live full lifecycle rerun unless this package review records
  `evidence_execution_authorized: yes`.

## Review Update Step

When implementation actually runs, update `review.md` and `review.zh.md` with
changed files, commands, test results, compatibility review, scope review,
subagent findings, unresolved findings, and final assessment.
