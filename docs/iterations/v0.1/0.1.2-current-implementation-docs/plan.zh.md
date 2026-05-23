# Plan

Status: review complete

英文版本：`plan.md`。

## Files

- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
- `README.md`
- `backend/README.md`
- `frontend/README.md`

## Steps

1. 检查 current branch 和 working tree。
2. 阅读 active backend app factory、routes、runtime、event log、world params、archive 和 params-agent
   code。
3. 阅读 frontend API client、dashboard page 和 major components。
4. 阅读 current tests，建立 test coverage map。
5. 新增 current implementation docs。
6. 更新 README 和 release/iteration indexes。
7. 运行 docs verification。
8. 更新 `review.md`。

## Verification

Docs-only package 使用 Markdown/static checks：

```bash
git diff --check -- README.md backend/README.md frontend/README.md docs
rg -n "[ \t]+$" README.md backend/README.md frontend/README.md docs
```

本 package 不 rerun backend/frontend tests，因为没有修改 code/test/runtime behavior。
