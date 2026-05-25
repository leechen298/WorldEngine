# Plan

Status: complete

英文版本：`plan.md`。

## Steps

1. 创建 root coding-agent guidance：
   - `AGENTS.md`
2. 创建 project direction docs：
   - `docs/project-north-star.md`
   - `docs/product-model.md`
   - `docs/scope-boundaries.md`
   - `docs/roadmap.md`
   - `docs/glossary.md`
3. 创建 iteration governance：
   - `docs/iterations/README.md`
   - `docs/iterations/templates/*`
4. 创建 v0.2 planning structure：
   - `docs/iterations/v0.2/README.md`
   - `docs/iterations/v0.2/v0.2-plan.md`
   - `docs/iterations/v0.2/0.2.1-project-north-star/*`
5. 创建 release placeholders：
   - `docs/releases/v0.1.md`
   - `docs/releases/v0.2.md`
6. 创建 testing evidence guide：
   - `docs/testing/README.md`
   - `docs/testing/results/.gitkeep`
7. 运行 docs-only verification。
8. 更新 `review.md`。

## Verification

```bash
rg -n "released|implemented|complete|demo-specific backend|application-specific backend|WorldEngine is.*application-specific|application-specific only" AGENTS.md docs
rg -n "TODO|TBD|to be filled|Pending verification|in progress" AGENTS.md docs
git ls-files --others --exclude-standard -- AGENTS.md docs | sort
rg -n "[ \t]+$" AGENTS.md docs
```

## Expected Result

- 只新增或修改 `AGENTS.md` 和 `docs/` 下文件。
- 不改变 runtime、frontend 或 tests。
- Docs 明确 v0.2 是 planned foundation，不是 released implementation。
