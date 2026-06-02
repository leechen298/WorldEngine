# Code Review Playbook

Status: reusable code-review guide

英文版本：`code-review-playbook.md`。

本 playbook 标准化 WorldEngine 中针对某个 version、iteration package、feature 或当前
code surface 的 implementation reliability 审核方式。它是 version-agnostic：每个目标仍由
自己的 contracts、files、commands 和 review boundaries 定义范围。

当用户要求执行验证并给出 PASS/FAIL verdict 时，使用
`product-capability-validation-playbook.zh.md`。当用户要求编写或更新测试文档时，使用
`test-documentation-playbook.zh.md`。

## When To Use

当用户要求审核代码、审计 implementation logic，或判断 implementation 是否可靠时，使用本
playbook。

示例：

```text
审核 <version> 代码
review <version> code
审核 <iteration-package> 代码
代码审核 <feature-or-package>
```

一句话请求是有效 trigger。它启动 code review。它不是 PASS verdict，也不等同于 final
closeout。

## Non-Negotiable Rules

- 声称 review scope 前，先读 `AGENTS.md`、`docs/iterations/README.md` 和
  `docs/iterations/AGENTS.md`。
- 审核代码前，先读目标 version 或 package state：`README.md`、`CURRENT_STATE.md`、
  `GOAL_RUNNER.md`、`CAMPAIGN_PLAN.md`、version plan，以及存在的 code-bearing child
  package docs。
- 不要把 `final / closeout complete` 或 `final-closeout-complete` 当成 code-review
  result。
- 没有在当前 work session 运行命令时，不要声称 tests passed。
- 除非用户明确授权 repair 且所需 iteration package 允许，否则不要在 review-only request 中
  修复 implementation issues。
- Findings 必须基于当前 files、line references、commands 和 contract text。

## Review Scope Selection

对于 version target，只审核 implementation-bearing children，除非用户明确要求 documentation
governance review。Documentation-only closeout packages 可以用来查 evidence 和 exclusions，
但它们不是 code surface。

从以下来源建立 code-surface map：

- child package 的 `contract.md`、`technical-design.md`、`test-plan.md`、`plan.md` 和
  `review.md`。
- parent `CURRENT_STATE.md`、`CAMPAIGN_PLAN.md` 和 version plan。
- 当前 git state 和 changed-file lists。
- package 点名的 implementation files、test files、API/frontend files、migrations、
  fixtures 和 generated artifacts。

把每个 surface 分类为 in scope、out of scope、skipped、blocked 或 evidence only。

## Review Workflow

1. Confirm target and route.
   - 判断用户点名的是 version、package、feature 还是 current working tree。
   - 识别 active package state 和 code-bearing child packages。
   - 如果适用，明确 final closeout 只是 evidence context。

2. Read contracts before code.
   - 提取 allowed changes、forbidden changes、compatibility constraints、schema/API
     semantics、test expectations 和 explicit exclusions。
   - 在判断 implementation 前，把歧义记录为 review risk。

3. Inspect implementation.
   - 按 contract 检查 runtime/schema/API/frontend behavior。
   - 如果触及 compatibility-sensitive surfaces，检查 event、runtime、Agent、memory、
     archive、params、loader 和 frontend boundaries。
   - 检查 failure paths、invalid inputs、edge cases、data leakage、mutable state、hidden
     side effects、persistence、migration、network/provider calls 和 concrete
     application-specific content。
   - 检查 public errors、diagnostics、envelopes 和 response shapes 是否符合 package
     contract。

4. Inspect tests and evidence.
   - 检查 focused tests 是否覆盖最高风险 behavior 和 failure paths。
   - 检查 broader regression evidence 是否匹配 claimed blast radius。
   - 只有在需要确认某个 finding 或 claim 时运行 focused commands，并记录 exact commands
     和 results。
   - 如果没有运行命令，必须明确说明。

5. Use independent review when available.
   - 当 subagents/evaluators 可用且授权时，使用 read-only code-review subagent 或
     evaluator。
   - 可以对 feature 或 package review 使用 Superpowers `requesting-code-review`。给 reviewer
     提供 target、contracts、code surfaces、base/head 或 current tree context，以及期望的
     findings format。
   - main agent 仍负责用 source files 和 command evidence 核实 reviewer claims。

6. Report findings first.
   - 先按 P0/P1/P2/P3 severity 报告 findings。
   - 每个 finding 必须包含 file/line references、impact、triggering scenario，以及为什么
     违反 contract 或 existing behavior。
   - 然后列出 open questions、tests run or not run、scope exclusions 和 residual risk。
   - 如果没有 findings，要明确说明，同时报告 test gaps 或 residual risk。

## Severity Guide

- P0：data loss、security exposure、destructive runtime behavior，或无 workaround 的 core
  workflow 断裂。
- P1：contract violation、serious compatibility regression、incorrect public API/schema
  behavior，或很可能阻断生产使用的 bug。
- P2：重要 edge-case handling 缺失、有意义风险的 test coverage 薄弱、diagnostics 混乱，或
  非阻断 scope drift。
- P3：minor maintainability、wording、polish，或低风险 evidence issue。

## Output Template

```text
Findings
- [P1] <title> -- <file>:<line>
  Impact:
  Evidence:
  Suggested direction:

Open Questions
- ...

Verification
- Commands run:
- Not run:

Scope And Residual Risk
- ...
```

## Durable Evidence

如果 review 是 iteration closeout 的一部分，把重要 findings 和 commands 记录到相关 package
`review.md`。

如果 review 是 standalone post-closeout 或 version-level audit，只有在用户要求 durable
evidence，或 review result 会被后续 package 依赖时，才在 `docs/testing/results/` 下创建
summary。命名格式：

```text
YYYY-MM-DD-<target>-code-review.md
```

该 summary 不得暗示 product validation passed；除非已经通过
`product-capability-validation-playbook.zh.md` 单独执行 validation。
