# v0.3 Compatibility Audit

Status: ready for review

## Audit Scope

This audit covers the v0.3 loader, runtime context bridge, external fixture
readiness, and compatibility evidence accumulated through package 0.3.5. It is
documentation-only and does not patch loader or bridge behavior.

## Acceptance Questions

| Question | Result | Evidence |
|---|---|---|
| Can generic WorldSpec data be loaded and validated? | Yes, with focused evidence | 0.3.2 loader implementation and tests. |
| Can validated loaded data become optional runtime context? | Yes, as inert context | 0.3.4 bridge implementation and tests. |
| Does the bridge preserve v0.1 runtime compatibility? | Yes, for tested surfaces | 0.3.4 runtime step, event, params, archive, loader, and schema smoke tests. |
| Are external fixtures kept outside core? | Yes, by contract | 0.3.5 external fixture runner contract and review. |
| Is v0.4 handoff ready? | Conditionally ready for planning | No P1/P2 blockers are identified; v0.4 must still start through its own reviewed package. |

## Compatibility Classifications

- Runtime: unchanged with evidence. The runtime context is optional and inert;
  0.3.4 tests show existing step behavior still passes.
- API: unchanged with partial evidence. No loader or bridge API exposure was
  added; event API compatibility tests passed.
- Event: unchanged with evidence. Event API and schema compatibility tests
  passed, including optional refs coverage.
- Archive: unchanged with evidence. Archive snapshot summary tests passed.
- Params: unchanged with evidence. World params and params agent tests passed.
- Schema: unchanged with evidence. WorldSpec schema smoke tests passed; no
  schema files changed in 0.3.6.
- Frontend-facing behavior: not touched. No frontend files changed; broader UI
  smoke was not run for this audit.
- Fixture boundary: documented. External fixtures remain public consumers and
  no concrete fixture data was added.
- Legacy path: not touched. Reviews record no `backend/worldengine/` changes.

## Findings

- P1: none identified.
- P2: none identified.
- P3: Direct root-level `pytest` commands are unreliable in this repository
  environment based on 0.3.2 evidence; future package test plans should use
  backend venv `python -m pytest` from `backend/`.
- P3: Frontend-facing compatibility is currently inferred from no frontend
  changes and backend response tests; release-candidate review may choose to
  run broader UI or E2E smoke if that surface is considered release-critical.
- P3: External fixture reports and public runner invocation may need stricter
  machine-readable detail in a later version.

## Assumptions

- Review evidence from 0.3.2 and 0.3.4 is current enough for this audit because
  this package does not change implementation files.
- The compatibility baseline from 0.3.0 remains the correct surface list for
  v0.3 release-candidate preparation.
- "Ready for v0.4 handoff" means ready to inform v0.4 planning, not permission
  to start Agent-in-World implementation inside v0.3.

## Verification Requirements for Release Candidate

The 0.3.7 release-candidate package should trace each release claim back to
this audit and `evidence-index.md`. If release-candidate review needs fresh
runtime evidence, it should run the backend venv pytest commands recorded in
0.3.4 before claiming compatibility still passes.

## Final Assessment

The audit is ready for review. No P1 or P2 compatibility blocker is identified
from recorded v0.3 evidence. v0.3 may proceed to release-candidate bundle
preparation after this documentation package is reviewed.
