# 0.12.5 Full Lifecycle Checker And Autonomous Validation

英文原文：`README.md`。

状态：review complete / PARTIAL
类型：mixed validation package
implementation_authorized: no
evidence_execution_authorized: yes for deterministic autonomous checker commands only
provider_live_call_authorized: no
external_validation_authorized: no

## 目标

使用 checker/scorecard/review evidence 对 v0.12 MVP full lifecycle 做分类，同时诚实区分 deterministic saved-result checker validation 与 fresh external Validation Client autonomous execution。

## 范围

评审通过后允许：

- 运行现有 WorldEngine deterministic autonomous checker commands。
- 验证 existing saved-result fixtures，包括 full lifecycle autonomous fixture。
- 记录 scorecard/checker evidence paths 和 command outputs。
- 只有当前已存在 exported result directory 并在当前 session 被检查时，才可把 fresh external Validation Client execution 分类为 PASS、PARTIAL、BLOCKED 或 FAIL。
- 当 external client、provider/environment、checker assets、permissions 或 result directory 缺失时记录 BLOCKED。

禁止：

- 不为强行 PASS 修改 product code。
- 不在本仓库实现 Validation Client。
- 除非 WorldEngine/environment configuration 和 package review 明确授权，不做 provider live-call。
- 不把 UI smoke 当 full lifecycle validation。
- 不把历史 v0.8/v0.9/v0.10/v0.11 result 复用为 v0.12 PASS。
- 不包含 hidden evaluator data、raw/private evidence、raw thought、private memory、private prompts、provider traces、raw provider responses 或 secrets。
- 不做 complete MVP closeout；它属于 `0.12.6`。

## 预期交付物

- `full-lifecycle-validation-result.md`
- `scorecard-summary.md`
- `read-only-evaluator-review.md`
- package review evidence，以及 closeout 后 parent route update。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## 状态清单

- [x] 文档已起草
- [x] Contract 已评审
- [x] Technical design 已评审
- [x] Test plan 已评审
- [x] Evidence execution 已授权
- [x] Checker verification 已完成
- [x] Fresh external validation 已分类
- [x] Review 已完成

## 当前判断

Deterministic autonomous checker evidence 已通过。Fresh external Validation Client validation 因没有 current v0.12 result directory 而 BLOCKED。Read-only evaluator review 已通过这个 bounded classification。Package classification 为 PARTIAL，不支持 v0.12 MVP PASS claim。
