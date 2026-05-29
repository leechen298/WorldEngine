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
- 只写一行 package summary 不够。
- 后续 agent 不应该再靠猜测补 scope、allowed files、forbidden files、
  verification、compatibility constraints 或 handoff state。
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
