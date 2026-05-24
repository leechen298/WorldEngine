# Review

Status: review complete

英文版本：`review.md`。

## Changed Files

| File | Change |
|---|---|
| `docs/iterations/v0.2/0.2.3-event-contract-extension/*` | 新增完整 0.2.3 documentation gate，并记录 implementation 前的 review approval。 |
| `docs/iterations/v0.2/README.md` | 同步 0.2.3 implementation 前 approval state。 |
| `docs/iterations/v0.2/README.zh.md` | 同步 0.2.3 implementation 前 approval state。 |
| `docs/iterations/v0.2/v0.2-plan.md` | 同步 0.2.3 implementation 前 approval state。 |
| `docs/iterations/v0.2/v0.2-plan.zh.md` | 同步 0.2.3 implementation 前 approval state。 |
| `docs/iterations/v0.2/0.2.3-event-contract-extension/README.md` | 记录 implementation 前的 review approval。 |
| `docs/iterations/v0.2/0.2.3-event-contract-extension/README.zh.md` | 记录 implementation 前的 review approval。 |
| `docs/iterations/v0.2/README.md` | 记录 implementation 前的 review approval。 |
| `docs/iterations/v0.2/README.zh.md` | 记录 implementation 前的 review approval。 |
| `docs/iterations/v0.2/v0.2-plan.md` | 记录 implementation 前的 review approval。 |
| `docs/iterations/v0.2/v0.2-plan.zh.md` | 记录 implementation 前的 review approval。 |

## Commands Run

```bash
git status --short --branch
git diff --check
find docs/iterations/v0.2/0.2.3-event-contract-extension -maxdepth 1 -type f | sort
rg -n "0.2.3-event-contract-extension|EventRef|refs|Event Contract|backward compatible|payload|EventPage|EventStep|EventStepPage" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
rg -n "RuntimeEngine|WorldSpec loader|backend/worldengine|village|migration|agent memory|pseudo-self|referential integrity|resolve refs|frontend|API route" docs/iterations/v0.2/0.2.3-event-contract-extension docs/iterations/v0.2/v0.2-plan.md
git diff --name-only | rg -v '^(docs/iterations/v0.2/)'
git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'
```

## Test Results

这是 documentation-stage package。Backend、frontend、runtime、schema implementation、API、UI、
fixture、loader、generator 和 test implementation commands 未运行，因为本阶段不能改变这些文件。

Implementation was intentionally deferred at the documentation gate.

Verification observations：

- `git status --short --branch` 显示当前 branch 是 `v0.2`，且只有 v0.2 documentation changes。
- `git diff --check` 成功退出，没有 whitespace errors。
- `find docs/iterations/v0.2/0.2.3-event-contract-extension -maxdepth 1 -type f | sort`
  列出了完整 English seven-file set 和完整 `.zh.md` mirrors。
- Status/content search 在 package 和 v0.2 index/plan documents 中找到了 `EventRef`、
  `refs`、`Event Contract`、`backward compatible`、`payload`、`EventPage`、
  `EventStep` 和 `EventStepPage`。
- Boundary search 只找到了 `RuntimeEngine`、`WorldSpec loader`、`backend/worldengine`、
  village、migration、agent memory、pseudo-self、referential integrity、resolve refs、
  frontend 和 API route 的 planned boundary references。
- `git diff --name-only | rg -v '^(docs/iterations/v0.2/)'` 没有输出匹配。
- `git status --porcelain=v1 -uall | awk '{print $2}' | rg -v '^docs/iterations/v0.2/'`
  没有输出匹配。这个 no-match exit code 对 negative docs-only scope guard 是预期结果。

## Compatibility Review

本 documentation stage 没有改变 runtime behavior、event log storage、API response shape、
frontend behavior 或 legacy backend behavior。

文档中的 Event Contract extension 是 additive：EventRef 是 event-local，`Event.refs` 默认是
empty list，`payload` 保持不变并完全 backward compatible。

## Scope Review

本 documentation stage 限定在 `docs/iterations/v0.2/`。它没有修改 0.2.2，没有实现
`backend/app/schemas/event.py`，没有新增 `backend/app/tests/test_event_schema_compat.py`，也没有启动
0.2.4。

## Unresolved Findings

- P1: none.
- P2: none.
- P3: none.

## Final Assessment

0.2.3 documentation gate 已在 implementation stage 前完成 review approval。Implementation
在该 gate 阶段被有意延后。

## Implementation Closeout

### Changed Files

