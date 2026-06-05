# LLM-backed Lifecycle Validation Specification and Runbook

Status: planned validation specification and runbook, documentation-only

Chinese mirror: `llm-backed-lifecycle-validation-plan.zh.md`.

## Scope

This document defines the next validation plan for proving whether
WorldEngine can run an LLM-backed lifecycle. It is a testing plan, not a new
WorldEngine product iteration, not a Validation Client milestone, and not a
code implementation request.

This documentation pass does not authorize:

- live DeepSeek or other provider calls.
- runtime, API, schema, checker, fixture, frontend, or Validation Client code
  changes.
- new saved result artifacts.
- a PASS claim for LLM-backed world creation, LLM-backed world evolution, or
  persistent Agent autonomy.

Current baseline:

- `0.8.9` has passed the basic full lifecycle autonomous validation rerun.
- DeepSeek or any other real LLM provider has not been validated through a
  live WorldEngine call.
- Current basic evidence proves that an external client can create a world,
  advance ticks, observe events and snapshots, capture one WorldEngine-backed
  Agent action, submit director guidance, export evidence, and pass the
  saved-result checker.
- Current basic evidence does not prove LLM-backed world creation, rule-driven
  world evolution, event legality under generated rules, or sustained Agent
  memory, thought, behavior, and intent.

## Purpose

The goal is to prepare an executable validation plan that a later chat can run
or implement. The plan should answer one question:

Can WorldEngine create a world from a basic user premise, call an LLM through
WorldEngine-owned provider configuration, generate public world parameters and
rules, evolve those parameters over time, generate or select rule-compliant
events, and provide public evidence that Agents act from continuing state
instead of client scripts?

The first execution of this plan is expected to find implementation gaps. That
is acceptable and is part of the plan. A gap discovered by this plan should be
routed to the appropriate follow-up area instead of being treated as a failed
testing process.

## Authority Boundary

WorldEngine owns all LLM behavior:

- provider selection.
- provider API key handling.
- provider calls.
- prompts and prompt construction.
- raw provider responses.
- generation, evolution, legality, memory, and Agent decision behavior.
- authoritative checker or scorecard contracts that judge WorldEngine
  lifecycle evidence.

The Validation Client remains an external observer and operation surface:

- it may let the user input a basic worldview or later external direction.
- it may display public WorldEngine state, events, snapshots, and Agent
  evidence.
- it may record operation logs and export evidence bundles.
- it must not store, display, forward, or manage provider API keys.
- it must not call the LLM provider directly.
- it must not generate authoritative world content.
- it must not act as the authoritative evaluator.

## Current Validation Contract

The following statements define the expected current status before this plan
is implemented or executed.

- Current `GET /manifest` proves provider environment readiness only. It can
  report public provider class, readiness, credential source class, and model
  label, but it does not prove a live provider call happened.
- Current `POST /worlds` returns a public world creation response, but the
  current response is a generic deterministic response. It does not prove
  LLM-backed world creation.
- Current tick, event, snapshot, and Agent action evidence proves basic
  lifecycle flow, but it does not prove generated world rules, rule-driven
  parameter evolution, legal event generation, or persistent Agent autonomy.
- Therefore the first LLM-backed lifecycle validation run may legitimately
  return FAIL because of missing implementation.
- A missing implementation gap is useful evidence. It should be classified and
  routed rather than hidden behind deterministic fallback behavior.

PASS may only come from one or more of these sources:

- documented checker output of PASS.
- scorecard summary where every critical item is `pass`.
- a second Agent read-only review that finds no blocking P1 or P2 issue in
  the evidence and checker result.

The following may not be used as PASS sources:

- Validation Client UI smoke passing by itself.
- `/manifest` showing that a provider is configured.
- an API key existing in the environment.
- a deterministic mock or generic world being able to run.
- a human or Agent subjective impression that the result "looks like LLM".
- user direction being written directly into world state as final fact.

## Redaction Contract

