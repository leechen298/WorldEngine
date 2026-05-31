# 产品能力验证 Playbook

状态：可复用验证指南

英文版本：`product-capability-validation-playbook.md`。

本文档把 v0.4 post-closeout 之后形成的完整验证方式沉淀为后续版本可复用的
项目级流程。它不绑定某个版本；每个 version 或 package 仍然必须定义自己的
scope、commands、evidence 和 PASS 条件。

## 何时使用

当用户询问某个版本、release candidate 或当前产品状态是否真的已经验证、ready、
clean 或 passing 时，使用本 playbook。

示例：

```text
/goal 测试 <version>
/goal 验证 <version> 是否达到 clean pass
/goal 测试 <iteration-package>
/goal 对当前产品能力做完整验证
/goal run post-closeout validation for vX.Y
```

一句话请求可以作为有效触发词；但一句话 verdict 只有在当前会话证据已经证明后才有效。

## 不可违反的规则

- 先读 `AGENTS.md`、`docs/iterations/README.md` 和 active version/package 文档，
  再声明 scope。
- 没有在当前 work session 运行命令或 checker，不要声称 tests passed；除非有
  durable result file 明确记录当前会话证据。
- Agent observation、人工观察或计划不能作为 PASS 来源。
- validation package 不得顺手修产品代码，除非 package 明确授权 repair。
- 不得把当前版本扩大到未来 roadmap scope。
- 如果某个 check 是 out of scope、skipped、blocked 或 absent，必须直接说明。

## Package 要求

如果验证需要新增或修改 tests、checker code、fixtures、result schema、product code、
runtime behavior、API behavior 或 frontend behavior，必须先创建 mixed/code iteration
package。

如果只是审计已有证据并更新文档，documentation-only package 可以足够，但仍然必须记录
no-code boundary 和 no-test rationale。

## 能力矩阵

完整产品能力验证必须产出或更新一份 matrix，至少覆盖：

- version 和 scope boundaries。
- 核心用户路径。
- API/backend behavior。
- backend 和 frontend unit test coverage。
- frontend pages 和 interactions。
- data state changes、events、logs、persistence 和 evidence surfaces。
- invalid inputs、permission boundaries、limits 和 failure paths。
- E2E scenarios 和 gaps。
- Agent smoke scenarios 和 deterministic checker support。
- Codex/test-runner autonomous scenarios、saved-result checker support，以及是否存在
  broad autonomous runner。
- 已有测试覆盖和缺口。

## 命令 Profile

具体命令由版本决定。产品级 clean-pass profile 通常包括：

```bash
make check-backend
make check-frontend
cd backend && .venv/bin/python -m pytest <version-focused-unit-tests> -q
cd backend && .venv/bin/python -m pytest app/tests tests -q
cd frontend && pnpm test
cd frontend && pnpm build
make test-e2e
make validate-agent-smoke-fixtures
make validate-agent-smoke-result RESULT_DIR=<smoke-result-dir>
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=<autonomous-result-dir>
git diff --check
```

版本相关的 focused backend tests 应在 broad backend regression 之前补充。如果 frontend
code 在 scope 内，应在 build 和 E2E 前运行 focused frontend unit tests 或完整 frontend
unit suite。Documentation-only package 不得假装运行这套 profile；如果 product-level
validation 不在 scope 内，必须写明。

## Unit Test Evidence

当 version 或 package 包含 backend logic、frontend logic、schemas、adapters、
validators 或 test/checker tooling 时，产品级验证必须包含 unit tests。

必须记录：

- 与 version 或 package risk 绑定的 focused unit-test commands。
- broad backend unit/regression command results。
- frontend code 或 dashboard behavior 在 scope 内时的 frontend unit-test command results。
- runner 有输出时，记录 test file count 或 pass/fail count。

当有 unit-testable logic 改动时，不得用 E2E、Agent smoke 或 autonomous checker
results 替代 unit tests。

## E2E 证据

E2E PASS 必须有明确断言，不能只是成功打开页面。对于会改变状态的流程，尽量至少交叉
验证两个 evidence surfaces：

- UI result。
- API state。
- event 或 log evidence。
- artifact 或 report output。

必须记录 command、exit code、pass/fail count，以及 report/artifact path。

## Agent 测试分类

必须区分这些类别：

- Agent smoke：Agent 通过 UI/CLI 操作，PASS/FAIL 来自 deterministic checker。
- Minimal autonomous saved-result validation：result directory 由 deterministic 或
  scorecard checker 校验。
- Full autonomous runner/full suite：autonomous runner 自主规划并执行多步任务，
  scorecard/checker 判断结果。
- 人工观察：只能作为辅助 evidence，不能作为 PASS 来源。

不要把 Agent smoke 或 saved-result validation 说成 full autonomous。

## 必需 Evidence Artifacts

完整 validation closeout 应记录：

- scenario 或 capability matrix。
- command table，包含 exit code 和 pass/fail counts。
- focused 和 broad unit-test results。
- artifact paths。
- result directories。
- Agent tests 的 operation logs。
- Agent smoke 或 autonomous saved-result validation 的 `result.json`。
- 用于 PASS/FAIL 的 checker command。
- 当 goal/package 要求时，记录 subagent 或 evaluator findings。
- P1/P2/P3 unresolved findings。
- final verdict：`clean pass`、`partial pass`、`failed` 或 `blocked`。

Durable summaries 应放在 `docs/testing/results/`。

## Verdict 规则

只有所有 required in-scope commands 和 checkers 都通过时，才能写 `clean pass`。

如果部分 required surfaces 通过，但至少一个 required in-scope check 失败、blocked
或缺失，应写 `partial pass`。

如果核心 required behavior 被证据反驳，应写 `failed`。

只有 validation 无法继续，且 blocker 有明确复现证据时，才写 `blocked`。

对于 future-scope 或 intentional skipped checks，应写 `out of scope` 或 `skipped`，
不能写 `passed`。

## 一句话验证请求

项目可以接受这样的一句话请求：

```text
/goal 验证 <version> 是否达到 clean pass
```

这句话只是在启动本 playbook，不是在完成验证。

最终回复可以很短，但前提是证据已经存在或刚刚产出。安全的一句话 verdict 仍然必须引用
证据来源，例如：

```text
<version> clean pass is verified by its iteration review and the current-session command matrix recorded there.
```

如果证据没有覆盖 frontend、E2E、Agent smoke、autonomous、external validation 或
product readiness，最终 verdict 必须点名这些 exclusions。
