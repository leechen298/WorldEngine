# v0.13 最小可运行 MVP 锚点

英文源文件：`README.md`。

状态：documentation preparation / active child 0.13.1
类型：mixed goal campaign
implementation_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## Goal 入口

自然语言目标别名：

```text
complete v0.13 minimum runnable MVP
finish v0.13 minimum runnable MVP
完成 v0.13 最小可运行 MVP
做出一个能跑的 MVP 版本
```

Goal runner：`GOAL_RUNNER.zh.md`。

## 目标

交付一条足够小、但从头到尾完整的纵向切片，证明下面这条产品闭环：

```text
世界简述
-> 可运行世界包
-> Session 启动
-> 有界世界推进
-> Agent 感知、决策并提出动作
-> WorldEngine 通过公开规则接受或拒绝
-> 一次被接受和一次被拒绝的用户干预
-> 事件、diff、快照、Agent 经历和投影证据
-> 管理控制台与通用客户端协议看到同一场运行
-> 外部 Godot 执行端和 checker 对运行结果分类
```

这个版本优先选择最不容易被外部条件阻断的路径。核心闭环能够运行之前，不得强制依赖实时
LLM provider、实时网络、生产级持久化、精美游戏或第三个外部仓库。

## 方向重置

v0.10-v0.12 的文档和实现证据保留为历史背景，但它们不再定义 v0.13 的目标架构，也不能证明
本次锚点运行已经通过。只有经过 v0.13 contract 重新核对的现有代码才可以复用；现有代码不得
反过来缩小或改写目标流程。

本次重置不会删除或回滚已有工作，而是建立一份新的评审契约，用来决定哪些内容保留、替换或隔离。

## 仓库职责

| 仓库 | 负责 | 不得负责 |
| --- | --- | --- |
| `WorldEngine` | 通用世界生成、运行和 Agent 契约，历史真实，公共客户端协议，管理控制台，公开证据导出 | 具体验证世界、Godot 场景、外部判定答案、客户端直接写入正典事实 |
| `WorldEngine-Validation-Client` | Godot 场景执行端、具体外部锚点世界、操作记录、独立 checker、最终外部结果目录 | Provider 所有权、WorldEngine 内部实现、直接数据库访问、绕过公共 API 修改正典 |

WorldEngine 始终是 canonical world facts 和 event legality 的权威。External checker 只对“当前
公开证据是否支持本 validation suite verdict”拥有判定权，不能重新定义世界事实。

v0.13 暂不新建第三个仓库。外部仓库内部必须把 Godot executor 和 checker 拆成独立包与独立
进程，executor 不能自行宣布验证通过。

## 子包顺序

1. `0.13.0-worldengine-runnable-anchor`
   - 已关闭：WorldEngine 侧 headless 闭环、通用 HTTP 协议、管理控制台和公开 evidence
     bundle 已按 package 范围验证。全后端回归仍为 `484 passed, 1 failed`，不写成全仓全部通过。
2. `0.13.1-godot-validation-client-anchor`
   - 当前只进入文档准备阶段。必须先建立并评审外部 milestone，之后才能授权 Godot、checker、
     Web、API 或外部仓库修改。
3. `0.13.2-anchor-run-validation-and-closeout`
   - 让同一个外部场景依次经过 WorldEngine、管理控制台、Godot 和 checker，并根据当前证据以
     `PASS`、`PARTIAL`、`BLOCKED` 或 `FAIL` 收口。

只有当前 active child 可以授权实现。后续 planned child 不会自动授权代码或外部仓库变更。

## 当前 active package

`0.13.0-worldengine-runnable-anchor` 已按 WorldEngine 侧范围关闭。当前 active child 是
`0.13.1-godot-validation-client-anchor`，但只处于文档准备状态；其实现、外部仓库修改和
证据执行均未授权。完整 v0.13 仍未得到证明，必须等 Godot/checker package 实际运行，再由
`0.13.2` 记录相关联的结果。

## MVP 非目标

- 必过验收路径不依赖 live provider。
- 不做 WorldEngine 与 Godot 的逐帧同步。
- 不强制 WebSocket；带 cursor 的 HTTP polling 已足够。
- 不做生产数据库、分布式 runtime、多人游戏或部署。
- 不做精美游戏美术、战斗系统、完整经济和库存模拟或游戏发行。
- 不做多 Agent 社会、递归子世界、完整人格模型、raw thought 或 private memory 暴露。
- WorldEngine 仓库内不放具体锚点世界内容。
- 不把 v0.10-v0.12 的历史证据声明为 v0.13 PASS。

## Campaign 退出条件

只有满足以下条件，v0.13 才算完成：

- WorldEngine 侧锚点闭环可以从干净状态启动并运行。
- 管理控制台只通过 public/control APIs 操作。
- 通用客户端协议中不出现 Godot 专属语义。
- 一次合法干预经过规则被接受，一次直接指定事实的干预被拒绝，并留下证据。
- 至少一次后续 Agent 决策引用先前公开事件或经历。
- Godot 看到同一份公开状态，并通过公共协议回传至少一个类型化反馈事件。
- 独立 checker 关联 WorldEngine 和 Godot 证据，输出当前的 `PASS`、`PARTIAL`、
  `BLOCKED` 或 `FAIL`。
- 没有未解决的 P1/P2 finding。
