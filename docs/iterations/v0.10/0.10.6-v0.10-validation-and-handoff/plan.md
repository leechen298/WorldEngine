# Plan

Chinese mirror: `plan.zh.md`.

1. Create complete package docs and mirrors.
2. Run documentation completeness and whitespace checks.
3. Request read-only evaluator review.
4. If PASS, record `implementation_authorized: yes` and
   `evidence_execution_authorized: yes` for validation commands only.
5. Run backend, frontend, E2E, manifest, and whitespace validation commands.
6. Record PASS/PARTIAL/BLOCKED/FAIL evidence.
7. Request closeout evaluator review.
8. Synchronize v0.10 parent closeout and v0.11 handoff route.

Stop if validation reveals an in-scope P1/P2 defect. Do not implement v0.11 or
v0.12 work in this package.
