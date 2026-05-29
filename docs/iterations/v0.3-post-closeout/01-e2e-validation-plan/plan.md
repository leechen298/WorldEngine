# Plan

## Ordered Execution Steps

1. Read the parent campaign docs and v0.3 source inputs.
2. Confirm that this package is planning-only.
3. Define repository and documentation checks.
4. Define backend deterministic checks.
5. Define focused WorldSpec loader validation.
6. Define focused runtime context bridge validation.
7. Define event API and Event.refs compatibility validation.
8. Define API smoke checks.
9. Define E2E framework availability detection.
10. Define browser E2E execution only when configured.
11. Define fallback when E2E is unavailable.
12. Define v0.3 release-claim and compatibility-claim review.
13. Define concrete demo-world regression checks.
14. Update `review.md` with docs-only evidence.

## Phase Boundaries

Planning ends with review-ready docs. Execution starts only in
`02-e2e-validation-execution`.

## Stop Conditions

Stop if:

- required v0.3 source files are missing.
- the plan would require implementation changes.
- the plan introduces demo-world details or private oracle details.
- the plan pre-populates successful validation results.
- the plan changes v0.3 release status.

## Review Update Step

Record changed files, files read, commands not run, no-test rationale,
compatibility review, scope review, unresolved P1/P2/P3, and final assessment
in `review.md`.
