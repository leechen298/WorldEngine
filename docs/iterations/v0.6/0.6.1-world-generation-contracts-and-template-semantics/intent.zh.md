# 意图

Status: review complete

## 问题 / 目的

v0.6 会加入第一个世界生成能力，但 generated world 只有在契约先被明确评审后，才
能成为安全的 engine input。如果没有已评审的 contract，后续实现可能会误做以下事
情：

- 在 core repository 中存储具体 demo-world 内容。
- 把 AI output 当成未经验证的隐藏副作用。
- 生成无法通过现有 `WorldSpec` loader 的数据。
- 暗示当前 evidence 尚不支持的 runtime、API、quality、validation 或 release
  claim。

本 package 在实现开始前定义这些边界。

## 为什么现在做

`0.6.0` 已完成 v0.6 campaign baseline，并把路线交给当前 active child。
`CURRENT_STATE.md` 现在把目标路由到
`0.6.1-world-generation-contracts-and-template-semantics`，且 implementation
authorization 仍关闭。下一个 package `0.6.2` 不能在缺少公开概念和模板语义评审
的情况下安全实现 deterministic generator core。

## 与 roadmap 的关系

roadmap 将 World Generation v1 交给 v0.6：从模板和结构化 AI-assisted plan 生成
可运行的 `WorldSpec` 数据。本 package 是该 roadmap item 的契约层。它保留 v0.3
`WorldSpec` loader/runtime-context bridge、v0.4 Agent Loop 边界和 v0.5 memory
substrate，同时为后续 additive generation work 做准备。

## 非目标

- 不实现 generation schema、service、API、UI、test、fixture、persistence 或
  migration。
- 不定义 external validation readiness；这属于 v0.7。
- 不定义 projection application readiness；这属于 v0.8。
- 不加入具体 world content、example、seed data、validation oracle 细节或
  application-specific backend 行为。
- 不加入 live external AI-provider integration。
- 不改变 runtime tick behavior、event emission、loader behavior、runtime-context
  derivation、Agent Loop behavior、memory behavior、params、archive 或 frontend
  behavior。

## 预期交接

本 package 向 `0.6.2` 交接一个已评审、documentation-only 的契约，用于第一个
deterministic generator core。交接内容包括：

- 公开概念名称与字段语义。
- 保持 generic 和 deterministic 的模板语义。
- validation 与 diagnostics 预期。
- 针对现有 engine surfaces 的兼容性约束。
- `0.6.2` 记录 `implementation_authorized: yes` 前必须满足的条件。
