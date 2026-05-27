# 0.3.7 v0.3 发布候选包

状态：`review complete`

类型：仅文档

## 目标

准备 v0.3 发布候选证据包，供人工 / ChatGPT 评审；不声明 v0.3 最终发布，
也不修补缺失功能。

## 范围

本包汇总已完成的 v0.3 迭代证据、兼容性覆盖、限制、假设、未解决问题和最终
收口前置条件。它是已有证据的评审包，不是运行时、schema、API、前端、
fixture、迁移或测试实现包。

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
- [x] 文档阶段证据已完成
- [x] 发布候选包已完成
- [ ] 人工 / ChatGPT 评审完成
- [ ] 评审完成

## 交付物

- `docs/iterations/v0.3/v0.3-release-candidate-bundle.md`
- `docs/iterations/v0.3/v0.3-release-candidate-bundle.zh.md`
- `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.md`
- `docs/iterations/v0.3/0.3.7-v0.3-release-candidate-bundle/final-review-bundle.zh.md`
- `review.md` 和 `review.zh.md` 中的本包评审证据
- v0.3 里程碑索引和计划文档中的状态更新

## 假设

- 0.3.0 到 0.3.6 的包评审仍是历史包证据的事实来源。
- 0.3.7 可以组装候选包，但 v0.3 最终发布仍受 0.3.8 约束。
- 发布候选声明必须可追溯到已有评审、`evidence-index.md`、
  `compatibility-audit.md` 或明确的限制说明。
- 未阻塞发布候选评审的 P3 问题可以作为交接项保留。

## 开放风险

- 如果人工 / ChatGPT 评审发现 P1/P2 证据缺口，0.3.8 最终收口必须保持
  阻塞，直到缺口被解决或被明确接受。
- 除非评审要求新的 UI 或 E2E 冒烟覆盖，否则前端可见兼容性证据仍是间接的。
- 历史包证据来自较早的包会话；本包不会重新运行运行时或构建测试，除非
  `review.md` 明确记录。
