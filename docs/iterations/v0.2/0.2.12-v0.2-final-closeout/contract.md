# Contract

## Public Concepts

- Final closeout: the documentation-only act of marking v0.2 final after the
  release-candidate bundle is accepted and blockers are cleared or explicitly
  classified.
- Final review decision: the human / ChatGPT approval, rejection, or conditional
  acceptance that determines whether final closeout may proceed.
- Blocking finding: an unresolved P1/P2 issue that prevents final closeout.
- Accepted handoff: a non-blocking finding, currently expected to be P3 only,
  that is retained for v0.3 or later work with explicit closeout wording.
- Historical evidence: commands and test results recorded by earlier package
  reviews, distinct from commands run during 0.2.12.

## Compatibility Constraints

- Runtime behavior must not change.
- Schema behavior and validation behavior must not change.
- Event storage, event pagination, archive behavior, grouping behavior, and API
  response behavior must not change.
- Frontend behavior must not change.
- Fixture, migration, and test implementation files must not change.
- `backend/worldengine/` must remain untouched.
- Final release status may be claimed only after approval and only if no
  unresolved P1/P2 findings remain.
- Final closeout wording must distinguish historical package evidence from
  current-session 0.2.12 verification.

## Allowed Changes

- Add or update files under
  `docs/iterations/v0.2/0.2.12-v0.2-final-closeout/`.
- Update `docs/releases/v0.2.md` and `docs/releases/v0.2.zh.md` after review
  approval.
- Update `docs/iterations/v0.2/README.md` and
  `docs/iterations/v0.2/README.zh.md`.
- Update `docs/iterations/v0.2/v0.2-plan.md` and
  `docs/iterations/v0.2/v0.2-plan.zh.md`.
- Update `docs/iterations/v0.2/findings.md` if final review changes finding
  status, blocker classification, or v0.3 handoff wording.
- Run read-only documentation checks, status consistency checks, release
  wording checks, concrete demo anchor sweeps, and changed-file scope guards.

## Forbidden Changes

- Do not modify runtime services, schemas, API routes, app assembly, event log
  behavior, archive behavior, persistence behavior, agent behavior, frontend
  implementation, fixture files, migration files, or test implementation files.
- Do not modify `backend/worldengine/`.
- Do not implement WorldSpec loading, RuntimeEngine-to-WorldCell migration,
  runtime bridge, generation, projection, agent loop, memory, self-continuity,
  resolver, or causality behavior.
- Do not create external fixture or validation repositories.
- Do not add concrete external-world names, characters, locations, roles,
  resources, story rules, seed data, UI selectors, private runner state, or
  application-specific backend logic.
- Do not claim tests, builds, runtime behavior, API behavior, or frontend
  behavior passed unless the command or flow is run in the current session.
- Do not mark v0.3 ready to start unless v0.2 final closeout is approved and
  recorded.

## Acceptance Requirements

- This package contains English and Chinese mirrors for README, intent,
  contract, technical design, test plan, plan, and review docs.
- Package README and the v0.2 milestone index mark 0.2.12 as
  `ready for review` during the documentation stage.
- Final-closeout implementation is explicitly gated on 0.2.11
  release-candidate approval.
- Final status requirements state that unresolved P1/P2 findings block
  closeout.
- The open P3 finding `v0.2-P3-003` is treated as a v0.3 handoff only if
  final review accepts it as non-blocking.
- Verification requirements include `git diff --check`, release-status wording
  checks, status consistency checks, changed-file scope checks, and concrete
  demo anchor sweep.
- Backend, frontend, API smoke, E2E, Agent smoke, runtime, schema execution,
  fixture, and migration tests are not claimed unless they are run in the
  current 0.2.12 session.
- English and Chinese mirrors remain synchronized for package docs and status
  docs.

## North Star Check

This package protects WorldEngine as a generic recursive world engine by
closing the foundation milestone through evidence and boundaries rather than
through application-specific logic. It does not add concrete worlds, product
UI, private validation internals, or runtime shortcuts.

## Out-of-Scope Follow-ups

- v0.3 may begin only after approved v0.2 final closeout and a separate v0.3
  package contract.
- Current-session runtime/API/frontend regression evidence belongs in the
  first v0.3 code or mixed package that changes behavior, unless a reviewer
  explicitly asks to run those checks during closeout.
- Any newly discovered P1/P2 gap must become a blocker or a separately
  reviewed follow-up, not an unreviewed 0.2.12 implementation patch.
