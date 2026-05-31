# 0.5.1 记忆与自我连续性契约

状态：review complete
类型：documentation-only
implementation_authorized: no

## 目标

定义 v0.5 后续可以实现的公开记忆与自我连续性概念：working memory、
episodic memory、relationship state、self-summary、reflection record 和
personality drift signal。

本包先建立 schema 语义、来源规则、授权条件、兼容性要求和明确的非目标；
在这些契约通过评审前，不修改 runtime、schema、API、service、frontend、
fixture、migration 或 test implementation。

## 范围

允许：

- 创建并更新本包文档及中文镜像。
- 为六个 v0.5 记忆 / 自我连续性表面定义公开概念契约。
- 为后续 implementation package 定义计划中的 additive schema 语义。
- 定义 `0.5.2` 在添加 working-memory 和 episodic-memory 代码前必须满足的授权条件。

禁止：

- 不实现 schema、store、service、API、frontend behavior、fixture、migration 或 test。
- 不把 memory 接入 Agent Loop perception 或 action path。
- 不让 memory、relationship state、self-summary、reflection 或 personality drift 改变 action selection 或 action result。
- 不加入具体 world name、map、character、location、resource、story rule、seed data、private validation oracle detail 或 application-specific backend logic。
- 不修改 `backend/worldengine/`。

## 交付物

- 完整 package document set 和中文镜像。
- 六个 v0.5 概念的契约语义。
- `0.5.2` 的 implementation authorization criteria。
- documentation-stage review evidence、evaluator evidence 和 scope guard evidence。

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

## 当前评估

本包是 documentation-only 且已完成 review。本包自身保持
`implementation_authorized: no`；`0.5.2` 必须通过自己的 documentation/contract
evaluator 后，才可以授权任何 code changes。
