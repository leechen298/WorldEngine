# 0.2.4 WorldSpec Reference Fixture

Status: ready for review

Type: code

英文版本：`README.md`。

## Goal

创建第一份 reference WorldSpec fixture 的 documentation gate。0.2.4 是“第一份可验证的世界样本”，
不是“第一个可运行的世界”。

通过 review approval 后，本包可以新增一个小型、确定性的 `tiny_village.world.json` fixture，
以及聚焦的 validation tests，用来证明该 fixture 符合 0.2.2 的 `WorldSpec`、`WorldCell` 和
`EntityRef` schema language。

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
- [ ] Contract reviewed
- [ ] Technical design reviewed
- [ ] Test plan reviewed
- [ ] Documentation gate approved
- [ ] Ready for implementation
- [ ] Implementation complete
- [ ] Tests/evidence complete
- [ ] Review complete

## Implementation Boundary

Implementation 必须等这个 documentation gate 通过 review 后才能开始。通过后，
implementation stage 只允许修改：

- `backend/data/world_specs/tiny_village.world.json`
- `backend/app/tests/test_worldspec_fixture.py`
- 本 package 的 `review.md` 和 `review.zh.md` closeout evidence

Documentation stage 不能创建 fixture 或 test file。

本包不包含 schema implementation、production WorldSpec loader、runtime bridge、
RuntimeEngine behavior、event log storage、module、API route、frontend、
`backend/worldengine/`、village runtime、game-specific backend logic、world generation、
agent memory、pseudo-self、persistence/restart logic 或 0.2.5 工作。
