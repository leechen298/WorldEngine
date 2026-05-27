# v0.3 Evidence Index

Status: ready for review

## Purpose

This index maps v0.3 package evidence to the compatibility surfaces required
before release-candidate review. It records what is supported by current
package evidence, what is documentation-only, and what remains a handoff risk.

## Evidence Matrix

| Package | Type | Status | Evidence source | Key commands / results | Compatibility coverage | Findings |
|---|---|---|---|---|---|---|
| 0.3.0 planning baseline | documentation-only | review complete | `0.3.0.../review.md` | `git diff --check`; file/status/wording checks | Version boundary, v0.3 package sequence, compatibility baseline | No P1/P2/P3 recorded |
| 0.3.1 loader contract | documentation-only | review complete | `0.3.1.../review.md` | `git diff --check`; contract/status/scope checks | Loader input, output, error, validation, runtime separation | No unresolved P1/P2/P3 |
| 0.3.2 loader implementation | mixed or code | review complete | `0.3.2.../review.md` | Backend venv `python -m pytest` loader and schema smoke checks passed; root `pytest` forms failed due environment/import path | Pure WorldSpec loader, schema validation, no runtime/API coupling | P3: direct root pytest forms are not reliable in this environment |
| 0.3.3 bridge contract | documentation-only | review complete | `0.3.3.../review.md` | `git diff --check`; contract/status/compatibility checks | Runtime context semantics, compatibility evidence requirements, RuntimeEngine boundary | No P1/P2/P3 recorded |
| 0.3.4 bridge implementation | mixed or code | review complete | `0.3.4.../review.md` | Backend venv `python -m pytest` bridge, runtime step, event, params, archive, loader, and schema smoke checks passed | Optional inert runtime context, runtime/API/event/params/archive compatibility | No implementation P1/P2/P3 recorded |
| 0.3.5 external fixture readiness | documentation-only | review complete | `0.3.5.../review.md` | `git diff --check`; contract/redaction/status/scope checks | Public external fixture runner boundary and redacted report expectations | P3: public CLI/API docs and stricter report schema may be needed later |

## Compatibility Surface Index

| Surface | Classification | Evidence |
|---|---|---|
| WorldSpec loader | changed with evidence | 0.3.2 implemented `backend/app/core/worldspec_loader.py`; focused loader tests passed through backend venv. |
| Runtime context bridge | changed with evidence | 0.3.4 implemented `backend/app/core/runtime_context.py` and optional inert `RuntimeEngine` storage; focused bridge tests passed. |
| Runtime tick and `world_time_seconds` | unchanged with evidence | 0.3.4 runtime step tests passed. |
| API envelope and response shape | unchanged with partial evidence | 0.3.4 event compatibility tests passed; no new API route was added by loader or bridge work. |
| `/runtime/step` or runtime step behavior | unchanged with evidence | 0.3.4 runtime step tests passed. |
| `/world/events` | unchanged with evidence | 0.3.4 event API compatibility tests passed. |
| `/world/event-steps` | unchanged with evidence | 0.3.4 event API compatibility tests passed. |
| Optional `Event.refs` compatibility | unchanged with evidence | 0.3.4 event schema compatibility tests passed. |
| World params and params apply behavior | unchanged with evidence | 0.3.4 world params and params agent tests passed. |
| Archive snapshot and summary behavior | unchanged with evidence | 0.3.4 archive snapshot summary tests passed. |
| Frontend-facing response shapes | not touched | No frontend files changed in 0.3 loader or bridge implementation packages. Backend compatibility tests cover the currently tested response surfaces. |
| Schema compatibility | unchanged with evidence | 0.3.2 and 0.3.4 schema smoke tests passed; no schema files were modified by 0.3.6. |
| Fixture boundary | documentation-only evidence | 0.3.5 defines public runner and redacted report boundary without adding fixture data. |
| Legacy `backend/worldengine/` boundary | not touched | Package reviews record no changes under the legacy path. |

## Assumptions

- Prior package review files are accurate records of the commands run in those
  implementation or documentation sessions.
- The backend venv `python -m pytest` invocation is the reliable pytest pattern
  for v0.3 evidence because direct root `pytest` invocations failed in 0.3.2.
- Frontend-facing compatibility can be treated as not touched for this audit
  because v0.3 loader and bridge packages did not modify frontend files or add
  new API exposure.

## Open Risks

- P3: Frontend-facing response shape evidence is indirect unless a later
  release-candidate package runs broader backend or frontend smoke coverage.
- P3: External fixture reports may need a machine-readable schema before
  automation can consume them consistently.
- P3: Public CLI/API documentation may need expansion for external runners
  before v0.7 validation readiness.

## Handoff Readiness

v0.3 evidence supports release-candidate preparation with no known P1 or P2
blockers in the package reviews. v0.4 may use the loader and inert runtime
context bridge as foundations only after the v0.3 release-candidate and
closeout gates complete.
