# Intent

## Problem

v0.8 需要让 WorldEngine 为 external validation 做准备，但不能把 external validator 吸收到
core repository。`0.8.3` 之后，core 已有 bounded readiness probe，但后续 package 仍需要
清楚定义哪些 public evidence 可以 hand off 给 external validator。

如果没有本 package，后续 smoke/evidence work 可能混淆：

- core-side evidence 和 external validation PASS。
- public evidence references 和 private validator artifacts。
- blocked/skipped/out-of-scope classifications 和 PASS。
- v0.7 checker/docs clean-pass evidence 和 v0.8 readiness。

## Objective

创建一个 reviewed documentation-only contract，定义 v0.8 的 external validation handoff
boundary。

该 contract 必须说明：

- WorldEngine 可以暴露或记录哪些 public handoff facts。
- 允许哪些 status values 和 evidence classes。
- redaction 与 forbidden-detail confirmation 如何表达。
- unresolved findings、blockers、skipped checks 和 out-of-scope surfaces 如何分类。
- 哪些 private external validator details 仍被禁止。

## Non-Goals

- 不实现 external validator。
- 本 package 不实现 schema/checker/template files。
- 不添加 API、runtime、frontend、backend test、fixture、migration、generated artifact、
  external repository 或 `backend/worldengine/` changes。
- 不运行或声明 external validation。
- 不声明 product readiness、projection app readiness、frontend/E2E PASS、Agent smoke
  PASS、autonomous PASS、generation quality PASS 或 final v0.8 readiness。

## Handoff Outcome

如果本 package reviewed，`0.8.5` 可以使用该 contract 记录 core-side smoke evidence 和
non-claims，而不需要 private external validation details。
