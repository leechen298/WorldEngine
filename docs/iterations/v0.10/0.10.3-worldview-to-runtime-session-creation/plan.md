# Plan

## Ordered Execution Steps

1. Read package docs and existing generation/session code.
2. Run documentation / contract evaluator.
3. If PASS, record `implementation_authorized: yes`.
4. Add session request/summary schema.
5. Extend session store and route.
6. Update manifest discovery.
7. Add focused tests.
8. Run `test-plan.md` commands.
9. Run implementation/evidence evaluator.
10. Update package and parent review, then hand off to `0.10.4`.

## Phase Boundaries

No implementation edits before authorization. Implementation is limited to
allowed files. Closeout must record non-claims.

## Stop Conditions

Stop if live provider calls, runtime execution, snapshots, dashboard,
checker, Validation Client, persistence, generated results, external
validation, or `backend/worldengine/` are required.

## Review Update Step

Update review before authorization and closeout with changed files, commands,
test results, evaluator evidence, compatibility, scope, findings, and handoff.
