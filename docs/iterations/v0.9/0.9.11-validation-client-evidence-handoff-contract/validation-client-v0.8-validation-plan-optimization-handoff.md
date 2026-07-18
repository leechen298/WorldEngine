# Validation Client v0.8 Validation Plan Optimization Handoff

Chinese mirror:
`validation-client-v0.8-validation-plan-optimization-handoff.zh.md`.

Status: handoff prepared / external optimization iteration not started

## Purpose

This document hands WorldEngine v0.9 validation requirements to the separate
`WorldEngine-Validation-Client` repository. It does not authorize or implement
client code in this repository.

The target Validation Client milestone is an optimization iteration:

```text
v0.8-worldengine-v0.9-validation-plan-optimization
```

The iteration goal is to update the Validation Client's complete WorldEngine
test plan and evidence capability so the client can be repeatedly adjusted as
WorldEngine evolves. The resulting client should be a strict external carrier
for WorldEngine v0.9 validation:

- operate WorldEngine only through public surfaces.
- display public lifecycle evidence.
- record human/Agent-visible operations.
- export checker-compatible evidence bundles.
- preserve `pass`, `fail`, `blocked`, and `not_run` without relabeling.
- never own provider keys, provider calls, LLM generation, world evolution,
  Agent autonomy, scorecard authority, or PASS decisions.

## Current Authority State

WorldEngine v0.9 is the authority for engine behavior and validation contracts.

Current WorldEngine facts:

- Basic lifecycle validation has historical checker-level PASS evidence.
- v0.9 LLM-backed lifecycle validation is not PASS.
- `0.9.11-validation-client-evidence-handoff-contract` defines the public
  evidence bundle contract for external clients.
- `0.9.12-llm-backed-full-lifecycle-validation-execution` produced a
  checker-valid `BLOCKED` result, not a live provider PASS.
- The 2026-06-06 saved result was blocked before live LLM-backed lifecycle
  execution because provider environment variables were absent and a broad
  staged runner command was not available.
- Validation Client export PASS and external validation PASS have not been
  claimed.

Therefore Validation Client v0.8 must support both successful and blocked
evidence. A checker-valid `BLOCKED` result is a valid evidence outcome, but it
is not a product PASS.

## Repository Split

WorldEngine repository owns:

- provider configuration and provider calls.
- LLM-backed world creation and structured public generation output.
- world rules, parameter evolution, events, snapshots, diffs, and legality.
- Agent continuity, consolidation, autonomy evidence, and public summaries.
- checker, scorecard, scenario contracts, and PASS authority.
- redaction boundaries for engine-owned evidence.

Validation Client repository owns:

- web/client workflows used by a human or Codex-like Agent.
- WorldEngine connection preflight and public surface discovery.
- operation logs, UI-visible state, API summaries, screenshots, and downloads.
- evidence bundle display and export.
- replay/fork/branch views when backed by public event, diff, snapshot, and
  commit-point evidence.
- second-Agent and human handoff templates.

Validation Client must not:

- manage or display provider keys.
- call DeepSeek or any LLM provider directly.
- generate authoritative world content.
- compute authoritative parameter changes or final world states.
- script Agent actions and label them as WorldEngine autonomy.
- decide PASS independently from WorldEngine checker/scorecard/second-Agent
  review.
- expose raw prompts, raw provider requests or responses, provider traces,
  authorization headers, API keys, private Agent memory, private Agent goals,
  raw thought, hidden context, private evaluator data, seeds, or oracle data.
- convert narrative projections or diagnostic conversations into canonical
  world events or Agent memory.

## Required Reading

Validation Client v0.8 work should start by reading these WorldEngine files:

```text
/Users/leechen/projects/WorldEnginProjects/WorldEngine/AGENTS.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/project-north-star.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/product-model.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/scope-boundaries.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/roadmap.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/README.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/llm-backed-lifecycle-validation-plan.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/README.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-suite-execution.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-artifact-contract.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/llm-backed-scorecard.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/second-agent-review-protocol.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/provider-live-smoke-deepseek.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-world-creation.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/world-rule-parameter-evolution.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/rule-compliant-event-generation.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/agent-persistent-autonomy-evidence.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/agent-autonomous/scenarios/llm-backed-full-lifecycle-autonomous.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/contract.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/technical-design.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/iterations/v0.9/0.9.12-llm-backed-full-lifecycle-validation-execution/review.md
/Users/leechen/projects/WorldEnginProjects/WorldEngine/docs/testing/results/2026-06-06-llm-backed-lifecycle-validation.md
```

