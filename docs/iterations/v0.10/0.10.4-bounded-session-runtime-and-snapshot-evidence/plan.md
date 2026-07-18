# Plan

Chinese mirror: `plan.zh.md`.

1. Create the complete package docs and mirrors.
2. Run documentation completeness and whitespace checks.
3. Request read-only evaluator review.
4. If PASS, record `implementation_authorized: yes`.
5. Add focused failing tests for session run/pause/resume/snapshot behavior.
6. Implement the smallest scoped backend changes.
7. Run focused and expanded focused backend tests.
8. Request implementation closeout evaluator review.
9. Update package and parent v0.10 review/current-state handoff.

Stop before implementation if the documentation gate has unresolved P1/P2
findings or if the implementation would require out-of-scope runtime
architecture, persistence, external validation, provider calls, dashboard work,
or `backend/worldengine/` changes.