Evidence may record only public, redacted, reviewable summaries. It must not
record:

- API keys.
- authorization headers.
- raw prompts.
- raw provider requests.
- raw provider responses.
- raw provider traces.
- private Agent memory.
- private Agent goals.
- raw thought.
- raw chain-of-thought.
- hidden context.
- private evaluator data.
- private validation oracle logic.

Allowed provider evidence is limited to public or redacted fields such as:

- `provider_class`.
- `model_label`.
- `success` or `failure`.
- latency bucket or latency in milliseconds.
- approximate token usage or coarse token buckets.
- public failure category.

Allowed Agent evidence is limited to public summaries such as:

- observed behavior.
- public action.
- public intent summary.
- public memory summary.
- public thought or reflection summary.
- public event reaction.

These summaries must not expose hidden internal state, private memory payloads,
or raw reasoning text.

## Five Validation Layers

| Layer | Name | Primary question | Required result |
| --- | --- | --- | --- |
| 1 | Provider live smoke | Can WorldEngine make a minimal live DeepSeek provider call without leaking secrets? | Redacted live call evidence exists and passes redaction. |
| 2 | LLM-backed world creation | Can a user premise produce a public, system-digestible world state and rule set through WorldEngine-owned LLM behavior? | The result is materially premise-specific and not the deterministic generic response. |
| 3 | LLM-assisted world evolution | Can ticks evolve world parameters and events through rules rather than fixed counters? | Events, snapshots, diffs, and replay evidence correspond to rule-driven changes. |
| 4 | Agent autonomy evidence | Can Agents show multi-round public behavior from continuing state, memory summaries, thought summaries, and optional intent? | Actions are evidenced by WorldEngine public evidence, not client scripts. |
| 5 | Evidence review | Can a first Agent operate the flow, export evidence, and a second Agent or checker validate it? | Checker or scorecard gives PASS, and second-Agent review finds no blocking issue. |

## Layer 1: Provider Live Smoke

### Goal

Validate that DeepSeek provider environment variables are configured and
WorldEngine can perform a minimal live provider call.

### Required operations

- Start WorldEngine with provider configuration owned by environment
  variables.
- Read public provider readiness through WorldEngine public surfaces.
- Trigger the smallest possible live provider call through a WorldEngine-owned
  endpoint, command, or test hook that is explicitly designed for provider
  smoke validation.
- Record a redacted provider live summary.

### Required evidence

- provider class, for example `deepseek_api`.
- public or redacted model label.
- call status: `success`, `failure`, `blocked`, or `not_configured`.
- latency.
- approximate token count or token bucket.
- public failure category when the call fails.
- redaction flags proving no key, raw prompt, raw response, or authorization
  header is present.

### Forbidden evidence

- API key value.
- request authorization header.
- raw prompt.
- raw response.
- provider account id.
- provider raw trace.
- full request or response body.

### PASS condition

PASS requires a checker or scorecard to confirm that a live provider call was
attempted through WorldEngine, the call succeeded, and all redaction checks
passed.

### Expected current gap

Current `GET /manifest` proves environment readiness only. It does not prove
that a live provider call can be made. If no smoke endpoint or equivalent
WorldEngine-owned call path exists, classify the result as `provider` or
`checker_gap` depending on whether the missing piece is runtime capability or
testing infrastructure.

## Layer 2: LLM-backed World Creation

### Goal

Validate that a user can enter a basic worldview and WorldEngine can generate a
public world state that the runtime can consume.

The generated state must include the foundation needed for runtime evolution,
not only labels or flavor text.

### Required generated content

WorldEngine should generate:

- public world identity and premise summary.
- locations, entities, Agents, items, and relevant environment state.
- world runtime parameters.
- parameter meanings.
- initial parameter values.
- parameter evolution rules.
- boundary conditions.
- event legality rules.
- rule references or public rationale summaries.
- initial snapshot and visualization payload.

