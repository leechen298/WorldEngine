# Intent

英文原文：`intent.md`。

## 问题

v0.12 现在已有公开 session Agent state、runtime step、memory summary 和 rest consolidation evidence。人类和验证工具仍需要一个可读检查层，用公开 artifact 汇总行为，但不能变成 world mutation 路径。

早期 external projection work 已经建立了 world-level narrative projection 和 diagnostic dialogue evaluation 的边界。MVP 需要面向 session 的版本，让验证器可以回答：

- 这个 session 和 tick range 里发生了什么？
- 使用了哪个 branch 或 Agent evidence？
- 投影是否保持只读？
- diagnostic inspection 是否仍在 out-of-world，并且不进入 Agent memory？

## 用户价值

MVP validator 可以通过可读 narrative 和 diagnostic summary 检查公开行为，而不只能阅读 raw event list。

## 工程价值

这个包把 v0.11 rule/evolution evidence 与 v0.12 Agent evidence 连接到后续 Validation Client evidence handoff，同时不把 client logic 嵌入 WorldEngine。

## 非目标

- 不把 story generation 作为 canonical world evolution。
- 不把 diagnostic chat 作为 in-world dialogue。
- 不通过 inspection 改变 personality、skill、relationship、inventory、injury、death 或 memory。
- 不做 provider live call。
- 不实现外部 Validation Client。
- 不做完整 MVP checker/closeout。
