# Technical Design

## 文档结构

本 package 在以下路径添加具体 child package：

```text
docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/
```

Package 包含标准七个英文文档及对应中文镜像。虽然本 package 是 documentation-only，但它会改变
goal routing、status semantics、evidence rules 和 mirror obligations，因此仍包含
`technical-design.md` 与 `test-plan.md`。

## 受影响文件

允许的 child package 文件：

- `README.md` 与 `README.zh.md`
- `intent.md` 与 `intent.zh.md`
- `contract.md` 与 `contract.zh.md`
- `technical-design.md` 与 `technical-design.zh.md`
- `test-plan.md` 与 `test-plan.zh.md`
- `plan.md` 与 `plan.zh.md`
- `review.md` 与 `review.zh.md`

允许的 parent status 文件：

- `docs/iterations/v0.8/README.md`
- `docs/iterations/v0.8/README.zh.md`
- `docs/iterations/v0.8/v0.8-plan.md`
- `docs/iterations/v0.8/v0.8-plan.zh.md`
- `docs/iterations/v0.8/GOAL_RUNNER.md`
- `docs/iterations/v0.8/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.8/CURRENT_STATE.md`
- `docs/iterations/v0.8/CURRENT_STATE.zh.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.8/review.md`
- `docs/iterations/v0.8/review.zh.md`

不影响 runtime、schema、API、frontend、backend test、checker implementation、
fixture、migration、generated result、external repository 或 legacy implementation files。

## 控制流

1. 用户启动 v0.8 `/goal` development。
2. Agent 读取 parent `CURRENT_STATE.md`、`GOAL_RUNNER.md`、`CAMPAIGN_PLAN.md`、
   `v0.8-plan.md` 和 `review.md`。
3. Agent 确认当前没有 active child，parent route 是 documentation review。
4. Agent 从 `docs/iterations/v0.7/` 验证当前 v0.7 handoff state。
5. Agent 创建本 package，更新 parent status 以 route 到 `0.8.1`，并记录
   documentation-only evidence。
6. 后续工作通过创建或确认 `0.8.1` 的完整 package document set 来启动。

## 兼容策略

- 把 `0.7.9` checker/docs clean pass 仅作为 handoff evidence。
- 保留 v0.8 对 runtime/API/frontend/E2E/Agent/autonomous、external validation、
  external consumer、product readiness 和 minimum working-state readiness 的 non-claims。
- 在每个 child package 创建并 review 前，planned package entries 只作为 route-map specs。
- 保持 implementation authorization 关闭。

## 防漂移规则

- Parent 与 child status surfaces 必须一致记录：`0.8.0` review complete，`0.8.1`
  selected / child docs not created。
- 英文和中文镜像必须保持 status、authorization、scope、forbidden changes、findings 和
  final assessment 语义一致。
- 当前 v0.7 checker/docs clean pass 不得转换成 v0.8 PASS evidence。
- 不得引入 external validator implementation 或 concrete external application detail。