World runtime rules should be grounded in real-world common sense whenever the
premise allows it. Required rule categories include:

- time and time progression.
- weather and environmental conditions.
- resources and scarcity.
- population or social pressure where applicable.
- life state and health constraints.
- spatial distance and reachability.
- causality and delayed effects.
- action or event preconditions.

### Required operations

- Enter a basic world premise through the Validation Client or another public
  external surface.
- Let WorldEngine generate the public world state and rule package.
- Export the generated state and summaries as public evidence.
- Compare the response against the current deterministic generic response.

### PASS condition

PASS requires evidence that the generated world is premise-specific,
system-digestible, redacted, and not the deterministic generic response.

Possible proof includes:

- live provider smoke already passed in the same run or an accepted prerequisite
  run.
- world creation evidence records a redacted provider-backed generation status.
- two materially different premises produce materially different world
  parameters, rules, entities, or initial conditions.
- the generated output includes rule and parameter structures that can be
  consumed by later tick evolution.

### Forbidden behavior

- Validation Client generates the world content.
- deterministic fallback is reported as LLM-backed generation.
- generated text exists but cannot be consumed by WorldEngine runtime.
- raw prompt or raw response is exported as evidence.
- concrete validation world seed data is stored in the WorldEngine repository.

## Layer 3: LLM-assisted World Evolution

### Goal

Validate that world evolution is not only a fixed tick counter. World
parameters must be automatically calculated and evolved by WorldEngine
according to rules.

### Required evolution behavior

During tick progression, WorldEngine should show:

- parameter changes derived from rules.
- external events generated or selected by WorldEngine and optionally assisted
  by the LLM.
- environmental changes.
- state changes that respect preconditions and boundaries.
- snapshots and diffs that can support replay.
- event records that explain public rule references or public legality
  summaries.

### User direction boundary

User direction may influence only external events and world environment. It
must not directly mutate Agent private state or write final illegal outcomes
into the world.

Examples:

- Forbidden: "Agent A dies immediately."
- Allowed as external direction: "Agent A may face lightning risk."

For the allowed direction, WorldEngine must decide whether anything happens
based on public world rules such as:

- weather.
- location.
- shelter.
- probability.
- life state.
- spatial reachability.
- causal timing.
- event severity.

### Required operations

- Advance the world across enough ticks to observe multiple state changes.
- Capture events, snapshots, and diffs.
- Submit at least one natural-language direction that creates an environmental
  risk rather than a direct result.
- Verify that the outcome is decided by WorldEngine rules.
- Verify that replay or diff evidence can explain the state transition.

### PASS condition

PASS requires events, snapshots, diffs, and replay evidence to correspond to
rule-driven changes. Fixed counters, static mock events, or direct insertion
of user-desired outcomes are not enough.

### Expected current gap

Current basic lifecycle evidence has tick progression and events, but it does
not yet prove that world rules drive parameter evolution or that event legality
is enforced.

## Layer 4: Agent Autonomy Evidence

### Goal

Validate that Agents show continuing behavior from WorldEngine public evidence.
An Agent must not be represented as autonomous only because one
`params.applied` event exists.

### Required autonomy evidence

At least one Agent should show multi-round evidence including:

- observation.
- memory summary continuity.
- public thought or reflection summary.
- formation of a tendency, concern, desire, or goal candidate.
- intent generation or explicit absence of intent.
- action selection.
- action execution.
- reaction to world events.
- change in public state or memory summary after the event.

Intent does not need to exist on every tick. "Observe", "wait", and "no clear
intent" are valid public states when they are consistent with the Agent's
state and context.

### Required operations

- Run enough ticks or interaction rounds to observe at least two Agent decision
  moments.
- Capture public Agent evidence before and after an event.
- Verify that at least one action follows from WorldEngine public evidence.
- Verify that the Validation Client did not script the Agent action.

### PASS condition

PASS requires checker or scorecard evidence that Agent action came from
WorldEngine public evidence and that public summaries show continuity across
multiple rounds.

