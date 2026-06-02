# Natural-Language Validation Triggers

Status: reusable agent routing guide

英文版本：`natural-language-validation-triggers.md`。

当用户说出这类短 validation request 时使用本指南：

```text
测试 <version>
验证 <version>
<version> 是否通过
测试 <iteration-package>
验证当前产品
clean pass
```

## Primary Workflow

执行 `docs/testing/product-capability-validation-playbook.zh.md`。

Trigger phrase 只表示用户要求执行或分类 validation；它本身不是 PASS verdict。

## Boundary

报告结果前必须：

- 读取 active version 或 package state。
- 确定 in-scope validation surface。
- 识别 out of scope 或 unsupported 的 surfaces。
- 如果 validation 会修改 tests、checkers、fixtures、result schemas、
  runtime/API/frontend behavior 或 durable evidence rules，先创建或使用所需 iteration
  package。

不要因 validation trigger 静默修改 implementation 或 test infrastructure。如果需要 repair
或新增 tests，必须通过 package gate 路由。

## Required Classification

每个 in-scope command、checker、suite 或 workflow 必须分类为：

- passed。
- failed。
- blocked。
- skipped。
- out of scope。

不要把 blocked、skipped 或 out-of-scope 写成 pass-equivalent language。

## Required Distinctions

Validation reports 必须区分：

- backend/unit/checker tests。
- frontend unit/build checks。
- Browser E2E。
- Agent smoke。
- minimal autonomous saved-result validation。
- full autonomous runner/full suite。
- manual observation。
- external validation suite evidence。
- projection readiness。
- product readiness。

如果当前 evidence 没有覆盖其中某个 surface，必须点名 exclusion，不得暗示更宽范围 PASS。

## Evidence Requirements

报告 validation verdict 前必须记录：

- 当前 branch、commit 和 worktree state。
- 实际运行的 exact commands 或 workflows。
- 每个 command 的 exit status 和 result summary。
- E2E、Agent smoke、autonomous、external reports 或 generated summaries 的 raw artifact
  paths。
- unresolved P1/P2/P3 findings。
- skipped、blocked 和 out-of-scope items 及原因。
- final verdict source。

Durable summaries 放在 `docs/testing/results/` 或相关 package `review.md`。

## Verdict Discipline

没有在当前 work session 运行相关 command 或 checker 并得到支持结论时，不要声称 tests、
builds、E2E、UI smoke、Agent smoke、autonomous、external suite、projection readiness、
product readiness 或 clean pass。

旧证据只能作为 historical context，除非重新刷新或明确标记为 historical scope。
