# Intent

英文镜像：`intent.md`。

## 为什么需要本包

外部验证客户端已经可以记录 evidence bundle、Agent 操作日志和人工验证交接材
料。WorldEngine 侧仍需要更清晰地规划两个前置条件：

1. LLM provider readiness：可以配置和观察，但不能暴露 secret。
2. public handoff manifest：外部验证消费者可以读取，但不会知道私有 validator
   细节。

本包在任何后续 code、API、schema 或 checker 实现开始前，把这些前置条件写清
楚。

## 问题

如果没有本计划，后续 agent 容易混淆职责：

- 验证客户端可能试图管理 LLM key 或 provider。
- WorldEngine 可能把 provider trace、private prompt 或 validation internals 泄漏到
  public report。
- 外部 Agent 验证可能期待 WorldEngine 尚未定义的字段。
- 历史 v0.7 / v0.8 closeout evidence 可能被过度声明为 external validation
  readiness。

## 期望结果

本包 review 后，后续实现聊天可以创建 scoped child package，公开 redacted
handoff manifest 和 provider readiness contract。外部验证客户端随后可消费这些
public surfaces，同时保持验证实现和人工判断在 WorldEngine 核心仓库之外。
