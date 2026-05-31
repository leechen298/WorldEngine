# 意图

状态：review complete

## 问题

v0.5 需要在代码出现前把记忆与自我连续性概念定义清楚。否则后续实现可能把
working memory、event-linked memory、relationship state、self narrative、
reflection 和 drift 混成隐式副作用，难以检查和测试。

这些概念指向 agent pseudo-self，风险更高。WorldEngine 必须把它们定义成可检查的工程记录与信号，
而不是意识声明，也不能变成 application-specific behavior。

## 目标

本包完成后，WorldEngine 会拥有以下概念的稳定公开契约：

- working memory。
- episodic memory。
- relationship state。
- self-summary。
- reflection record。
- personality drift signal。

本包还定义 `0.5.2` 在只实现 working memory 和 episodic memory substrate 前必须证明的条件。

## 非目标

- 不实现任何 backend schema、store、service、route、frontend、test、fixture、migration 或 durable persistence behavior。
- 不把 memory context 接入 `POST /world/agent/loop/step`。
- 不修改 action semantics、accepted action types、params patch semantics、event behavior、runtime tick behavior 或 API envelope shape。
- 不实现 relationship behavior、self-summary generation、automatic reflection 或 personality drift action modifier。
- 不加入 concrete world content、external validation internal 或 application-specific backend logic。

## 为什么现在做

v0.5 roadmap goal 是 Memory and Self-Continuity Substrate。`0.5.0` 已创建 campaign boundary，
并把版本拆成 review-gated child packages。本包是 planning baseline 与第一个 implementation package 之间必需的契约层。

## North Star 对齐

North Star 要求 agent 能累积记忆、通过反馈更新，并通过 identity continuity、
self-narrative、relationship history、personality drift 和 decision pattern 形成持续的 pseudo-self。
本包用可检查契约支持这个方向，同时保留明确边界：WorldEngine 不声称真实意识。

## 预期交接

如果评审通过，本包交接给
`0.5.2-working-and-episodic-memory-substrate`。该包实现范围只限 additive generic
working-memory / episodic-memory schemas、in-memory substrate 和 focused backend tests。
