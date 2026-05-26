# Test Plan

Status: ready for review

英文版本：`test-plan.md`。

## Documentation Checks

- 验证 package 拥有所有 required English 和 Chinese mirror documents。
- 验证 package README status 是 `ready for review`。
- 验证 v0.2 milestone index 将 0.2.7 记录为 `ready for review`。
- 验证 Markdown diffs 没有 whitespace errors。
- 验证 documentation-stage pass 没有修改 runtime、API、frontend、fixture、migration 或 test implementation files。

## Unit Tests For Implementation Stage

添加或确认 focused tests 覆盖：

- EntityRef accepts non-empty generic `id` and `kind`, optional `label`, and default empty metadata。
- EntityRef rejects empty `id` and empty `kind`。
- WorldCell accepts default `kind = "world"`, empty entity refs, empty child cells, and empty metadata。
- WorldCell validates nested child cells recursively。
- WorldCell rejects non-world `kind`。
- WorldCell rejects invalid child cell payloads。
- WorldCell rejects invalid entity reference payloads。
- WorldSpec accepts `schema_version = "0.2"` and a required root WorldCell。
- WorldSpec rejects unsupported schema versions。
- WorldSpec rejects empty `id`。
- WorldSpec model_dump output can be model_validate'd back to an equivalent WorldSpec。
- Generic smoke payloads remain domain-neutral and contain no concrete external-world anchors。

Existing tests 可以满足这些要求。Implementation 只应为 uncovered cases 添加 tests。

## Regression Tests For Implementation Stage

- Existing backend schema tests 必须继续通过。
- 如果 schema code changes，existing backend app tests 应通过。
- 如果触及 schema imports 或 shared model behavior，Event schema compatibility 不得 regression。

## Commands

Documentation-stage checks:

```bash
git status --short --branch
git diff --check
```

Implementation-stage checks, if only docs/contracts and tests are changed:

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
make check-backend
```

Implementation-stage checks, if schema code changes:

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py app/tests/test_event_schema_compat.py -q
make check-backend
cd backend && .venv/bin/python -m pytest app/tests -q
```

Concrete demo anchor sweep:

使用 `/tmp` 或其他 untracked path 下的 temporary untracked pattern file。Sweep 只针对 touched docs and tests。Review evidence 只记录 abstract match categories；不要把 concrete pattern lists 写入 tracked documentation。

## Acceptance Criteria

- Documentation-stage package 在 implementation 开始前 complete 且 ready for review。
- Contract docs 已为 EntityRef、WorldCell 和 WorldSpec 规划。
- Acceptance requirements 可通过 concrete commands 测试。
- Assumptions 和 open risks 已记录。
- 本 package 不授权 loader、runtime bridge、generation、projection、memory、agent loop、frontend、fixture、migration 或 external repository work。
- Implementation review 必须记录 changed files、commands、test results、compatibility review、scope review 和 unresolved findings。

## Not Run

Backend 和 frontend tests 对本 documentation-stage pass 不是 required。若 implementation 修改 schema、test 或 backend behavior files，必须按上面的 command matrix 运行。
