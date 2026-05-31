# 0.4.0 v0.4 规划与兼容性基线

状态：review complete
类型：documentation-only

## 目标

创建 v0.4 文档根目录、goal campaign 控制文件、版本计划、兼容性基线和 v0.3 交接映射，不修改实现文件。

## 范围

建立确定性的文档轨道，并保持实现授权关闭。

允许修改：

- 创建 `docs/iterations/v0.4/**` 父级和 child 文档。
- 定义 goal 入口 `完成 v0.4`。
- 定义 subagent/evaluator checkpoints 和 package sequence。
- 仅把 v0.3 收口后证据记录为 handoff context。

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
- [x] 契约已评审
- [x] 技术设计已评审
- [x] 测试计划已评审
- [x] 本 documentation-only package 不适用实现授权
- [x] 本 documentation-only package 不适用实现完成
- [x] 文档证据完成
- [x] 评审完成

## 最终评估状态

当前值：`review complete`。
