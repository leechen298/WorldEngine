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

## English / Chinese Mirror Rule

如果 active English iteration doc 有 `.zh.md` 镜像，必须同步更新。
中文镜像可以保留 technical terms in English。

Status、scope、conclusion、allowed changes、forbidden changes、evidence 和
review findings 必须等价。

除非 package contract 或当前任务明确允许，不要创建新的 mirror。

## Release / Closeout Rules

不要把 version 标记为 complete 或 released，除非 final closeout package 允许。

Release candidate 不是 release。

Documentation-only closeout 不得声称新的 runtime behavior。

Final closeout 必须引用 evidence 和 unresolved findings。

如果 validation 未执行，必须明确说明。
