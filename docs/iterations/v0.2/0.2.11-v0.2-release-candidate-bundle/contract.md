# Contract

## Public Concepts

- Release-candidate bundle: a review packet that summarizes v0.2 evidence and
  limitations without declaring final release.
- Final review bundle: the ChatGPT / human review handoff document generated
  from the release-candidate evidence.
- Release-candidate claim: a v0.2 capability or boundary statement that must
  map to existing documentation, tests, package review evidence, or a visible
  limitation.
- Evidence source: a completed package review, contract, audit, compatibility
  review, boundary document, release draft, or command run during 0.2.11.
- Blocking finding: an unresolved P1/P2 issue that prevents final closeout
  unless resolved or explicitly accepted by review.

## Compatibility Constraints

- Runtime behavior must not change.
- Schema behavior and validation behavior must not change.
- Event storage, event pagination, and API response behavior must not change.
- Frontend behavior must not change.
- Fixture, migration, and test implementation files must not change.
- Release-candidate docs must not claim final release status.
- Release-candidate claims must distinguish implemented, documented, tested,
  reviewed, planned, not implemented, historical, and finding states.
- Unresolved P1/P2 findings must remain visible and must block 0.2.12 final
  closeout until resolved or explicitly accepted.

## Allowed Changes

- Add `docs/iterations/v0.2/v0.2-release-candidate-bundle.md`.
- Add `docs/iterations/v0.2/v0.2-release-candidate-bundle.zh.md`.
- Add `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.md`.
- Add `docs/iterations/v0.2/0.2.11-v0.2-release-candidate-bundle/final-review-bundle.zh.md`.
- Update `docs/releases/v0.2.md` with release-candidate evidence and
  limitations.
- Update `docs/releases/v0.2.zh.md` with synchronized Chinese mirror content.
- Update `docs/iterations/v0.2/findings.md` if release-candidate assembly
  discovers, closes, or retargets findings.
- Update this package's `review.md` and `review.zh.md` with evidence.
- Update v0.2 milestone index and plan status fields for 0.2.11.
- Run read-only repository searches, path checks, release-status wording
  checks, and documentation sanity checks.

## Forbidden Changes

- Do not modify runtime services, modules, event log behavior, archive
  behavior, agent behavior, persistence, API routes, app assembly, or frontend
  behavior.
- Do not modify schema implementation files.
- Do not modify tests or fixtures.
- Do not add migrations.
- Do not modify `backend/worldengine/`.
- Do not implement WorldSpec loading, RuntimeEngine-to-WorldCell migration,
  runtime bridge, generation, projection, agent loop, memory,
  self-continuity, resolver, or causality behavior.
- Do not create external repositories or add external validation internals.
- Do not add concrete external-world names, characters, locations, roles,
  resources, story rules, seed data, UI selectors, private runner state, or
  application-specific backend logic.
- Do not claim tests, builds, runtime behavior, API behavior, or frontend
  behavior passed unless the command or flow is run in the current session.
- Do not mark v0.2 final or 0.2.12 ready without human / ChatGPT approval.

## Acceptance Requirements

- `docs/iterations/v0.2/v0.2-release-candidate-bundle.md` and `.zh.md` exist
  and summarize v0.2 scope, completed packages, evidence, limitations,
  unresolved findings, compatibility status, and final-closeout prerequisites.
- `final-review-bundle.md` and `.zh.md` exist in this package directory and
  follow the final review bundle template structure.
- `docs/releases/v0.2.md` and `.zh.md` are updated from draft/planned wording
  to release-candidate wording without declaring final release.
- Each release-candidate claim maps to a concrete evidence source or is
  marked as planned, not implemented, historical, or finding.
- P1/P2/P3 findings are listed explicitly, including whether each blocks
  final closeout.
- Release-status wording checks confirm that final release is not claimed.
- Concrete demo anchor sweep passes or any residuals are classified as
  historical/review-only.
- Changed files are limited to approved documentation paths.
- English and Chinese mirrors are synchronized for package docs, bundle docs,
  final-review docs, and release docs.

## North Star Check

This package protects WorldEngine as a generic recursive world engine by
making v0.2 evidence reviewable while preserving future scope boundaries. It
does not introduce concrete worlds, product-specific backend logic,
application-specific fixtures, or runtime behavior.

## Out-of-Scope Follow-ups

- 0.2.12 may perform final closeout only after the 0.2.11 release-candidate
  bundle passes review.
- v0.3 may design and implement WorldSpec loader and runtime bridge work only
  after v0.2 closeout and a separate reviewed package contract.
- Future runtime, API, frontend, E2E, or compatibility regression evidence
  belongs in the first relevant code or mixed package, not in this
  documentation-only release-candidate bundle unless the command is explicitly
  run as read-only verification.
