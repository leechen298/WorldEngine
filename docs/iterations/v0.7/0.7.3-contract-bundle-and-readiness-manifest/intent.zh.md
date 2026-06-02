# Intent

## Problem / Purpose

v0.7 已经有 reviewed public readiness contracts 和 redacted validation report
checker，但 external validation suite 仍需要知道哪些 contract files、schemas、
report formats 与 evidence classifications 属于 public v0.7 readiness surface。

本 package 创建 generic readiness manifest，让 external consumers 不依赖 private
chat context、internal repository structure 或 consumer-specific fixture details，也能发现
WorldEngine 的 public surfaces。

## Why Now

`0.7.2` 已完成 machine-checkable redacted report semantics。下一步稳定边界是
public manifest，用来引用这些 semantics 和 reviewed contract surfaces，并支撑后续
projection-consumer work。

## Relationship To Roadmap

本 package 实现 v0.7 roadmap 中 contract bundle 与 readiness manifest discovery 的步骤。
它保持 generic and public，不构建 projection read models、external validation suites、
product apps 或 runtime features。

## Non-Goals

- 不运行 external validation suite。
- 不实现 projection read models 或 APIs。
- 不加入 private suite configuration、private paths、UI selectors、oracle internals、
  transcripts、event payloads、concrete worlds、seed data 或 consumer-specific examples。
- 不修改 runtime、API、frontend、persistence、migrations、generation、Agent loop、
  memory 或 event behavior。
- 不声明 product readiness、projection readiness、external suite PASS 或 release readiness。

## Expected Handoff

Closeout 后，`0.7.4-projection-consumer-read-model-contracts` 会接收 reviewed public
manifest 与 checker evidence，用来识别 projection read-model contracts 可引用的 public
contract surfaces 和 readiness classifications。
