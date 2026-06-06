# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

### `worldview premise`

A public user-provided description of the desired world. It may include
setting, tone, constraints, broad entities, environmental conditions, or
high-level rules, but it is untrusted input.

Required semantics:

- It must be bounded by request validation.
- It must not be copied directly into canonical final world state without
  structured generation and validation.
- It must not contain API keys, provider headers, private evaluator data,
  hidden prompts, private Agent memory, or application-specific oracle data.
- Public evidence may include length, digest, public premise tags, and
  redacted summaries, but not raw private prompt traces.

### `LLM-backed generation request`

A WorldEngine-owned request to transform a public worldview premise into a
generated public world model candidate.

Required semantics:

- It must be initiated by WorldEngine, not Validation Client.
- It must classify provider state as `provider_backed`, `deterministic_fallback`,
  `not_configured`, `blocked`, or `failed`.
- It must keep deterministic fallback visible and must not report fallback as
  LLM-backed PASS.
- It must be testable without live provider access through blocked and safe
  fallback paths.

### `generated world model`

A public, system-digestible world model candidate derived from the worldview
premise.

Required public field groups:

```text
schema_version
world_id
generation_id
generation_status
generation_mode
creation_mode
llm_backed
provider_backed
deterministic_generic_fallback_detected
provider_class
model_label
worldengine_owned_generation
premise_digest
public_world_model
world_creation_summary
validation_metadata
redaction
warnings
blockers
```

`public_world_model` must be structured data, not only prose. It should
include only public fields such as:

```text
title_label
premise_summary
world_parameters_outline
locations_outline
entities_outline
agents_outline
items_outline
environment_outline
rules_outline
boundary_conditions
runtime_readiness_inputs
```

This package may define outlines required for `0.9.2`, but full structured
rule/parameter schema remains owned by `0.9.3`.

The generated model must not be a prompt digest plus a fixed observer. It must
include public, redacted correspondence between the worldview premise and
generated world parameters, entities, agents, environment, boundary
conditions, visualization references, and rule outlines.

### `world_creation_summary`

A public evidence artifact or response section that validators can inspect.
It must show whether the generated output is:

- premise-specific.
- system-digestible.
- redacted.
- distinct from the deterministic generic response.
- runtime-ready or blocked with a public reason.
- `provider_backed`, `deterministic_fallback`, `not_configured`, `blocked`, or
  `failed`.

It must not include raw prompts, raw responses, provider traces, private
evaluator data, or concrete external validation seed worlds.

### `generation validation metadata`

Public validation metadata used to classify the candidate before runtime use.

Required groups:

```text
premise_specificity
system_digestibility
deterministic_fallback_label
runtime_readiness
redaction_status
provider_generation_status
diagnostics
```

Diagnostics must use stable public codes, public messages, optional public
paths, severity, and no private source payloads.

### `generation provenance summary`

A public summary of how generation was classified.

Required public fields:

```text
creation_mode
llm_backed
provider_backed
worldengine_owned_generation
provider_class
model_label
call_status
deterministic_generic_fallback_detected
safe_mock_only
provider_live_call_evidence
```

`safe_mock_only` must never count as provider-backed generation PASS.
`provider_live_call_evidence` must be absent, false, or blocked unless live
provider execution is explicitly authorized and redaction-checked in the
current session.

## Compatibility Constraints

- Existing `POST /worlds` deterministic generic behavior must remain
  available and clearly labeled.
- Existing public handoff manifest behavior remains additive-compatible.
- Existing v0.6 generation schemas and loader/runtime-readiness semantics
  remain compatible.
- Existing `WorldSpec` schema changes must be additive unless this contract is
  updated and re-reviewed.
- Existing API response envelope behavior must remain compatible unless the
  implementation intentionally uses a public top-level response shape already
  required by v0.8 handoff.
- Existing unconfigured provider behavior remains safe and testable.
- New public outputs must use generic WorldEngine concepts, not external
  application details.
- Validation errors and rejected request diagnostics must not echo raw
  worldview input, secret-like values, raw provider details, hidden context, or
  private field labels.

## Allowed Changes

After review authorization, this package may modify:

- `backend/app/api/routes/`
- `backend/app/api/app_factory.py`
- `backend/app/agent/provider_config.py`
- `backend/app/agent/worldview_generation.py`
- `backend/app/schemas/`
- `backend/app/core/world_generation.py` or a similarly scoped active-backend
  generation helper, if needed for reusable validation or public summaries.
- focused backend tests under `backend/app/tests/`.
- `tools/testing/validate_agent_autonomous_result.py` and focused tests only
  if public `world_creation_summary` checker support is needed.
- package `review.md` and `review.zh.md`.
- v0.9 parent status/review docs only for route/status handoff after review or
  implementation closeout.

## Forbidden Changes

This package must not:

- modify `backend/worldengine/`.
- modify the Validation Client repository.
- make Validation Client own provider calls, prompt assembly, generation,
  evaluation, or provider credentials.
- add concrete demo-world names, maps, characters, locations, resources, story
  rules, seed data, oracle internals, or application-specific backend logic.
- persist provider keys, authorization headers, raw prompts, raw provider
  requests, raw provider responses, provider traces, hidden context, private
  evaluator data, private Agent memory, raw thought, or chain-of-thought.
- claim LLM-backed generation PASS from deterministic fallback, safe mock, or
  provider readiness alone.
- use `/provider/live-smoke` safe mock success as provider-backed world
  generation evidence.
- claim provider live PASS unless a live call is explicitly authorized, run,
  and redaction-checked in the current session.
- implement `0.9.3+` rule schema, bounded runtime controls, event legality,
  Agent continuity, narrative projection, diagnostic dialogue, Validation
  Client evidence export, or full lifecycle validation.
- introduce migrations, durable generated-world persistence, product UI,
  game packaging, or external repository changes.
- modify Agent loop, private memory, private goals, or Agent continuity
  behavior from `backend/app/agent/`.

## North Star Check

This package keeps WorldEngine as a generic recursive world generation engine.
It defines public engine contracts and generated model summaries rather than a
specific game world or application backend. External clients remain consumers
of the public generation/evidence contract.

## Out-of-Scope Follow-ups

- `0.9.3`: full world model rule and parameter schema.
- `0.9.4`: worldview generation fidelity evaluation.
- `0.9.5`: bounded runtime control and run budget.
- `0.9.7`: rule-linked event legality and evolution.
- `0.9.10`: LLM-backed checker, fixtures, schema, and scorecard.
- `0.9.11`: Validation Client evidence handoff contract.
- `0.9.12`: LLM-backed full lifecycle validation execution.

## Stop Rules

Stop implementation if:

- generated output cannot be represented as structured public data.
- premise specificity cannot be evidenced without raw prompt or raw provider
  response exposure.
- provider configuration requires secrets outside environment-owned runtime
  configuration.
- Validation Client changes are required.
- deterministic fallback would need to be reported as LLM-backed PASS.
- the implementation requires concrete demo-world content.
- tests cannot prove redaction and fallback/blocker classification.
- validation errors would echo raw/private request values.
- implementation discovers this package needs the broader rule schema or
  checker architecture owned by later packages.
