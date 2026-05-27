# 0.3.5 External Fixture Contract Readiness

状态：`review complete`

类型：仅文档

## 目标

定义外部验证样例运行器如何通过公开契约消费 WorldEngine，同时不在核心仓库内
创建外部仓库、具体样例内容或私有验证内部细节。

## 范围

本包新增公开的外部验证样例运行器契约，并补齐说明外部运行器如何调用
WorldEngine、如何返回脱敏证据的迭代包文档。

本包不实现代码，不创建样例，不添加测试输入，不添加外部仓库，不定义重置
API，不暴露 UI 选择器，不修改 schema，不改变运行时行为，不添加 API 路由，
不实现产品验证应用。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

由于本仅文档包为后续外部消费者契约和证据流程做准备，因此包含
`technical-design.md` 和 `test-plan.md`。

## 交付物

- `docs/contracts/external-fixture-runner-contract.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/README.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/intent.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/contract.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/technical-design.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/test-plan.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/plan.md`
- `docs/iterations/v0.3/0.3.5-external-fixture-contract-readiness/review.md`
- 对应的 `*.zh.md` 迭代包镜像文档。

## 状态清单

- [x] 文档已起草
- [ ] 契约已评审
- [ ] 技术设计已评审
- [ ] 测试计划已评审
- [ ] 实现已完成
- [x] 文档证据已完成
- [ ] 评审已完成

## 交接

文档评审通过后，未来外部验证样例运行器可以把该契约作为公开消费边界。
本包不得标记为 `ready for implementation`；代码或混合实现必须进入后续已评审
迭代包。
