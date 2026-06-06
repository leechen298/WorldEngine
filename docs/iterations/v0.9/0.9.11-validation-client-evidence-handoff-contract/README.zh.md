# 0.9.11 Validation Client Evidence Handoff Contract

英文镜像：`README.md`。

Status：documentation reviewed / no implementation authorized
Type：documentation contract package
implementation_authorized：no
provider_live_call_authorized：no
evidence_execution_authorized：no
external_validation_authorized：no

## Package

Name：`0.9.11-validation-client-evidence-handoff-contract`

## 目标

定义 Validation Client 可以展示或导出的 LLM-backed lifecycle public evidence bundle 和 artifact
fields，同时不让客户端拥有 provider calls、LLM behavior、evaluation authority 或 WorldEngine
private internals。

## Documents

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## Scope Summary

本 package 是 documentation-only。它定义 WorldEngine 产出、autonomous result checker 检查的
public evidence artifacts 交接契约。它只可更新本 package 和 parent v0.9 routing/review docs。

不得修改 Validation Client code、frontend code、backend runtime behavior、provider credential
handling、checker implementation、fixtures、generated results、external repositories 或
`backend/worldengine/`。

## Status Checklist

- [x] Docs drafted
- [x] Contract reviewed
- [x] Technical design reviewed
- [x] Test plan reviewed
- [x] Documentation review complete

## Current Route

```text
0.9.11-validation-client-evidence-handoff-contract-documentation-reviewed
```

Implementation 仍未授权。未来 package 或 external repository milestone 可以基于本 contract
实现 client display/export behavior。