Validation Client v0.8 work should also read current client docs and code:

```text
/Users/leechen/projects/WorldEngine-Validation-Client/AGENTS.md
/Users/leechen/projects/WorldEngine-Validation-Client/docs/specs/validation-client-design.md
/Users/leechen/projects/WorldEngine-Validation-Client/docs/specs/validation-client-design.zh.md
/Users/leechen/projects/WorldEngine-Validation-Client/docs/milestones/v0.7-agent-autonomous-validation/
/Users/leechen/projects/WorldEngine-Validation-Client/apps/api/app/worldengine_client.py
/Users/leechen/projects/WorldEngine-Validation-Client/apps/api/app/routes/evidence.py
/Users/leechen/projects/WorldEngine-Validation-Client/apps/api/app/routes/validation_runs.py
/Users/leechen/projects/WorldEngine-Validation-Client/apps/web/src/pages/RuntimeConsole.tsx
/Users/leechen/projects/WorldEngine-Validation-Client/apps/web/e2e/v0.7-ui-smoke.spec.ts
```

The v0.7 milestone contains useful operation-log and evidence foundations, but
some v0.7 documents still point at WorldEngine 0.8.9 gates. Treat those as
historical references. v0.8 must target WorldEngine v0.9.

## Client Capability Target

Validation Client v0.8 should extend v0.7 instead of rebuilding it.

The minimum capability target is:

1. Connect to WorldEngine and record preflight evidence.
2. Discover public surfaces from `/manifest` and `/openapi.json`.
3. Create or inspect a WorldEngine-backed validation session.
4. Run bounded lifecycle operations through public runtime controls.
5. Submit natural-language world direction as external guidance only.
6. Display and export rule-linked evolution and event legality evidence.
7. Display and export Agent continuity/autonomy evidence.
8. Display narrative projection and diagnostic dialogue as out-of-world
   inspection surfaces only.
9. Export v0.9 named evidence artifacts with a manifest.
10. Produce a saved-result directory that can be checked by WorldEngine when
    the active scenario supports checker validation.
11. Preserve `BLOCKED` and `not_run` outcomes when WorldEngine lacks provider,
    runner, schema, or full lifecycle support.

## Public Surface Matrix

Validation Client v0.8 should use these public WorldEngine surfaces when
available. If a surface is unavailable, the client must record `blocked` or
`not_run` evidence instead of faking the operation.

| Capability | WorldEngine public surface | Client role |
| --- | --- | --- |
| Preflight | `GET /health` | Record reachability and latency summary. |
| Public contract discovery | `GET /manifest` | Display provider readiness warning and public surface list. Do not treat readiness as live-call proof. |
| API discovery | `GET /openapi.json` | Discover operation IDs and URLs. |
| Basic world creation | `POST /worlds` | Use for basic lifecycle only; record if response is generic deterministic output. |
| Worldview generation | `POST /world/generation/worldview` | Submit premise and display public generated world/rule readiness evidence. |
| Provider live smoke | `POST /provider/live-smoke` | Call only the WorldEngine endpoint; never call provider directly or handle keys. |
| Runtime state | `GET /runtime/state` | Display tick, world time, step seconds. |
| Single tick | `POST /runtime/step` | Advance one tick and record operation/API evidence. |
| Bounded run | `POST /runtime/run` | Run a user-specified tick count or world-time duration; never default to unbounded run. |
| Pause | `POST /runtime/pause` | Pause future bounded runs. |
| Resume | `POST /runtime/resume` | Resume future bounded runs. |
| Events | `GET /world/events` | Display event timeline and export event evidence. |
| Event steps | `GET /world/event-steps` | Display grouped tick evidence. |
| Snapshots | `GET /archive/snapshots` | Display replay anchor evidence where available. |
| World params | `GET /world/params` | Display public parameter state. |
| Natural-language direction | `POST /worlds/{world_id}/direction` | Queue external environmental direction with timing/window evidence. |
| Legacy guidance | `POST /worlds/{world_id}/director-guidance` | Keep compatibility for basic lifecycle; prefer direction contract for v0.9. |
| Event legality | `POST /worlds/{world_id}/evolution/evaluate-event` | Submit candidate/rule set only as public evaluation input; record accepted/rejected result. |
| Agent continuity | `POST /worlds/{world_id}/agents/{agent_id}/continuity/evaluate` | Display public continuity/consolidation/action evidence; do not create private state. |
| Narrative projection | `POST /worlds/{world_id}/narrative/project` | Display as external story/projection output only. |
| Diagnostic dialogue | `POST /worlds/{world_id}/agents/{agent_id}/diagnostics/dialogue/evaluate` | Display as out-of-world inspection only; do not write into world memory. |

