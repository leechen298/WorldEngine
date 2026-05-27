# 0.3.3 Runtime Context Bridge Contract

状态：`review complete`

类型：仅文档

## 目标

定义已验证的 `WorldSpec` 派生数据如何成为可选运行时上下文，但不实现桥接层，
也不改变运行时行为。

## 范围

本包新增运行时上下文桥接契约文档，定义桥接输入、派生上下文形状、兼容性
规则、禁止行为，以及 `0.3.4` 实现前必须提供的证据。

本包不实现桥接层，不改变 `RuntimeEngine`，不修改 schema，不新增 API 路由，
不发出事件，不改变归档或参数行为，不创建 fixture，也不触碰前端行为。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

本包虽然是仅文档包，但会准备后续代码包，因此包含 `technical-design.md` 和
`test-plan.md`。

## 交付物

- `docs/contracts/runtime-context-bridge-contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/README.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/intent.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/contract.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/technical-design.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/test-plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/plan.md`
- `docs/iterations/v0.3/0.3.3-runtime-context-bridge-contract/review.md`
- 对应的 `*.zh.md` 镜像。

## 状态清单

- [x] 文档已起草
- [ ] 契约已评审
- [ ] 技术设计已评审
- [ ] 测试计划已评审
- [ ] 实现完成
- [x] 文档证据完成
- [ ] 评审完成

## 交接

文档评审批准后，`0.3.4-runtime-context-bridge-implementation` 可以实现最小
可选桥接层。本包不能标记为 ready for implementation；实现准备状态属于后续
代码或混合包，并且只能在评审通过后设置。
