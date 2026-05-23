# Plan

## Files

Create:

- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
- `docs/iterations/v0.1/0.1.2-current-implementation-docs/README.md`
- `docs/iterations/v0.1/0.1.2-current-implementation-docs/intent.md`
- `docs/iterations/v0.1/0.1.2-current-implementation-docs/contract.md`
- `docs/iterations/v0.1/0.1.2-current-implementation-docs/plan.md`
- `docs/iterations/v0.1/0.1.2-current-implementation-docs/review.md`

Modify:

- `README.md`
- `docs/releases/v0.1.md`
- `docs/iterations/v0.1/README.md`
- `docs/iterations/v0.1/v0.1-plan.md`

Do not touch:

- `backend/`
- `frontend/`
- `.gitignore`

## Steps

1. Inspect backend app factory, routes, schemas, runtime, world, archive,
   validation, and agent modules.
2. Inspect frontend API client, dashboard, panels, tests, and build scripts.
3. Write the current implementation overview.
4. Write backend and frontend implementation docs.
5. Write API reference and test map.
6. Update v0.1 docs to link the implementation docs.
7. Run docs-only checks.
8. Record evidence in `review.md`.

## Verification

Run:

```bash
git status --short
git diff --check -- README.md docs
rg -n "[ \t]+$" README.md docs
```
