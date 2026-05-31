# 合同

状态：review complete

implementation_authorized: no

## 审计合同

本 package 必须 audit，而不是 implement。它只可以更新 v0.6 documentation 和 parent status
surfaces。

Audit 必须区分：

- current-session command evidence 与 historical handoff evidence。
- implementation checks 与 documentation checks。
- dashboard E2E smoke 与 product readiness。
- loader/runtime-context readiness 与 full runtime migration。
- generated `WorldSpec` validity 与 generation quality。
- v0.6 generation readiness 与 v0.7 external validation、v0.8 projection readiness。

## 必需 Evidence Index

Audit 必须包含以下 evidence：

- `0.6.0` 与 `0.6.1` documentation gates。
- `0.6.2` deterministic generator core。
- `0.6.3` structured generation plan compiler。
- `0.6.4` AI-assisted boundary and plan import。
- `0.6.5` preview API and generation metadata。
- `0.6.6` regeneration and runtime-readiness integration。
- `0.6.7` dashboard preview and E2E smoke。

## 兼容性要求

- Schema/API extensions 在 reviewed generation surface 内保持 additive。
- Existing API response envelopes 和 validation error behavior 保持兼容。
- Existing runtime tick/event behavior 不被 generation readiness checks 改变。
- Existing dashboard runtime、world、timeline、memory 和 agent panels 保持兼容。
- `backend/worldengine/` 保持 untouched。

## 退出标准

只有在以下条件满足时，才能把本 package 标记为 review complete：

- documentation checks 通过。
- changed-file scope guard 确认本 package 为 documentation-only work。
- documentation/evidence evaluator 报告无 P1/P2 findings。
- unresolved findings 已分类。
- release-candidate handoff recommendation 明确。
