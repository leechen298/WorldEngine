# Iteration Documentation Agent Rules

Status: process standard

英文版本：`AGENTS.md`。

本文件约束 `docs/iterations/` 下的文档工作。根目录 `AGENTS.md` 和 `CLAUDE.md`
仍然约束全仓行为。本文件定义 version plan、planned package、iteration package、
validation plan、evidence 和 review 文档必须达到的详细程度。

本文件不实现、也不定义外部自动化控制器。

## Purpose

创建或修改 `docs/iterations/` 下文件时使用本文件。它把 iteration 文档应有的详细程度
写成明确规则，避免后续 agent 只能从示例中猜 scope、evidence 要求或 closeout 状态。

这些规则适用于：

- version plan。
- planned package。
- 具体 iteration package。
- validation plan。
- post-closeout validation 文档。
- review 和 evidence 记录。

## Version Plan Standard

任何包含多个 planned sub-iterations 的 `vX.Y-plan.md`，都必须把每个 planned package
写成准迭代包规格（quasi-package specification）。

每个 planned package 必须包含这些字段：

```text
Package name
Status
Type
Goal
Why this exists
Inputs / required reading
Allowed changes
Forbidden changes
Expected deliverables
Expected tests / verification
Compatibility constraints
Scope guardrails
Exit criteria
Handoff to next package
```

硬规则：

- `README.md` 可以是 package index 或 summary。
- `vX.Y-plan.md` 必须是详细执行规格。
- `vX.Y-plan.md` 中的 planned-package specifications 本身不创建具体 child package
  directories、package files，也不代表 implementation authorization。
- 只写一行 package summary 不够。
- 后续 agent 不应该再靠猜测补 scope、allowed files、forbidden files、
  verification、compatibility constraints 或 handoff state。
- 宽范围的生成或规划版本请求，默认不得为每个 planned child iteration 创建完整 document
  set。只有当用户明确请求某个 child package、要求创建或完成某个 child package，或已
  review 的 active package 明确授权下一个 child package documentation 时，才创建具体
  child package document set。
- 如果缺少任一 required planned-package 字段，review 至少必须记录 P2。
- 如果缺少 `Forbidden changes`、`Compatibility constraints` 或 `Scope guardrails`
  可能导致 runtime、API 或 schema 越界，review 必须记录 P1。

## Iteration Package File Standard

Code 和 mixed package 必须包含：

```text
README.md
intent.md
contract.md
technical-design.md
test-plan.md
plan.md
review.md
```

Documentation-only package 至少必须包含：

```text
README.md
intent.md
contract.md
plan.md
review.md
```

只有当 documentation-only package 不准备或改变 runtime、schema、API、UI、test、
fixture、process、evidence、validation、release 或 automation-consumption 行为时，
才可以省略 `technical-design.md` 和 `test-plan.md`。

如果 documentation-only package 修改以下内容，则必须包含 `test-plan.md`，并建议包含
`technical-design.md`：

```text
process rules
version semantics
product boundaries
evidence rules
validation templates
release status
package sequencing
automation consumption contracts
```

## Codex Plan-Mode Document Generation Standard

当用户要求 `/plan`、要求先为 iteration documentation 制定计划，或提出会创建/修订多个
`docs/iterations/` 文件的宽范围请求时，使用本标准。

Plan-mode documentation work 必须先产出可 review 的 generation plan，再进行大规模起草。
小型 docs-only change 的 plan 可以只出现在聊天回复中。新 version plan、新 iteration
package、validation chain、goal campaign 或多文件重写，必须在 closeout 前把 plan 记录到
对应的 `plan.md`、`CAMPAIGN_PLAN.md`、parent `vX.Y-plan.md` 或 package `review.md`
中。

generation plan 必须包含：

```text
Objective
Authoritative inputs read
Documentation type
Files to create or update
Files explicitly out of scope
Required package status values
Allowed changes
Forbidden changes
Review gates
Verification commands
Open questions or assumptions
Stop conditions
Handoff after plan approval
```

硬规则：

- plan-mode documentation drafting 期间，不得修改 runtime、schema、API、frontend、
  backend tests、fixtures、migrations 或 external repositories。
