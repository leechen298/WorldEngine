# Intent

## Problem

v0.7 readiness work 容易过度声明 product readiness，或泄露 private external validation details。
在实现 report schemas、checkers、readiness manifests、projection payloads 或 APIs 前，
WorldEngine 需要 reviewed public semantics，明确 external validation 和 projection consumer
readiness 的含义。

## Goal

创建 documentation-only contract package，定义 readiness claim taxonomy、redacted evidence
requirements、projection consumer boundaries、compatibility requirements，以及 `0.7.2` 的
authorization criteria。

## Why Now

`0.7.0` 已建立 campaign routing 和 external-consumer boundaries。下一步需要让这些边界足够具体，
使后续 code-bearing packages 能实现 schemas 和 checkers，而不是临时发明 product-specific 或 private
validation semantics。

## Relationship To Roadmap

本 package 是 v0.7 的 contract stage。它准备 `0.7.2` report schema and redaction checker、
`0.7.3` readiness manifest，以及 `0.7.4` projection read-model work，同时保持 v0.8 projection
application work out of scope。

## Non-goals

- 不实现 report schemas 或 redaction checkers。
- 不实现 contract bundle 或 readiness manifest tooling。
- 不实现 projection read-model schemas 或 APIs。
- 不运行 external validation suites。
- 不声明 runtime/API/frontend/E2E/Agent/autonomous/product/release readiness。
- 不添加 concrete external-world 或 product-specific examples。

## Expected Handoff

`0.7.2-validation-report-schema-and-redaction-checker` 接收 reviewed redacted report semantics、
readiness status values、forbidden leaked-detail rules 和 checker authorization criteria。

## North Star Alignment

本 package 通过让 external validation suites 和 projection applications 成为 WorldEngine public
contracts 的 consumers，保护 generic engine boundary。它不把 WorldEngine 变成 validation app、
projection app 或 product-specific backend。
