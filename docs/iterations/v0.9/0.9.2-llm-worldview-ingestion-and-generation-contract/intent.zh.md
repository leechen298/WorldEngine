# Intent

英文镜像：`intent.md`。

## Problem

WorldEngine 当前暴露的是 deterministic generic public world creation。这个路径对 v0.8
handoff 和 compatibility 有价值，但不能证明 WorldEngine 能把用户的 basic worldview premise
转成 LLM-supported、premise-specific、system-digestible world model。

v0.9 现在已有 provider smoke boundary，但 provider readiness 或 provider smoke endpoint
本身不会生成世界。下一个缺口是把 public worldview input、WorldEngine-owned generation、
provider/fallback classification、redacted evidence 和 runtime-digestible generated world
output shape 连起来的 contract。

## Goal

创建完整、可 review 的 `0.9.2` mixed-package contract，后续可实现：

- 接受 public basic worldview premise。
- 生成 public generated world model summary，而不是只返回 deterministic generic response。
- 分类 generation 是 provider-backed、deterministic fallback、not configured 还是 blocked。
- 暴露 premise specificity、system digestibility、runtime readiness 和 redaction 的 validation metadata。
- 保持 existing deterministic `POST /worlds` behavior compatible。

## Non-goals

- documentation stage 不实现代码。
- documentation/contract review 前不授权 implementation。
- 不运行 live provider calls。
- 不声明 LLM-backed world creation PASS。
- 不创建 concrete demo-world fixtures 或 validation seed worlds。
- 不修改 Validation Client，也不让它生成内容。
- 不实现 public outline 之外的 world rules。
- 不实现 bounded runtime controls、rule-linked evolution、event legality、Agent
  continuity、narrative projection、diagnostic dialogue、checker scorecards 或 full
  lifecycle validation。

## Why Now

v0.8 basic lifecycle handoff 证明 basic world creation 可以支撑 external validation
readiness，但 LLM-backed validation suite 仍被 provider proof、LLM-backed world creation、
rule-linked evolution、event legality、persistent Agent autonomy evidence 和 checker/schema
support 阻塞。`0.9.1` 解决 provider smoke 和 redaction boundary，但不生成世界。`0.9.2`
是下一步必要桥梁：定义一个可 inspect、可 validate 的 generated world contract，同时不泄露
provider internals，也不把 engine 收窄成具体 application world。

## North Star Alignment

本工作支持 WorldEngine north star：让 world generation 成为 generic engine-owned capability。
Generated worlds 必须 structured、validated、inspectable；runtime compatibility 保持稳定；
external projection 或 validation clients 只消费 public contracts，而不拥有 LLM behavior。