- package documents 通过 review 且 review evidence 记录 approval 前，不得写
  implementation-ready claims。
- 不得只靠 memory 生成完整 package。必须先读取相关 roadmap、version plan、parent
  package、current package docs，以及 governing `AGENTS.md` files。
- 如果 plan 暴露 missing scope、contradictory status、missing required inputs 或
  unclear implementation authorization，停止为 `NEEDS_USER_INPUT`，或在 `review.md`
  中记录 blocker。
- 如果用户只要求 `/plan`，除非用户明确授权 drafting 或 execution，否则产出 plan 后停止。
- 如果用户用 `/goal` 要求完成 package，goal 可以在同一个 goal 内执行选中的 plan-mode
  gates，但 plan 和 gates 仍必须在 package docs 或 review evidence 中可见。
- 对宽范围 version-level documentation request，应先创建或更新 version root 和 version
  plan。除非用户或已 review 的 active package 明确授权具体 child package documents，否则不得
  预先创建每个 planned child package 的 `README.md`、`intent.md`、`contract.md`、
  `technical-design.md`、`test-plan.md`、`plan.md` 或 `review.md`。
- plan 必须绑定 active package。除非 parent plan 明确拥有该 scope，不要包含 adjacent
  future versions 或 convenient follow-on work。

## Concept Learning / Research Synthesis Gate

当 iteration work 依赖陌生概念、密集 source material、research paper、course、external
framework，或 active package 尚未解释清楚的 internal design area 时，使用本 gate。

输出必须是 durable、reviewable artifact，而不只是临时聊天记录。如果 learning result
需要支撑后续 implementation 或 review，应写入 active package 的 `plan.md`、
`technical-design.md`、`review.md`，或 package-local `notes/*.md` 文件。

learning report 必须包含：

```text
Learning objective
Sources read
Source reliability / authority
Glossary and prerequisite concepts
Concept walkthrough
Evidence table mapping claims to sources
Diagrams when they clarify the concept
Claims from the source material
Agent interpretation / synthesis
Caveats and weak evidence
Open questions
Follow-up reading or experiments
Impact on the active package
```

硬规则：

- 区分 source material 的 claims 和 agent 自己的 inference。
- 尽可能引用 source section、heading、page、figure、table、file 或 symbol。
- 如果无法取得精确 page 或 figure references，必须说明，并使用最精确可得的 section、
  heading、file 或 symbol reference。
- 当 evidence weak 或 disputed 时，不得把 paper、course、external article、generated
  summary 或 subagent output 当作 ground truth。
- concept map、method flow 和 evidence map 默认优先使用 Markdown-native Mermaid
  diagrams。只有 Markdown-native diagram 不足且 active package 允许该 asset 时，才使用
  generated 或 binary visual assets。
- 不得只基于 learning report 实现代码。Implementation 仍必须经过正常 iteration
  package contract、design、test plan 和 review gates。

密集材料的 subagent 拆分：

- 一个 subagent 可以梳理 problem statement、contribution、method、evidence、
  limitations 和 claimed results。
- 一个 subagent 可以从 approved sources 收集 prerequisite context。
- 一个 subagent 可以检查 figures、tables、notation、algorithms、code paths 或需要谨慎验证的
  claims。
- 一个 subagent 可以作为 skeptical reviewer，识别 unsupported claims、missing
  baselines、unclear assumptions 或 follow-up questions。

main agent 必须等待被请求的 subagents，调和 contradictions，并写出最终 learning report。
不要把割裂的 subagent notes 直接粘成 final artifact。

## Goal Development Campaign Subagent Gate

WorldEngine `/goal` development campaigns 必须使用 independent subagent 或 evaluator
checkpoints。适用范围包括 goal campaign、full child-package cycle、code package、mixed
package、migration、refactor、deployment retry loop，或会改变 runtime behavior、
schemas、APIs、frontend behavior、backend tests、fixtures、migrations 或 release
claims 的 implementation-bearing validation repair。

本 gate 把 Codex follow-goals 行为适配到本仓库的 iteration model：

- North Star 和 scope boundaries 优先。
- active iteration package 是唯一 implementation scope。
- Documentation、contract、design、test-plan 和 review gates 仍控制 implementation
  authorization。
