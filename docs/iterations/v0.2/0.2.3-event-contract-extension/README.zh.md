# 0.2.3 Event Contract Extension

Status: review complete

Type: code

英文版本：`README.md`。

## Goal

定义 additive Event Contract extension 的 reviewed documentation gate。本包准备最小的
event-local structured reference layer，但不改变当前 Event construction、payload semantics、
API responses、event log storage、runtime behavior 或 frontend behavior。

## Documents

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

中文镜像以 `.zh.md` 文件提供，后续必须和英文 package documents 同步。

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation gate approved
- [x] Implementation complete
- [x] Tests/evidence complete
- [x] Review complete

## Implementation Boundary

Implementation 必须等这个 documentation gate 通过 review 后才能开始。通过后，
implementation stage 只允许修改：

- `backend/app/schemas/event.py`
- `backend/app/tests/test_event_schema_compat.py`
- 本 package 的 `review.md` 和 `review.zh.md` closeout evidence

本包不包含 event log storage、runtime engine、module、API route、frontend、
`backend/worldengine/`、WorldCell runtime connection、reference resolution、
referential integrity、WorldSpec loader、village runtime、agent memory、pseudo-self 或
0.2.4 工作。
