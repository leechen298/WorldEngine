# Technical Design

## Current State

v0.3 currently has package evidence through the 0.3.7 release-candidate bundle.
The release placeholder still says v0.3 is planned / not released, and the
milestone index lists 0.3.8 as planned / gated before this documentation
package.

The final-closeout package touches only documentation status and evidence
surfaces. It does not touch loader code, runtime context code, schemas, API
routes, frontend code, fixtures, migrations, or test implementation files.

## Contract Alignment and Invariants

Final closeout must preserve these invariants:

- release-candidate review approval is required before final status changes.
- no unresolved P1/P2 finding may remain open at final closeout.
- historical evidence from 0.3.0 through 0.3.7 must not be presented as
  current-session 0.3.8 test execution.
- open P3 items may remain only as explicit accepted handoffs.
- v0.4 remains a future milestone requiring its own reviewed package.

## Proposed Implementation

Documentation-stage work creates this package and marks it ready for review.

After review approval, implementation may:

1. Update `docs/releases/v0.3.md` and `docs/releases/v0.3.zh.md` from planned
   / not released wording to final-closeout wording supported by review.
2. Update v0.3 milestone index and detailed plan status docs.
3. Update `docs/iterations/v0.3/findings.md` only for final-review blocker
   classification, accepted P3 handoffs, or newly discovered findings.
4. Update this package's README checklist and review evidence.
5. Run the documentation verification commands in `test-plan.md`.

If final review identifies an unresolved P1/P2 blocker, closeout must stop and
record the blocker instead of changing final status.

## Affected Surfaces

- `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/**`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/v0.3/README.zh.md`
- `docs/iterations/v0.3/v0.3-plan.md`
- `docs/iterations/v0.3/v0.3-plan.zh.md`
- `docs/iterations/v0.3/findings.md`, only if finding status changes.
- `docs/releases/v0.3.md`
- `docs/releases/v0.3.zh.md`

## Data Model / Schema Changes

None. This package must not change schemas, validation behavior, database
models, event fields, API models, fixtures, or migrations.

## Runtime / Service Design

None. This package must not change runtime services, loader behavior, bridge
behavior, API routes, event log behavior, archive behavior, params behavior, or
frontend behavior.

## Compatibility

Compatibility is maintained by scope:

- runtime, schema, API, event, archive, params, frontend, fixture, migration,
  and test implementation files are not modified.
- final status claims are documentation claims backed by historical package
  evidence and current-session documentation checks.
- current-session commands must be listed separately from historical evidence.

## Risks

- A status update could imply v0.3 final release before review approval. The
  test plan checks release and status wording before closeout.
- A P1/P2 blocker could be missed. The test plan includes unresolved P1/P2
  scans over `findings.md` and closeout docs.
- Documentation mirrors could drift. The test plan checks English and Chinese
  file presence and status wording.
- A future v0.4 handoff could be overstated as implementation permission. The
  contract and test plan require v0.4 to remain a separate reviewed package.
