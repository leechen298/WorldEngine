# v0.2 自动迭代种子计划

英文版本：`00-chatgpt-plan.md`

## 用途

本文件用于启动 v0.2 的自动迭代工作流。它让 ChatGPT、Codex A 和
Codex B 可以按 package 逐个推进 v0.2，同时避免把 core repository 变成
application-specific backend。

## 当前 v0.2 状态

v0.2 仍处于 `planned / in progress` 状态。0.2.1 到 0.2.5 已按 v0.2
索引记录为完成或 historical artifact。0.2.6 负责重排剩余 package sequence，
并为 0.2.7 到 0.2.12 准备自动迭代工作流。

## WorldEngine 北极星

WorldEngine 是递归世界生成与运行引擎。长期目标包括 world generation、
runtime、recursive world structures、agents living in worlds、memory、
feedback-shaped behavior，以及随时间形成的 pseudo-self。

v0.2 只建立基础能力，不实现未来版本的 runtime、agent、memory、generation、
projection 或 application surfaces。

## v0.2 边界

v0.2 可以做：

- documentation governance。
- EntityRef / WorldCell / WorldSpec schema foundation。
- EventRef / Event.refs additive event contract。
- generic schema smoke validation。
- external fixture / validation boundary。
- redacted validation report template。
- legacy boundary。
- iterative development automation workflow。
- evidence / compatibility / release-candidate documentation。

v0.2 不可以做：

- WorldSpec loader。
- RuntimeEngine migration to WorldCell。
- runtime bridge。
- Agent-in-World loop。
- memory / self-continuity substrate。
- world generation。
- projection API。
- external fixture repository。
- external validation repository。
- product UI。
- application-specific backend。
- concrete demo world fixture。
- concrete external-world seed data。

## 已完成的 package

- `0.2.1-project-north-star`：文档治理和项目北极星。
- `0.2.2-recursive-world-contract`：递归 schema 基础。
- `0.2.3-event-contract-extension`：增量式事件引用结构。
- `0.2.4-worldspec-reference-fixture`：已由 0.2.5 supersede 的 historical
  concrete fixture artifact。
- `0.2.5-core-boundary-cleanup-and-roadmap-reset`：边界清理、通用 schema
  冒烟验证和路线图重置。

## 计划中的剩余 package

- `0.2.6-iteration-workflow-and-plan-reset`：工作流、计划重排和历史内容抽象。
- `0.2.7-recursive-schema-contract-hardening`：schema contract hardening。
- `0.2.8-event-reference-contract-hardening`：event reference contract hardening。
- `0.2.9-generic-schema-evidence-and-boundary-audit`：evidence 和 boundary audit。
- `0.2.10-legacy-boundary-and-compatibility-review`：legacy compatibility review。
- `0.2.11-v0.2-release-candidate-bundle`：release-candidate bundle。
- `0.2.12-v0.2-final-closeout`：通过 review approval 后执行 final closeout。

0.2.7 到 0.2.12 的执行级细节见：

- `docs/iterations/v0.2/v0.2-plan.md`
- `docs/iterations/v0.2/v0.2-plan.zh.md`

## Codex A 职责

Codex A 负责准备或审核 package documents，确认 intent、contract、
technical design、test plan、execution plan 和 review evidence 都符合当前
package boundary。

Codex A 在准备 documentation-stage package 时不得实现代码。

## Codex B 职责

Codex B 只在 package 通过 review 和 approval 后实现。它必须遵循已批准的
contract、technical design、test plan 和 plan，并把 evidence 记录到
`review.md`。

如果实现过程中发现会改变已批准 contract 的设计缺口，Codex B 必须停止。

## 批准闸

Human / ChatGPT review 必须在实现前批准 package documents。documentation-only
package 可以在文档检查和 review evidence 完成后收口；code 或 mixed package
必须先有 approved package，才能进入代码实现。

## 实现闸

实现只能在 approval 之后开始，并且必须停留在 package contract 和 v0.2
boundary 内。

## 测试闸

只运行 package test plan 指定的测试。除非当前 session 实际运行过对应命令或流程，
不得声称 tests、builds、E2E、UI smoke、runtime behavior 或 backend behavior 通过。

## Diff 审核闸

Codex A 审核 Codex B 的 diff，重点检查 scope、compatibility、evidence 和
forbidden changes。发现项使用 P1/P2/P3 severity。

## 修复循环

默认最大修复循环次数为 `N = 3`。

每轮循环：

1. 运行 required tests。
2. 审核 diff 和 evidence。
3. 在 scope 内修复 P1/P2 问题。
4. 记录结果。

如果 `N = 3` 后仍有 P1/P2 findings，停止并升级给 human / ChatGPT review。

## 最终 ChatGPT 审核

0.2.11 生成 release-candidate bundle。只有 release-candidate bundle 通过
human / ChatGPT review 后，0.2.12 才能执行 final closeout。
