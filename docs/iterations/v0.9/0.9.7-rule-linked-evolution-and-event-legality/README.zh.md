# 0.9.7 规则关联演化与事件合法性

英文原文：`README.md`。

Status：implementation complete / verification passed
Type：mixed implementation package

## 目标

让世界参数演化和被选中的事件都能追溯到公开规则、当前公开状态、约束、概率、因果关系、位置和时间。

本包把已生成的规则/参数产物、有界运行时状态，以及已排队的世界方向引导，转化为确定性的公开证据。只有当这些证据证明候选事件合法时，该事件才可以被接受为世界演化事件。

## 范围

本包允许在 `backend/app/` 这条 active backend path 中扩展：

- 公开的事件候选与事件合法性 schema。
- 基于公开 `GeneratedRuleParameterSet` 的确定性规则关联合法性检查。
- 被接受参数变化的公开状态差异摘要。
- 针对非法、无法解析、越界、含私有信息、直接最终事实或不支持的事件候选的公开拒绝诊断。
- 合法事件被接受时的增量事件 payload 证据。
- focused backend/API 测试，覆盖合法事件接受、非法事件拒绝、受方向引导但仍符合规则的候选、脱敏以及差异一致性。

本包不得执行 live provider、不得创建 generated results、不得执行 checker、不得修改 checker fixtures、不得运行 external validation、不得添加 frontend 或 Validation Client 工作、不得实现 Agent continuity、narrative projection、diagnostic dialogue、durable scheduling，也不得修改 `backend/worldengine/`。

## 交付物

- 面向规则关联演化的公开事件候选合同。
- 带公开规则/状态证据的事件合法性结果合同。
- 被接受参数变化的状态差异产物合同。
- 在 active backend 范围内检查并接受合法事件候选的确定性 helper 或 API 行为。
- Focused tests，证明合法接受、非法拒绝、脱敏，以及与既有 event、runtime、rule-parameter、direction 和 public handoff surface 的兼容性。

Closeout 后交接到：

```text
0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence
```

## 当前授权

Documentation/contract/design/test-plan review 已通过。Implementation 仅授权本包记录的 scoped active-backend rule-linked evolution and event legality work。

Provider live calls、generated-result creation、checker execution、checker fixture changes、external validation、Validation Client changes、frontend UI、Agent continuity、narrative projection、diagnostic dialogue、durable scheduling 和 `backend/worldengine/` changes 仍未授权。

## 最终评估状态

Scoped active-backend `0.9.7` work 的 implementation 已完成。本次 implementation
session 中，focused verification、related public-surface regression 和 backend
regression 均已通过。Closeout 后交接到
`0.9.8-brain-inspired-agent-continuity-and-consolidation-evidence`
documentation-package creation/review。
