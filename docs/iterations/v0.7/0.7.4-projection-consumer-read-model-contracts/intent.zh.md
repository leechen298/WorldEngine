# Intent

## Problem / Purpose

v0.7 已提供 public readiness manifest discovery，但 projection consumers 仍需要
generic read-model contracts，明确未来 read-only payloads 可以包含什么。没有这个边界，
后续工作容易泄露 private consumer details、创建 product-specific surfaces，或过早暗示
v0.8 projection application readiness。

## Why Now

`0.7.3` 已完成 public contract discovery semantics。下一步需要定义只读 projection model
language，供 `0.7.5` compatibility evidence 和 v0.8 application work 引用。

## Relationship To Roadmap

本 package 实现 v0.7 roadmap 中 projection consumer read-model contracts 的步骤。它面向
schema/contract，不构建 projection application、UI、product backend 或 write-enabled API。

## Non-Goals

- 不构建 projection app 或 dashboard。
- 不添加 API routes，除非 reviewed update 明确扩展 scope。
- 不添加 write APIs、reset APIs、persistence、migrations、private runner hooks 或
  consumer-specific backend logic。
- 不暴露 concrete external validation worlds、private app state、UI selectors、raw
  memory records、provider secrets、prompts、traces、transcripts 或 event payloads。
- 不声明 projection app readiness、product readiness、v0.8 readiness 或 external consumer PASS。

## Expected Handoff

Closeout 后，`0.7.5-quality-regression-and-compatibility-evidence` 接收 reviewed
projection read-model contract/schema/checker evidence，并可对 v0.7 已创建的 public
surfaces 运行 compatibility checks。
