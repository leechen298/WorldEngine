# v0.13 Campaign Plan

英文源文件：`CAMPAIGN_PLAN.md`。

状态：documentation preparation / active child 0.13.1

## 目标

把架构讨论推进成一条对外可见、可被独立判定的 MVP，同时不让当前实现细节或单一客户端技术
反过来定义 WorldEngine。

## 权威输入

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/project-plan.md`
- `docs/roadmap.md`
- `docs/living-world-development-flow.zh.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- v0.13 package 中记录的用户已确认决策

现有 runtime 代码只是实现资产清单，不是权威设计输入。

## Campaign 阶段

### 阶段 1：WorldEngine 可运行锚点

已按 `0.13.0` package 范围关闭：headless core、通用协议、管理控制台和 evidence bundle 已
在不依赖外部服务的条件下得到验证，但这不代表全仓全部通过或完整 v0.13 PASS。

### 阶段 2：Godot executor 与独立 checker

当前只进行文档准备。先为 `WorldEngine-Validation-Client` 中的最小 Godot 2D executor 和
独立 checker 进程建立并评审外部 milestone；只有实现另行获批后，具体锚点世界才会放入
该外部仓库。

### 阶段 3：端到端验收

通过管理控制台和 Godot 运行同一场景，关联 WorldEngine evidence、Godot observations 和
checker assertions，并记录当前分类结果。

## Campaign 约束

- 同一时间只有一个 active package。
- 实现前必须经过文档和 evaluator gate。
- WorldEngine-only active package 不修改外部仓库。
- 最小 PASS 路径不要求 live provider。
- 客户端不能自证通过。
- WorldEngine 中不放具体验证内容。
- 外部运行证据存在之前，不声明完整 MVP PASS。

## 退出条件

只有 `v0.13-plan.zh.md` 中所有 package exit criteria 都满足，且 `0.13.2` 记录最终证据分类后，
campaign 才能结束。
