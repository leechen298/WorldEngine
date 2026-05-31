# Plan

Status: review complete

## Steps

1. Read completed v0.5 child package reviews.
2. Create evidence index and compatibility audit.
3. Run documentation checks, scope guard, forbidden-surface sentinel, focused
   backend compatibility, and full backend regression.
4. Record unresolved finding classification.
5. Run read-only evidence/compatibility evaluator.
6. If evaluator passes, mark `0.5.5` review complete and hand off to `0.5.6`.

## Stop Conditions

- Stop on missing docs or mirrors.
- Stop on stale parent/child status.
- Stop on missing current-session evidence for implemented surfaces.
- Stop on unresolved P1/P2.
- Stop if audit expands into implementation, RC declaration, or final release.

## Handoff Criteria

- Evidence index complete.
- Compatibility audit complete.
- Current verification commands recorded.
- No unresolved P1/P2.
- Evaluator PASS recorded.
- Parent status surfaces point to `0.5.6`.
