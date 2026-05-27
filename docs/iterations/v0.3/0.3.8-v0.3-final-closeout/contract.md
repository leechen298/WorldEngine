# Contract

## Public Concepts

- Final closeout: the documentation-only act of marking v0.3 final after the
  release-candidate bundle is accepted and blockers are cleared or explicitly
  classified.
- Final review decision: the human / ChatGPT approval, rejection, or
  conditional acceptance that determines whether final closeout may proceed.
- Blocking finding: an unresolved P1/P2 issue that prevents final closeout.
- Accepted handoff: a non-blocking finding, expected to be P3 only, that is
  retained for v0.4 or later work with explicit closeout wording.
- Historical evidence: commands and test results recorded by earlier package
  reviews, distinct from commands run during 0.3.8.

## Compatibility Constraints

- Runtime behavior must not change.
- Schema behavior and validation behavior must not change.
- Event storage, event pagination, archive behavior, grouping behavior, params
  behavior, and API response behavior must not change.
- Frontend behavior must not change.
- Fixture, migration, and test implementation files must not change.
- `backend/worldengine/` must remain untouched.
- Final release status may be claimed only after approval and only if no
  unresolved P1/P2 findings remain.
- Final closeout wording must distinguish historical package evidence from
  current-session 0.3.8 verification.

## Allowed Changes

- Add or update files under
  `docs/iterations/v0.3/0.3.8-v0.3-final-closeout/`.
- Update `docs/releases/v0.3.md` and `docs/releases/v0.3.zh.md` after review
  approval.
- Update `docs/iterations/v0.3/README.md` and
  `docs/iterations/v0.3/README.zh.md`.
- Update `docs/iterations/v0.3/v0.3-plan.md` and
  `docs/iterations/v0.3/v0.3-plan.zh.md`.
- Update `docs/iterations/v0.3/findings.md` if final review changes finding
  status, blocker classification, or v0.4-or-later handoff wording.
- Run read-only documentation checks, status consistency checks, release
  wording checks, concrete demo anchor sweeps, P1/P2 blocker checks, and
  changed-file scope guards.

## Forbidden Changes

- Do not modify runtime services, schemas, API routes, app assembly, event log
  behavior, archive behavior, persistence behavior, params behavior, agent
  behavior, frontend implementation, fixture files, migration files, or test
  implementation files.
- Do not modify `backend/worldengine/`.
- Do not implement new WorldSpec loader behavior, RuntimeEngine migration,
  runtime bridge behavior, generation, projection, Agent-in-World loop, memory,
  self-continuity, resolver, or causality behavior.
- Do not create external fixture or validation repositories.
- Do not add concrete external-world names, characters, locations, roles,
  resources, story rules, seed data, UI selectors, private runner state, or
  application-specific backend logic.
- Do not claim tests, builds, runtime behavior, API behavior, or frontend
  behavior passed unless the command or flow is run in the current session.
- Do not mark v0.4 ready to implement; v0.4 requires its own reviewed
  iteration package.

## Acceptance Requirements

- This package contains English and Chinese mirrors for README, intent,
  contract, technical design, test plan, plan, and review docs.
- Package README and the v0.3 milestone index mark 0.3.8 as
  `ready for review` during the documentation stage.
- Final-closeout implementation is explicitly gated on 0.3.7
  release-candidate approval.
- Final status requirements state that unresolved P1/P2 findings block
  closeout.
- Open P3 findings are retained as handoffs only if final review accepts them
  as non-blocking.
- Verification requirements include `git diff --check`, final-status wording
  checks, status consistency checks, unresolved P1/P2 blocker checks,
  changed-file scope checks, and concrete demo anchor sweep.
- Backend, frontend, API smoke, E2E, Agent smoke, runtime, schema execution,
  fixture, migration, and test implementation checks are not claimed unless
  they are run in the current 0.3.8 session.
- English and Chinese mirrors remain synchronized for package docs and status
  docs.

## North Star Check

This package protects WorldEngine as a generic recursive world engine by
closing the WorldSpec loader and runtime bridge milestone through evidence and
boundaries rather than through application-specific logic. It does not add
concrete worlds, product UI, private validation internals, or runtime
shortcuts.

## Out-of-Scope Follow-ups

- v0.4 may begin only through a separate v0.4 package contract.
- Fresh runtime/API/frontend regression evidence belongs in a reviewed package
  that asks for it, unless final reviewers explicitly require it during
  closeout.
- Machine-readable external validation report hardening remains a later
  validation-readiness concern.
- Any newly discovered P1/P2 gap must become a blocker or a separately
  reviewed follow-up, not an unreviewed 0.3.8 implementation patch.
