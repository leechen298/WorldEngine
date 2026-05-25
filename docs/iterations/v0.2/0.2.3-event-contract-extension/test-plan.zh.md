# Test Plan

英文版本：`test-plan.md`。

## Unit Tests

这个 documentation gate 通过 review 和 approval 后，新增
`backend/app/tests/test_event_schema_compat.py`，测试：

- Existing Event construction without refs still works。
- Event.refs defaults to empty list。
- Event accepts refs with id、kind、role 和 metadata。
- EventRef rejects empty id。
- EventRef rejects empty kind。
- Event.model_dump includes refs when provided。
- Event.model_validate round-trip preserves refs。
- EventPage validates Event with and without refs。
- EventStep validates items with Event refs。
- EventStepPage validates nested EventStep values。
- Existing current event examples remain compatible。
- Import smoke for EventRef and Event。

## Regression Tests

Existing backend tests 必须继续通过，因为本包不能改变 event log storage、runtime engine behavior、
modules、API routes、frontend behavior 或 `backend/worldengine/`。

## Commands

本 package 的 documentation-stage commands：

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.3-event-contract-extension -maxdepth 1 -type f | sort
rg -n "0.2.3-event-contract-extension|ready for implementation|EventRef|refs|Event Contract|backward compatible|payload|EventPage|EventStep|EventStepPage" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|concrete demo|migration|agent memory|pseudo-self|referential integrity|resolve refs|frontend|API route" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

Implementation-stage commands 只记录，等 review approval 后新增代码时再运行：

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
from app.schemas.event import Event, EventRef
print(Event, EventRef)
PY
```

## Acceptance Criteria

- Documentation gate 只改变 `docs/iterations/v0.2/`。
- Package directory 包含完整 English seven-file set 和完整 `.zh.md` mirrors。
- v0.2 README 和 plan documents 显示 0.2.3 为 `ready for implementation`。
- `review.md` 和 `review.zh.md` 记录 documentation-stage evidence，并说明 implementation has not
  started。
- Documentation stage 不改变 backend、frontend、runtime、schema implementation、API、UI、fixture、
  loader、generator 或 test implementation files。
- Implementation 只能在本 package review 和 approval 后开始。

## Not Run

Documentation stage 不运行 backend、frontend、runtime、E2E、UI smoke、Agent smoke 或
implementation tests，因为没有改变 code、runtime、schema implementation、API、UI、fixture、
loader、generator 或 test implementation files。
