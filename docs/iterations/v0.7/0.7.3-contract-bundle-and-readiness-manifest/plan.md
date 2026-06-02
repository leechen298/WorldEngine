# Plan

## Phase 1: Documentation Gate

1. Read `0.7.1` contracts, `0.7.2` schema/checker evidence, current API
   references, contract docs, release docs, and parent v0.7 state.
2. Draft package docs and Chinese mirrors.
3. Run documentation-gate checks from `test-plan.md`.
4. Use documentation/contract evaluator and mirror/scope evaluator.
5. Fix P0/P1/P2 findings or stop.
6. Record `implementation_authorized: yes` only after evaluator approval.

## Phase 2: Implementation

1. Add readiness manifest schema.
2. Add v0.7 readiness manifest.
3. Add readiness manifest checker.
4. Add focused checker tests.
5. Keep implementation isolated to approved files.

## Phase 3: Verification

1. Run focused manifest checker tests.
2. Run external validation report checker tests as adjacent regression.
3. Run `git diff --check`.
4. Run changed-file scope guard.
5. Use implementation-scope, code-review, validation-evidence, and closeout
   consistency evaluators.
6. Fix or explicitly resolve every P0/P1/P2 finding.

## Phase 4: Closeout

1. Update package review evidence.
2. Update parent v0.7 route/status surfaces to hand off to `0.7.4`.
3. Run closeout consistency review.
4. Stop if parent and child status surfaces disagree.

## Stop Conditions

- Manifest requires private runner state or private repository paths.
- Manifest implies external suite PASS without accepted evidence.
- Public contract identifiers drift from actual docs.
- Scope guard reports out-of-scope files.
- Required evaluator returns unresolved P0/P1 or blocking P2.

## Review Update Step

Every phase that changes files must update `review.md` before claiming
completion. Tests not run must be recorded explicitly with reason.
