# Plan

## Ordered Execution Steps

1. Read parent v0.4 docs and this package docs.
2. Confirm the current route in `CURRENT_STATE.md` matches `action-validation-implementation` or record a route mismatch in `review.md`.
3. Confirm allowed and forbidden file classes from `contract.md`.
4. Run a documentation / contract evaluator when required by `GOAL_RUNNER.md`.
5. If this is documentation-only, update only approved docs and keep implementation authorization closed.
6. If this is mixed or code and review has authorized implementation, make only the approved implementation changes.
7. Run the exact verification commands from `test-plan.md`.
8. Run required subagent/evaluator checkpoints and classify findings.
9. Update `review.md` with changed files, commands, test results, compatibility review, scope review, findings, and final assessment.
10. Update parent `CURRENT_STATE.md` only after this package reaches a reviewed route status.

## Phase Boundaries

- Documentation phase ends only after package docs are reviewed.
- Implementation phase starts only after `implementation_authorized: yes` is recorded for mixed/code packages.
- Verification phase cannot make pass claims without current-session command evidence.
- Closeout phase cannot proceed with unresolved P1 or unaccepted P2.

## Stop Conditions

- Stop when a required evaluator checkpoint is missing.
- Stop on P1 or unresolved P2 findings.
- Stop and record a blocker when required file classes are not authorized by the active contract.
- Do not treat historical evidence as current-session pass evidence.

Also stop if any required evaluator checkpoint is unavailable or if git state shows out-of-scope modifications.

## Review Update Step

`review.md` must be updated before package handoff. Parent state updates are allowed only after review evidence supports the new child status.
