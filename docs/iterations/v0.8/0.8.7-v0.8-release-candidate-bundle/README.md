# 0.8.7 v0.8 Release Candidate Bundle

Status: review complete
Type: documentation-only release-candidate package
implementation_authorized: no
evidence_execution_authorized: no
audit_execution_authorized: no
release_candidate_authorized: yes, limited to bounded release-candidate bundle
approval and handoff to final-closeout review

## Purpose

This package prepares a bounded v0.8 release-candidate bundle from reviewed
v0.8 package evidence. It gives reviewers one evidence surface before final
closeout while keeping final v0.8 release and readiness claims explicitly out
of scope.

The bundle is a documentation artifact. It does not implement runtime,
schema, API, frontend, backend tests, checker behavior, fixtures, migrations,
external repositories, external validator behavior, external application
behavior, generated results, deployment behavior, or `backend/worldengine/`
changes.

## Inputs

Required inputs:

- v0.8 parent docs and route state.
- `0.8.6-v0.8-evidence-and-boundary-audit/audit-report.md`.
- `0.8.6-v0.8-evidence-and-boundary-audit/review.md`.
- Reviewed `0.8.0` through `0.8.5` package reviews.
- Testing result docs and contract artifacts referenced by the audit report.

## Deliverables

- Complete package docs and Chinese mirrors.
- `release-candidate-summary.md` and `release-candidate-summary.zh.md`.
- Evidence reference table with bounded claim mapping.
- Explicit unresolved finding and exclusion list.
- Review gate for whether the package may hand off to
  `0.8.8-v0.8-final-closeout`.

## Review Gate

Read-only documentation/contract review passed with no P1/P2/P3 findings. The
release-candidate bundle is approved only for handoff to
`0.8.8-v0.8-final-closeout` document-package creation and review.

This approval does not authorize implementation, evidence execution, audit
execution, external validation, final closeout, final v0.8 release, product
readiness, external validation PASS, external consumer PASS, frontend/E2E
PASS, Agent smoke PASS, autonomous PASS, generation-quality PASS, or final
v0.8 readiness.
