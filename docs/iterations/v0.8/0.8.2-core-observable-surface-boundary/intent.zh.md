# 意图

## 问题 / 目的

`0.8.1` 已定义 minimum working-state taxonomy，但后续 packages 仍需要精确边界：validator
或 projection consumer 可以从 core repository 观察什么。如果没有这个边界，v0.8 容易漂移到
private validator behavior、product-specific backend logic，或过度暴露 memory/runtime 信息。

本 package 在任何 implementation 或 smoke evidence package 启动前，先定义 observable
public surface families。

## 为什么现在做

`0.8.1` review 后，`/goal` route 已选择 `0.8.2`。下一个 implementation-bearing package
`0.8.3` 必须先知道哪些 public core surfaces 可以 harden，哪些 exposure 仍然禁止。

## 与 roadmap 的关系

v0.8 为 external validator 准备 core-side readiness。本 package 把 v0.8 与 v0.7 的
projection/readiness contracts 转成后续工作可使用的 observable boundary，但不实现这些 surfaces。

## 非目标

- 不实现 schemas、checkers、APIs、UI、tests、evidence artifacts 或 runtime changes。
- 不运行 core-side smoke evidence。
- 不定义 external validator connection flows 或 private scenarios。
- 不声明 observable surface readiness 或 minimum working-state evidence。

## 预期交接

`0.8.3-generation-runtime-agent-loop-readiness` 接收：

- allowed observable surface families。
- forbidden exposure rules。
- implementation authorization criteria。
- compatibility 和 redaction expectations。
