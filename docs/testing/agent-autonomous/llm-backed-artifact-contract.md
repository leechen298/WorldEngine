# LLM-backed Lifecycle Artifact Contract

Status: planned / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Purpose

This contract defines minimum JSON artifact fields for future
LLM-backed lifecycle autonomous validation. These structures are documentation
contracts until implemented by schemas or checkers.

## Shared Requirements

Every summary artifact should include:

- `schema_version`
- `scenario`
- `status`
- `source`
- `created_at`
- `redaction`
- `evidence_refs`
- `failures`

`status` must be one of:

- `pass`
- `fail`
- `blocked`
- `not_run`

`redaction` should include:

- `api_keys_included`
- `authorization_headers_included`
- `raw_prompts_included`
- `raw_provider_responses_included`
- `provider_traces_included`
- `private_agent_memory_included`
- `private_agent_goals_included`
- `raw_thought_included`
- `hidden_context_included`

All values must be `false` for PASS.

## `provider-live-summary.json`

Minimum fields:

- `provider_class`
- `model_label`
- `call_attempted`
- `call_status`
- `latency_ms`
- `token_usage_bucket`
- `public_failure_category`
- `worldengine_owned_call`

Forbidden fields:

- API key
- authorization header
- raw prompt
- raw request
- raw response
- provider trace

## `world-creation-summary.json`

Minimum fields:

- `premise_summary`
- `world_id`
- `creation_mode`
- `llm_backed`
- `deterministic_generic_fallback_detected`
- `public_initial_state_ref`
- `public_entities_summary`
- `public_agents_summary`
- `visualization_ref`

PASS requires `llm_backed=true` and
`deterministic_generic_fallback_detected=false`.

## `world-rule-summary.json`

Minimum fields:

- `parameter_count`
- `parameters`
- `rule_count`
- `evolution_rules`
- `boundary_conditions`
- `event_legality_rules`
- `real_world_rule_categories`

Required real-world categories when applicable:

- `time`
- `weather`
- `resources`
- `life_state`
- `space_distance`
- `causality`
- `preconditions`

## `rule-parameter-summary.json`

Minimum fields:

- `tick_start`
- `tick_end`
- `changed_parameters`
- `rule_links`
- `unexplained_changes`
- `fixed_counter_only_detected`

PASS requires no unexplained material changes and
`fixed_counter_only_detected=false`.

## `event-legality-summary.json`

Minimum fields:

- `events_checked`
- `random_events`
- `user_guided_external_directions`
- `illegal_direct_outcomes_rejected`
- `rule_adjudications`
- `direct_final_state_mutation_detected`

PASS requires no direct final-state mutation and at least one rule
adjudication when user direction is used.

## `agent-autonomy-summary.json`

Minimum fields:

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

PASS requires multi-round continuity, no client-scripted action, and no raw
thought or private memory.

## `diff-replay-summary.json`

Minimum fields:

- `events_ref`
- `snapshots_ref`
- `diffs_ref`
- `replay_supported`
- `state_jump_targets`
- `missing_replay_links`

## `scorecard-summary.json`

Minimum fields:

- `scorecard`
- `verdict_source`
- `score_items`
- `critical_failures`
- `unverified_items`
- `final_status`

`verdict_source` must be `scorecard_checker` or another documented checker
source accepted by the scenario.
