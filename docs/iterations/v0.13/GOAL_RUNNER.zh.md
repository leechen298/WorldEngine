# v0.13 Goal Runner

英文源文件：`GOAL_RUNNER.md`。

状态：documentation preparation active

## Goal 入口

当用户要求完成最小可运行 MVP、完成 v0.13，或提出同等目标时，运行本 campaign。

## 当前路由

`0.13.0-worldengine-runnable-anchor` 已按 WorldEngine 侧范围关闭。当前 active child 是
`0.13.1-godot-validation-client-anchor`，但只进入文档准备阶段。
`implementation_authorized`、`external_repository_changes_authorized` 和
`evidence_execution_authorized` 均保持 `no`；修改任何外部代码或运行 Godot/checker 证据前，
必须先准备并评审外部 milestone。

## 状态机

1. 依次读取 `CURRENT_STATE.zh.md`、`CAMPAIGN_PLAN.zh.md`、`v0.13-plan.zh.md` 和当前
   active child package。
2. 只有 `active_child` 是当前实现范围。
3. 完成并验证 active child 文档。
4. 请求只读 documentation/contract evaluator。
5. 用户批准且 active child review 记录 `implementation_authorized: yes` 之前，不得实现。
6. 只实现 active child contract。
7. 按 `docs/iterations/AGENTS.md` 要求，在对应 gate 请求 implementation-scope、
   code-review、validation-evidence 和 closeout-consistency evaluator。
8. 用当前命令和证据更新 active child `review.zh.md`。
9. 只有 active child 退出条件通过，或 package 诚实记录 blocker 后，才更新
   `CURRENT_STATE.zh.md` 并推进下一包。

## 风险排序 Gate

`0.13.0` 的顺序：

```text
文档契约
-> 通用协议 schema
-> 确定性生成与 Session boot
-> runtime/event/diff/snapshot 主干
-> 与经历关联的 Agent 第二次决策
-> 被接受和被拒绝的用户干预
-> 管理控制台
-> 聚焦测试与 API/UI smoke
-> closeout
```

进入 `0.13.1` 时，必须先读取外部仓库的 `AGENTS.md` 并建立该仓库自己的已评审 milestone
文档，之后才能修改 Godot、checker、Web 或 API 文件。

## Stop Conditions

出现以下情况时停止实现并先更新 active 文档：

- 必过路径需要 live provider 才能运行。
- 具体验证世界将进入 WorldEngine 仓库。
- 管理控制台将绕过 API 直接写正典状态。
- 公共客户端协议出现 Godot 专属 node、scene tree、animation、collision shape 或 frame 语义。
- 客户端 action 或 feedback event 可以绕过规则判定和事件证据直接修改正典状态。
- 只能通过 private state 或 raw thought 证明 Agent 连续性。
- checker import WorldEngine 内部代码，或接受 executor 自己声明的 PASS。
- 仍有未解决的 P1/P2 finding。

## 证据规则

历史结果不能作为当前 v0.13 证据。任何 PASS 声明都必须来自当前 package run 产生的命令结果
和 artifacts。