- runtime claims 必须有 current-session command evidence。
- closeout 仍必须有 changed-file consistency 和 `review.md` evidence。
- main agent 负责 synthesis、verification、final status 和 conflict resolution。

implementation-bearing child packages 的必跑 checkpoints：

1. 记录 `implementation_authorized: yes` 前，运行 documentation / contract evaluator。
2. 文件修改后、broad verification 前，运行 implementation-scope evaluator。
3. focused tests 后、E2E、API smoke、autonomous validation 或 final status 前，运行
   code-review subagent 或 evaluator。
4. 把 tests、E2E、API smoke、autonomous validation、deployment 或 release claims 标记为
   passed 前，运行 validation-evidence evaluator。
5. package `review.md` 写入最终 route status 前，运行 closeout consistency review。

documentation-only goal campaign children 的必跑 checkpoints：

- 当 child 修改 process rules、goal routing、evidence rules、package sequencing、
  validation templates、release status、automation-consumption contracts，或 English /
  Chinese mirror obligations 时，必须运行 read-only documentation evaluator。
- 只有 trivial text-only edits 不影响任何 gate、contract、status、claim 或 automation
  route 时，才可以跳过 subagents。

失败处理：

- 如果 required `/goal` development checkpoint 中 subagent tooling 不可用，记录为
  `BLOCKED` 或 `NEEDS_USER_INPUT`；不得静默降级成 optional。
- 如果 required subagent 或 evaluator 返回 P0 / P1 findings，必须修复或在 closeout
  前停止。
- 如果 P2 findings 仍存在，必须 fix、带理由 downgrade、仅在 package contract 允许时
  carry，或在 clean pass 前停止。
- 如果 subagent output 与 source files、command evidence 或 git state 冲突，main
  agent 必须用 authoritative evidence 解决冲突后才能写 final status。

## Subagent / Evaluator Use Standard

只有当用户明确要求 subagents / parallel agent work，或 active package 的
`GOAL_RUNNER.md`、contract 或 plan 明确授权时，iteration work 才允许使用 subagents。
Subagents 是 review、evaluation、exploration 和可清晰拆分的 worker tasks 的可选工具。
它不是强制仪式，也不放宽 package gates。

对于 `/goal` development campaigns，上面的 Goal Development Campaign Subagent Gate
就是 explicit authorization，并且其中列出的 checkpoints 是 mandatory。

当 subagents 能实质提升可靠性时使用，例如：

- 学习或总结陌生、密集的 source material。
- 对范围较大或风险较高的 documentation changes 做 independent review。
- 对 implementation-bearing packages 做 code review。
- 做 compatibility、scope、security、release-claim 或 evidence-honesty checks。
- 做 English / Chinese mirror quality checks。
- 做 autonomous validation 或 black-box validation review。
- 并行检查彼此独立的 files 或 subsystems。

默认模式：

- Subagents 默认是 read-only evaluators。
- 优先把 subagents 用于 read-heavy exploration、tests、triage、log analysis、
  learning reports 和 summarization。
- 谨慎使用 parallel write-heavy workflows，因为并发编辑会制造 conflicts 和 coordination
  overhead。
- 只有 active package contract 明确允许 worker implementation，且 main agent 已记录
  delegation 为什么属于 scope 内时，subagent 才可以编辑文件。
- 除非 active contract 明确授权对应 file class，否则 subagents 不得修改 runtime、
  schema、API、frontend、backend tests、fixtures、migrations、external repositories
  或 out-of-scope documents。

Main-agent responsibilities：

- dispatch 前定义每个 subagent 的 scope、inputs 和 expected output。
- 说明 main agent 是否必须等待所有 subagents 再继续。
- 保持 subagent tasks 在 active package 和 current goal 内。
- 汇总结果，不要把割裂的 subagent output 直接粘成 final status。
- 将 subagent findings 分类为 P0 / P1 / P2 / P3。
- 对每个 P0 / P1 / P2 finding，必须 fix、带理由 downgrade、在允许时 carry，或记录为
  blocker。
