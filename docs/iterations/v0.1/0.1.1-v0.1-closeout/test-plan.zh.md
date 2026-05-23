# Test Plan

Status: complete

英文版本：`test-plan.md`。

## Goal

验证 v0.1 scaffold baseline 的 backend、frontend 和 root workflow。

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

- Root Make workflow commands 可见。
- Backend dependency check 通过。
- Frontend dependency check 通过。
- Backend pytest suite 通过。
- Frontend unit tests 通过。
- Frontend production build 成功，任何 warning 都要记录。

## Not Run

- 不需要 browser E2E。
- 不需要 live API curl smoke。
- 不需要 runtime migration checks。
