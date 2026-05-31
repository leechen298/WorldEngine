# Technical Design

Status: final / closeout complete

## Closeout Model

Final closeout has three phases:

1. prepare closeout records while status remains `ready for review`;
2. run final verification and evaluator review;
3. synchronize parent and roadmap status to `final / closeout complete` only
   after the gate passes.

## Final Evidence Matrix

| Surface | Required Final Evidence | Claim Boundary |
| --- | --- | --- |
| Documentation and mirrors | required-docs check `missing=0` | v0.6 docs complete |
| Changed-file scope | cumulative scope guard `out_of_scope=0` | only reviewed v0.6 surfaces |
| Backend | full backend regression | reviewed generation/runtime/API backend surfaces |
| Frontend | frontend unit test and build | dashboard generation preview only |
| E2E | `make test-e2e` | focused dashboard/runtime smoke including generation preview |
| Status | status consistency checks | all current surfaces agree |

## Deferred Scope Matrix

| Surface | Final Closeout Position |
| --- | --- |
| External validation readiness | deferred to v0.7 |
| Projection readiness | deferred to v0.8 |
| Product readiness | not claimed by v0.6 closeout |
| Agent smoke/autonomous | not claimed unless explicitly run, expected out of scope |
| Generation quality | not claimed; validity and quality remain separate |
| Concrete content | forbidden in core repository |

## Status Synchronization

If final gate passes, update:

- v0.6 parent status files to `final / closeout complete`;
- `0.6.10` package docs and final-closeout record to final status;
- roadmap status entries for v0.6 only if they do not imply v0.7/v0.8
  completion.
