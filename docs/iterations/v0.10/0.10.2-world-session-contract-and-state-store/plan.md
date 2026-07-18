# Plan

## Ordered Execution Steps

1. Read v0.10 route and this package docs.
2. Run documentation / contract evaluator.
3. If PASS, record `implementation_authorized: yes`.
4. Add session schemas.
5. Add in-memory session store.
6. Add session routes and router registration.
7. Update manifest surfaces.
8. Add focused backend tests.
9. Run `test-plan.md` commands.
10. Run implementation/evidence evaluator.
11. Update package and parent review, then hand off to `0.10.3`.

## Phase Boundaries

Do not edit implementation files before review authorization. During
implementation, edit only allowed files. During closeout, record exact command
evidence and non-claims.

## Stop Conditions

Stop if implementation requires worldview generation, runtime run, snapshots,
dashboard, persistence, provider live calls, checker fixture work, Validation
Client, generated results, external validation, or `backend/worldengine/`.

## Review Update Step

Update `review.md` before authorization and before final closeout with changed
files, commands, test results, evaluator evidence, compatibility review, scope
review, unresolved findings, and handoff.
