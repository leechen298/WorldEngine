# Intent

英文镜像：`intent.md`。

## Problem

v0.9 已具备 WorldEngine-owned provider、world generation、rule、runtime、direction、Agent
continuity、projection/diagnostic，以及 LLM-backed saved-result checker support。Validation
Client 仍需要 stable public contract，明确在验证 LLM-backed lifecycle 时可以展示或导出哪些
artifacts。

如果没有这个 contract，client 可能误变成 evaluator、发明缺失的 LLM behavior、索要 provider
secrets、暴露 private evidence，或导出 WorldEngine checker 无法消费的 artifact shapes。

## Intent

定义 redacted public handoff contract，让 client 只负责把 WorldEngine evidence 交给 humans 和
checkers。Contract 必须保持以下边界：

- WorldEngine 拥有 provider calls、generated world behavior 和 canonical evidence。
- Checker 拥有 PASS/FAIL/BLOCKED/NOT_RUN classification。
- Client 只拥有 display/export。
- Evidence bundle 必须 public、redacted、基于 relative paths，且足够 stable 供后续 client 实现。

## Non-Intent

本 package 不实现 client UI、client export code、provider calls、live validation、generated
results、checker changes 或 backend runtime behavior。
