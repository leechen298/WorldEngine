# 0.2.2 Recursive World Contract

Status: ready for implementation

Type: code

英文版本：`README.md`。

## Goal

定义第一个 recursive world schema package 的 reviewed implementation contract。
本包准备 EntityRef、WorldCell 和最小 WorldSpec schema，不改变 runtime behavior。

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
- [ ] Implementation complete
- [ ] Tests/evidence complete
- [ ] Review complete

## Implementation Boundary

Implementation 必须等这个 documentation gate 通过 review 后才能开始。通过后，
implementation stage 只允许修改：

- `backend/app/schemas/entity.py`
- `backend/app/schemas/world_cell.py`
- `backend/app/tests/test_world_cell_schema.py`

本包不包含 runtime、API route、frontend、fixture、loader、generator 或 legacy backend
变更。
