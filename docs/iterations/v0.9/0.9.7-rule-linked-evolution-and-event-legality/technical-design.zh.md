# 技术设计

英文原文：`technical-design.md`。

## Active Backend 放置位置

实现必须留在 `backend/app/`。推荐文件形状如下：

```text
backend/app/schemas/world_evolution.py
backend/app/core/rule_linked_evolution.py
backend/app/api/routes/world.py
backend/app/tests/test_rule_linked_evolution_legality.py
```

如果本地代码风格更适合相邻的窄模块名，可以调整命名。不得在 `backend/worldengine/` 下新增运行时功能。

## 数据流

1. 调用方提交或构造一个 `WorldEventCandidate`。
2. 确定性合法性 helper 接收：
   - candidate。
   - `GeneratedRuleParameterSet`，或已接受的规则/参数集合摘要。
   - 当前公开参数值。
   - 当前 runtime tick 和 world time。
   - 可选的 `0.9.6` 已接受 direction queue refs。
3. Helper 验证 rule refs、parameter refs、allowed operations、constraints、timing、causality evidence、probability evidence 和 redaction。
4. 如果候选被接受，helper 返回 `WorldEventLegalityResult(status="accepted")`，其中包含 `WorldStateDiff` 和 `WorldEvolutionEvidence`。
5. 如果候选通过可应用的 route 被接受，公开 parameter patches 会应用到 active in-memory `WorldState`，同时 accepted event 会记录 diff/replay evidence。
6. 如果候选被拒绝，helper 返回公开 diagnostics，不追加 accepted event，也不做 state mutation。

## Schema 说明

`WorldEventCandidate`

- `candidate_id`：稳定的公开 id。
- `world_id`：公开 world id。
- `event_type`：公开 event type。
- `source`：公开来源标签，默认 `world_rule`。
- `proposed_tick`：可选的当前或未来 tick。
- `proposed_world_time_seconds`：可选的世界时间。
- `rule_refs`：非空公开 rule ids。
- `parameter_patches`：非空公开参数 patch 请求。
- `direction_refs`：可选公开 direction ids。
- `cause_refs`：非空公开事件或状态 refs。
- `location_refs`：可选公开 refs。
- `probability_evidence`：结构化的公开概率或权重证据。
- `causality_evidence`：结构化的公开因果证据。
- `public_summary`：脱敏后的公开摘要。

`WorldParameterPatch`

- `parameter_ref`
- `op`
- `value`
- `rule_ref`
- `public_explanation`

操作词表必须兼容 `0.9.3` 的 allowed ops：`add`、`set`、`remove`。

`WorldEventLegalityDiagnostic`

- `code`
- `message`
- `path`
- `severity`

诊断信息不得回显不安全的用户值或 provider 值。

## 合法性算法

确定性 helper 应当：

1. 扫描 candidate ids、refs、summaries、evidence objects、patches 和 values 中的脱敏标记。
2. 如果提供了完整 rule set，使用既有 `0.9.3` validation helper 验证它。
3. 为 rules、parameters、constraints 和 current values 建立公开 lookup maps。
4. 要求至少一个 candidate rule ref 和一个公开 cause ref。
5. 对每个 patch：
   - 要求 parameter ref 能解析。
   - 要求 rule ref 能解析。
   - 要求 parameter 被 matched rule 覆盖。
   - 要求 operation 位于 matched rule 的 `allowed_ops` 中。
   - 计算 patch 后的公开值。
   - 验证公开 constraints 和 value type。
6. 基于当前 runtime state 和有界请求窗口验证 candidate timing。
7. 要求公开 causality evidence 和 probability evidence。
8. 拒绝 direct final fact 或 Agent private-state 类别。
9. 只有不存在 blocking diagnostics 时才返回 accepted evidence。

## Event 集成

如果实现暴露 API route，accepted results 可以追加一个通用事件类型，例如 `world.evolution.accepted`。payload 必须是公开的，并包含：

```text
world_id
candidate_id
legality_status
matched_rule_ids
changed_parameter_ids
state_diff
evidence
redaction_status
direct_state_mutation_applied: false
```

Accepted apply behavior 只能更新 accepted diff 覆盖的公开 in-memory world parameters。它不得安装 durable rules、不得 mutate hidden state，也不得绕过 public diff/evidence record。Evaluate-only helper 可以用于测试或内部调用，但任何 canonical application 都必须同时记录 accepted event 和可 replay 的 state diff。

Rejected candidates 只有在 payload 不包含 unsafe raw candidate values，且不会暗示 canonical state 已被接受时，才可以追加 `world.evolution.rejected`。

## API Surface

实现可以添加一个增量公开 endpoint，例如：

```text
POST /worlds/{world_id}/evolution/evaluate-event
```

如果 route 非必要，helper 和 tests 足以完成本包。若添加 route，必须列入 public handoff manifest，并由 focused API tests 覆盖。

## 兼容性

- 不改变 `Event` 的 required fields。
- 不改变既有 `/world/events`、`/runtime/step`、`/runtime/run`、`/worlds/{world_id}/direction` 或 `/world/generation/worldview` response shape，除非只是必要的 additive manifest exposure。
- 不把 rule sets 安装进 durable runtime state。
- 不把 natural-language direction 转成 direct event outcome。
- 添加 rule-linked evidence 时，保持 `/world/params`、`/world/event-steps` 和 `/world/snapshots` 兼容。

## 脱敏

脱敏 marker vocabulary 至少必须包括：

```text
api_key
authorization
credential
hidden context
private evaluator data
private goal
private memory
private prompt
provider trace
provider_trace
provider_secret
raw prompt
raw provider request
raw provider response
raw request
raw response
self_state
sk-live-
sk-test-
```

检测到任何 marker 时，由 unsafe candidate 派生的公开 ids、lists 和 summaries 必须置空，或替换为通用诊断。

## 停止条件

如果出现以下情况，停止实现并回到 documentation review：

- 合法性判断需要 provider-backed interpretation。
- checker support 或 fixture changes 成为必要条件。
- 需要 Agent continuity、memory、relationship、inventory 或 life/death semantics。
- 实现需要 durable scheduling、background execution 或 persistent rule installation。
- 事件合法性无法通过公开 rule/state evidence 解释。
