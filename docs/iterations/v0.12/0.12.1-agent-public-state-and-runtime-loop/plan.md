# Plan

Chinese mirror: `plan.zh.md`.

1. Read parent v0.12 current state, goal runner, campaign plan, v0.12 plan, and
   `0.12.0` handoff.
2. Read existing Agent loop, perception, action adapter, session store,
   session routes, manifest route, and related tests.
3. Complete this package document set and run documentation checks.
4. Request documentation / contract evaluator review.
5. If PASS, record `implementation_authorized: yes` for this package only.
6. Add focused tests for session Agent list/read/step, client-scripted-action
   rejection, public evidence, redaction boundary, and manifest discovery.
7. Implement the smallest additive session Agent state and runtime loop.
8. Run focused backend verification from `test-plan.md`.
9. Request implementation-scope evaluator review.
10. Repair any P1/P2 findings inside this package scope.
11. If verification and evaluator review pass, update package and parent v0.12
    route to `0.12.2-agent-memory-and-rest-consolidation-mvp-documentation-package-needed`.
