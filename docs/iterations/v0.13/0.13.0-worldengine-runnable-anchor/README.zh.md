# 0.13.0 WorldEngine 可运行锚点

英文源文件：`README.md`。

状态：closed / WorldEngine 侧锚点已验证
类型：mixed implementation package
implementation_authorized: yes
provider_live_call_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## 目标

实现一条确定性的 WorldEngine 侧纵向切片：能够生成可运行世界包、启动一个 Session、推进精确
锁步 tick、让一个 Agent 完成有因果证据的动作循环、判定一次被接受和一次被拒绝的用户干预、
暴露通用客户端投影，并通过项目管理控制台操作整个流程。

本 package 证明核心可以运行，但不声明完整 MVP PASS；Godot 和外部 checker 仍然是 v0.13
必须完成的后续 package。

## 范围

评审批准后，本 package 可以新增：

- 版本化、通用的 control/runtime/evidence HTTP contract。
- 基于结构化输入和固定 seed 的确定性世界包生成。
- Package readiness validation 和不可变 `package_hash`。
- 进程内 Session boot 和 lockstep `step N` 执行。
- 单调 event sequence、tick、revision、snapshot 和 `state_hash` 证据。
- 一个 WorldEngine-owned Agent perception/decision/action/result loop。
- 能影响后续 Agent 决策的有界公开 experience link。
- 带明确 tick-boundary window 的 accepted/rejected intervention。
- 为未来客户端准备的通用 action 和 feedback request 边界。
- 只使用 public/control API 的工作型管理控制台。
- 聚焦 backend、frontend 和 E2E tests。

## 交付物

- Public capability manifest 和版本化 API schemas。
- 确定性 `RunnableWorldPackage` 和 readiness result。
- 可运行 Session state、event/diff/snapshot 主干和 public projection。
- Agent 因果链证据和引用先前经历的后续决策。
- 来自同一个 open window 的 accepted/rejected intervention evidence。
- 覆盖生成、Session 控制、Agent 检查、干预、时间线和 evidence export 的管理控制台。
- 通用黑盒协议测试和 review evidence。

## 文档

- [x] `intent.md`
- [x] `contract.md`
- [x] `technical-design.md`
- [x] `test-plan.md`
- [x] `plan.md`
- [x] `review.md`

## 状态清单

- [x] 文档已起草
- [x] 用户评审完成
- [x] Documentation/contract evaluator PASS
- [x] 实现已授权
- [x] 实现完成
- [x] 聚焦验证完成
- [x] 独立评审 gate 完成
- [x] Package closeout 完成

## 当前评估

WorldEngine 侧锚点已经实现，并依次通过聚焦后端、前端、E2E、黑盒、真实浏览器、代码评审、
验证证据和收口一致性 gate 后关闭。全后端测试仍如实记录为 `484 passed, 1 failed`，原因是
无关的脏 legacy manifest/test 不匹配，因此不声明全仓全部通过。完整 v0.13、Godot 和外部
checker 仍是尚未执行的后续 package 工作。
