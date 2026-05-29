# E2E / Integration / API Smoke Validation Plan

状态：`restart ready`
类型：validation planning

## 目标

定义 v0.2 post-closeout E2E / integration / API smoke validation scope，但不执行任何
validation commands。

## 当前 Campaign 说明

本 package 之前已达到 review complete。对当前 `v0.2-post-closeout` goal campaign
而言，该 review 属于 archived evidence；campaign 进入
`02-e2e-validation-execution` 前，必须重新执行或带理由明确重新接受它。

## 范围

本 package 规划：

- repository and documentation checks。
- backend deterministic checks。
- schema smoke checks。
- event compatibility checks。
- runtime step checks。
- world events checks。
- event steps checks。
- params checks when available。
- archive checks when available。
- API smoke checks。
- E2E framework availability checks。
- release claim validation。
- concrete demo-world regression checks。

## E2E 定义

WorldEngine v0.2 不声明 product UI。对本 post-closeout package 来说，E2E 指：

- 如果有 runnable framework，则运行 browser E2E。
- 否则使用 backend integration 加 API smoke 加 release claim validation 作为 fallback。

如果不存在 E2E framework，或 suite 无法运行，必须把 E2E 记录为 not configured 或
blocked。不得把这种情况转成 successful result。

## 交付物

- `intent.md`
- `intent.zh.md`
- `contract.md`
- `contract.zh.md`
- `test-plan.md`
- `test-plan.zh.md`
- `plan.md`
- `plan.zh.md`
- `review.md`
- `review.zh.md`

## 最终评估状态

Restart ready。本 package 在当前 campaign 中尚未执行 validation。
