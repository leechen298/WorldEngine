# Intent

英文源文件：`intent.md`。

v0.12 需要可见的 in-world Agent life evidence。现有 request-driven Agent loop surfaces
证明 perception 和 action adapters 存在，但它们本身不能证明 session-scoped Agent autonomy，
因为 client 可以直接提交 intent。

本包新增第一层 MVP Agent continuity：

- Agent 在 session 内有 public state。
- Agent step 读取 public runtime/session/event context。
- WorldEngine 选择 public intent state，例如 no-intent、wait、rest 或 bounded action。
- 结果作为 public evidence events 记录，供后续 memory、narrative、diagnostics 和 validation
  handoff packages 使用。

本包刻意保持最小，不实现 long-term memory consolidation、sleep、narrative/diagnostic
surfaces、external Validation Client automation 或 final MVP closeout。
