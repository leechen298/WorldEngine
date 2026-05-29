# v0.2 Post-Closeout Validation

状态：`planned / ready for review`
类型：post-closeout validation planning

## 目标

创建 v0.2 closeout 之后的独立验证文档链。

v0.2 feature 和 documentation closeout 已完成。v0.2 独立
E2E / integration validation 尚未执行。v0.2 Codex autonomous validation
尚未执行。

本 package 不重新打开 v0.2 implementation，不改变 v0.2 release status。本轮只创建
validation documents。

## 治理规则

本 validation documentation 位于 `docs/iterations/v0.2-post-closeout/`，并遵循
`docs/iterations/AGENTS.md` 中关于 evidence、review 和 post-closeout validation
的规则。

## 验证链

0. Master validation planning。
1. E2E / integration / API smoke validation plan。
2. E2E / integration / API smoke execution template。
3. Codex autonomous validation plan。
4. Codex autonomous validation execution and review template。
5. Final validation bundle template。

## Package Index

| Package | Type | Status | Purpose |
|---|---|---|---|
| `01-e2e-validation-plan` | validation-planning | review complete | 定义 v0.2 post-closeout E2E、integration 和 API smoke validation 范围。 |
| `02-e2e-validation-execution` | validation-execution | not executed | 执行 v0.2 post-closeout E2E、integration 和 API smoke validation。 |
| `03-codex-autonomous-validation-plan` | validation-planning | planned / ready for review | 定义独立 Codex autonomous validation 范围。 |
| `04-codex-autonomous-validation-execution` | validation-execution | not executed | 执行独立 Codex autonomous validation。 |
| `05-final-validation-bundle` | validation-bundle | not executed | 汇总最终 v0.2 post-closeout validation result。 |

## 结果状态

validation documents 可以使用以下状态：

- `planned`
- `ready for execution`
- `executed`
- `passed`
- `passed with P3`
- `blocked`
- `failed`
- `not executed`

本 package 中的 execution report 不记录成功结果。execution report 初始状态为
`not executed`，后续 validation run 必须用 current-session evidence 填写结果。

## 范围

允许：

- 定义 post-closeout validation workflow。
- 定义 report templates 和 evidence requirements。
- 定义 E2E / integration / API smoke execution expectations。
- 定义 Codex autonomous validation expectations。
- 定义 final validation bundle requirements。

禁止：

- 本 documentation pass 不运行 backend、frontend、E2E、API smoke、runtime、
  schema execution、fixture、migration 或 autonomous validation commands。
- 不修改 runtime、schema、API、frontend、backend tests、fixtures 或 external
  repositories。
- 不加入具体 demo-world 名称、地点、角色、资源、story rules、seed data、UI
  selectors 或 private oracle details。
- 不声明 v0.2 validation 已完成。
- 不改变 v0.2 final / complete status。

## 交付物

- `validation-master-plan.md`
- `validation-master-plan.zh.md`
- `validation-report-template.md`
- `validation-report-template.zh.md`
- `review.md`
- `review.zh.md`
- `01-e2e-validation-plan/`
- `02-e2e-validation-execution/`
- `03-codex-autonomous-validation-plan/`
- `04-codex-autonomous-validation-execution/`
- `05-final-validation-bundle/`

## 最终评估状态

documentation checks 通过后，本 documentation package 可进入 human / ChatGPT
review。
