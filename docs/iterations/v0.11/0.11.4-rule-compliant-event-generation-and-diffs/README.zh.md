# 0.11.4 规则合规事件生成与 Diff

英文源文件：`README.md`。

状态：review complete
类型：混合实现包
implementation_authorized: yes
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

为 session 生成或选择公开 world event candidate，通过公开 rules 和当前 state 评估，只应用合法的 public diffs，并记录可 replay 的 evidence 来解释世界为什么变化。

## 范围

评审通过后允许：

- 保留现有 manual `/worlds/{world_id}/evolution/evaluate-event` legality/apply 路径。
- 新增一个很小的 session-scoped rule-bound evolution step，从已附加的 public rule set、当前 public parameters、runtime tick/time 和 queued public direction refs 构造 deterministic public candidate。
- 每个 generated/selected candidate 必须先通过现有 public legality evaluator，才能修改 state。
- 记录 accepted/rejected legality evidence、public diffs、direction refs、rule refs、parameter refs 和可 replay event-log records。
- 为 session evolution step 增加 additive manifest discovery。
- 增加聚焦后端测试，覆盖 legal/illegal candidates、direction influence、lightning-risk-as-pressure、diff application、replay evidence、redaction 和 runtime/session compatibility。

禁止范围：

- 不做隐藏 random oracle 或不可解释选择。
- 不允许非法最终结果。
- 不直接修改死亡、受伤、物品栏、关系、Agent 目标、Agent 私有记忆或 Agent 私有状态。
- 不让用户直接施加最终事实。
- 不实现玩家掉落物品、直接详细事件触发或 player-as-world-entity gameplay。
- 不调用 provider，不暴露 raw prompts、raw responses、provider traces、secrets、hidden context 或 private evaluator data。
- 不实现 Validation Client，也不执行外部验证。
- 不增加具体 demo-world seed data。
- 不新增持久化 / 迁移。
- 不做 frontend work。
- 不修改 `backend/worldengine/`。

## 交付物

- session-scoped rule-bound evolution step API。
- deterministic public event candidate selection/generation。
- legality result 和 public state diff evidence。
- 可 replay 的 accepted/rejected event records。
- 测试证明 lightning-risk guidance 只保持为 external pressure，不能直接造成 Agent injury/death。
- 聚焦验证和 review evidence。

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
