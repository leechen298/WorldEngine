# Plan

## Phase 1: Documentation Gate

1. Read `0.7.2`, `0.7.3`, and `0.7.4` review evidence.
2. Draft package docs and Chinese mirrors.
3. Run documentation-gate checks.
4. Use documentation/contract and mirror/scope evaluators.
5. Fix P0/P1/P2 findings or stop.
6. Record `evidence_execution_authorized: yes` only after evaluator approval.

## Phase 2: Evidence Execution

1. Run existing checker tests under `tools/testing`.
2. Run readiness manifest and projection read-model CLI validators.
3. Parse v0.7 JSON schema/manifest files.
4. Run formatting and changed-file scope checks.
5. Classify unrun surfaces as skipped or out of scope.

## Phase 3: Evidence Matrix

1. Create `evidence-matrix.md` and Chinese mirror.
2. Record exact commands, results, supported claims, and exclusions.
3. Record compatibility and residual-risk notes.

## Phase 4: Review And Handoff

1. Update `review.md` and Chinese mirror with evidence.
2. Use validation-evidence and closeout consistency evaluators.
3. Update parent v0.7 route/status surfaces to hand off to `0.7.6`.

## Stop Conditions

- Any in-scope command fails.
- Evidence requires product-code repair.
- A skipped or out-of-scope check is written as PASS.
- A broad readiness claim lacks current-session evidence.
- Scope guard reports out-of-scope files.
