# 0.4.1 世界内 Agent 闭环契约

状态：planned
类型：documentation-only

## 目标

在代码变更前定义 v0.4 世界内 Agent 闭环的公开概念、事件语义、API 边界、错误模型和实现授权条件。

## 范围

定义 PerceptionFrame、ActionIntent、ActionResult 和 loop-step 语义。

允许修改：

- 定义 `PerceptionFrame`、`ActionIntent`、`ActionResult` 和 `LoopStep` 语义。
- 仅以文档定义 event 和 error model contracts。
- 定义允许动作词汇：`noop` 和经过校验的 `params.patch`。
- 定义 API boundary，但本包不新增 route。

禁止修改：

- 本 documentation-only package 不得修改 runtime、schema、API、frontend、backend test、fixture、migration 或 legacy 实现文件。
- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。

## 交付物

- 完整 package docs 和中文镜像。
- documentation-only verification 和未运行代码测试的理由。
- 记录 changed files、commands、compatibility review、scope review 和 P1/P2/P3 findings 的 review。

## 文档

- [x] `README.md`
- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

本包需要中文镜像，并在同一轮文档创建中生成。

## 状态清单

- [x] 文档已草拟
- [ ] 契约已评审
- [ ] 技术设计已评审
- [ ] 测试计划已评审
- [ ] 已授权实现，如适用
- [ ] 实现完成，如适用
- [ ] 测试/证据完成
- [ ] 评审完成

## 最终评估状态

当前值：`planned`。
