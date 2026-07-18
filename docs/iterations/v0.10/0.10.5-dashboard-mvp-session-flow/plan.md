# Plan

Chinese mirror: `plan.zh.md`.

1. Create complete package docs and mirrors.
2. Run documentation completeness and whitespace checks.
3. Request read-only evaluator review.
4. If PASS, record `implementation_authorized: yes`.
5. Add focused frontend API/client/dashboard tests.
6. Implement smallest scoped dashboard/API-client changes.
7. Run frontend unit tests, frontend build, backend compatibility tests, and
   targeted E2E when environment allows.
8. Request implementation closeout evaluator review.
9. Update package and parent v0.10 review/current-state handoff.

Stop before implementation if the docs gate has unresolved P1/P2 findings or
if implementation requires provider key UI, backend feature expansion,
Validation Client code, concrete demo assets, or `backend/worldengine/`.
