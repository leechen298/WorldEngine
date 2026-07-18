# Intent

英文源文件：`intent.md`。

`0.12.1` 让 Agent 在 session 内变得可见。`0.12.2` 为这个 Agent 增加最小 public memory
trail。

目标不是模拟 private mind。MVP 需要 durable-looking、redaction-safe public summaries，让
validators 可以看到：

- Agent 公开观察到了什么。
- 记录了什么 short-term public memory。
- rest 何时把 observations consolidation 成 episodic public summary。
- 哪些 event/runtime refs 支撑该 summary。

本包刻意避开 personality 和 skill mutation、raw private memory、diagnostic conversation
memory，以及 final validation automation。