### Forbidden behavior

- Client scripts write Agent actions and present them as WorldEngine autonomy.
- direct private memory or private goal mutation.
- raw thought, raw chain-of-thought, private memory, or hidden context appears
  in evidence.
- one isolated `params.applied` event is treated as sufficient autonomy.

## Layer 5: Evidence Review

### Goal

Validate the complete lifecycle evidence through a two-Agent workflow and a
deterministic or scorecard checker.

### Required review flow

- First Agent operates the Validation Client from a human observer or director
  perspective.
- First Agent exports a complete evidence bundle.
- WorldEngine checker or scorecard validates the result directory.
- Second Agent performs read-only review of the saved evidence.
- Final PASS or FAIL is based on checker or scorecard output plus second-Agent
  review, not self-reporting by the first Agent.

### Required classification for FAIL

Every FAIL must be classified into at least one of these categories:

- `provider`.
- `world_creation`.
- `world_evolution`.
- `event_legality`.
- `agent_autonomy`.
- `redaction`.
- `client_evidence`.
- `checker_gap`.

## Capability Matrix

| Capability | Current known status | Required LLM-backed evidence | Likely follow-up if missing |
| --- | --- | --- | --- |
| Provider env readiness | `/manifest` can report public readiness from env | Redacted live call summary | WorldEngine implementation iteration if call path is missing; provider/environment FAIL if configured path fails |
| LLM-backed creation | Current `POST /worlds` is generic deterministic | Premise-specific public world state and rule pack | WorldEngine implementation iteration |
| Runtime parameters and rules | Basic lifecycle does not prove rule schema | Parameters, meanings, initial values, evolution rules, boundaries | WorldEngine implementation iteration |
| Rule-driven evolution | Basic ticks and events exist | Diffs and snapshots tied to rules | WorldEngine implementation iteration |
| Event legality | External direction is accepted as guidance | Illegal direct result rejected; external risk resolved by rules | WorldEngine implementation iteration |
| Agent continuity | One WorldEngine-backed Agent action observed | Multi-round memory, thought, intent, action, reaction summaries | WorldEngine implementation iteration |
| Client evidence | Validation Client can export basic evidence | LLM-backed lifecycle evidence fields and operation logs | Validation Client milestone if display/export/log fields are missing |
| Checker support | Basic saved-result checker exists | Scenario and schema support for LLM-backed evidence | `docs/testing` and `tools/testing` testing asset enhancement |

## Scenario Contracts

The following scenario names are authoritative for future checker or saved
result implementation. If a checker or result schema is later added, these
names should be reused.

### `provider-live-smoke-deepseek`

Goal:

- Prove WorldEngine can perform a minimal live DeepSeek provider call through
  WorldEngine-owned configuration and return only redacted public evidence.

Required operations:

- Start WorldEngine with DeepSeek environment variables configured.
- Read public provider readiness.
- Trigger the smallest WorldEngine-owned live provider smoke call.
- Capture redacted provider live summary.
- Run checker or scorecard validation over the saved evidence.

Forbidden operations:

- Validation Client calls DeepSeek directly.
- Agent reads or records API key values.
- operation log stores raw provider request, raw provider response, raw prompt,
  authorization header, or provider trace.
- `/manifest` readiness alone is treated as live-call proof.

Required artifacts:

- `result.json`.
- `operation-log.jsonl`.
- `api-summary.json`.
- `provider-live-summary.json`.
- `scorecard-summary.json` or checker output.
- redaction scan artifact.

PASS source:

- documented checker or scorecard PASS confirming live call success and
  redaction pass.

FAIL taxonomy:

- `provider` if configuration, network, quota, provider response, or live call
  fails.
- `redaction` if secret or raw provider content appears.
- `checker_gap` if no supported checker or schema can validate the evidence.
- `client_evidence` if required operation evidence is missing.

Redaction requirements:

- Record only provider class, model label, success/failure, latency, approximate
  token statistics, and public failure category.
- Do not record API key, raw prompt, raw response, authorization header, or raw
  provider trace.

### `llm-backed-world-creation`

Goal:

- Prove a basic user worldview can produce a public, system-digestible,
  LLM-backed world state through WorldEngine.

Required operations:

- Enter a basic world premise through the external client or public surface.
- Create the world through WorldEngine.
- Capture public initial state, entities, items, Agents, locations, world
  parameters, rule definitions, boundary conditions, and visualization payload.
- Compare against the deterministic generic world response.

Forbidden operations:

- Validation Client generates or rewrites world content.
- deterministic fallback is marked as LLM-backed.
- raw prompt or raw response is exported.
- user premise is copied directly into final state without WorldEngine
  generated structure.

Required artifacts:

- `result.json`.
- `operation-log.jsonl`.
- `api-summary.json`.
- `world-creation-summary.json`.
- `world-rule-summary.json`.
- `initial-snapshot.json` or equivalent public snapshot artifact.
- `scorecard-summary.json` or checker output.

PASS source:

- checker or scorecard PASS showing the world is premise-specific,
  system-digestible, redacted, and not deterministic generic output.

FAIL taxonomy:

- `world_creation` if creation is deterministic, generic, non-digestible, or
  not provider-backed.
- `provider` if provider-backed creation cannot run because live provider
  access fails.
- `redaction` if raw prompt, raw response, or private provider data leaks.
- `client_evidence` if required public evidence is missing.
- `checker_gap` if no checker can distinguish generic deterministic output from
  LLM-backed output.

Redaction requirements:

- Store public generated state and public rule summaries only.
- Do not store raw prompts, raw provider responses, private traces, or hidden
  generation internals.

### `world-rule-parameter-evolution`

Goal:

- Prove that generated world parameters evolve across ticks according to
  WorldEngine rules rather than static counters or hard-coded mock behavior.

Required operations:

- Start from an LLM-backed world with public parameters and rules.
- Advance multiple ticks.
- Capture parameter diffs, events, snapshots, and replay references.
- Verify that each material parameter change has a public rule reference or
  public legality explanation.

Forbidden operations:

- static counter-only tick progression is reported as rule evolution.
- direct mutation without rule evidence is reported as valid.
- Validation Client calculates authoritative world parameter changes.
- hidden implementation details are exported as proof.

Required artifacts:

- `result.json`.
- `operation-log.jsonl`.
- `api-summary.json`.
- `rule-parameter-summary.json`.
- `world-lifecycle-summary.json`.
- `diff-replay-summary.json`.
- events and snapshots artifacts.
- `scorecard-summary.json` or checker output.

PASS source:

- checker or scorecard PASS showing rule-linked parameter changes across
  ticks.

FAIL taxonomy:

- `world_evolution` if parameters do not evolve, evolve only by fixed counter,
  or lack rule linkage.
- `world_creation` if required rules or parameters were never generated.
- `redaction` if private prompts, raw responses, or hidden internals appear.
- `client_evidence` if diffs, snapshots, or event evidence is missing.
- `checker_gap` if rule linkage cannot be validated.

Redaction requirements:

- Public rule ids, public explanations, parameter names, values, and diffs are
  allowed.
- Private provider traces, raw prompt text, and hidden reasoning are forbidden.

### `rule-compliant-event-generation`

Goal:

- Prove random events and user-directed external guidance are constrained by
  world rules and cannot directly force illegal final outcomes.

Required operations:

- Run a world with public event legality rules.
- Capture at least one WorldEngine-generated or selected random event.
- Submit at least one natural-language external direction that describes a
  risk, pressure, or environmental tendency rather than a final outcome.
- Verify that WorldEngine accepts, rejects, delays, transforms, or resolves the
  direction according to public rules.
- Capture event legality summaries and resulting diffs or snapshots.

Forbidden operations:

