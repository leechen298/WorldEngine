# Contract

Status: final / closeout complete

## Package Decision

`0.5.7` is documentation-only final closeout. It may update final status only
after final verification and closeout consistency evaluator approval.

Implementation authorization remains `no`.

## Closeout Criteria

v0.5 may be marked `final / closeout complete` only if:

- child packages `0.5.1` through `0.5.6` are review complete.
- final docs/mirror checks pass.
- final changed-file scope guard passes.
- final forbidden-surface sentinel passes.
- final focused backend compatibility passes.
- final full backend regression passes.
- final unresolved finding classification has no P1/P2.
- closeout consistency evaluator passes.

## Final Included Capability

v0.5 closes with:

- working-memory and episodic-memory contracts.
- additive backend memory schemas.
- generic in-memory memory substrate.
- bounded read-only memory context in Agent Loop perception.
- refined deferred contracts for relationship state, self-summary, reflection
  records, and personality drift signals.
- release-candidate bundle reviewed before final closeout.

## Final Excluded Capability

v0.5 does not close with:

- durable persistence.
- public memory APIs.
- vector retrieval or indexing.
- self-summary generation.
- automatic reflection.
- relationship behavior.
- personality drift action modifiers.
- frontend product behavior.
- world generation.
- external validation readiness or report automation.
- projection application readiness.

## Final Verification Matrix

Required final commands:

- `git diff --check`
- required docs/mirrors check for v0.5 parent and child packages.
- baseline-aware changed-file scope guard.
- forbidden-surface sentinel for `backend/worldengine`, frontend, alembic, and
  migrations.
- focused v0.5 memory/loop/action backend compatibility.
- full backend regression.

## Status Surfaces

After evaluator approval, synchronize:

- `docs/iterations/v0.5/CURRENT_STATE.md`
- `docs/iterations/v0.5/CURRENT_STATE.zh.md`
- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/v0.5-plan.md`
- `docs/iterations/v0.5/v0.5-plan.zh.md`
- `docs/iterations/v0.5/review.md`
- `docs/iterations/v0.5/review.zh.md`
- `docs/roadmap.md`
- `docs/roadmap.zh.md`

## Allowed Changes

- Final closeout docs and mirrors under this package.
- Parent v0.5 status surfaces.
- Roadmap status lines for v0.5 final handoff.

## Forbidden Changes

- No implementation file changes.
- No `backend/worldengine/**`, frontend, migration, fixture, generated result,
  external repository, release tag, or push changes.
- No unrun validation claims.