- 用 current-session evidence 验证任何 claimed fix 或 pass。
- 在 `review.md` 中记录 material subagent reviews，包括 reviewed scope、findings、
  commands run or not run，以及 unresolved risks。

Hard stops：

- 如果 subagent 报告无法在 active contract 内修复的 P0 / P1，停止为 `BLOCKED`、
  `FAILED` 或 `NEEDS_USER_INPUT`。
- 如果 subagent output 与 source files、command evidence 或 actual git state 冲突，
  closeout 前以当前 source/evidence 为准解决冲突。
- 不得使用 subagents 绕过 review gates、implementation authorization、Closeout
  Consistency Gate 或 evidence requirements。

## Required Content For Each Package File

每个 package 文件都必须具体到可以 review。只有占位标题不够。

### README.md

必须包含：

```text
Status
Type
Goal
Scope
Deliverables
Final assessment state, if applicable
```

### intent.md

必须包含：

```text
Problem / purpose
Why now
Relationship to roadmap
Non-goals
Expected handoff
```

### contract.md

必须包含：

```text
Public concepts
Allowed changes
Forbidden changes
Compatibility requirements
Out-of-scope follow-ups
```

### technical-design.md

必须包含：

```text
Documentation or implementation structure
Affected files
Data / control flow, if relevant
Compatibility strategy
Anti-drift rules
```

### test-plan.md

必须包含：

```text
Exact commands to run
Expected results
Commands not run and why
Blocker recording rule
No unverified claims rule
```

### plan.md

必须包含：

```text
Ordered execution steps
Phase boundaries
Stop conditions
Review update step
```

### review.md

必须包含：

```text
Changed files
Commands run
Test results
Compatibility review
Scope review
Unresolved P1/P2/P3
Final assessment
```

## Anti-Drift Requirements

任何 future version 或 package planning 都必须说明：

```text
where the work lives
what files may change
what files must not change
which current behaviors are compatibility-sensitive
which adjacent tempting features are explicitly out of scope
which later version owns those tempting features
how the next package receives handoff
```

禁止：

- 加入 concrete demo world details。
- 用 external validation worlds 反向驱动 core abstractions。
- 在 current package 中实现 future-version work。
- 混合 documentation planning 和 implementation，除非当前 package contract 明确允许。
- 在没有 current-session evidence 的情况下声称 tests passed。

## Validation And Post-Closeout Documentation Standard

post-closeout validation 文档必须区分这些状态：

```text
feature closeout complete
independent validation not yet performed
validation planned
validation executed
validation passed / blocked / failed
```

不能把 validation plan 写成 validation result。

post-closeout validation 文档应该包含：

```text
intent
contract
test plan
API smoke plan
E2E / integration plan
autonomous review plan
execution plan
report template
review
```

硬规则：

- E2E 没跑就记录 `not executed` 或 `not configured`。
- Codex autonomous validation 没跑就不能写 passed。
- 如果没有 E2E framework，要说明 fallback 是 API smoke 加 backend integration tests。
- Validation report 不能预填 `passed`。
- 只有当前 session 真实运行过的命令才能记录为 passed。
- 如果命令不可用，必须记录 blocker。

## Evidence And Review Rules

Evidence 和 review 记录必须遵守：

```text
No unverified test claims.
No hidden blockers.
No vague "tests passed".
Record exact commands.
Record not-run checks and why.
P1 blocks closeout.
Unresolved P2 blocks final unless explicitly accepted.
P3 can be carried only with explicit handoff.
```

Severity definitions：

```text
P1: blocks implementation or closeout.
P2: should be fixed before final review unless explicitly accepted.
P3: non-blocking polish or future handoff.
```

## External Automation Boundary

WorldEngine iteration docs 可以被外部自动化 controller 消费。WorldEngine 不负责 agent
scheduling、Codex role assignment、retry loops 或 orchestration。

`docs/iterations/` 必须提供 deterministic package specs，而不是 automation
implementation。

## Codex Goal Campaign Standard

可运行的 parent 或 umbrella package 可以支持 Codex App `/goal` campaign execution。
这类 package 不能把 memory 或 chat context 当成唯一入口。

goal campaign package 必须提供：

