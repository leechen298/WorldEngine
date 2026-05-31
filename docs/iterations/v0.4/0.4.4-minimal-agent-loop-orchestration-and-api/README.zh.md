# 0.4.4 最小 Agent 闭环编排与 API

状态：review complete
类型：mixed or code

## 目标

接入 request-driven 最小世界内 Agent 闭环：构建 perception，获得或接受 intent，校验并应用 intent，发出可审查 result evidence，并返回稳定 API response。

## 范围

连接最小 loop 和已评审 API 边界，不添加后台自治。

允许修改：

- 在获批 `backend/app/` 模块下添加 request-driven loop service。
- 以 additive 方式扩展既有 agent-loop schemas，用于 loop step request/response models。
- 只有 contract 授权时才新增一个已评审 API route。
- 通过 backend app factory 和 route dependency state 注册/接入 loop service。
- 测试中使用确定性 provider 或显式 test intent。
- 添加聚焦 service/API 测试和相邻兼容性检查。

禁止修改：

- 不得添加记忆、情节记忆、关系状态、自我摘要、反思或人格漂移；这些属于 v0.5。
- 不得添加世界生成；这属于 v0.6。
- 不得添加外部验证 runner 就绪或报告自动化；这属于 v0.7。
- 不得添加投影应用就绪；这属于 v0.8。
- 不得添加具体世界名称、地图、角色、地点、资源、故事规则、seed data、UI 特定应用行为或私有验证 oracle 细节。
- 不得在 `backend/worldengine/` 下新增 runtime feature。
- 不得替换或破坏 `/world/agent/params/propose-and-apply`。

## 交付物

- 完整 package docs 和中文镜像。
- 实现后记录聚焦测试、兼容性测试和必需 subagent/evaluator checkpoints。
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
- [x] 契约已评审
- [x] 技术设计已评审
- [x] 测试计划已评审
- [x] 已授权实现，如适用
- [x] 实现完成，如适用
- [x] 测试/证据完成
- [x] 评审完成

## 最终评估状态

当前值：`review complete`。
