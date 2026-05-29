# Test Plan

状态：`planned / ready for review`

## Future execution checks

后续 execution package 应运行或明确记录 blocker：

```bash
git status --short --branch
git rev-parse HEAD
git diff --check
```

documentation 和 release claim checks：

```bash
test -f docs/releases/v0.2.md
test -f docs/iterations/v0.2/evidence-index.md
test -f docs/iterations/v0.2/compatibility-review.md
test -f docs/iterations/v0.2/boundary-audit.md
rg -n "final / closeout complete|0.2.12 verification is documentation-only|does not rerun" docs/releases/v0.2.md
```

可考虑的 backend deterministic checks：

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

可考虑的 focused checks：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py app/tests/test_event_api_compat.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_runtime_step.py app/tests/test_world_params.py app/tests/test_archive_snapshot_summary.py -q
```

API smoke 可以使用 TestClient 或 curl。如果使用 curl，execution 必须先用 repository
支持的命令启动 backend，并记录 server command、port、environment variables 和 shutdown
handling。

E2E availability check：

```bash
test -f frontend/playwright.config.ts
test -f frontend/package.json
```

这些文件存在并不足以证明 E2E 可运行。execution 必须发现 install、start 和 test
commands，并为 missing dependencies、browser binaries、ports、services 或 environment
variables 记录 blockers。

## 预期结果

- 成功运行的 commands 必须记录 exit code 和 output summary。
- 无法运行的 commands 必须记录 blocker、reason 和 impact。
- browser E2E 不可用时可以标记为 not configured 或 blocked。
- fallback validation 必须使用 API smoke 加 backend integration checks。

## 本 package 未运行的命令

本 package 是 planning-only，因此不运行 backend、frontend、E2E、API smoke、runtime、
schema execution、fixture 和 migration commands。

## Blocker 记录规则

如果 required command 无法运行，execution report 必须把结果分类为 `blocked`，除非另一个已完成的
validation line 能证明同一 claim，且 report 解释了替代关系。

## No unverified claims rule

除非检查在同一 execution session 中运行并记录 command result，否则不得声称检查成功。