- user direction directly kills, heals, teleports, rewrites, or otherwise forces
  an Agent final state without rule adjudication.
- Validation Client creates authoritative events.
- impossible events pass without legality status.
- raw prompt or response is used as public proof.

Required artifacts:

- `result.json`.
- `operation-log.jsonl`.
- `api-summary.json`.
- `event-legality-summary.json`.
- event artifacts.
- snapshot and diff artifacts.
- `scorecard-summary.json` or checker output.

PASS source:

- checker or scorecard PASS showing that external direction affected only
  external events or environment, and WorldEngine decided final outcomes
  through rules.

FAIL taxonomy:

- `event_legality` if illegal direct outcomes are accepted or rule adjudication
  is missing.
- `world_evolution` if events do not produce coherent state changes.
- `agent_autonomy` if event handling directly mutates private Agent intent or
  memory.
- `redaction` if private state or provider raw content leaks.
- `client_evidence` if event evidence is incomplete.
- `checker_gap` if legality cannot be checked.

Redaction requirements:

- Public legality summaries, event ids, rule references, and public outcomes
  are allowed.
- Private Agent memory, private goals, hidden context, raw thought, raw prompt,
  and raw response are forbidden.

### `agent-persistent-autonomy-evidence`

Goal:

- Prove at least one Agent shows sustained public autonomy evidence across
  multiple rounds.

Required operations:

- Create or load an LLM-backed world with at least one Agent.
- Advance enough ticks to observe multiple Agent decision moments.
- Capture observation, memory summary, public thought or reflection summary,
  intent or no-intent state, selected action, executed action, and event
  reaction.
- Verify that action source is WorldEngine public evidence rather than client
  script.

Forbidden operations:

- a single `params.applied` event is treated as persistent autonomy.
- Validation Client scripts Agent action and records it as WorldEngine action.
- direct private memory, private goal, or hidden context mutation.
- raw chain-of-thought is exported.

Required artifacts:

- `result.json`.
- `operation-log.jsonl`.
- `api-summary.json`.
- `agent-autonomy-summary.json`.
- Agent event artifacts.
- snapshots before and after Agent decision moments.
- `scorecard-summary.json` or checker output.

PASS source:

- checker or scorecard PASS showing multi-round continuity and no
  client-scripted Agent action.

FAIL taxonomy:

- `agent_autonomy` if actions are absent, single-round only, scripted by client,
  or not tied to public WorldEngine evidence.
- `world_evolution` if no world change exists for Agents to observe.
- `redaction` if private memory, private goal, hidden context, raw thought, or
  raw chain-of-thought leaks.
- `client_evidence` if operation logs or Agent evidence are missing.
- `checker_gap` if continuity cannot be validated.

Redaction requirements:

- Public memory summaries, public thought summaries, public intent summaries,
  public action summaries, and public reactions are allowed.
- Private memory payloads, private goals, raw thoughts, raw chain-of-thought,
  hidden context, and private relationship internals are forbidden.

### `llm-backed-full-lifecycle-autonomous`

Goal:

- Prove the complete LLM-backed lifecycle: provider live smoke, LLM-backed
  creation, rule-driven evolution, rule-compliant events, persistent Agent
  autonomy evidence, evidence export, checker PASS, and second-Agent read-only
  review.

Required operations:

- Run `provider-live-smoke-deepseek` or consume an accepted same-session
  provider live smoke prerequisite.
- Create an LLM-backed world from a basic user premise.
- Advance ticks until rule-driven parameter evolution, events, snapshots, and
  diffs are visible.
- Submit at least one external environmental direction and validate legality.
- Observe multi-round Agent autonomy evidence.
- Export evidence bundle from the Validation Client.
- Run WorldEngine checker or scorecard over the result directory.
- Run second-Agent read-only evidence review.

Forbidden operations:

