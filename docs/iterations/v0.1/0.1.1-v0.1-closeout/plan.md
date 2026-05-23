# Plan

## Files

Create:

- `docs/iterations/v0.1/README.md`
- `docs/iterations/v0.1/v0.1-plan.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/README.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/intent.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/contract.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/test-plan.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/plan.md`
- `docs/iterations/v0.1/0.1.1-v0.1-closeout/review.md`
- `docs/testing/results/2026-05-23-v0.1-closeout.md`

Modify:

- `README.md`
- `docs/releases/v0.1.md`

Do not touch:

- `backend/`
- `frontend/src/`
- `frontend/package.json`
- `backend/pyproject.toml`
- `.gitignore`

## Steps

1. Inspect current branch, commit history, test files, route files, and docs.
2. Run the verification commands in `test-plan.md`.
3. Update root README with current v0.1 capability and verification link.
4. Update `docs/releases/v0.1.md` with capability boundary, known limitations,
   and evidence.
5. Add durable test result documentation.
6. Update `review.md` with changed files, commands, results, and residual risk.

## Verification

Run:

```bash
git status --short
git diff --check -- README.md docs
rg -n "[ \t]+$" README.md docs
```
