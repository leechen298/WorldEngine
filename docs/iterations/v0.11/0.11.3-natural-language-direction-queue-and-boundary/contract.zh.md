# Contract

英文源文件：`contract.md`。

状态：文档已起草 / 等待评审

## 公开概念

- **Session direction**：绑定到 WorldSession 的用户自然语言指令，并按世界级 guidance 评估。
- **Queued direction**：被接受的公开 guidance，可在后续影响事件候选生成、概率、环境趋势、规则约束或评估提示。
- **Rejected direction**：被拒绝的指令，包括尝试直接最终事实、Agent 私有状态变更、Agent 目标变更、物品注入、关系覆盖、规则绕过或私有标记暴露。
- **Direction boundary**：用户 guidance 永远不直接修改世界状态、最终事实、Agent 私有状态、Agent 目标、物品栏、关系或事件结果。
- **Replayable operation record**：公开、脱敏的 operation-log / event-style 记录，让 client 能重建某条 direction 已入队或被拒绝，但不暴露原始指令文本或私有上下文。
- **Client status classification**：公开的 queued / rejected direction 状态、分类类别和 direct-mutation 标记，供外部消费者在不运行隐藏逻辑的情况下检查。

## 允许修改

评审通过后，本包可以修改：

- `backend/app/schemas/session.py`，用于 additive session direction 摘要响应模型或 session 字段。
- `backend/app/core/world_session.py`，用于内存 session direction 队列存储和摘要 helper。
- `backend/app/api/routes/session.py`，用于 additive `POST /sessions/{session_id}/directions` 和 `GET /sessions/{session_id}/directions` 接口。
- `backend/app/api/routes/world.py`，仅用于公开 manifest / discovery 条目。
- 聚焦后端测试，覆盖 session direction queue、既有 world direction 兼容、manifest 兼容和脱敏。
- 接受和拒绝 session directions 的公开 operation evidence；使用脱敏 event-style records，包含 session id、world id、接受时的 direction id、status/classification、timing metadata、未脱敏时的 public context keys、instruction length 和 `direct_state_mutation_applied: false`。
- session direction responses 和 summaries 中的 client-readable status classification。
- 当前 package 文档以及 v0.11 route / review 状态文档。

除非通过评审的设计更新明确改变，否则实现必须复用现有 `WorldDirectionRequest`、`WorldDirectionResponse`、`WorldDirectionQueueItem` 和 `classify_world_direction` 语义。

## 禁止修改

本包不得：

- 实现规则合规事件生成、状态 diff 或事件应用。
- 允许 “kill this Agent now” 这类直接最终事实命令。
- 把 lightning-risk guidance 变成结果；它只能成为外部压力。
- 通过 direction guidance 修改 Agent 私有记忆、目标、自我状态、关系、物品栏、受伤、死亡或位置。
- 增加玩家掉落物品、直接详细事件触发或玩家作为世界实体的玩法。
- 绕过公开规则、状态、概率、时间、位置或合法性检查。
- 在公开事件 payload 或摘要中暴露原始指令文本。
- 暴露 secret、原始 provider trace、原始 prompt、原始 response、隐藏上下文或私有 evaluator 数据。
- 增加 provider 调用、外部 Validation Client 调用、持久化、迁移、具体 demo-world fixture 或 `backend/worldengine/` 修改。

## 兼容性要求

- 现有 `/worlds/{world_id}/direction` 行为和测试必须保持兼容。
- 现有 session create、worldview-to-session、rule attach/read、run、status、events 和 snapshot API 必须保持 additive 兼容。
- Direction queue 响应必须保持公开且脱敏安全。
- 被拒绝的 direction 不得创建 queued item，且必须报告 `direct_state_mutation_applied: false`。
- 被接受和被拒绝的 session directions 必须产生可 replay 的公开 operation evidence，且不回显原始指令。
- Client consumers 必须能从公开 status/classification 字段区分 queued 和 rejected guidance。
- 未知 session 必须返回现有 session 404 行为。

## 范围外后续

- `0.11.4` 负责事件候选生成、合法性评估、diff 应用、direction 消费和 replay evidence。
- `0.11.5` 负责 worldview fidelity validation 和 v0.11 closeout。
- `v0.12` 负责 Agent continuity 和外部自动化验证集成。
