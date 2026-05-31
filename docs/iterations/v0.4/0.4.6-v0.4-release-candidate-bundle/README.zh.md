# 0.4.6 v0.4 发布候选包

状态：review complete
类型：documentation-only

## 目标

从已评审实现和审计证据准备 v0.4 release-candidate bundle，不声明最终发布，也不添加实现变更。

## 范围

打包评审证据，但不声明发布。

允许修改：

- 在 `docs/iterations/v0.4/` 下创建 release-candidate bundle docs。
- 汇总 package statuses、evidence、commands、findings 和 compatibility claims。
- 定义 0.4.7 的 final review questions。
- 使用 evaluator review 检查 claim support 和 mirror quality。

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

## 补充文档

- [x] `release-candidate-bundle.md`
- [x] `release-candidate-bundle.zh.md`

## 状态清单

- [x] 文档已草拟
- [x] 契约已评审
- [x] 技术设计已评审
- [x] 测试计划已评审
- [x] 实现不适用于本 documentation-only package
- [x] 实现完成不适用于本 documentation-only package
- [x] 文档证据完成
- [x] 评审完成

## 最终评估状态

当前值：`review complete`。