- treating UI smoke as full lifecycle PASS.
- treating provider readiness as live call proof.
- treating deterministic generic world output as LLM-backed.
- direct API calls recorded as Agent operation-log operations.
- client-scripted Agent actions.
- user direction written directly as final state.
- raw prompt, raw response, API key, private memory, raw thought, or hidden
  context in evidence.

Required artifacts:

- `result.json`.
- `operation-log.jsonl`.
- `transcript.md`.
- `console.log`.
- screenshots.
- `api-summary.json`.
- `provider-live-summary.json`.
- `world-creation-summary.json`.
- `world-rule-summary.json`.
- `rule-parameter-summary.json`.
- `event-legality-summary.json`.
- `agent-autonomy-summary.json`.
- `world-lifecycle-summary.json`.
- `validation-client-evidence-bundle.json`.
- `scorecard-summary.json`.
- second-Agent read-only review report.

PASS source:

- WorldEngine checker or scorecard PASS for all critical items, plus
  second-Agent read-only review with no blocking P1 or P2 issue.

FAIL taxonomy:

- `provider`.
- `world_creation`.
- `world_evolution`.
- `event_legality`.
- `agent_autonomy`.
- `redaction`.
- `client_evidence`.
- `checker_gap`.

Redaction requirements:

- All redaction requirements from the component scenarios apply.
- Any leak of API key, authorization header, raw prompt, raw response, provider
  trace, private memory, private goal, raw thought, raw chain-of-thought, or
  hidden context is immediate FAIL.

## Recommended Result Layout

Recommended live result directory:

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

Recommended durable result summaries:

```text
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.md
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md
```

Recommended result files:

```text
result.json
operation-log.jsonl
transcript.md
console.log
api-summary.json
provider-live-summary.json
world-creation-summary.json
world-rule-summary.json
rule-parameter-summary.json
event-legality-summary.json
agent-autonomy-summary.json
world-lifecycle-summary.json
validation-client-evidence-bundle.json
scorecard-summary.json
second-agent-review.md
screenshots/
raw/
```

The `raw/` directory may contain raw public artifacts from WorldEngine and the
Validation Client. It must still obey redaction. It must not contain provider
raw requests, provider raw responses, raw prompts, API keys, authorization
headers, private Agent memory, private Agent goals, raw thought, or hidden
context.

## Suggested Scorecard Items

The full lifecycle scorecard should include these critical items:

- `provider_live_smoke`: pass only when a live WorldEngine-owned provider call
  succeeds with redacted evidence.
- `world_creation_llm_backed`: pass only when public world creation is
  premise-specific and not deterministic generic output.
- `world_rules_generated`: pass only when parameters, meanings, initial values,
  evolution rules, and boundaries are present.
- `parameter_evolution_rule_linked`: pass only when tick changes link to public
  rules.
- `event_legality_enforced`: pass only when random and user-guided external
  events obey world rules.
- `agent_persistent_autonomy`: pass only when multi-round Agent public evidence
  exists and is not client-scripted.
- `diff_replay_available`: pass only when events, diffs, and snapshots support
  replay or state inspection.
- `redaction_clean`: pass only when forbidden private/provider content is
  absent.
- `client_evidence_complete`: pass only when operation log, API summary,
  screenshots, transcript, and evidence bundle exist.
- `second_agent_review_clean`: pass only when read-only review finds no
  blocking P1 or P2 issue.

## Suggested Execution Sequence

Future validation should run in this order:

1. Preflight: confirm WorldEngine and Validation Client repositories are clean
   enough for scoped evidence generation.
2. Provider smoke: run `provider-live-smoke-deepseek`.
3. World creation: run `llm-backed-world-creation`.
4. Evolution: run `world-rule-parameter-evolution`.
5. Event legality: run `rule-compliant-event-generation`.
6. Agent autonomy: run `agent-persistent-autonomy-evidence`.
7. Full lifecycle: run `llm-backed-full-lifecycle-autonomous`.
8. Checker: run the documented WorldEngine checker or scorecard command.
9. Second-Agent review: read-only review of the result directory.
10. Durable result: write the result summary under `docs/testing/results/`.

