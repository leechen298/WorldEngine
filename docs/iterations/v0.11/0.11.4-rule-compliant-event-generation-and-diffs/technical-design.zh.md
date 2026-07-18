# 技术设计

英文源文件：`technical-design.md`。

状态：文档已起草 / 等待评审

## 实现结构

本包保留现有 manual event evaluator，并新增 session-scoped evolution step：

```text
POST /sessions/{session_id}/evolution/step
```

Session step 是 deterministic。它使用附加到 session 的 accepted public rule set、session direction queue、当前 runtime tick/time 和 current public parameters 构造一个 public `WorldEventCandidate`。随后该 candidate 必须通过 `evaluate_world_event_candidate`。只有 accepted 且带 public `state_diff` 的 candidate 才能 apply。

## 影响文件

允许的实现文件：

- `backend/app/schemas/world_evolution.py`
- `backend/app/core/rule_linked_evolution.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_session_rule_bound_evolution_api.py`
- 必要时修改现有聚焦兼容测试

允许的文档 / 状态文件：

- 当前 package 目录。
- `docs/iterations/v0.11/CURRENT_STATE.md`
- `docs/iterations/v0.11/CURRENT_STATE.zh.md`
- `docs/iterations/v0.11/README.md`
- `docs/iterations/v0.11/README.zh.md`
- `docs/iterations/v0.11/v0.11-plan.md`
- `docs/iterations/v0.11/v0.11-plan.zh.md`
- `docs/iterations/v0.11/review.md`
- `docs/iterations/v0.11/review.zh.md`

## 数据 / 控制流

```text
client
  -> POST /sessions/{session_id}/evolution/step
  -> resolve WorldSession
  -> require accepted public rule set
  -> inspect queued public directions
  -> deterministically build/select one public candidate
  -> evaluate_world_event_candidate(...)
  -> if accepted and apply=true:
       apply public ParamPatchItem list to WorldState
       append world.session_evolution.accepted event
     else:
       append world.session_evolution.rejected or blocked evidence
  -> return public result with candidate, legality, diff, and replay refs
```

Candidate selection 必须简单且可解释。它可以选择最高优先级 accepted rule 及其第一个 public target parameter，根据 current state 和 rule constraints 推导下一个 bounded public value，并附加当前可用 queued direction id。不得使用 unbounded randomness、provider output、hidden evaluator data 或 raw instruction text。

## 兼容策略

- 复用现有 `WorldEventCandidate`、`WorldEventEvaluationRequest` 和 `evaluate_world_event_candidate` 语义。
- 保持 manual world-level evaluation 兼容。
- Session changes 保持 additive。
- Event-log replay records 保持 additive。
- 当 session 缺少 attached accepted rules 或无法生成合法 candidate 时，返回公开 blocked/not-ready responses。

## 防漂移规则

- 不实现多步 narrative simulation。
- 除非 contract 更新并通过 review，否则不消费 / dequeue directions。
- 不修改 Agent private state。
- 不引入 provider calls 或 external validation。
- 不增加具体 world fixtures。
