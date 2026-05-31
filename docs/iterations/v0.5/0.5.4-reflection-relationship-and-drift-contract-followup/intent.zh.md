# 意图

状态：review complete

## 存在原因

Relationship state、self-summary、reflection records 和 personality drift signals
属于 pseudo-self continuity concepts。它们也很容易被过度实现：可能暗示 agent identity
changes、隐藏 action modifiers、summarization pipelines 或 world-specific personality rules。

`0.5.4` 将这些概念收紧为更明确的 contracts，并在本 child package 中保持 implementation
closed。

## 结果

- 明确每个概念的 evidence、provenance 和 inspectability rules。
- 保持 v0.4/v0.5 loop compatibility。
- 明确 `0.5.4` 不授权 schema-only implementation。
- 定义后续 package 添加 schemas 或 behavior 前必须证明的条件。

## 非目标

- 不做 backend code、schemas、tests、APIs、migrations、persistence 或 frontend changes。
- 不做 action modifiers、automatic reflection、self-summary generation 或 relationship
  behavior。
- 不添加 concrete world content、validation oracle details 或 application-specific
  backend logic。
- 不修改 `backend/worldengine/`。

## 交接

下一个 package `0.5.5-v0.5-evidence-and-compatibility-audit` 接收完整的 v0.5
evidence surface：已实现的 working/episodic memory substrate、read-only loop memory
context，以及 higher-risk concepts 的 deferred continuity contracts。
