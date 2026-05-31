# Technical Design

Status: review complete

## Design

The release-candidate bundle is a documentation index, not a new runtime
artifact. It consolidates reviewed evidence into four sections:

1. package readiness table;
2. release-candidate claim boundary;
3. unresolved finding classification;
4. final-closeout handoff checklist.

## Package Readiness Table

| Package | Status Used By RC | Evidence Included |
| --- | --- | --- |
| `0.6.0` | review complete | campaign boundary and generation scope baseline |
| `0.6.1` | review complete | public generation contracts and template semantics |
| `0.6.2` | review complete | deterministic template catalog generator and backend tests |
| `0.6.3` | review complete | structured generation plan compiler and backend tests |
| `0.6.4` | review complete | AI-assisted boundary and plan import tests |
| `0.6.5` | review complete | validation metadata and preview API tests |
| `0.6.6` | review complete | regeneration and runtime-readiness API tests |
| `0.6.7` | review complete | dashboard preview, frontend unit/build, E2E, browser smoke |
| `0.6.8` | review complete | evidence and compatibility audit with evaluator PASS |

## Claim Boundary

| Surface | Release Candidate Position |
| --- | --- |
| Backend generation schemas/core | Included as reviewed v0.6 implementation evidence. |
| Preview/regeneration/readiness API | Included as reviewed API evidence. |
| Dashboard generation preview | Included as focused UI/E2E smoke evidence. |
| Loader/runtime-context readiness | Included only for the boundary checked in `0.6.6`. |
| External validation worlds | Excluded; no readiness claim. |
| Projection application | Excluded; no readiness claim. |
| Agent smoke/autonomous runner | Excluded; no pass claim. |
| Generation quality | Excluded; validity and quality remain separate. |
| Product readiness | Excluded; release candidate is not a whole-product PASS. |
| Final release | Excluded until `0.6.10` completes. |

## Handoff Checklist

The handoff to `0.6.10` should include:

- the release-candidate status and checklist result;
- confirmation that no P1/P2 finding is unresolved;
- the exact current-session evidence counts inherited from reviewed child
  packages;
- explicit not-run/out-of-scope surfaces;
- a requirement to rerun final closeout checks defined by `0.6.10` before
  marking v0.6 final.
