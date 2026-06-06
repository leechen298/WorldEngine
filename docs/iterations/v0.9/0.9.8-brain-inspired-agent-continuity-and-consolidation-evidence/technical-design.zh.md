# Technical Design

英文原文：`technical-design.md`。

## Active Backend Placement

Implementation 必须保持在 `backend/app/` 内。优先形态是：

```text
backend/app/schemas/agent_continuity.py
backend/app/core/agent_continuity.py
backend/app/api/routes/world_agent.py or backend/app/api/routes/world.py
backend/app/tests/test_agent_continuity_consolidation_evidence.py
```

如果 local patterns 更适合，也可以选择 narrow adjacent module name。不得在 `backend/worldengine/` 下添加 runtime features。

## Data Flow

1. Caller 或 Agent loop 观察 public runtime/event/memory context。
2. Deterministic helper 接收 public Agent id、runtime tick/world time、public event refs、public memory summary refs 和 candidate public state。
3. Helper 扫描 private markers，并拒绝 raw/private evidence。
4. Helper 为 observe/intent/action/no-intent/wait/rest/sleep/consolidating/reacting states 生成 `AgentContinuityArtifact`。
5. Consolidation helper 记录 phase windows 和 public source/emitted summary refs，不把 personality、memory 或 skill mutation 设计成每 tick 强制发生。
6. 如果通过 apply-capable route 暴露，accepted artifacts 追加 public event evidence。Rejected scripted-autonomy evidence 返回 diagnostics，且不写 canonical accepted autonomy event。

## Schema Notes

`AgentContinuityArtifact`

- `schema_version`
- `world_id`
- `agent_id`
- `tick_id`
- `world_time_seconds`
- `state`
- `perception_summary_refs`
- `working_memory_summary`
- `long_term_memory_summary_refs`
- `personality_summary_refs`
- `skill_summary_refs`
- `intent_summary`
- `event_reaction_refs`
- `consolidation_phase_refs`
- `evidence_refs`
- `redaction_status`

`AgentConsolidationArtifact`

- `phase_id`
- `world_id`
- `agent_id`
- `status`
- `start_tick`
- `end_tick`
- `start_world_time_seconds`
- `end_world_time_seconds`
- `source_short_term_summary_refs`
- `emitted_long_term_summary_refs`
- `personality_summary_status`
- `skill_summary_status`
- `public_explanation`
- `redaction_status`

`AgentContinuityDiagnostic`

- `code`
- `message`
- `path`
- `severity`

## Deterministic Algorithm

Helper 应该：

1. 扫描 ids、refs、summaries、evidence、diagnostics 和 optional route payloads 中的 private markers。
2. 要求 public world id、Agent id、tick、world time 和 allowed public state。
3. 要求 event reaction artifacts 引用 public event ids。
4. 拒绝 direct client-scripted autonomy claims，除非它们被明确表示为 rejected diagnostics。
5. 要求 accepted action state evidence 引用 public Agent action 和 action-result events，并带有 WorldEngine-owned provenance。
6. 拒绝 automatic per-tick personality、long-term memory 或 skill mutation flags。
7. 只有 consolidation artifacts 记录 bounded phase window 或 active phase tick evidence 时才接受。
8. 只返回 public summaries 和 public refs。

## Event Integration

Accepted artifacts 可以追加通用事件，例如：

```text
agent.continuity.recorded
agent.action.continuity.recorded
agent.consolidation.recorded
agent.autonomy.rejected
```

Accepted payloads 必须包含 public artifact ids、Agent id、world id、state、summary refs、redaction status 和 evidence refs。不得包含 raw thought、private memory payloads、raw prompts、provider traces 或 hidden context。

## API Surface

Implementation 可以添加 additive public endpoint，例如：

```text
POST /worlds/{world_id}/agents/{agent_id}/continuity/evaluate
```

如果不需要 route，helper 和 tests 对本包就足够。如果添加 route，必须写入 public handoff manifest，并用 focused API tests 覆盖。

## Compatibility

- 不改变 existing Agent loop required request 或 response fields。
- 不改变 existing memory store semantics，除非是 additive public summary/reference behavior。
- 不改变 existing event 或 runtime response shapes。
- 不改变 `0.9.7` rule-linked event legality behavior。
- 添加任何新 surface 时保持 public manifest compatibility。

## Redaction

Redaction marker vocabulary 至少必须包含：

```text
api_key
authorization
chain-of-thought
credential
hidden context
private evaluator data
private goal
private memory
private prompt
provider trace
provider_secret
raw prompt
raw provider request
raw provider response
raw request
raw response
raw thought
self_state
sk-live-
sk-test-
```

## Stop Conditions

如果出现以下情况，停止 implementation 并回到 documentation review：

- continuity evidence 需要 raw reasoning 或 private memory payloads。
- implementation 需要 live provider interpretation。
- checker support 或 fixture changes 变成必要条件。
- narrative projection 或 diagnostic dialogue 变成必要条件。
- durable scheduling 或 background execution 变成必要条件。
- Agent continuity 无法用 public summaries 和 refs 解释。
