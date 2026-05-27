# 0.3.1 WorldSpec 加载器契约

状态：`评审完成`

类型：仅文档

## 目标

在实现加载器代码前，定义 WorldSpec 加载器契约。

## 范围

本包新增文档契约，定义未来加载器如何接收、解析、校验、返回或拒绝通用
`WorldSpec` 输入。

本包不实现加载器，不连接运行时，不修改 schema，不新增 API 路由，不创建
fixture，也不触碰前端行为。

## 文档

- [x] `intent.zh.md`
- [x] `contract.zh.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.zh.md`
- [x] `plan.zh.md`
- [x] `review.zh.md`

虽然本包是仅文档包，但它会准备后续代码包，因此保留
`technical-design.zh.md` 和 `test-plan.zh.md`。

## 交付物

- `docs/contracts/worldspec-loader-contract.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/README.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/intent.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/contract.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/technical-design.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/test-plan.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/plan.zh.md`
- `docs/iterations/v0.3/0.3.1-worldspec-loader-contract/review.zh.md`

## 状态清单

- [x] 文档已起草
- [x] 契约已评审
- [x] 技术设计已评审
- [x] 测试计划已评审
- [ ] 实现已完成
- [x] 文档证据已完成
- [x] 评审已完成

## 交接

评审批准后，`0.3.2-worldspec-loader-implementation` 可以按已评审契约实现
最小加载器。本包不得标记为 ready for implementation；实现就绪状态属于后续
代码或混合包，并且只能在文档评审通过后设置。
