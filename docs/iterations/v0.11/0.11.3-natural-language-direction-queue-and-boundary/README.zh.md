# 0.11.3 自然语言方向队列与边界

英文源文件：`README.md`。

状态：review complete
类型：混合实现包
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

允许用户用自然语言引导某个 session 的世界演化，但该引导必须停留在直接世界变更之外。被接受的引导只能排队为公开的世界级压力、概率变化、事件候选偏置、环境趋势、规则约束或后续评估提示。被拒绝的引导不得修改最终事实、Agent 私有状态、Agent 目标、关系或物品栏。

## 范围

评审通过后允许：

- 新增 session 级方向队列 / 读取接口。
- 复用现有公开 world-direction 分类器与脱敏边界。
- 记录接受 / 拒绝方向证据，且不回显原始指令。
- 暴露公开队列摘要，供后续事件生成使用。
- 增加 session direction 行为和 manifest 可发现性的聚焦后端测试。

禁止范围：

- 不允许用户引导直接造成死亡、受伤、治疗、物品、关系、位置、私有记忆、私有目标或最终事实变更。
- 不实现玩家掉落物品、玩家作为世界实体的游戏玩法，也不接受直接详细事件触发。
- 不绕过规则，不暴露隐藏 evaluator oracle、原始 provider trace、原始 prompt、原始 response、secret、Agent 私有记忆或隐藏上下文。
- 不实现规则合规事件生成或 diff 应用；该范围属于 `0.11.4`。
- 不实现 Validation Client，也不执行外部验证。
- 不新增持久化或迁移。
- 不修改 `backend/worldengine/`。

## 交付物

- session 级方向队列 API。
- session 级方向摘要 API。
- additive manifest 发现入口。
- 接受和拒绝 guidance 的可 replay 公开 operation records。
- queued / rejected direction 结果的 client-readable status classification。
- `direct_state_mutation_applied: false` 的公开接受 / 拒绝证据。
- 证明直接最终事实命令会被拒绝，而 lightning-risk 引导只会作为外部压力入队的示例。
- 聚焦后端测试和 review evidence。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## 状态清单

- [x] 文档已起草
- [x] Contract 已评审
- [x] Technical design 已评审
- [x] Test plan 已评审
- [x] 实现已授权
- [x] 实现完成
- [x] 测试 / evidence 完成
- [x] Review 完成

## 最终评估

PASS。已在 reviewed scope 内完成实现。
