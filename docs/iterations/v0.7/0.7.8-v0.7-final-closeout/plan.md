# Plan

## Phase 1: Draft Closeout

1. Create package docs and Chinese mirrors.
2. Create `final-closeout.md` and Chinese mirror.

## Phase 2: Final Verification

1. Run checker regression and CLI validation.
2. Run JSON parse checks.
3. Run docs/evidence link checks.
4. Run `git diff --check` and scope guard.

## Phase 3: Final Review

1. Update final closeout evidence.
2. Use final evaluator and mirror/scope evaluator.
3. Fix blockers or stop.

## Phase 4: Parent Final Status

1. If evaluators pass, update parent v0.7 status surfaces to
   `final / closeout complete`.
2. Record final status in parent review.

## Stop Conditions

- Any final command fails.
- Any P1/P2 remains unresolved.
- Scope guard reports out-of-scope files.
- Final closeout would imply unrun product/runtime/external claims.