Partial validation is allowed during development, but the user should not need
to manually issue separate phase commands during the formal run. A single
future validation instruction should be able to drive the staged sequence until
PASS, classified FAIL, or a stop rule is reached.

## Stop Rules

Stop the run immediately and classify the result if:

- evidence includes API key, authorization header, raw prompt, raw response,
  provider trace, private memory, private goal, raw thought, raw chain-of-
  thought, or hidden context.
- provider cost, rate limit, or quota risk exceeds the configured validation
  budget.
- no WorldEngine-owned live provider call path exists.
- the only available world creation output is deterministic generic output.
- user direction directly becomes final world fact without rule adjudication.
- Agent action is client-scripted or cannot be tied to WorldEngine public
  evidence.
- required artifacts are missing and cannot be regenerated from the same run.

## Follow-up Routing

If the gap is only checker, scenario, fixture, or saved-result schema support,
route it to testing asset enhancement under:

- `docs/testing`.
- `tools/testing`.

This does not default to a WorldEngine product iteration.

Open a WorldEngine implementation iteration when any of these are missing:

- provider live smoke endpoint or command.
- provider call abstraction.
- LLM redacted evidence schema.
- LLM-backed world creation behavior.
- world parameter and rule schema.
- world rule evolution engine.
- event legality engine.
- Agent persistent memory evidence.
- Agent persistent action evidence.

Open a Validation Client milestone when any of these are missing:

- UI display for LLM-backed lifecycle evidence.
- evidence bundle fields.
- Agent operation log export.
- API summary export.
- replay, diff, or snapshot display needed for external evidence review.

If DeepSeek fails but WorldEngine has the required interface and redacted
evidence path, record provider/environment validation FAIL. Do not change
product code merely to make the provider pass.

If raw prompt, raw response, API key, authorization header, private Agent
memory, private Agent goal, raw thought, raw chain-of-thought, or hidden
context leaks, classify as immediate `redaction` FAIL and prioritize the
redaction boundary before further validation.

## Assumptions

- DeepSeek API key is managed by WorldEngine environment variables.
- The Validation Client does not save, display, or forward provider keys.
- The Validation Client remains an external client and does not own LLM
  generation or authoritative evaluation.
- The first LLM-backed validation may discover gaps. After gaps are classified,
  decide whether to open a WorldEngine implementation iteration such as
  `0.8.10`, a Validation Client milestone such as `v0.8`, or a testing asset
  enhancement.
- The current task is documentation-only. It does not run live DeepSeek tests
  and does not modify runtime, API, checker, fixture, frontend, or Validation
  Client code.
- The validation focus is whether the functional chain can run. It is not
  expected to prove final game-quality world rules or final game-quality Agent
  behavior in one step.

## Handoff Prompt For A Future Validation Chat

Use this prompt after the required implementation and checker support exists:

```text
/goal Run llm-backed-full-lifecycle-autonomous validation.

Read:
- docs/testing/llm-backed-lifecycle-validation-plan.md
- docs/testing/agent-autonomous/scorecard.md
- docs/testing/product-capability-validation-playbook.md
- the current WorldEngine implementation package documents if a package created
  the LLM-backed provider/world/evolution/Agent surfaces.

Run the staged validation from provider live smoke through full lifecycle.
Use WorldEngine-owned provider calls only. Do not let the Validation Client
own LLM generation or evaluation. Export evidence under:

test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/

Then run the documented checker or scorecard. Ask a second Agent for read-only
review of the saved evidence. Write durable result summaries under:

docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.md
docs/testing/results/YYYY-MM-DD-llm-backed-lifecycle-validation.zh.md

Report PASS only from checker or scorecard PASS plus no blocking second-Agent
review issue. If FAIL, classify it as provider, world_creation,
world_evolution, event_legality, agent_autonomy, redaction, client_evidence,
or checker_gap.
```
