# Intent

英文版本：`intent.md`。

0.10.4 把 session 推进为 bounded runtime execution unit。当前 global runtime controls
已经支持 bounded run 和 archive callbacks，但 external clients 需要 session-scoped controls
和 evidence references，才能从 session id 驱动 MVP flow，而不是使用松散的 global endpoints。

本包意图以 additive wrapper 复用现有 runtime behavior：

- 保持现有 `/runtime/*` endpoints 兼容。
- 要求 bounded run requests。
- paused sessions 在 resume 前阻塞 session runs。
- session run 后暴露 public event/snapshot deltas。
- 列出与 session-readable timeline 相关的 snapshots。

本包不证明 product PASS、Agent autonomy、provider quality 或 external checker PASS。它只证明
focused session runtime evidence slice。
