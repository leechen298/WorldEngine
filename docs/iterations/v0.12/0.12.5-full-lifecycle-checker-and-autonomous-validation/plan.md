# Plan

Chinese mirror: `plan.zh.md`.

1. Read v0.12 parent state, `0.12.4` handoff contract, existing autonomous
   checker, fixtures, and result docs.
2. Draft package docs with explicit validation/classification boundaries.
3. Run documentation gate checks.
4. Request documentation evaluator review.
5. Repair P1/P2 findings inside package scope.
6. If review passes, record `evidence_execution_authorized: yes` for checker
   commands only.
7. Run deterministic autonomous fixture checker commands from `test-plan.md`.
8. Inspect whether a current v0.12 external Validation Client result directory
   exists. If not, record fresh external validation as BLOCKED.
9. Create result docs: validation result, scorecard summary, and read-only
   evaluator review.
10. Request read-only evaluator review of the result/classification.
11. Repair in-scope P1/P2 findings or record PARTIAL/BLOCKED/FAIL.
12. Update parent route to `0.12.6-mvp-release-candidate-and-closeout`.
