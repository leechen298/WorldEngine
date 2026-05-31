# v0.5 Release Candidate Bundle

Status: prepared for review

This bundle is prepared by `0.5.6` for review. It is not final closeout.

## Included Packages

- `0.5.1-memory-self-continuity-contracts`: review complete.
- `0.5.2-working-and-episodic-memory-substrate`: review complete.
- `0.5.3-memory-context-loop-integration`: review complete.
- `0.5.4-reflection-relationship-and-drift-contract-followup`: review complete.
- `0.5.5-v0.5-evidence-and-compatibility-audit`: review complete.

## Included Implementation Files

- `backend/app/schemas/agent_memory.py`
- `backend/app/agent/memory.py`
- `backend/app/tests/test_agent_memory_substrate.py`
- `backend/app/schemas/agent_loop.py`
- `backend/app/agent/perception.py`
- `backend/app/api/app_factory.py`
- `backend/app/tests/test_agent_perception.py`
- `backend/app/tests/test_agent_loop_api.py`

## Included Behavior

- Generic working-memory and episodic-memory schemas.
- Process-local in-memory memory substrate.
- Optional bounded read-only memory context in Agent Loop perception.
- Internal app-state memory store wiring for perception context.

## Excluded Behavior

- Memory persistence.
- Public memory APIs.
- Loop request memory selectors.
- Memory writes during loop steps.
- Action semantic changes.
- Relationship behavior.
- Self-summary generation.
- Automatic reflection.
- Personality drift action modifiers.
- Frontend behavior.
- World generation.
- External validation readiness.
- Projection application readiness.

## Evidence Summary

From `0.5.5` audit:

- `git diff --check`: passed.
- Required docs/mirrors check: `missing=0`.
- Baseline-aware changed-file scope guard: `out_of_scope=0`.
- Forbidden implementation surface sentinel: no output for
  `backend/worldengine`, frontend, alembic, or migrations.
- Focused v0.5 memory/loop/action compatibility: `33 passed`.
- Full backend regression: `145 passed`.
- Evidence/compatibility evaluator: PASS, no P1/P2/P3 findings.

## Review Questions

- Does the bundle keep WorldEngine generic?
- Are all v0.5 implementation changes additive?
- Are deferred capabilities clearly not implemented?
- Is current evidence sufficient for final closeout review?
- Are there any unresolved P1/P2 findings?

## Final Closeout Gate

`0.5.7` must run final consistency and verification checks before v0.5 may be
marked final.