| File | Change |
|---|---|
| `backend/app/schemas/event.py` | 新增 event-local `EventRef`，包含非空 `id` 和 `kind`、可选 `role`、默认 `metadata`，并给 `Event` 增加 additive `refs`。 |
| `backend/app/tests/test_event_schema_compat.py` | 新增聚焦兼容性测试，覆盖旧 Event 构造、EventRef validation/defaults、Event refs serialization、wrapper validation、round-trip reconstruction 和 import smoke。 |
| `docs/iterations/v0.2/0.2.3-event-contract-extension/README.md` | Status sync：0.2.3 移到 `review complete`，并勾选 implementation/test/review checklist items。 |
| `docs/iterations/v0.2/0.2.3-event-contract-extension/README.zh.md` | Status sync：0.2.3 移到 `review complete`，并勾选 implementation/test/review checklist items。 |
| `docs/iterations/v0.2/README.md` | Status sync：0.2.3 移到 `review complete`。 |
| `docs/iterations/v0.2/README.zh.md` | Status sync：0.2.3 移到 `review complete`。 |
| `docs/iterations/v0.2/v0.2-plan.md` | Status sync：0.2.3 移到 `review complete`。 |
| `docs/iterations/v0.2/v0.2-plan.zh.md` | Status sync：0.2.3 移到 `review complete`。 |
| `docs/iterations/v0.2/0.2.3-event-contract-extension/review.md` | 记录 implementation-stage evidence。 |
| `docs/iterations/v0.2/0.2.3-event-contract-extension/review.zh.md` | 记录同步的 implementation-stage evidence。 |

### Commands Run

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q
cd backend && .venv/bin/python -m pytest app/tests -q
cd backend && .venv/bin/python - <<'PY'
from app.schemas.event import Event, EventRef
print(Event, EventRef)
PY
git diff --check
git diff --name-only
rg -n "EntityRef|WorldCell|WorldSpec" backend/app/schemas/event.py
rg -n -e "Status: pre-implementation approval" -e "0.2.3-event-contract-extension.*pre-implementation approval" docs/iterations/v0.2/0.2.3-event-contract-extension/README.md docs/iterations/v0.2/0.2.3-event-contract-extension/README.zh.md docs/iterations/v0.2/README.md docs/iterations/v0.2/README.zh.md docs/iterations/v0.2/v0.2-plan.md docs/iterations/v0.2/v0.2-plan.zh.md
git status --short --branch
git status --porcelain=v1 -uall
```

### Test Results

- RED check：`cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q`
  在 implementation 前 exit `1`，输出 `9 failed`；失败原因是
  `ImportError: cannot import name 'EventRef' from 'app.schemas.event'`。
- Focused schema compatibility test：`cd backend && .venv/bin/python -m pytest app/tests/test_event_schema_compat.py -q`
  exit `0`；latest rerun 输出 `9 passed`。
- Backend regression test：`cd backend && .venv/bin/python -m pytest app/tests -q`
  exit `0`；latest rerun 输出 `87 passed`。
- Import smoke：Event/EventRef import command exit `0`，输出
  `<class 'app.schemas.event.Event'> <class 'app.schemas.event.EventRef'>`。
- `git diff --check` exit `0`，没有 whitespace errors。
- `rg -n "EntityRef|WorldCell|WorldSpec" backend/app/schemas/event.py`
  没有输出匹配；exit `1` 对这个 negative coupling check 是预期结果。
- 0.2.3 status files 中针对 pre-implementation approval state 的 stale-status search
  没有输出匹配；exit `1` 对这个 negative status guard 是预期结果。

### Compatibility Review

本实现是 additive。旧的、不带 `refs` 的 Event dictionaries 仍可 validate；`Event.refs`
默认是空列表；`payload` behavior 未改变；存在 refs 时，`model_dump()` /
`model_validate()` 会保留 refs。带 refs 和不带 refs 的 Event values 都能在
`EventPage`、`EventStep` 和 `EventStepPage` 中 validate。

本轮没有改变 event log storage、runtime engine behavior、module behavior、API route、
frontend、fixture、loader、generator、migration、reference resolution、referential
integrity、WorldSpec loader、village runtime、agent memory、pseudo-self 或 legacy
`backend/worldengine/` behavior。

### Scope Review

Implementation 保持在 approved 0.2.3 scope 内：`backend/app/schemas/event.py`、
`backend/app/tests/test_event_schema_compat.py`，以及本 package 的 review evidence。
`backend/app/schemas/event.py` 没有 import 或 reference `EntityRef`、`WorldCell`、
`WorldSpec`。

0.2.3 package README 和 v0.2 index/plan status files 只同步了 implementation closeout
状态，避免 evidence 已记录后仍停留在 stale pre-implementation state。本轮没有启动
0.2.4、WorldSpec loader、runtime bridge、village runtime、frontend、agent memory、
pseudo-self 或 legacy backend work。

### Unresolved Findings

- P1: none.
- P2: none.
- P3: none.

### Final Assessment

0.2.3 implementation complete。Event contract 现在通过 `Event.refs` 获得了 additive、
event-local `EventRef` layer；当前会话内 required focused 和 backend regression checks
均通过。Package 和 v0.2 status files 现在显示 `review complete`。

## Review Approval Closeout

Documentation gate 已在 implementation 前通过 review。当前 implementation 已完成，本
package 状态为 review complete。没有遗留 P1/P2/P3 findings。