```text
README.md with Goal Entry
GOAL_RUNNER.md
CURRENT_STATE.md
CAMPAIGN_PLAN.md or equivalent parent plan section
child package README / contract / plan / review files
```

`README.md` 负责自然语言 goal alias，例如 `完成 <package-name>`。

`GOAL_RUNNER.md` 负责 execution state machine、adaptive gate selection、
risk-based gate 顺序、review loops、implementation authorization rule、
verification loop、closeout consistency gate 和 stop conditions。

`CURRENT_STATE.md` 负责当前 active child、current campaign status、archived
evidence policy 和 next action。

`CAMPAIGN_PLAN.md` 或 parent plan 负责 child sequence、campaign exit criteria
和跨 child handoff rules。

`review.md` 负责 evidence 和 final status。它不能成为 goal entry 的唯一来源。

如果 package 被 reset 后重新运行 campaign，历史 evidence 必须保留可见，但除非被当前
goal 明确重新接受，否则必须标记为 archived 或 non-current。

## 英文 / 中文镜像规则

### 默认双语输出规则

active iteration docs 默认应中英文同步。以下类型的 active iteration documentation
应在同一轮同时生成或同步英文与中文镜像：

- version index。
- version plan。
- package README。
- package contract。
- package plan。
- package review。
- release candidate 或 closeout docs。
- post-closeout validation docs。
- validation report templates。
- evidence、compatibility 或 boundary audit docs。

新建英文 active iteration document 时，如果目录约定、package contract 或当前任务要求
中文镜像，就必须同轮生成 `.zh.md`。

如果有意不生成中文镜像，必须在 package 的 `review.md` 中记录原因。

### 已有镜像同步规则

如果 active English iteration doc 已经有 `.zh.md` 镜像，必须同轮更新英文和中文。

如果只更新其中一侧，review 至少必须记录 P2，除非 package contract 明确允许只改英文
或只改中文。

### 中文文档质量规则

中文镜像必须是自然中文文档，不是英文原文加中文标点，也不是英文原文加少量中文连接词。

解释、目标、范围、结论、审查意见、状态说明、阻塞原因和验证说明必须使用自然中文表达。

只有下列内容可以保留英文：

- 代码符号。
- 文件路径。
- 命令名称。
- API route。
- package name。
- status literal。
- field name。
- 翻译后会降低精度的项目固定术语。

不要把普通说明句留成英文。

不要写大段中英混写，也不要写成大部分是英文、只夹少量中文连接词的段落。

当清晰的中文标题存在时，不要机械复制英文 heading 和正文。

### 结构等价规则

中文镜像必须保留与英文文件相同的含义和 review 语义。

以下内容在英文和中文之间必须等价：

- Status。
- Type。
- Goal。
- Scope。
- Allowed changes。
- Forbidden changes。
- Compatibility requirements。
- Expected deliverables。
- Expected tests / verification。
- P1/P2/P3 findings。
- Final assessment。
- Release / closeout status。
- Validation status。
- Blockers 和 not-run reasons。

### 标题翻译规则

标题可以保留 code-like nouns 或 package names，但通用标题应该翻译成可读中文。

示例：

- `Goal` 可以写成 `目标`。
- `Scope` 可以写成 `范围`。
- `Allowed changes` 可以写成 `允许修改`。
- `Forbidden changes` 可以写成 `禁止修改`。
- `Expected tests / verification` 可以写成 `预期测试 / 验证`。
- `Final assessment` 可以写成 `最终评估`。

不要求逐字一一对应翻译；如果更自然的中文标题更清楚，应使用更清楚的中文标题。

### Review enforcement

如果中文镜像缺失、过旧、语义弱于英文，或在应使用自然中文的位置大段中英混写：

- 普通 documentation 记录 P2。
- 如果不一致影响 release status、validation status、forbidden changes、
  compatibility constraints 或 closeout evidence，记录 P1。

## Release / Closeout Rules

不要把 version 标记为 complete 或 released，除非 final closeout package 允许。

Release candidate 不是 release。

Documentation-only closeout 不得声称新的 runtime behavior。

Final closeout 必须引用 evidence 和 unresolved findings。

如果 validation 未执行，必须明确说明。
