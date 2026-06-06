# Plan

Chinese mirror: `plan.zh.md`.

## Ordered Steps

1. Read v0.9 parent docs and this package document set.
2. Run documentation checks from `test-plan.md`.
3. Send this package to a read-only documentation/contract evaluator.
4. Fix or record evaluator findings.
5. If no P0/P1/blocking P2 remains, update `review.md` to
   `implementation_authorized: yes`; otherwise stop before code changes.
6. Implement the smallest provider smoke path in `backend/app/`.
7. Add public provider summary schemas and redaction tests.
8. Preserve `/manifest` compatibility and existing public handoff tests.
9. Run focused backend tests.
10. Run checker tests only if checker support is changed.
11. Run backend regression if code changes touch shared backend surfaces.
12. Update `review.md` with commands, results, compatibility review, scope
    review, unresolved findings, final assessment, and handoff to `0.9.2`.

## Phase Boundaries

Documentation phase:

- Create and review package documents.
- No runtime, API, schema, test, checker, provider, or fixture files may
  change before authorization.

Implementation phase:

- May start only after this package review records
  `implementation_authorized: yes`.
- Must remain within the allowed backend/checker/test scope.

Evidence execution phase:

- Live provider calls are optional and must be bounded.
- If no provider key or network is available, record `not_configured` or
  `blocked`, not PASS.

## Stop Conditions

Stop if:

- package docs are missing or conflict.
- evaluator reports unresolved P0/P1/blocking P2.
- implementation requires Validation Client changes.
- implementation requires concrete world content.
- smoke evidence would expose keys, raw prompts, raw responses, raw traces, or
  private account details.
- provider behavior expands into world generation.
- tests cannot prove unconfigured behavior and redaction.

## Review Update Step

Before closeout, `review.md` must record:

- changed files.
- commands run.
- test results.
- live provider status or blocked/not-configured status.
- compatibility review.
- scope review.
- unresolved P1/P2/P3 findings.
- final assessment and handoff.