## Runtime Control Requirements

The client UI should expose bounded controls:

- step once.
- run `N` ticks.
- run `N` world-time seconds when supported.
- pause.
- resume.
- run another bounded segment after pause/resume.

The UI must not present the world as an unbounded infinite loop without an
explicit user-controlled run budget. Operation logs should record the exact
requested budget, result summary, tick range, and whether the run was paused or
blocked.

## Scenario Matrix

| Scenario | Required client operations | Required client artifacts | Allowed result |
| --- | --- | --- | --- |
| `worldengine-full-lifecycle-autonomous` | Create world, step/run ticks, read events/snapshots, observe Agent action evidence, submit direction/guidance, export bundle, run checker. | `result.json`, `operation-log.jsonl`, `api-summary.json`, `world-lifecycle-summary.json`, screenshots/transcript, `redaction-scan.json`, `scorecard-summary.json`. | PASS only from WorldEngine checker/scorecard. |
| `provider-live-smoke-deepseek` | Discover `/provider/live-smoke`, call WorldEngine endpoint, record redacted status. | `provider-live-summary.json`, `operation-log.jsonl`, `redaction-scan.json`. | PASS/BLOCKED/FAIL from WorldEngine public response and checker rules. |
| `llm-backed-world-creation` | Submit premise, call WorldEngine-owned world generation/creation path, record generic fallback detection. | `world-creation-summary.json`, public state refs, visualization refs. | PASS only if LLM-backed and not deterministic generic fallback. |
| `world-rule-parameter-evolution` | Run bounded ticks, collect params/events/diffs, map changed parameters to rules. | `world-rule-summary.json`, `rule-parameter-summary.json`, `diff-replay-summary.json`. | PASS only if rule-linked changes are evidenced. |
| `rule-compliant-event-generation` | Submit legal/illegal candidate or direction-linked event, record adjudication and state diff. | `event-legality-summary.json`, event refs, diff refs. | PASS only if no direct final-state mutation and legality evidence exists. |
| `agent-persistent-autonomy-evidence` | Observe multi-round public Agent continuity evidence, including intent/no-intent states and event reactions. | `agent-autonomy-summary.json`, public memory/thought summaries, event refs. | PASS only if evidence is WorldEngine-originated and not client-scripted. |
| `llm-backed-full-lifecycle-autonomous` | Execute the full sequence: provider smoke, world creation, rule evolution, event legality, Agent autonomy, evidence export, checker/scorecard, second-Agent review. | Complete v0.9 evidence bundle. | PASS only from checker/scorecard plus clean second-Agent review. |

Direct API harvesting used to build artifacts must be logged separately as API
evidence. It must not be disguised as a user-visible Agent operation in
`operation-log.jsonl`.

## Evidence Bundle Contract

The exported bundle should support this shape:

```text
evidence-bundle/
  manifest.json
  result.json
  operation-log.jsonl
  api-log.jsonl
  api-summary.json
  provider-live-summary.json
  world-creation-summary.json
  world-rule-summary.json
  rule-parameter-summary.json
  event-legality-summary.json
  agent-autonomy-summary.json
  diff-replay-summary.json
  world-lifecycle-summary.json
  narrative-projection-summary.json
  diagnostic-conversation-summary.json
  redaction-scan.json
  scorecard-summary.json
  second-agent-review.md
  transcript.md
  console.log
  screenshots/
```

Only scenario-required artifacts need to exist, but missing required artifacts
must remain visible as `blocked`, `not_run`, or `fail`.

