# Test Plan

英文版本：`test-plan.md`

## Documentation Checks

- 验证 package 拥有全部 required English 和 Chinese mirror documents。
- 验证 package README status 是 `ready for review`。
- 验证 v0.2 milestone index 将 0.2.8 记录为 `ready for review`。
- 验证 Markdown diffs 没有 whitespace errors。
- 验证 documentation-stage pass 未修改 runtime、schema、API、frontend、
  fixture、migration 或 test implementation files。

## Implementation Stage Unit Tests

新增或确认 focused tests 覆盖：

- Event construction without `refs` 仍 validate，并产生 `refs == []`。
- Event accepts refs with non-empty generic `id` and `kind`。
- EventRef accepts optional `role`。
- EventRef accepts omitted `metadata` and defaults it to `{}`。
- EventRef accepts free-form metadata，且 v0.2 runtime 不解释它。
- EventRef rejects empty `id`。
- EventRef rejects empty `kind`。
- Event model_dump output 可被 model_validate 回 equivalent Event，同时保留 refs。
- EventPage validates events with and without refs。
- EventStep 和 EventStepPage validate nested events with refs。
- Generic test payloads 保持 domain-neutral，且不包含 concrete external-world
  anchors。

Existing tests 可满足这些要求。Implementation 只应为未覆盖 cases 添加 tests。

## Implementation Stage Regression Tests

- Existing event schema compatibility tests 必须继续通过。
- 如果 event schema code changes，existing backend app tests 应通过。
- 如果 shared schema behavior 或 contract imports 被触及，recursive schema tests
  不应受影响。

## Commands

Documentation-stage checks：

```bash
git status --short --branch
git diff --check
```

Implementation-stage checks，如果只修改 docs/contracts 和 focused tests：

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q
make check-backend
```

Implementation-stage checks，如果 event schema code changes：

```bash
git status --short --branch
git diff --check
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py app/tests/test_world_cell_schema.py app/tests/test_worldspec_schema_smoke.py -q
make check-backend
cd backend && .venv/bin/python -m pytest app/tests -q
```

Concrete demo anchor sweep：

使用 `/tmp` 或其他 untracked path 下的 temporary untracked pattern file。对
touched docs 和 tests 运行 sweep。Review evidence 只记录 abstract match
categories；不要把 concrete pattern lists 写入 tracked documentation。

## Acceptance Criteria

- Documentation-stage package 在 implementation 开始前已 complete 且 ready for
  review。
- EventRef 和 Event.refs 的 contract documentation 已纳入计划。
- Acceptance requirements 可用 concrete commands 测试。
- Assumptions 和 open risks 已记录。
- 本 package 不授权 resolver、causality、runtime bridge、generation、projection、
  memory、agent loop、frontend、fixture、migration、external repository 或 API
  route work。
- Implementation review 必须记录 changed files、commands、test results、
  compatibility review、scope review 和 unresolved findings。

## Not Run

Backend 和 frontend tests 不要求在本 documentation-stage pass 运行。如果 schema、
test 或 backend behavior files 发生变化，implementation 阶段必须按上方 command
matrix 运行。
