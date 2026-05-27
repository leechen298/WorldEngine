# 0.3.8 v0.3 Final Closeout

状态：`ready for review`

类型：仅文档

## 目标

在 0.3.7 发布候选包之后，为 v0.3 准备一个窄范围、仅文档的最终收口包，
不修改运行时、schema、API、前端、fixture、migration 或测试实现文件。

## 范围

本包定义 v0.3 最终收口所需的证据、验收检查和状态更新。只有当评审确认
0.3.7 发布候选包已被接受，并且没有未解决的 P1/P2 问题阻塞收口时，才可
执行最终收口。

本包在评审批准后的实现阶段，只能更新发布、里程碑、计划、问题清单和本包
评审文档。不得添加功能，不得用代码补证据缺口，也不得在未获批准时声明
最终发布。

## 文档

- [x] `README.md`
- [x] `README.zh.md`
- [x] `intent.md`
- [x] `intent.zh.md`
- [x] `contract.md`
- [x] `contract.zh.md`
- [x] `technical-design.md`
- [x] `technical-design.zh.md`
- [x] `test-plan.md`
- [x] `test-plan.zh.md`
- [x] `plan.md`
- [x] `plan.zh.md`
- [x] `review.md`
- [x] `review.zh.md`

## 状态清单

- [x] 文档已起草
- [x] 契约已起草
- [x] 技术设计已起草
- [x] 测试计划已起草
- [x] 文档阶段证据完成
- [ ] 人工 / ChatGPT 评审完成
- [ ] 最终收口已实现
- [ ] 评审完成

## 评审后的计划交付

- 更新 `docs/releases/v0.3.md`
- 更新 `docs/releases/v0.3.zh.md`
- 更新 `docs/iterations/v0.3/README.md`
- 更新 `docs/iterations/v0.3/README.zh.md`
- 更新 `docs/iterations/v0.3/v0.3-plan.md`
- 更新 `docs/iterations/v0.3/v0.3-plan.zh.md`
- 如果最终评审解决、接受、重定向或发现问题，则更新
  `docs/iterations/v0.3/findings.md`。
- 在 `review.md` 和 `review.zh.md` 中记录本包实现阶段证据。

## 假设

- 0.3.0 到 0.3.7 在最终收口执行前都保持 review complete。
- 0.3.7 发布候选包是最终收口的证据基础。
- v0.3 被标记为最终状态前，必须取得人工 / ChatGPT 批准。
- 开放的 P3 问题只有在最终评审明确接受为非阻塞时，才可作为已接受交接项
  保留。
- 最终收口时不得存在未解决的 P1/P2 问题。

## 开放风险

- 最终评审可能发现 P1/P2 证据缺口；该缺口必须阻塞收口，直到被解决或明确
  分类。
- 发布措辞可能误导读者认为运行时行为或测试已在本会话重新执行。最终收口
  必须区分历史包证据和 0.3.8 当前会话命令。
- 前端可见兼容性证据仍然是间接证据，除非评审者在最终收口前要求新的 UI 或
  E2E smoke 覆盖。
- 如果实现阶段不一起检查发布文档、里程碑索引、计划文档和包 README，状态
  可能发生漂移。
