# Intent

英文版本：`intent.md`。

0.10.5 让 MVP session 可见。Backend 现在可以从 worldview input 创建 session，并用 public
evidence 运行 bounded session ticks，但 dashboard 仍呈现为分散的 backend/runtime/generation/world
panels。

目标 dashboard flow 是：

```text
enter worldview -> create session -> run bounded ticks -> inspect status,
timeline, and snapshots
```

UI 应保持 operational 且信息密集，不做 marketing-like 页面。它应展示 session id、generation
mode、runtime evidence 和 snapshot evidence，但不暴露 private prompts、provider traces 或 secrets。

Dashboard 仍是 client。Backend session/runtime APIs 仍是 system authority。
