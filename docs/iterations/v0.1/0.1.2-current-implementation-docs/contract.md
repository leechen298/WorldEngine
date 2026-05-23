# Contract

## Public Concepts

This package documents current v0.1 concepts:

- application factory.
- in-memory runtime state.
- event log and timeline.
- world module tree.
- world params and validation.
- dry-run validation.
- archive snapshots and summaries.
- params agent.
- dashboard panels.
- API client.
- test coverage map.

## Compatibility Constraints

- No backend code may change.
- No frontend code may change.
- No API schema may change.
- No test code may change.
- The pre-existing `.gitignore` working-tree change must not be touched.

## Allowed Changes

- Add `docs/current-implementation.md`.
- Add `docs/backend-implementation.md`.
- Add `docs/frontend-implementation.md`.
- Add `docs/api-reference-v0.1.md`.
- Add `docs/testing/v0.1-test-map.md`.
- Add this iteration package.
- Update v0.1 index docs to link this package.
- Update README/release docs only to link the current implementation docs.

## Forbidden Changes

- Do not modify `backend/`.
- Do not modify `frontend/src/`.
- Do not modify package manager files.
- Do not add WorldCell or WorldSpec schemas.
- Do not create runtime migration plans in this package.
- Do not label placeholders as completed recursive-world capability.

## North Star Check

The docs must treat v0.1 as a runtime scaffold, not as the final recursive
world engine. The first game surface must remain future projection work.

## Out-of-Scope Follow-ups

- v0.2 Recursive World Contract.
- Event contract extension.
- WorldSpec fixture.
- Runtime migration.
- UI redesign.
