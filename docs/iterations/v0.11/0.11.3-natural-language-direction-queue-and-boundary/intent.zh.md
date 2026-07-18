# 意图

英文源文件：`intent.md`。

状态：文档已起草 / 等待评审

## 问题 / 目的

v0.11 需要用户引导，但自然语言命令不能直接变成世界事实。类似“kill this Agent now”的命令必须被拒绝。类似“this Agent may face lightning-strike risk”的弱引导只能作为公开外部压力被接受，后续规则约束事件生成仍必须通过规则、状态、概率、位置、时间和合法性来评估。

## 为什么现在做

`0.11.1` 已标记 provider / worldview readiness，`0.11.2` 已把公开规则附加到 session。`0.11.4` 在生成合法事件和 diff 之前，需要一个 session 级位置，把用户方向存为受边界约束的公开 guidance。

## Roadmap 关系

本包推进 v0.11 “MVP Rule-Bound World Evolution” 里程碑。不实现 Agent pseudo-self、长期记忆、自动化自主验证或完整 MVP closeout。它为后续规则约束事件生成准备方向输入。

## 非目标

- 不让用户引导直接修改事实。
- 不生成事件、不应用事件、不应用状态 diff。
- 不修改 Agent 私有记忆、目标、人格、关系、伤害、死亡或物品栏。
- 不写 Validation Client 代码，也不执行外部验证。
- 不调用 provider。
- 不新增持久化或迁移。
- 不修改 `backend/worldengine/`。

## 预期交接

`0.11.4-rule-compliant-event-generation-and-diffs` 将接收一个公开的 session 级方向队列及接受 / 拒绝证据。后续事件生成可以引用 queued direction id，但仍必须通过公开规则和当前状态证明合法性。
