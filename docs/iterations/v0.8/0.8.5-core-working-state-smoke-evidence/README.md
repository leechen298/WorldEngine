# 0.8.5 Core Working State Smoke Evidence

Status: review complete
Type: mixed validation package
implementation_authorized: no
evidence_execution_authorized: yes, limited to exact commands in `test-plan.md`

## Purpose

This package defines the core-side smoke evidence that v0.8 must run before
later packages can discuss minimum working-state readiness. It does not run or
implement an external validator, and it does not make product-readiness or
external-validation PASS claims.

The package prepares evidence for these public core surfaces:

```text
WorldSpec schema and loader
  -> generation preview/regeneration/runtime-readiness
  -> core-readiness probe
  -> runtime step and event evidence
  -> Agent loop perception/action evidence
  -> memory-context and archive compatibility
  -> handoff status classification
```

## Current State

Current reviewed inputs include:

- `0.8.1` minimum working-state taxonomy.
- `0.8.2` observable surface boundaries.
- `0.8.3` core-readiness route and focused backend/API evidence.
- `0.8.4` external-validation handoff contract.
- v0.7 `0.7.9` checker/docs repair evidence as handoff context only.

`0.8.5` must convert those inputs into a current-session command matrix for
core-side evidence. It must explicitly classify any skipped, blocked, or
out-of-scope surface.

## Evidence Scope

In-scope after review:

- focused backend/API/schema tests for generation, runtime context, runtime
  step, Agent loop, memory context, archive, and core-readiness surfaces.
- focused public contract/checker commands if they are repository-local and
  needed to confirm v0.7 handoff compatibility.
- changed-file and artifact scope guards.
- redaction and overclaim scans.
- optional documentation result artifacts under `docs/testing/results/` only
  if the reviewed test plan authorizes them.

Out of scope unless a later reviewed package authorizes it:

- external validator execution.
- external app or projection app execution.
- product-specific scenarios or acceptance targets.
- frontend feature changes.
- runtime/API behavior changes.
- checker/schema/template implementation changes.
- fixture or migration changes.
- `backend/worldengine/` work.

## Review Gate

Read-only documentation/contract review passed with no P1/P2/P3 findings.
`review.md` records bounded `evidence_execution_authorized: yes` for the exact
commands in `test-plan.md`, and those commands passed within their bounded
proof surfaces. Validation-evidence review passed with no blocking findings.
Implementation remains unauthorized.
