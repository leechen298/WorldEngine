# 技术设计

英文源文件：`technical-design.md`。

## 设计立场

本设计来自目标活世界流程，不从现有实现结构推导。进入实现阶段后，先审计当前代码是否可以安全
复用；不兼容路径可以在新的版本化 surface 后隔离，但本 package 不做破坏性删除。

## 规划结构

实现应在 active `backend/app/` 路径下建立一个职责完整、通用的 engine 边界：

```text
backend/app/engine/
  models.py             规范化正典 runtime records
  generation.py         deterministic WorldBrief -> RunnableWorldPackage
  rules.py              action/direction/feedback legality
  session.py            boot、lockstep step、state 和 revision ownership
  agent_runtime.py      public perception、deterministic policy、action chain
  evidence.py           events、diffs、snapshots、hashes、export

backend/app/schemas/engine_v1.py
backend/app/api/routes/engine_v1.py
backend/app/tests/test_engine_v1_*.py
```

实现阶段代码审计后可以调整准确文件，但职责必须保持分离。任何实质性的路径或边界变化都要先更新
文档并重新评审。

管理控制台在 `frontend/src/` 下新增一个聚焦的操作 surface，包含：

- 结构化 world brief 和 seed 输入。
- Generated package readiness 和 hash 显示。
- Session boot 和精确 step 控制。
- 带 tick/revision/state hash 的 canonical projection 摘要。
- Agent public state、最新 perception/decision/action result 和 experience refs。
- Active intervention window、direction submission 和 judgment result。
- Event/diff/snapshot timeline 和 evidence export。

它不能变成营销页面或游戏投影。

## 确定性生成

必过路径只使用结构化输入和固定 seed，输出以下规范化 public sections：

```text
world_spec
rule_catalog
action_catalog
agent_seed_set
projection_manifest
evidence_policy
```

计算 hash 前按 identifier 和 collection 排序。Readiness validation 检查引用、mutable fields、
rule/action preconditions、Agent seeds 和 projection fields。Session boot 只接受 ready package，
并保存 `source_package_hash`。

Generator 不随代码附带具体世界 fixture。Core tests 在测试代码中构造通用结构化输入；外部仓库
以后拥有具体 anchor brief 和 visual assets。

## Session 与 Lockstep Runtime

最小 runtime 是进程内、命令驱动的：

1. Session 以 `ready` 且 paused 状态启动。
2. 客户端用 `request_id` 和可选 `expected_revision` 请求 `step_count`。
3. 每一步打开或推进明确 intervention window，消费 accepted queued direction，评估 world
   rules，运行 Agent cycle，判定 action/feedback candidate，应用 accepted diff，记录 rejected
   result，保存 snapshot，并发布新 projection。
4. Tick、world time、event sequence 和 revision 单调增长。
5. 每一步后根据规范化 canonical public state 计算 `state_hash`。

MVP 中每个 step 是原子的。Commit 之前失败时保留旧 revision，并在 canonical history 之外记录
安全 diagnostic，不允许 partial diff。

## Event、Diff、Snapshot 与 Projection 主干

每次 canonical mutation 都遵循：

```text
request/candidate
-> rule judgment
-> accepted 或 rejected event
-> applied diff 或明确 no-diff
-> canonical state
-> snapshot
-> public projection
```

Evidence 使用稳定关联字段：

- `request_id`
- `package_id` 和 `package_hash`
- `world_id` 和 `session_id`
- `tick`、`event_sequence` 和 `revision`
- `state_hash_before` 和 `state_hash_after`
- rule、action、direction、Agent 和 event refs。

Event polling 使用 `after_sequence`；WebSocket 明确推迟。

## 最小 Agent Runtime

必过 Agent 路径是 deterministic 且 provider-independent 的，不是聊天 wrapper，也不暴露
private thought。

Cycle 1：

1. 从 projection、allowed actions 和近期 public events 构造 public perception frame。
2. 通过 deterministic policy interface 选择 bounded public intent。
3. 产生 `ActionRequest`。
4. Rule service 返回 `ActionResult`。
5. 记录 public causal evidence 和 `AgentExperienceRef`。

Cycle 2 或更晚：

- Public decision input 包含先前 experience ref。
- 输出记录哪条 prior ref 影响了 public decision。
- 测试必须观察到：与没有 prior experience 的同一路径相比，decision/evidence result 有变化。

这是连续性的最低证明。Long-term memory、consolidation、personality drift 和 self-narrative
明确推迟。

## 用户干预

只有明确 open window 接受干预，且两条必测请求使用相同 `window_id`：

- 合法：bounded pressure/constraint，进入 queued direction 或 event candidate，在后续 step
  中被评估。
- 非法：直接指定 final fact、inventory、death、teleport 或同类 canonical patch；返回稳定
  semantic code，没有 diff。

Window-closed rejection 需要单独测试，不能冒充非法 direction 的语义拒绝。

## 通用客户端边界

协议保持 engine-neutral：

- HTTP JSON command/query operations。
- 操作前进行 capability discovery。
- Mutation 使用 request ID 保证幂等。
- 使用 expected revision 做 optimistic concurrency。
- 使用 event cursor polling。
- Typed action 和 feedback 始终经过 WorldEngine judgment。

管理控制台是第一个 consumer。`0.13.1` 中的 Godot 必须能够在 WorldEngine 内没有 private
adapter service 的情况下实现同一流程。

## 错误处理

- Invalid world package：返回 field diagnostics，不进入 ready。
- Unknown package/session：`404` 类响应。
- 重复 mutation request ID：幂等返回原始 result。
- Stale expected revision 或 closed window：稳定 conflict code，不修改状态。
- Illegal action/direction/feedback：domain-level rejected result、rejected event、reason code，
  没有 applied diff。
- Atomic step failure：保留旧 revision，不产生 partial canonical diff。
- Evidence export gap：export 标记 incomplete，后续 checker 不得解释为 PASS。

## 兼容策略

- 新增干净的版本化 surface，不把目标概念硬塞进历史 routes。
- 本 package 中与 existing APIs 并存注册。
- 只有 contract-level tests 证明等价后才复用内部代码。
- `0.13.0` 不删除历史 endpoints 或 dirty files。

## 防漂移规则

- Core source/tests 中没有具体外部场景。
- Live provider fallback 不得成为 PASS 前提。
- 不存在 frontend-only success path。
- 没有 event 和 diff evidence 就不能修改状态。
- 不接受客户端编写的 final outcome 作为 Agent action result。
- `0.13.2` 外部 evidence 之前不声明完整 MVP。