`manifest.json` must include:

- `schema_version`
- `bundle_id`
- `scenario`
- `result_status`
- `client_role`
- `provider_owner`
- `evaluator_role`
- `created_at`
- `artifact_index`
- `redaction_status`
- `checker_contract`
- `unsupported_items`

Expected fixed values:

```json
{
  "client_role": "display_export_only",
  "provider_owner": "worldengine",
  "evaluator_role": "worldengine_checker_or_second_agent_review"
}
```

Each `artifact_index` entry should include:

- `name`
- `path`
- `required`
- `displayable`
- `exportable`
- `producer`
- `schema_version`
- `redaction_status`

Artifact paths must be relative and must stay inside the bundle directory.

## Artifact Mapping

| Artifact | Primary producer | Client responsibility |
| --- | --- | --- |
| `result.json` | Validation Client packaging / WorldEngine checker contract | Preserve scenario, final status, result dir metadata, and unsupported items. |
| `operation-log.jsonl` | Validation Client | Record visible user/Agent operations: clicks, inputs, navigation, export, checker command reference. |
| `api-log.jsonl` | Validation Client | Record direct public API calls and artifact harvest operations separately from visible operations. |
| `api-summary.json` | Validation Client | Summarize endpoints, status codes, latency buckets, and redaction status. |
| `provider-live-summary.json` | WorldEngine public endpoint / client packaging | Preserve provider class, model label, call attempted/status, latency, token bucket, failure category. |
| `world-creation-summary.json` | WorldEngine public evidence / client packaging | Record premise summary, world id, creation mode, LLM-backed status, generic fallback detection. |
| `world-rule-summary.json` | WorldEngine public evidence / client packaging | Record public parameters, rule count, boundary conditions, legality rules, real-world rule categories. |
| `rule-parameter-summary.json` | WorldEngine public evidence / client packaging | Record tick range, changed parameters, rule links, unexplained changes, fixed-counter detection. |
| `event-legality-summary.json` | WorldEngine public evidence / client packaging | Record checked events, random/user-guided directions, adjudications, direct mutation detection. |
| `agent-autonomy-summary.json` | WorldEngine public evidence / client packaging | Record multi-round public autonomy evidence and whether client scripting was detected. |
| `diff-replay-summary.json` | Validation Client over WorldEngine public evidence | Record event/snapshot/diff refs, replay support, jump targets, missing links. |
| `world-lifecycle-summary.json` | Validation Client packaging | Summarize creation, runtime, events, snapshots, direction, Agent evidence, export status. |
| `narrative-projection-summary.json` | WorldEngine public projection / client packaging | Record projection status as non-canonical external inspection. |
| `diagnostic-conversation-summary.json` | WorldEngine public projection / client packaging | Record diagnostic dialogue status as out-of-world inspection. |
| `redaction-scan.json` | Validation Client and/or checker | Record clean/leak status for all artifacts. |
| `scorecard-summary.json` | WorldEngine checker/scorecard or client packaging of checker output | Preserve checker verdict source and score items. |
| `second-agent-review.md` | Second Agent | Store read-only review output or `not_run`/`blocked` status. |

## Redaction Requirements

Every displayable or exportable artifact must declare redaction status. PASS
requires all blocking flags to be false:

- `api_keys_included`
- `authorization_headers_included`
- `raw_prompts_included`
- `raw_provider_requests_included`
- `raw_provider_responses_included`
- `provider_traces_included`
- `private_agent_memory_included`
- `private_agent_goals_included`
- `raw_thought_included`
- `hidden_context_included`
- `private_evaluator_data_included`
- `seed_or_oracle_data_included`

If a forbidden marker appears only as a redaction field name, the scanner
should classify it as metadata, not a leak. If a forbidden value appears in
content, the bundle must be `fail`.

## Status Preservation

Validation Client UI may translate labels for readability, but exported data
must preserve machine status values:

- `pass`
- `fail`
- `blocked`
- `not_run`
- `out_of_scope` when a scenario contract explicitly allows it.

Do not map `blocked`, `not_run`, or `unsupported` into PASS. Do not treat a
green UI smoke as a WorldEngine validation PASS.

## v0.8 Milestone Documents To Create In Validation Client

The Validation Client repository should create a new milestone directory:

