# Intent

## Problem / Purpose

v0.10 在 v0.9 full LLM-backed lifecycle validation 以 BLOCKED closeout 后，开始更窄的
MVP delivery track。若没有具体第一个 child package，agent 可能会把 v0.10 parent plan
误当成 implementation authorization，或继续等待 v0.9 provider/client blockers。

本包把 parent route 转成具体 documentation baseline，并记录 handoff boundary。

## Why Now

v0.10 parent docs 已完成草拟并 ready for review。当前 `CURRENT_STATE.md` route
说明没有 active child，下一步是 review parent documentation，然后创建或批准 `0.10.0`。

## Relationship To Roadmap

roadmap 将 v0.10 定义为 “MVP Debug Contract And Runnable World Session”。本包不构建
该 session，而是准备路由，让下一包先定义并实现 public manifest/debug handoff contract，
之后再开始 session work。

## Non-Goals

- 不做 backend、frontend、schema、API、checker、fixture、migration、provider 或
  Validation Client implementation。
- 不做 evidence execution 或 live provider call。
- 不声明 v0.10 已 runnable、validated、product-ready 或 externally automated。
- 不把 v0.9 BLOCKED evidence 转换成 v0.10 PASS claim。
- 不加入 concrete demo-world content 或 application-specific backend behavior。

## Expected Handoff

本包关闭后，v0.10 应路由到
`0.10.1-mvp-public-manifest-and-debug-handoff-documentation-package-needed`。
implementation 继续关闭，直到 `0.10.1` package 文档集创建、评审并记录
`implementation_authorized: yes`。
