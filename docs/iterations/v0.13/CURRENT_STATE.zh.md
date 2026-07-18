# 当前状态

英文源文件：`CURRENT_STATE.md`。

campaign_status: documentation preparation / active child 0.13.1
active_child: 0.13.1-godot-validation-client-anchor
implementation_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## 当前决策

`0.13.0-worldengine-runnable-anchor` 已按 WorldEngine 侧范围关闭。其聚焦后端、前端、E2E、
黑盒、浏览器和 evaluator gate 已通过；无关的全后端结果仍记录为 `484 passed, 1 failed`。
Campaign 现在进入 `0.13.1` 文档准备阶段，让 Godot adapter 和独立 checker 消费通用协议，
而不是反过来重新定义协议。

## 历史证据规则

- v0.10-v0.12 的文档和命令结果在本 campaign 中只作为历史背景。
- 它们不能证明 v0.13 行为。
- 只有当前测试证明满足 v0.13 contract 的既有实现才可以保留。
- 即使新 package 选择了不同架构，也不得因此回滚或覆盖工作区里的既有用户改动。

## 下一步

读取外部仓库治理规则，准备完整且可评审的
`0.13.1-godot-validation-client-anchor` 文档 package。在该 package 通过 documentation
evaluator 并获得明确的实现和外部仓库修改授权前，不修改 Godot、checker、legacy Web/API
或任何外部仓库文件。
