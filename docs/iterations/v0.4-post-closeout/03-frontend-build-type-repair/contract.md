# Contract

## Public Concepts

- Frontend build type repair: a minimal change set that resolves TypeScript
  build failures without changing WorldEngine runtime semantics.
- Clean-pass validation rerun: current-session rerun of the command matrix
  required to decide whether the v0.4 post-closeout validation has moved from
  partial pass to clean pass.

## Allowed Changes

This package may modify or create only:

- `docs/iterations/v0.4-post-closeout/03-frontend-build-type-repair/**`
- parent `docs/iterations/v0.4-post-closeout/{README.md,CURRENT_STATE.md,CAMPAIGN_PLAN.md,GOAL_RUNNER.md,review.md}`
- `frontend/src/components/MemoryPanel.test.ts`
- `frontend/src/components/TimelinePanel.test.ts`
- `frontend/src/components/TimelinePanel.vue`
- `frontend/src/components/WorldPanel.test.ts`
- `docs/testing/results/2026-05-31-v0.4-overall-product-capability-validation.md`

## Forbidden Changes

- No `backend/app/**` runtime or API changes.
- No `backend/worldengine/**` changes.
- No database migration, schema, external repository, fixture-world, seed data,
  or private oracle changes.
- No full autonomous runner implementation.
- No broad frontend refactor, UI redesign, route change, or feature addition.
- No deletion of valid selector assertions solely to make TypeScript pass.

## Compatibility Requirements

- Existing Vue component behavior and public dashboard selectors must remain
  compatible.
- Existing frontend Vitest expectations must remain meaningful.
- Existing E2E, Agent smoke, and autonomous checker contracts remain the
  authority for validation PASS.
- Clean pass may be claimed only if every command in `test-plan.md` exits `0`.

## North Star Check

This repair keeps WorldEngine generic. It fixes build-time typing around the
dashboard validation surface and does not add demo-specific backend logic,
world content, or application-specific abstractions.

## Out-of-Scope Follow-ups

- Full autonomous runner/full-suite coverage.
- Per-test isolated E2E world state.
- Any v0.5+ product capability.
