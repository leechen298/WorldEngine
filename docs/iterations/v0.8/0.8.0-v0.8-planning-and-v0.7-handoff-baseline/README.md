# 0.8.0 Planning And v0.7 Handoff Baseline

Status: review complete
Type: documentation-only
implementation_authorized: no
evidence_execution_authorized: no

## Goal

Convert the v0.8 parent roadmap entry for `0.8.0` into a concrete
documentation-only child package that safely hands reviewed campaign
structure, current v0.7 handoff status, minimum working-state boundaries, and
external-validation boundaries to `0.8.1-minimum-working-state-contract`.

This package keeps implementation and evidence execution closed. It prepares
the goal campaign route; it does not implement contracts, schemas, APIs,
checkers, frontend behavior, fixtures, migrations, external validation
functions, or external applications.

## Scope

Allowed scope:

- Create this child package document set and Chinese mirrors.
- Synchronize parent v0.8 route/status surfaces after parent review.
- Record current v0.7 handoff as historical context only.
- Replace stale v0.7 post-closeout blocker wording with the current `0.7.9`
  checker/docs repair status while preserving v0.8 non-claims.
- Define the boundary between `0.8.0` documentation baseline work and later
  `0.8.1` minimum working-state contract work.
- Record documentation checks, subagent/evaluator evidence, compatibility
  review, scope review, and unresolved findings.

Forbidden scope:

- Do not modify runtime, schema, API, frontend, backend test, checker
  implementation, fixture, migration, external repository, generated result,
  or `backend/worldengine/` implementation files.
- Do not implement minimum working-state contracts, observable surfaces,
  schemas, checkers, services, APIs, UI, persistence, external validation
  behavior, projection application behavior, or tests.
- Do not add concrete external validation world data, concrete world names,
  maps, characters, locations, resources, story rules, seed data, private
  transcripts, UI selectors, private repository paths, hidden reset APIs,
  live provider behavior, or application-specific backend logic.
- Do not claim current v0.8 runtime, API, frontend, E2E, Agent smoke,
  autonomous, external validation, external consumer, product readiness,
  minimum working-state readiness, or final release behavior passed.

## Deliverables

- `README.md`
- `intent.md`
- `contract.md`
- `technical-design.md`
- `test-plan.md`
- `plan.md`
- `review.md`
- Chinese mirrors for each package document.
- Parent route/status synchronization for the active child selection.

## Status Checklist

- [x] Package documents drafted.
- [x] Chinese mirrors drafted.
- [x] Documentation checks complete.
- [x] Subagent/evaluator review complete.
- [x] Review evidence updated.
- [x] Handoff to `0.8.1` recorded.

## Final Assessment State

Current value: `review complete`.

This package is review complete and hands off reviewed campaign structure,
current v0.7 checker/docs clean-pass handoff context, minimum working-state
boundaries, external-validation boundaries, and implementation-closed status to
`0.8.1-minimum-working-state-contract`.
