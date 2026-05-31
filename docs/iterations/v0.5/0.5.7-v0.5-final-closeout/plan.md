# Plan

Status: final / closeout complete

## Steps

1. Create final closeout package docs and mirrors.
2. Run final docs/mirror/scope checks.
3. Run final focused backend compatibility.
4. Run final full backend regression.
5. Record final evidence, skipped checks, compatibility review, scope review,
   and unresolved findings.
6. Run closeout consistency evaluator.
7. If evaluator passes, synchronize final status surfaces and roadmap.
8. Re-run final lightweight consistency checks after status synchronization.

## Stop Conditions

- Stop on missing docs or mirrors.
- Stop on out-of-scope file changes.
- Stop on failed backend verification.
- Stop on unresolved P1/P2.
- Stop if final status is applied before evaluator approval.
- Stop if final wording claims unrun frontend, E2E, Agent smoke, autonomous, or
  external validation readiness.

## Handoff Criteria

- Final verification passes.
- Closeout consistency evaluator passes.
- v0.5 parent status surfaces are synchronized.
- roadmap v0.5 status is synchronized.
- final review records no unresolved P1/P2.
- commit is created after final verification.
