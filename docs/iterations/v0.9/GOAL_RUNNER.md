# Goal Runner

Chinese mirror: `GOAL_RUNNER.zh.md`.

Status: reviewed / 0.9.9 implementation complete / verification passed

## Goal Entry

Natural-language goals covered by this campaign include:

```text
完成 v0.9
开发 v0.9
编写 v0.9 文档
生成 v0.9 文档
启动 WorldEngine v0.9：LLM-backed World Lifecycle Foundation
```

The current route is recorded in `CURRENT_STATE.md`. Implementation
authorization is closed by default.

## Route Selection

1. Read `CURRENT_STATE.md`.
2. Read `README.md`, `CAMPAIGN_PLAN.md`, and `v0.9-plan.md`.
3. If the route points to a `*-documentation-package-needed` child, create or
   confirm that child's package document set before implementation or evidence
   execution.
4. For any child package, read files in this order:
   - `README.md`
   - `intent.md`
   - `contract.md`
   - `technical-design.md`
   - `test-plan.md`
   - `plan.md`
   - `review.md`
5. Do not implement until the active child package review records
   `implementation_authorized: yes`.

`v0.9-plan.md` is not itself an execution-approved child contract. Its planned
package sections must be converted into concrete package docs before code,
schema, API, checker, fixture, frontend, evidence, or provider work starts.

## Documentation Stage Gate

Documentation-only work may create or update v0.9 iteration documents, parent
package plans, roadmap specs, review evidence, handoff baselines, validation
boundaries, planned package specs, and Chinese mirrors.

Documentation-only work must not modify runtime, schema, API, frontend,
backend tests, checker implementation, fixtures, migrations, generated
results, external repositories, Validation Client code, or
`backend/worldengine/` implementation files unless a reviewed active child
package explicitly authorizes that file class.

## Implementation Authorization Rule

Implementation authorization is closed by default.

For mixed or code children:

1. `contract.md`, `technical-design.md`, `test-plan.md`, and `plan.md` must be
   reviewed.
2. A documentation/contract evaluator must report no P0/P1 and no blocking P2.
3. `review.md` must record `implementation_authorized: yes`.
4. The implementation must stay inside the active child package contract.

If implementation reveals a design gap, stop implementation, update the
relevant documents, and resume only after the updated contract, design, test
plan, or execution plan is reviewed.

## Provider And Redaction Rules

- Live provider calls require active child authorization.
- Provider keys must remain environment-owned by WorldEngine.
- Validation Client must not store, display, forward, or call provider keys.
- Evidence must never contain API keys, authorization headers, raw prompts,
  raw provider requests, raw provider responses, raw provider traces, private
  Agent memory, raw thought, raw chain-of-thought, hidden context, or private
  evaluator data.
- Public summaries may include provider class, model label, success/failure,
  latency, approximate token buckets, and failure categories.

## Runtime Control Rules

v0.9 implementation children that advance the world must use bounded run
controls. Infinite or unbounded default execution is not allowed for evidence
or provider-backed tests.

Required control semantics belong to `0.9.5` unless an earlier package
explicitly owns a smaller precondition:

- run one tick.
- run N ticks.
- run for a world-time duration.
- pause.
- resume.
- continue for N ticks or a duration.
- maximum tick, duration, provider-call, and cost guards.

## User Direction Rules

Natural-language user direction is world-level guidance, not direct mutation.

Allowed direction effects:

- environment trends.
- external pressure.
- event candidate bias.
- probability shifts.
- rule constraints.
- future evaluation hints.

Forbidden direction effects:

- direct Agent private memory mutation.
- direct Agent goal mutation.
- direct final fact assignment.
- direct death, injury, relationship, or inventory outcomes.
- bypassing world rules, probability, causality, location, time, or state.

## Agent Continuity And Consolidation Rules

Agent continuity in v0.9 is brain-inspired but not a claim of consciousness or
complete human neuroscience.

Allowed public evidence:

- perception summaries.
- working or short-term memory summaries.
- long-term memory summary references.
- personality summaries.
- skill summaries.
- intent, no-intent, wait, rest, or sleep states.
- action and event-reaction summaries.
- consolidation records that may span multiple ticks.

Forbidden Agent evidence or behavior:

- raw thought or raw chain-of-thought.
- private memory payloads.
- hidden context.
- private goals.
- automatic per-tick personality mutation.
- automatic per-tick long-term memory mutation.
- automatic per-tick skill drift.
- client-scripted action represented as Agent autonomy.

Memory, personality, and skill updates should settle through explicit
sleep/rest/low-activity consolidation phases where the active child package
owns that behavior. They must not be assumed to update every tick.

## Narrative Projection And Diagnostic Dialogue Rules

WorldEngine may define external narrative projection and out-of-world
player-to-Agent diagnostic conversation as inspection surfaces.

These surfaces are outside canonical world state by default:

- narrative projection must read from events, snapshots, and public Agent
  summaries without mutating canonical world state.
- diagnostic conversation may help a user or validator inspect an Agent, but
  it is not in-world dialogue by default.
- diagnostic conversation must not be inserted into world timeline or Agent
  memory unless a future reviewed bridge explicitly authorizes that behavior.
- evidence must keep projection provenance and redaction status explicit.

## Evidence And Reporting Rules

- Historical v0.8 evidence may be cited only as handoff evidence.
- Do not mark provider live smoke, world creation, evolution, event legality,
  Agent autonomy, checker support, Validation Client evidence export, or full
  LLM-backed lifecycle as passed without current-session checker or scorecard
  evidence.
- Do not use UI smoke as full WorldEngine validation PASS.
- Record exact commands, exit status, pass counts, skipped checks, blockers,
  artifact paths, and rationale in the active package `review.md`.
- Classify FAIL/BLOCKED using the testing taxonomy: `provider`,
  `world_creation`, `world_evolution`, `event_legality`, `agent_autonomy`,
  `agent_consolidation`, `narrative_projection`, `diagnostic_dialogue`,
  `redaction`, `client_evidence`, and `checker_gap`.

## Stop Conditions

Stop and record a blocker if a task would:

- implement code before active package authorization.
- run live provider calls without active package authorization.
- expose secrets, raw prompts, raw responses, or private Agent internals.
- let user direction directly impose final facts.
- model personality, long-term memory, or skill updates as automatic per-tick
  mutation.
- treat external diagnostic conversation as in-world dialogue or Agent memory
  by default.
- let narrative projection mutate canonical world state.
- create concrete demo-world content in the core repository.
- use deterministic generic output as LLM-backed PASS.
- claim LLM-backed PASS without checker, scorecard, or second-Agent review
  where required.
- modify Validation Client code from a WorldEngine package that only defines
  handoff contracts.
