# 0.12.4 Validation Client MVP Evidence Handoff

英文原文：`README.md`。

状态：review complete
类型：mixed documentation/contract package
implementation_authorized: no
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

定义独立 WorldEngine-Validation-Client iteration 执行 MVP validation 所需的 public evidence artifacts、result directory shape、operation/API log requirements、redaction checks、terminology 和 handoff prompt。

本包是 WorldEngine 侧 handoff contract。它不实现外部 client，不运行 provider live calls，不操作 external validation agent，也不声明 MVP PASS。

## 范围

评审通过后允许：

- 定义 MVP evidence artifact names 和 required/optional fields。
- 定义 public exported evidence 的 result directory shape。
- 定义 operation-log 和 API-log requirements。
- 定义 scorecard inputs 和 status taxonomy。
- 定义 redaction scan requirements。
- 定义世界内 Agent 与 external validation agent terminology。
- 为后续 Validation Client iteration 增加 Codex/OpenClaw-style handoff prompt。
- 只有本包后续记录 implementation authorization 时，才可增加 focused schema/checker documentation 或 tests。

禁止：

- 不在本仓库实现 Validation Client。
- 不让 client 拥有 provider calls、evaluator logic、world mutation、Agent autonomy 或 PASS decision authority。
- 不包含 raw/private evidence、raw thought、private memory、private goals、hidden context、provider traces、raw prompts、raw provider responses、secrets 或 private evaluator data。
- 不做 provider live calls、external validation execution、frontend、autonomous validation、complete MVP closeout 或 `backend/worldengine/` 变更。

## 交付物

- `mvp-evidence-artifact-contract.md`
- `validation-client-handoff-prompt.md`
- package docs、review evidence，以及 closeout 后的 parent route update。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`
- [x] `mvp-evidence-artifact-contract.md`
- [x] `validation-client-handoff-prompt.md`

## 状态清单

- [x] 文档已起草
- [x] Contract 已评审
- [x] Technical design 已评审
- [x] Test plan 已评审
- [ ] Implementation 已授权
- [ ] Implementation 已完成
- [ ] Tests 已完成
- [x] Review 已完成

## 当前判断

Documentation evaluator review 已通过。本包已完成 WorldEngine-side MVP evidence handoff contract。未授权 implementation、provider live-call 或 external validation execution。
