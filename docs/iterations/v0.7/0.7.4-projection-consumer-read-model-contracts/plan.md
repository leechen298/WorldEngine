# Plan

## Phase 1: Documentation Gate

1. Read `0.7.1` projection consumer contract, `0.7.3` readiness manifest
   evidence, and current runtime/event/Agent/memory/generation/API docs.
2. Draft package docs and Chinese mirrors.
3. Run documentation-gate checks.
4. Use documentation/contract and mirror/scope evaluators.
5. Fix P0/P1/P2 findings or stop.
6. Record `implementation_authorized: yes` only after evaluator approval.

## Phase 2: Implementation

1. Add projection read-model contract.
2. Add projection read-model schema.
3. Add projection read-model checker.
4. Add focused checker tests.

## Phase 3: Verification

1. Run focused projection read-model checker tests.
2. Run readiness manifest checker tests as adjacent regression.
3. Run `git diff --check` and changed-file scope guard.
4. Use implementation-scope, code-review, validation-evidence, and closeout
   consistency evaluators.

## Phase 4: Closeout

1. Update review evidence.
2. Update parent v0.7 route/status surfaces to hand off to `0.7.5`.
3. Run closeout consistency review.

## Stop Conditions

- Any read model needs product-specific or concrete world semantics.
- A projection surface mutates runtime or implies write capability.
- Projection contract readiness is confused with v0.8 app readiness.
- Scope guard reports out-of-scope files.

## Review Update Step

Every phase that changes files must update `review.md`; tests not run must be
recorded explicitly with reason.
