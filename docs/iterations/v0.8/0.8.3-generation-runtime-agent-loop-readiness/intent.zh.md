# Intent

## Objective

定义并在 review 后可选实现最小 generic generation/runtime/Agent-loop readiness path，
支撑 v0.8，同时不把 WorldEngine 变成 external validator。

## Problem

v0.6 generation 已能创建或 preview `WorldSpec` material。Runtime readiness 已能校验
candidate `WorldSpec` 并 summarise runtime context。Agent loop 已能构建 bounded perception
并执行 deterministic `noop`。这些能力彼此相邻，但还没有被组织成一条明确的 core-side
readiness probe。

没有这条 probe，v0.8 无法用当前 session evidence 做一个窄范围声明：candidate generated
world 已能通过 minimum generic core loop。同时，完整 generated-world runtime、external
validator、product app 或 live provider flow 都会超出当前 v0.8 scope。

## Intended Outcome

Review 后，本 package 可以授权一个 read-only、isolated probe：

1. 接受 generic generation preview input 或 candidate `WorldSpec`。
2. 使用既有 loader/runtime-context semantics 派生 runtime readiness。
3. 创建 isolated in-memory runtime context，不修改 app runtime。
4. 推进 isolated runtime 一步，并记录 bounded event evidence。
5. 对 bounded perception 运行 default Agent loop `noop`。
6. 只返回 redacted、generic evidence。

## Non-Goals

- 不在 app runtime 中 active execution generated world。
- 不实现 external validator。
- 不实现 external application、UI、product workflow 或 deployment。
- 不添加 public memory management API。
- 不实现 pseudo-self、self-narrative、relationship history、personality drift 或
  long-term preference surface。
- 不调用 live AI provider，也不判断 generation quality。

## Handoff Criteria

只有 review 记录以下任一结果时，本 package 才能 hand off 给 `0.8.4`：

- bounded core-readiness probe 的 implementation evidence；或
- 明确 deferral reason，以及阻止 minimum loop claim 的 exact missing evidence。
