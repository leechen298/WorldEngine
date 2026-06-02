# Contract

## Public Concepts

- `EvidenceReference`: a path, command result, or package review entry used as
  proof for a bounded v0.8 claim.
- `AuditFinding`: a P1/P2/P3 issue found while checking evidence, boundaries,
  compatibility, status, or redaction.
- `AuditDisposition`: one of `clear`, `blocked`, `carry_forward_p3`,
  `out_of_scope`, or `not_claimed`.
- `ReleaseCandidateRecommendation`: one of `recommended`, `blocked`, or
  `defer_pending_review`.

## Allowed Changes

Documentation stage:

- Create or update this package's docs and Chinese mirrors.
- Create an audit report template under this package.
- Update parent v0.8 status surfaces to ready-for-review.

Audit stage after review:

- Fill `audit-report.md` and `audit-report.zh.md`.
- Update this package `review.md` and mirrors with command results, findings,
  and release-candidate recommendation.
- Update parent route only if package review authorizes closeout.

## Forbidden Changes

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, generated result, external repository,
  external validator, external application, deployment, or `backend/worldengine/`
  files.
- Do not repair code inside this package.
- Do not add new evidence commands that are not documentation/audit checks.
- Do not hide unresolved P1/P2 findings.
- Do not convert skipped, blocked, out-of-scope, stale, or historical evidence
  into PASS.
- Do not claim external validation PASS, external consumer PASS, product
  readiness, frontend/E2E PASS, Agent smoke PASS, autonomous PASS,
  generation-quality PASS, or final v0.8 readiness.

## Required Audit Surfaces

The audit must cover:

- `0.8.0` through `0.8.5` package status and review evidence.
- v0.7 blocker and `0.7.9` checker/docs repair handoff boundaries.
- v0.3 loader/runtime bridge, v0.4 Agent loop, v0.5 memory, v0.6 generation,
  and v0.7 public contract compatibility references.
- `0.8.5` skipped/out-of-scope classifications.
- redaction and private-detail exclusions.
- parent route/status synchronization.

## Closeout Rule

This package may recommend `0.8.7-v0.8-release-candidate-bundle` only if no
unresolved P1 or blocking P2 remains. P3 may be carried forward only when the
audit report names the issue and explains why it does not block
release-candidate packaging.
