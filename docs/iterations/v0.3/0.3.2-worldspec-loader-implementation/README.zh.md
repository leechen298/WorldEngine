# 0.3.2 WorldSpec 加载器实现

状态：`待评审`

类型：文档与代码混合或代码

## 目标

按已评审的 `0.3.1-worldspec-loader-contract` 实现最小通用 `WorldSpec`
加载器，但不把已加载数据接入运行时。

## 范围

本包后续可新增一个小型加载器模块和聚焦后端测试，用于证明通用 `WorldSpec`
输入可以被解析、校验，并在失败时返回结构化错误。

本包不得把加载器连接到 `RuntimeEngine`、API 路由、持久化、事件、归档快照、
参数、前端行为、外部 fixture 仓库或具体外部验证世界。

## 文档

- [x] `intent.zh.md`
- [x] `contract.zh.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.zh.md`
- [x] `plan.zh.md`
- [x] `review.zh.md`

本包包含完整英文文档和中文镜像。

## 交付物

实现阶段：

- `backend/app/core/worldspec_loader.py`
- `backend/app/tests/test_worldspec_loader.py`
- 本包中的文档评审证据。

文档阶段：

- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/README.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/intent.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/contract.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/technical-design.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/test-plan.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/plan.zh.md`
- `docs/iterations/v0.3/0.3.2-worldspec-loader-implementation/review.zh.md`
- 对应英文文档。

## 状态清单

- [x] 文档已起草
- [ ] 契约已评审
- [ ] 技术设计已评审
- [ ] 测试计划已评审
- [ ] 实现已完成
- [x] 文档证据已完成
- [ ] 评审已完成

## 交接

文档评审批准后，本包可标记为 ready for implementation。实现必须使用
`worldengine-iteration-dev`，遵循本包文档，并在 `review.md` /
`review.zh.md` 中记录当前会话的实现和测试证据。
