# Plan

Status: ready for implementation

英文版本：`plan.md`。

## Documentation Stage

1. 在 `docs/iterations/v0.2/` 下创建 0.2.4 package directory。
2. 起草 English seven-file package：`README.md`、`intent.md`、`contract.md`、
   `technical-design.md`、`test-plan.md`、`plan.md` 和 `review.md`。
3. 起草同步的 Chinese `.zh.md` mirrors。
4. 更新 v0.2 README 和 plan documents，把 0.2.4 从 `planned` 移到 `ready for review`。
5. 运行 documentation-stage verification commands，并把 evidence 记录到 `review.md` 和
   `review.zh.md`。
6. 在 implementation 前停止。

## Review Gate

Review 已确认：

- Fixture 被描述为第一份可验证的世界样本，而不是第一个可运行的世界。
- Implementation boundary 限定在
  `backend/data/world_specs/tiny_village.world.json`、
  `backend/app/tests/test_worldspec_fixture.py`，以及本 package 的 closeout review files。
- Fixture contract 使用现有 0.2.2 `WorldSpec`、`WorldCell` 和 `EntityRef` schema language。
- 允许 test-only JSON reading，但禁止 production WorldSpec loader work。
- 0.2.4 已批准进入 implementation，但没有标记为 implementation complete 或 review complete。

## Implementation Stage After Approval

只有 review approval 后才能：

1. 新增 `backend/data/world_specs/tiny_village.world.json`。
2. 新增 `backend/app/tests/test_worldspec_fixture.py`。
3. 运行 focused fixture test。
4. 运行 broader backend app test suite。
5. 运行已记录的 import/validation smoke command。
6. 用 implementation-stage evidence 更新 `review.md` 和 `review.zh.md`。

## Stop Conditions

如果 implementation 发现需要做以下任何事，必须停止并回到 documentation review：

- 修改 `EntityRef`、`WorldCell`、`WorldSpec` 或 `Event` schema contracts。
- 新增 WorldSpec loader 或 runtime bridge。
- 把 fixture 连接到 `RuntimeEngine`。
- 新增 API route、frontend、event log、module、generator、persistence 或
  `backend/worldengine/` behavior。
- 新增 village runtime、game-specific backend logic、world generation、agent memory、
  pseudo-self 或 agent behavior loops。
- 启动 0.2.5。
