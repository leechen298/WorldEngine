# Contract

## Public Concepts

This package documents:

- v0.1 Runtime Scaffold.
- v0.1 capability boundary.
- v0.1 verification evidence.
- v0.1 known limitations.
- recommended transition criteria for v0.2.

## Compatibility Constraints

- No backend runtime behavior may change.
- No frontend behavior may change.
- No API schema may change.
- No tests may be added, removed, or modified.
- The pre-existing `.gitignore` working-tree change must not be touched.

## Allowed Changes

- Update `README.md`.
- Update `docs/releases/v0.1.md`.
- Add `docs/iterations/v0.1/` closeout docs.
- Add `docs/testing/results/2026-05-23-v0.1-closeout.md`.

## Forbidden Changes

- Do not modify `backend/`.
- Do not modify `frontend/src/`.
- Do not modify `frontend/package.json`.
- Do not modify `backend/pyproject.toml`.
- Do not add v0.2 schema files.
- Do not create a game runtime.

## North Star Check

This package explicitly labels v0.1 as a scaffold baseline. It does not narrow
WorldEngine into a game backend and does not claim recursive world capability
already exists.

## Out-of-Scope Follow-ups

- v0.2 Recursive World Foundation package work.
- Build chunk splitting or bundle optimization.
- Runtime migration to WorldSpec.
- Backend/frontend implementation changes.
