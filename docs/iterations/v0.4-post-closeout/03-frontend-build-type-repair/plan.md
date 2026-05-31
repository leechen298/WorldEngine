# Plan

## Files

Create:

- `docs/iterations/v0.4-post-closeout/03-frontend-build-type-repair/**`

Modify only if needed:

- parent v0.4 post-closeout campaign status files named in `contract.md`.
- reported frontend TypeScript failure files named in `contract.md`.
- durable validation result summary named in `contract.md`.

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- migrations
- external repositories
- autonomous runner expansion beyond the saved-result validator rerun.

## Ordered Steps

1. Read governing docs and package evidence.
2. Reproduce the frontend build failure.
3. Draft this repair package.
4. Run documentation/contract evaluator before implementation authorization.
5. Record implementation authorization if no P0/P1/P2 blocker remains.
6. Apply the minimal frontend TypeScript fix.
7. Run `cd frontend && pnpm build`.
8. Run a read-only frontend type/build reviewer.
9. Run the full required validation command set.
10. Run a read-only scope/evidence evaluator.
11. Update package, parent, and durable evidence docs with actual results.

## Phase Boundaries

- Do not edit frontend files before documentation/contract review completes.
- Do not claim clean pass before every required validation command exits `0`.
- Do not close the package with unresolved P1 or P2 findings.

## Stop Conditions

- Any required fix would change backend runtime/API behavior.
- Any required fix would exceed the reported frontend TypeScript build
  failures.
- Any validation PASS would depend on Agent self-judgment instead of the
  deterministic or scorecard checker.
- A required command fails and reveals a new blocker.

## Verification

The verification commands are exactly those listed in `test-plan.md`.
