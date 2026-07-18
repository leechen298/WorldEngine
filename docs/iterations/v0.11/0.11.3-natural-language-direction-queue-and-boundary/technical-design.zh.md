# 技术设计

英文源文件：`technical-design.md`。

状态：文档已起草 / 等待评审

## 实现结构

本包在现有 world direction 分类器外增加 additive session 级封装。

预期接口：

```text
POST /sessions/{session_id}/directions
GET  /sessions/{session_id}/directions
```

`POST` 接收现有 `WorldDirectionRequest`。它解析 session，通过 `classify_world_direction` 分类指令，并返回公开响应。若被接受，则存储绑定到 session `world_id` 的 `WorldDirectionQueueItem`；若被拒绝，则只增加 rejected evidence，不创建 queued item。

`GET` 返回公开 session direction 摘要，包含 queued items 和 rejected count。

被接受和被拒绝的提交也会创建公开 operation evidence。Evidence 可以使用现有 event log 风格，但必须可脱敏安全且可由 client replay：

```text
world.session_direction.queued
world.session_direction.rejected
```

Payload 包含 session id、world id、instruction text length、classification/status、`direct_state_mutation_applied: false`、timing metadata，以及仅在 classification 未 redacted 时包含 public context keys。被接受的记录包含生成的 direction id。被拒绝的记录不创建 queued item。

## 影响文件

允许的实现文件：

- `backend/app/schemas/session.py`
- `backend/app/core/world_session.py`
- `backend/app/api/routes/session.py`
- `backend/app/api/routes/world.py`
- `backend/app/tests/test_session_direction_queue_api.py`
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
  -> POST /sessions/{session_id}/directions
  -> session store resolves WorldSession
  -> classify_world_direction(...)
  -> if allowed:
       create WorldDirectionQueueItem
       append to session direction queue
       record public queued operation evidence
     else:
       increment rejected count
       record public rejected operation evidence
  -> return public response with direct_state_mutation_applied false
```

公开摘要绝不能包含原始指令文本。redacted 分类结果必须隐藏 branch id 和 context keys，与现有 world-direction 行为一致。

## 兼容策略

- 尽量复用现有 direction request / classification / response 模型。
- 所有 session 变更保持 additive。
- 不改变现有 world-direction endpoint 行为。
- 未知 session 处理保持与现有 session endpoints 一致。
- Manifest 增量增加且可发现。
- Operation evidence 通过公开 event/log inspection 可 replay，且不回显原始指令。
- Client status classification 通过公开 response 和 summary fields 可见。

## 防漂移规则

- 本包不消费 direction queue items。
- 不把 direction guidance 当作事件结果。
- 不增加具体世界内容或 demo story facts。
- 不存储原始指令文本。
- 不增加 provider、Validation Client、持久化、迁移或 `backend/worldengine/` 工作。
