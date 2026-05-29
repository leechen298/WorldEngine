# Test Plan

状态：`planned / ready for review`

## Autonomous reviewer checks

后续 Codex reviewer 必须运行或记录 blockers：

```bash
git status --short --branch
git rev-parse HEAD
git diff --check
```

reviewer 应检查 required docs 和 code：

```bash
test -f README.md
test -f docs/releases/v0.2.md
test -f docs/iterations/v0.2/evidence-index.md
test -f docs/iterations/v0.2/compatibility-review.md
test -f docs/iterations/v0.2/boundary-audit.md
test -f docs/scope-boundaries.md
test -f backend/app/schemas/world_cell.py
test -f backend/app/schemas/event.py
test -d backend/app/tests
```

环境 ready 时 reviewer 应运行 focused validation commands；否则记录 blockers：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py app/tests/test_event_api_compat.py -q
```

环境 ready 时 reviewer 可以运行 broader checks：

```bash
cd backend && .venv/bin/python -m pytest app/tests -q
```

## 预期结果

- 每个 file read 必须列入 independent review。
- 每个 command run 必须包含 exit code 和 result summary。
- 每个 skipped command 必须包含 reason 和 blocker impact。
- unsupported claims 必须列出。

## 本 package 未运行的命令

本 planning package 不运行 autonomous validation commands。

## Blocker 记录规则

如果 reviewer 无法运行 required command，review 必须记录 blocker，并解释它是否阻止 final
recommendation。

## No unverified claims rule

除非 reviewer 在同一 session 中运行相关命令，否则不得声明 tests、runtime behavior、API
behavior 或 E2E behavior 成功。
