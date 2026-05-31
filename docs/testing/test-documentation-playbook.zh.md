# 测试文档 Playbook

状态：可复用测试文档指南

英文版本：`test-documentation-playbook.md`。

本文档标准化 agent 为 WorldEngine version 和 iteration package 编写或更新测试文档、
测试方案、测试场景和测试用例的方式。它是 documentation/design workflow，本身不证明
测试已经通过。

当用户要求执行验证并输出 PASS/FAIL verdict 时，使用
`product-capability-validation-playbook.zh.md`。

## 何时使用

当用户要求编写、补充、整理、review 或准备测试文档时，使用本 playbook。

示例：

```text
/goal 编写 <version> 测试方案
/goal 补充 <iteration-package> 测试文档
/goal 设计 <feature-or-scenario> 测试用例
/goal 为当前 package 写 E2E / Agent 测试场景
/goal 生成当前产品的测试矩阵和测试计划
```

一句话请求可以作为有效触发词。它启动的是测试文档 workflow，不代表验证已经运行或通过。

## 必读文档

起草测试文档前，先读：

- `AGENTS.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- active version/package 的 `README.md`、`intent.md`、`contract.md`、
  `technical-design.md`、`test-plan.md`、`plan.md`、`review.md`，如果这些文件存在。
- `docs/testing/` 下相关既有文档。

## Package 边界

如果请求只写或更新测试文档，保持 documentation-only，并记录没有运行 code tests，
除非用户明确要求运行。

如果请求会新增或修改 test code、checker code、fixtures、schemas、runtime/API/frontend
behavior 或 result artifacts，必须先走 repository iteration package gate。

不要写出暗示产品行为已经验证通过的测试文档，除非验证实际运行并记录了 evidence。

## 必需输出

按请求 scope，产出或更新相关 artifacts：

- test strategy 或 test approach。
- capability/test matrix。
- active iteration package 的 `test-plan.md`。
- `docs/testing/e2e-scenarios/` 下的 E2E scenario documents。
- `docs/testing/agent-smoke/scenarios/` 下的 Agent smoke scenario documents。
- `docs/testing/agent-autonomous/scenarios/` 下的 Codex/test-runner autonomous
  scenario documents。
- result schema 或 checker contract documentation。
- fixture requirements。
- command matrix。
- evidence 和 artifact expectations。
- negative cases、boundary cases 和 failure-path cases。
- 从 contract requirements 到 tests 的 traceability。

## 测试文档矩阵

每次实质性测试文档编写都应覆盖：

- 被测试 capability 或 requirement。
- risk 或 failure mode。
- test level：unit、integration/API、E2E、Agent smoke、autonomous、manual
  observation 或 documentation audit。
- automation status：implemented、planned、blocked、not applicable 或 out of scope。
- command 或 future command。
- expected assertion。
- evidence source。
- fixture 或 data requirement。
- pass/fail owner：test runner、deterministic checker、scorecard checker 或
  human review。
- unresolved gaps。

## 测试用例模板

具体 test cases 使用这个结构：

```text
ID:
Capability:
Priority:
Type:
Preconditions:
Steps:
Expected assertions:
State/event/log evidence:
Artifacts:
Negative or boundary coverage:
Automation target:
Current status:
```

测试用例必须足够具体，让另一个 agent 可以直接实现或运行，而不需要临时发明断言。

## Unit Test 文档

Unit-test documentation 必须识别：

- focused unit-test files 或 future files。
- logic under test。
- positive cases。
- negative 和 boundary cases。
- fixture 或 mock data。
- expected command。
- 为什么 broad E2E 或 Agent checks 不能替代该 unit test。

## E2E 文档

E2E documentation 必须识别：

- user path 或 API path。
- setup 和 data reset requirements。
- UI assertions、API assertions，以及 event/log cross-checks。
- failure-path assertions。
- artifact/report path expectations。
- sandbox 或 local-server requirements。

除非目标明确只是 smoke navigation check，否则不要把 E2E 写成“只打开页面”。

## Agent 测试文档

Agent test documentation 必须区分：

- Agent smoke：UI/CLI operation 加 deterministic checker。
- minimal autonomous saved-result validation：saved result directory 加 deterministic
  或 scorecard checker。
- full autonomous runner/full suite：autonomous runner 加 scorecard/checker。
- 人工观察：只能作为 supporting evidence。

按需记录 `operation-log.jsonl`、`result.json`、transcripts、console logs、
screenshots、API summaries 和 checker commands。

## Review And Closeout

测试文档 closeout 应记录：

- changed documentation files。
- 是否改了 code、tests、checkers、fixtures 或 product behavior。
- 运行过的 documentation consistency checks，例如 `git diff --check`。
- 未运行的 tests 及原因。
- unresolved P1/P2/P3 documentation 或 coverage gaps。
- 适用时 handoff 到 implementation 或 validation。

如果用户后续要求运行验证，切换到 `product-capability-validation-playbook.zh.md`。
