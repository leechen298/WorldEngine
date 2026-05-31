# Contract

Status: review complete

## Package Decision

`0.5.6` is documentation-only. It prepares a release-candidate bundle for
review, but it does not declare final release.

Implementation authorization remains `no`.

## Included v0.5 Capabilities

- working memory schema semantics and additive backend record model.
- episodic memory schema semantics and additive backend record model.
- process-local generic in-memory agent memory substrate.
- bounded read-only memory context in Agent Loop perception.
- refined contracts for relationship state, self-summary, reflection records,
  and personality drift signals, with implementation deferred.

## Deferred Scope

- durable persistence.
- public memory APIs.
- vector retrieval or indexing.
- self-summary generation.
- automatic reflection.
- relationship behavior.
- personality drift action modifiers.
- world generation.
- external validation readiness and report automation.
- projection application readiness.
- frontend product behavior.

## Evidence Included

The bundle includes `0.5.5` audit evidence:

- focused v0.5 memory/loop/action compatibility: `33 passed`.
- full backend regression: `145 passed`.
- docs/mirror checks: `missing=0`.
- changed-file scope guard: `out_of_scope=0`.
- forbidden implementation surface sentinel: no output.
- evidence/compatibility evaluator PASS with no P1/P2/P3 findings.

## Reviewer Checklist

Reviewers should confirm:

- all child packages `0.5.1` through `0.5.5` are review complete.
- implementation-bearing packages have authorization and required evaluators.
- included capabilities do not exceed the v0.5 scope.
- deferred capabilities are not accidentally implemented.
- current evidence is v0.5 evidence, not v0.4 handoff evidence.
- no unresolved P1/P2 remains.
- final release is not declared in this package.

## Final Closeout Prerequisites

`0.5.7` must still:

- re-check parent and child status consistency.
- run final docs/mirror/scope checks.
- run the required final verification matrix.
- run closeout consistency evaluator.
- update final status only after evidence consistency passes.

## Allowed Changes

- Package docs and mirrors under this directory.
- Parent v0.5 status/review surfaces for accurate handoff only.

## Forbidden Changes

- No implementation file changes.
- No final release declaration.
- No `final / closeout complete` status.
- No release tag or push.
- No `backend/worldengine/**`, frontend, migration, fixture, or external
  repository changes.
