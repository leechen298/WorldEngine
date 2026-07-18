# Contract

英文源文件：`contract.md`。

状态：文档已起草 / 等待评审

## 公开概念

- **Rule-bound event candidate**：公开 event proposal，引用 public rule ids、parameter ids、direction ids、public cause refs、probability evidence、causality evidence 和 public summary。
- **Legality gate**：现有公开 evaluator，在任何 state mutation 前接受或拒绝 candidate。
- **Public state diff**：脱敏安全的 parameter changes 列表，且这些变化在公开 rules 和 constraints 下合法。
- **Session evolution step**：有边界的 session API，从 attached rules、queued directions、runtime state 和 current public parameters 中 deterministic 选择或生成 public candidate。
- **Replay evidence**：event-log records 和 response evidence，让 client 能重建 accepted/rejected legality 和 applied public diffs。

## 允许修改

评审通过后，本包可以修改：

- `backend/app/schemas/world_evolution.py`，用于 additive session evolution request/response/evidence models。
- `backend/app/core/rule_linked_evolution.py`，用于 deterministic public candidate selection helpers，但仍必须使用现有 legality evaluator。
- `backend/app/core/world_session.py`，用于保留 session evolution 所需的 accepted public rule sets。
- `backend/app/api/routes/session.py`，用于 additive session evolution step endpoint。
- `backend/app/api/routes/world.py`，用于 additive manifest/discovery entries，以及仅针对现有 evolution evidence 的兼容性修复。
- 聚焦后端测试，覆盖 session evolution、现有 world evolution 兼容、manifest 兼容、redaction 和 replay evidence。
- 当前 package 文档以及 v0.11 route/review 状态文档。

## 禁止修改

本包不得：

- 绕过现有 legality evaluator。
- 应用 rejected 或 blocked candidates。
- 生成隐藏随机或 provider-derived candidates。
- 修改 Agent 私有记忆、目标、自我状态、关系、物品栏、受伤、死亡或私有位置。
- 把 “lightning-strike risk” guidance 变成直接 Agent injury/death；它只能影响公开 event probability/candidate evidence。
- 增加玩家掉落物品、直接详细事件触发或 player-as-world-entity gameplay。
- 暴露原始 direction instructions、原始 provider data、secrets、hidden context、raw prompts、raw responses、private evaluator data 或 Agent private memory。
- 实现 Validation Client behavior 或执行外部验证。
- 增加 persistence/migrations、frontend changes、具体 demo fixtures 或 `backend/worldengine/` changes。

## 兼容性要求

- 现有 `/worlds/{world_id}/evolution/evaluate-event` 测试和行为必须保持 additive-compatible。
- 现有 session create/from-worldview/rules/directions/run/status API 必须保持 additive-compatible。
- Event log 和 event-step replay outputs 必须保持 additive-compatible。
- Rejected candidates 不得改变 public state。
- Accepted candidates 必须包含 rule refs、parameter refs、存在时的 direction refs、public diff evidence 和 `direct_state_mutation_applied: false`。
- Unknown sessions 或缺少 accepted rules 时，必须返回公开 blocked/not ready response，而不是 crash。

## 范围外后续

- `0.11.5` 负责 worldview fidelity scoring、v0.11 validation closeout 和 Validation Client handoff evidence。
- `v0.12` 负责 Agent continuity 和外部 autonomous validation automation。
