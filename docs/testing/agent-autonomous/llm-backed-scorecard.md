# LLM-backed Lifecycle Scorecard

Status: planned / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Purpose

This scorecard defines the critical items a future checker must evaluate for
`llm-backed-full-lifecycle-autonomous`. It is a documentation contract, not an
implemented checker.

## Score Items

| Item | Critical | PASS condition | FAIL condition | Artifact source |
| --- | --- | --- | --- | --- |
| `provider_live_smoke` | yes | WorldEngine-owned live DeepSeek call succeeds with redacted evidence. | No live call, provider failure, or `/manifest` readiness used as proof. | `provider-live-summary.json` |
| `world_creation_llm_backed` | yes | World is premise-specific, system-digestible, and not deterministic generic output. | Generic fallback, client-generated content, or non-digestible output. | `world-creation-summary.json` |
| `world_rules_generated` | yes | Parameters, meanings, initial values, evolution rules, boundaries, and event legality rules exist. | Rules or parameters missing, only flavor text exists. | `world-rule-summary.json` |
| `parameter_evolution_rule_linked` | yes | Tick changes link to public rules and produce diffs/snapshots. | Fixed counter only, no rule linkage, no state evidence. | `rule-parameter-summary.json`, `diff-replay-summary.json` |
| `event_legality_enforced` | yes | Random and user-guided external events are adjudicated by world rules. | User direction directly forces outcome or impossible event passes without legality status. | `event-legality-summary.json` |
| `agent_persistent_autonomy` | yes | Multi-round public Agent evidence shows observation, memory summary, thought/reflection summary, intent/no-intent, action, and reaction. | Single `params.applied`, no continuity, or client-scripted action. | `agent-autonomy-summary.json` |
| `diff_replay_available` | yes | Events, diffs, and snapshots support replay or state inspection. | Missing snapshots, missing diffs, or no replay reference. | `diff-replay-summary.json`, snapshots |
| `redaction_clean` | yes | Redaction scan finds no blocking leak. | API key, auth header, raw prompt/response, provider trace, private memory/goal/thought, hidden context, or oracle data appears. | `redaction-scan.json` |
| `client_evidence_complete` | yes | Operation log, API summary, screenshots, transcript, and evidence bundle exist. | Required artifact missing or malformed. | result directory |
| `second_agent_review_clean` | yes | Second-Agent read-only review finds no blocking P1/P2. | Any blocking P1/P2 or unsupported PASS claim. | `second-agent-review.md` |

## Verdict Rule

`llm-backed-full-lifecycle-autonomous` can PASS only when every critical item is
`pass`. Any critical `fail`, `blocked`, or `not_run` prevents PASS.

## Allowed Item Statuses

- `pass`
- `fail`
- `blocked`
- `not_run`
- `out_of_scope`

For the full lifecycle scenario, critical items should not be `out_of_scope`.
If a critical item is future scope, the full lifecycle scenario is not ready to
run as PASS-capable.
