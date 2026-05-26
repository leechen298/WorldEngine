# Contract

## Public Concepts

- Evidence index: a milestone-level document that maps active v0.2 claims to
  source documents, package reviews, verification commands, and status.
- Boundary audit: a milestone-level document that checks external consumer,
  concrete fixture, legacy directory, runtime compatibility, and future-scope
  boundaries.
- Evidence status: one of `implemented`, `documented`, `tested`, `reviewed`,
  `planned`, `not implemented`, `historical artifact`, or `finding`.
- Finding: an unresolved evidence, boundary, compatibility, or status issue
  recorded with priority and target package.

## Compatibility Constraints

- Runtime behavior must not change.
- Schema behavior and validation behavior must not change.
- API response shapes must not change.
- Frontend behavior must not change.
- Fixture, migration, and test implementation files must not change.
- `backend/app/` remains the active backend code path.
- `backend/worldengine/` remains legacy unless a later reviewed package
  changes that boundary.
- Documentation must distinguish implemented behavior from planned or
  future-scope claims.

## Allowed Changes

- Add `docs/iterations/v0.2/evidence-index.md`.
- Add `docs/iterations/v0.2/evidence-index.zh.md`.
- Add `docs/iterations/v0.2/boundary-audit.md`.
- Add `docs/iterations/v0.2/boundary-audit.zh.md`.
- Update `docs/iterations/v0.2/findings.md` to add, close, or retarget audit
  findings.
- Update this package's `review.md` and `review.zh.md` with audit evidence.
- Update v0.2 milestone index and plan status fields for 0.2.9.
- Run read-only repository searches, path checks, and documentation sanity
  checks.

## Forbidden Changes

- Do not modify runtime services, world state, modules, event log behavior,
  archive behavior, agent behavior, persistence, API routes, or app assembly.
- Do not modify schema implementation files.
- Do not modify frontend files.
- Do not modify tests or fixtures.
- Do not add migrations.
- Do not modify `backend/worldengine/`.
- Do not implement WorldSpec loading, runtime bridge, generation, projection,
  agent loop, memory, self-continuity, resolver, or causality behavior.
- Do not add external repositories or external validation internals.
- Do not add concrete external-world names, characters, locations, roles,
  resources, story rules, seed data, UI selectors, private runner state, or
  application-specific backend logic.
- Do not claim tests or runtime behavior passed unless the command is run in
  the current session.

## Acceptance Requirements

- `docs/iterations/v0.2/evidence-index.md` and `.zh.md` exist and map active
  v0.2 claims to evidence or explicitly mark them as planned, not implemented,
  historical, or finding.
- `docs/iterations/v0.2/boundary-audit.md` and `.zh.md` exist and cover
  external consumer boundaries, concrete fixture boundaries, legacy directory
  boundaries, runtime/schema/event boundaries, future-scope boundaries, and
  status drift.
- The deferred 0.2.7 plan/index status mismatch is either closed with evidence
  or remains visible in `findings.md` with a clear reason.
- The audit cites completed package review files for implemented/tested claims
  and does not promote unreviewed plans into evidence.
- Concrete demo anchor sweep results are recorded without storing concrete
  pattern lists in tracked docs.
- Documentation checks pass.
- Changed files are limited to approved documentation paths.

## North Star Check

This package audits whether v0.2 remains a generic recursive-world foundation.
It does not introduce concrete worlds, product-specific backend logic,
application-specific fixtures, or future runtime behavior.

## Out-of-Scope Follow-ups

- 0.2.10 reviews v0.1 runtime scaffold compatibility and legacy boundaries.
- 0.2.11 prepares the release-candidate bundle.
- v0.3 may design and implement WorldSpec loader and runtime bridge work only
  after v0.2 closeout.
