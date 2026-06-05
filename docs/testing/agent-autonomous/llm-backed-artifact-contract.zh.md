# LLM-backed Lifecycle Artifact Contract

状态：planned / checker-extension-required

父计划：`docs/testing/llm-backed-lifecycle-validation-plan.zh.md`。

## 目的

本文定义未来 LLM-backed lifecycle autonomous validation 的最小 JSON artifact 字段。
在 schemas 或 checkers 实现前，这些结构是文档合同。

## 共享要求

每个 summary artifact 应包含：

- `schema_version`
- `scenario`
- `status`
- `source`
- `created_at`
- `redaction`
- `evidence_refs`
- `failures`

`status` 必须是以下之一：

- `pass`
- `fail`
- `blocked`
- `not_run`

`redaction` 应包含：

- `api_keys_included`
- `authorization_headers_included`
- `raw_prompts_included`
- `raw_provider_responses_included`
- `provider_traces_included`
- `private_agent_memory_included`
- `private_agent_goals_included`
- `raw_thought_included`
- `hidden_context_included`

PASS 时所有值必须是 `false`。

## `provider-live-summary.json`

最低字段：

- `provider_class`
- `model_label`
- `call_attempted`
- `call_status`
- `latency_ms`
- `token_usage_bucket`
- `public_failure_category`
- `worldengine_owned_call`

禁止字段：

- API key
- authorization header
- raw prompt
- raw request
- raw response
- provider trace

## `world-creation-summary.json`

最低字段：

- `premise_summary`
- `world_id`
- `creation_mode`
- `llm_backed`
- `deterministic_generic_fallback_detected`
- `public_initial_state_ref`
- `public_entities_summary`
- `public_agents_summary`
- `visualization_ref`

PASS 需要 `llm_backed=true` 且 `deterministic_generic_fallback_detected=false`。

## `world-rule-summary.json`

最低字段：

- `parameter_count`
- `parameters`
- `rule_count`
- `evolution_rules`
- `boundary_conditions`
- `event_legality_rules`
- `real_world_rule_categories`

适用时 required real-world categories：

- `time`
- `weather`
- `resources`
- `life_state`
- `space_distance`
- `causality`
- `preconditions`

## `rule-parameter-summary.json`

最低字段：

- `tick_start`
- `tick_end`
- `changed_parameters`
- `rule_links`
- `unexplained_changes`
- `fixed_counter_only_detected`

PASS 需要没有 unexplained material changes，且 `fixed_counter_only_detected=false`。

## `event-legality-summary.json`

最低字段：

- `events_checked`
- `random_events`
- `user_guided_external_directions`
- `illegal_direct_outcomes_rejected`
- `rule_adjudications`
- `direct_final_state_mutation_detected`

PASS 需要没有 direct final-state mutation；使用 user direction 时至少有一个 rule
adjudication。

## `agent-autonomy-summary.json`

最低字段：

- `agent_id`
- `decision_moments`
- `observations`
- `public_memory_summaries`
- `public_thought_summaries`
- `intent_or_no_intent_states`
- `actions`
- `event_reactions`
- `client_scripted_action_detected`
- `single_event_only_detected`

PASS 需要 multi-round continuity、无 client-scripted action，并且没有 raw thought 或
private memory。

## `diff-replay-summary.json`

最低字段：

- `events_ref`
- `snapshots_ref`
- `diffs_ref`
- `replay_supported`
- `state_jump_targets`
- `missing_replay_links`

## `scorecard-summary.json`

最低字段：

- `scorecard`
- `verdict_source`
- `score_items`
- `critical_failures`
- `unverified_items`
- `final_status`

`verdict_source` 必须是 `scorecard_checker`，或 scenario 接受的其他 documented checker
source。
