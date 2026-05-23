# Test Plan

## Goal

Verify the current v0.1 baseline before recording closeout evidence.

## Commands

```bash
make help
make check-backend
make check-frontend
cd backend && .venv/bin/python -m pytest app/tests
cd frontend && pnpm test
cd frontend && pnpm build
```

## Acceptance Criteria

- Root workflow help prints available commands.
- Backend dependency check exits 0.
- Frontend dependency check exits 0.
- Backend pytest suite passes.
- Frontend vitest suite passes.
- Frontend build exits 0.
- Any warnings are documented instead of treated as failures.

## Not Run

- No live dev server smoke was run.
- No browser UI smoke was run.
- No API server curl smoke was run.
- No E2E test suite exists for v0.1 closeout.