```text
docs/milestones/v0.8-worldengine-v0.9-validation-plan-optimization/
```

Recommended files:

```text
README.md
README.zh.md
intent.md
intent.zh.md
contract.md
contract.zh.md
technical-design.md
technical-design.zh.md
test-plan.md
test-plan.zh.md
plan.md
plan.zh.md
review.md
review.zh.md
scenario-operation-matrix.md
scenario-operation-matrix.zh.md
artifact-contract.md
artifact-contract.zh.md
redaction-matrix.md
redaction-matrix.zh.md
autonomous-validation-runbook.md
autonomous-validation-runbook.zh.md
second-agent-review-template.md
second-agent-review-template.zh.md
```

The milestone should explicitly supersede stale v0.7 references to WorldEngine
0.8.9 while preserving v0.7 as historical foundation.

This milestone should be framed as a repeatable validation-plan optimization
iteration, not as a one-off compatibility patch. Later Validation Client
versions may repeat the same pattern whenever WorldEngine changes its public
validation surfaces, scenario contracts, artifact contracts, or checker rules.

## Suggested Implementation Packages Inside Validation Client

Validation Client may implement v0.8 as smaller internal tasks after its
milestone docs are reviewed:

1. Documentation and routing refresh.
2. WorldEngine v0.9 public surface discovery and capability model.
3. Evidence manifest and artifact-index schema.
4. Named artifact builders for provider/world/rule/event/Agent/replay summary.
5. Redaction scan and status preservation.
6. Runtime UI controls for bounded run, pause, resume, and additional run.
7. Scenario runner/export flow for current planned validation.
8. Checker-compatible saved-result export.
9. Frontend display for scorecard, blocked/not-run items, and second-Agent
   review.
10. API/web/E2E tests plus WorldEngine checker handoff validation.

## Validation Requirements For v0.8

The Validation Client v0.8 implementation should run focused and broad checks
appropriate to that repository. At minimum:

```bash
cd /Users/leechen/projects/WorldEngine-Validation-Client
cd apps/api && uv run pytest -q
pnpm --dir apps/web test
pnpm --dir apps/web build
pnpm run test
pnpm run build
git diff --check
```

If Playwright or equivalent E2E is present, run it for the v0.8 flow.

For checker handoff, export a result directory and validate it from the
WorldEngine repository when the scenario supports checker validation:

```bash
cd /Users/leechen/projects/WorldEnginProjects/WorldEngine
make validate-agent-autonomous-result RESULT_DIR=<result-dir>
```

If the result is `BLOCKED`, the checker should still accept the saved result
only when the artifacts honestly explain why it is blocked.

## Expected First Validation Outcome

The first v0.8 validation may still be `BLOCKED`.

That is acceptable when:

- WorldEngine provider environment is not configured.
- live provider smoke cannot be attempted through WorldEngine.
- WorldEngine lacks required LLM-backed evidence for a scenario.
- checker/schema support is missing.
- a required artifact is not yet generated.
- second-Agent review has not run.

The client must make the blocker visible and exportable. It must not hide the
blocker behind UI success.

## Follow-up Routing

Use this routing after v0.8 development or validation:

| Gap | Route |
| --- | --- |
| Missing provider live endpoint, provider abstraction, LLM-backed generation, world rules, event legality, Agent continuity/autonomy evidence | WorldEngine implementation iteration. |
| Missing checker/schema/fixtures/result validation for scenario artifacts | WorldEngine `docs/testing` + `tools/testing` package. |
| Missing UI display, operation log, API summary, evidence bundle fields, saved-result export, replay/diff/snapshot display | Validation Client milestone. |
| DeepSeek/provider call fails while WorldEngine API and evidence are complete | Provider/environment validation failure, not client code by default. |
| Raw prompt/response/key/private memory/raw thought leaks | Immediate redaction failure; fix boundary before continuing. |

## Success Definition

This handoff is complete when Validation Client has enough information to
start its own v0.8 milestone without guessing WorldEngine v0.9 responsibilities.

Validation Client v0.8 is complete only when its own repository records
reviewed milestone docs, implementation evidence, tests, and a checker-handoff
result that honestly reports `PASS`, `PARTIAL`, `BLOCKED`, or `FAIL`.
