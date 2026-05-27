# Contract

## Public Concepts

- Release-candidate bundle: a review packet that summarizes v0.3 evidence and
  limitations without declaring final release.
- Final review bundle: the human / ChatGPT handoff document generated from
  the release-candidate evidence.
- Release-candidate claim: a v0.3 capability, boundary, or compatibility
  statement that must map to existing review evidence, audit evidence, or a
  visible limitation state.
- Evidence source: a completed package review, package contract, evidence
  index, compatibility audit, findings table, release placeholder, or command
  run during 0.3.7.
- Blocking finding: an unresolved P1/P2 issue that prevents final closeout
  unless resolved or explicitly accepted by review.

## Compatibility Constraints

- Runtime behavior must not change.
- Schema behavior and validation behavior must not change.
- API route behavior and response shapes must not change.
- Event storage, event pagination, archive, params, and frontend-facing
  behavior must not change.
- Fixture, migration, and test implementation files must not change.
- Legacy `backend/worldengine/` behavior must not change.
- Release-candidate docs must not claim final release status.
- Claims must distinguish planned, documented, implemented, tested, not
  implemented, partial, historical, and finding states.
- Unresolved P1/P2 findings must remain visible and block 0.3.8 final
  closeout until resolved or explicitly accepted.

## Allowed Changes

- Create `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/**`.
- Add `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`.
- Add `docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md`.
- Add final-review bundle docs in this package directory.
- Update this package's `review.md` and `review.zh.md` with documentation
  verification evidence.
- Update v0.3 milestone index and v0.3 plan status fields for 0.3.7.
- Record findings in `docs/iterations/v0.3/findings.md` only if
  release-candidate assembly discovers a new or changed P1/P2/P3 issue.
- Run read-only repository searches, file checks, release-status wording
  checks, evidence traceability checks, and documentation sanity checks.

## Forbidden Changes

- Do not modify runtime services, schemas, API routes, event log behavior,
  archive behavior, params behavior, frontend behavior, agent behavior,
  persistence, or app assembly.
- Do not modify tests, fixtures, migrations, or `backend/worldengine/`.
- Do not implement loader, bridge, Agent-in-World, memory, self-continuity,
  generation, projection, external validation, product UI, game UI, resolver,
  or causality behavior.
- Do not create external repositories or add external validation internals.
- Do not add concrete world names, maps, characters, locations, roles,
  resources, story rules, seed data, UI selectors, private runner state, or
  application-specific backend logic.
- Do not claim tests, builds, runtime behavior, API behavior, or frontend
  behavior passed unless the command or flow is run in the current session.
- Do not mark v0.3 final or 0.3.8 complete.

## Acceptance Requirements

- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md` and `.zh.md` exist
  and summarize scope, package status, evidence, compatibility, limitations,
  assumptions, unresolved findings, and final-closeout prerequisites.
- `final-review-bundle.md` and `.zh.md` exist in this package directory and
  follow the final-review bundle template structure.
- Each release-candidate claim maps to a concrete evidence source or is marked
  as planned, not implemented, partial, historical, or finding.
- P1/P2/P3 findings are listed explicitly, including whether each blocks final
  closeout.
- Release-status wording checks confirm that final release is not claimed.
- Concrete demo anchor sweep passes or any residuals are classified as
  historical/review-only/false-positive.
- Changed files are limited to approved documentation paths.
- English and Chinese mirrors are synchronized for package docs, bundle docs,
  final-review docs, and status updates.

## North Star Check

This package protects WorldEngine as a generic recursive world engine by
making v0.3 loader and runtime-bridge evidence reviewable while preserving
future agent, memory, generation, and projection boundaries.

## Out-of-Scope Follow-ups

- 0.3.8 may perform final closeout only after 0.3.7 release-candidate review
  approval.
- v0.4 planning may use v0.3 evidence only after the v0.3 closeout gate.
- Fresh runtime, API, frontend, E2E, or build verification belongs in review
  only if explicitly run during this package; otherwise historical evidence
  must remain labeled as historical.
