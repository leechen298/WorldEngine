# Intent

英文镜像：`intent.md`。

## Problem

LLM-backed autonomous validation docs 已定义 provider live smoke、LLM-backed world
creation、rule parameter evolution、rule-compliant event generation、Agent persistent
autonomy evidence 和 full lifecycle validation，但它们仍是
`checker-extension-required`。

当前 saved-result autonomous checker 支持 basic dashboard 和 basic WorldEngine lifecycle
artifacts。它还不能根据 LLM-backed scenarios 需要的 public artifact set 分类结果，不能执行
LLM-backed scorecard critical items，也不能区分真实 structured result 和缺少 checker support
的 PASS 声明。

## Goal

本 package 完成后，LLM-backed autonomous result directories 具备 deterministic checker
support、scenario fixture coverage、redaction regression coverage，以及明确的
PASS/FAIL/BLOCKED/NOT_RUN classification rules。

## Non-goals

- 不运行 live provider calls。
- 不创建或重写 generated-result evidence 来强行 PASS。
- 不修改 product runtime behavior、public APIs 或 frontend UI。
- 不实现 Validation Client export behavior。
- 不声明 LLM-backed lifecycle PASS。
- 不修改 `backend/worldengine/`。

## Why Now

前面的 v0.9 packages 已创建 public provider、generated world、rules、runtime、direction、
event legality、Agent continuity 和 projection evidence surfaces。下一个 blocker 不是继续加
runtime capability，而是让 LLM-backed autonomous suite 获得 checker support，使后续 handoff
和 full-run packages 可以使用诚实的自动 verdict。

## North Star Alignment

本 package 通过让 LLM-backed world 和 Agent evidence 可检查、可验证来支持 North Star。它验证
public artifact contracts 和 redaction boundaries，不添加 concrete demo worlds、seed data、game
UI 或 application-specific logic，因此保持 WorldEngine generic。
