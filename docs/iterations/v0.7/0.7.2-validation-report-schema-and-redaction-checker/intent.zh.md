# Intent

## Problem / Purpose

v0.7 需要 trustworthy external-validation evidence rules，后续 packages 才能 archive
redacted reports、bundle contracts，或声明 core-side compatibility readiness。
当前 report template 只是 human-readable，并且仍列出 `pass / fail / blocked`；
reviewed `0.7.1` readiness contract 要求 `pass`、`fail`、`blocked`、`skipped`
和 `out_of_scope` 是 distinct states。

本 package 把这些 reviewed semantics 转成 generic report schema 和 checker，
同时不把 external validation application 或 private consumer detail 引入 WorldEngine。

## Why Now

`0.7.1` 已完成 public readiness 与 projection consumer contracts。它的 P3 handoff
明确要求 `0.7.2` 对齐 `docs/validation-report-template.md` 和 future
schema/checker，使它们支持新的 `skipped` 与 `out_of_scope` semantics。

后续 `0.7.3` readiness-manifest work 应消费 machine-checkable report semantics，
而不是只依赖 prose。

## Relationship To Roadmap

本 package 支撑 v0.7 roadmap：通过 public contracts 和 redacted evidence rules，
让 WorldEngine 准备好被 external validation suites 和 projection consumers 消费。
它不实现 external suites、projection applications、runtime features 或
product-specific behavior。

## Non-Goals

- 不运行或实现 external validation suite。
- 不加入 private examples、fixture paths、UI selectors、hidden reset APIs、
  oracle internals、transcripts、event payloads、concrete worlds、characters、
  locations、story rules 或 seed data。
- 不改变 runtime、API、frontend、persistence、migrations、generation、
  Agent loop、memory 或 event behavior。
- 不声明 product readiness、projection readiness、release readiness 或 external suite PASS。

## Expected Handoff

Closeout 后，`0.7.3-contract-bundle-and-readiness-manifest` 接收：

- reviewed report schema path。
- reviewed checker path。
- focused checker test evidence。
- updated template semantics。
- explicit scope and compatibility evidence，证明本 package 没有改变
  runtime/API/frontend behavior，也没有引入 external consumer internals。
