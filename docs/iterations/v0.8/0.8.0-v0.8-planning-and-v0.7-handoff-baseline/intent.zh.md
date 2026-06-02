# 意图

## 问题 / 目的

v0.8 parent package 定义了版本级 campaign，但当前 route 不能从 parent roadmap text
直接进入 implementation 或 evidence execution。`0.8.0` 创建第一个具体 child
package，并在 campaign 继续前记录当前 v0.7 交接状态。

本 package 需要立即修正的漂移是：v0.8 parent 文档仍把 post-closeout v0.7
code-review blockers 表述为未解决。当前 v0.7 状态已记录
`0.7.9-v07-cr-checker-schema-repair` review complete，并由
`docs/testing/results/2026-06-02-v0.7-overall-validation.md` 提供 v0.7
checker/docs validation scope 的 clean pass 证据。该证据清除了 V07-CR checker/docs
blocker gate，但不证明 v0.8 readiness。

## 为什么现在做

用户启动了 v0.8 的 `/goal` development。Campaign 规则要求先完成 parent review 并创建
具体 child package，之后才可进入任何 implementation-bearing work。没有本 package，
后续 agent 可能把 planned `0.8.x` entries 当作 executable contracts，或把 v0.7
historical evidence 过度声明为 v0.8 pass evidence。

## 与 roadmap 的关系

v0.8 准备 core-side minimum working-state 与 external-validation handoff boundary。本
package 是 documentation baseline，让 `0.8.1-minimum-working-state-contract` 可以定义真正的
readiness claim taxonomy。

## 非目标

- 不实现 minimum working-state behavior。
- 不实现 observable public surfaces。
- 不运行或实现 external validation。
- 不添加 external application behavior。
- 不修复 runtime、API、frontend、schema、checker、fixture、migration 或 generated result
  files。
- 不声明 v0.8 runtime/API/frontend/E2E/Agent/autonomous/product/external validation
  readiness。

## 预期交接

`0.8.1-minimum-working-state-contract` 接收：

- 已同步到 child selection 的 parent v0.8 route/status。
- 仅作为 handoff context 的当前 v0.7 checker/docs repair 状态。
- v0.8 readiness 与 external validation PASS 的明确 non-claims。
- 仍然关闭的 implementation 与 evidence execution。
