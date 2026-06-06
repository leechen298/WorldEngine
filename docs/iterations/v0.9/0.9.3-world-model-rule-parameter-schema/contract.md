# Contract

Chinese mirror: `contract.zh.md`.

## Public Concepts

### `generated rule parameter set`

A public structured bundle of generated world parameters, rules, constraints,
boundaries, and validation metadata derived from a generated world model.

Required semantics:

- It is public and redacted.
- It is not active runtime state.
- It can be validated deterministically before runtime use.
- It references the `world_id`, `generation_id`, and `premise_digest` from
  `0.9.2` when available.
- It must not include raw prompts, raw provider responses, provider traces,
  hidden context, private Agent memory, private evaluator data, or secrets.

### `world parameter definition`

A public generated parameter definition.

Required field groups:

```text
parameter_id
path
value_type
initial_value
visibility
description
constraints
source
rule_refs
```

Required semantics:

- `parameter_id` is stable inside the generated rule parameter set.
- `path` is a dot-separated public parameter path.
- `value_type` is one of `int`, `float`, `bool`, `string`, or `json`.
- `initial_value` must match `value_type`.
- `visibility` must stay public or internal-public; private Agent state is not
  allowed.
- `constraints` may include public bounds, enum values, required keys, or
  shape hints, but not hidden rule logic.
- `rule_refs` must point to public rule ids in the same set.

### `world evolution rule`

A public rule definition that describes how parameters may change.

Required field groups:

```text
rule_id
rule_kind
trigger
conditions
effects
target_parameter_refs
allowed_ops
priority
cooldown
evidence
```

Required semantics:

- `rule_id` is stable and public.
- `rule_kind` classifies the rule, such as `environment_trend`,
  `resource_drift`, `agent_public_pressure`, `boundary`, or `constraint`.
- `trigger` describes when the rule is eligible. This package defines schema
  only; it does not execute triggers.
- `conditions` are public deterministic checks or structured public
  expressions.
- `effects` describe allowed parameter operations and expected value changes.
- `target_parameter_refs` must resolve to parameter ids in the same set.
- `allowed_ops` must use the existing patch vocabulary: `add`, `set`,
  `remove`, or future-public no-op classification if needed.
- `evidence` must include public explanation fields and must not include raw
  LLM reasoning or provider traces.

### `world constraint`

A public constraint over parameters, rules, or the generated set as a whole.

Required semantics:

- Constraints must be deterministic enough for validation.
- Constraints may express value ranges, enum membership, required parameter
  refs, forbidden operation refs, or public dependency checks.
- Constraints must not encode untestable prose as the only rule.

### `world boundary`

A public boundary that limits generated-world behavior.

Required semantics:

- Boundaries are inspectable public constraints, not hidden runtime behavior.
- Boundaries may restrict private-state mutation, direct user-imposed final
  facts, provider trace exposure, concrete fixture content, or unbounded
  runtime changes.
- Boundaries do not execute in this package. They provide schema and
  validation evidence for later packages.

### `rule parameter validation result`

A deterministic public validation result for a generated rule parameter set.

Required field groups:

```text
validation_status
diagnostics
accepted_parameter_count
accepted_rule_count
rejected_parameter_count
rejected_rule_count
redaction_status
compatibility_summary
```

Validation must reject or diagnose:

- duplicate parameter ids.
- duplicate rule ids.
- unresolved rule refs.
- unresolved parameter refs.
- initial values that do not match declared `value_type`.
- rules with no target parameter refs when targets are required.
- prose-only rules with no structured trigger/effect.
- private, secret-like, provider-trace, raw prompt, or concrete fixture
  markers.

### `world rule summary`

A public summary artifact or response section that validators can inspect.

Required semantics:

- It summarizes accepted/rejected counts, parameter paths, rule ids, boundary
  ids, and diagnostics.
- It may include public explanations.
- It must not include raw provider content or private source payloads.

## Compatibility Constraints

- Existing `/world/params` behavior must remain compatible.
- Existing `ParamPatchItem`, `ApplyParamsRequest`, `ParamRegistry`, and
  `ParamValidator` semantics must remain compatible unless this contract is
  updated and re-reviewed.
- Existing deterministic `POST /worlds` behavior must remain compatible.
- Existing `/world/generation/worldview` response must remain compatible.
- Existing `WorldSpec` schemas must only receive additive fields if touched.
- Existing event schemas remain additive-compatible; event legality execution
  is out of scope.
- New schemas must be generic WorldEngine concepts and must not include
  concrete world content.
- Validation errors and diagnostics must not echo private field values,
  secret-like values, raw prompts, raw provider details, hidden context, or
  private field labels.

## Allowed Changes

After documentation review authorization, this package may modify:

- `backend/app/schemas/world_generation.py` for additive rule/parameter
  schemas, or a new active-backend schema module if local style requires it.
- `backend/app/core/world_generation.py` or a narrow new active-backend helper
  for deterministic validation and public summaries.
- `backend/app/api/routes/world_generation.py` only if an additive endpoint or
  existing worldview-generation response field is needed for rule/parameter
  validation.
- `backend/app/api/routes/world.py` and manifest data only for additive public
  surface discovery.
- `backend/app/world/validation/registry.py`,
  `backend/app/world/validation/validator.py`, and related validation tests
  only for additive compatibility support. Existing registered path behavior
  must not break.
- focused backend tests under `backend/app/tests/`.
- package `review.md` and `review.zh.md`.
- v0.9 parent status/review docs only for route/status handoff after review or
  implementation closeout.

## Forbidden Changes

This package must not:

- modify `backend/worldengine/`.
- modify frontend code.
- modify Validation Client or external repositories.
- execute live provider calls.
- persist generated rules or generated worlds to durable storage.
- install generated rules into active runtime state.
- run bounded runtime ticks as proof of rule evolution.
- implement worldview fidelity evaluation.
- implement natural-language direction, event legality, Agent continuity,
  narrative projection, diagnostic dialogue, checker fixtures, Validation
  Client evidence export, or full lifecycle validation.
- add concrete demo-world names, maps, characters, locations, resources, story
  rules, validation oracle data, or application-specific backend behavior.
- store or export API keys, authorization headers, raw prompts, raw provider
  requests, raw provider responses, provider traces, hidden context, private
  Agent memory, raw thought, chain-of-thought, or private evaluator data.
- claim rule-linked evolution PASS, LLM-backed lifecycle PASS, external
  validation PASS, or product readiness.

## North Star Check

This package keeps WorldEngine generic by defining public rule and parameter
contracts for generated worlds. It prepares the runtime and checker spine for
future world evolution without creating a specific game world or product
backend.

## Out-of-Scope Follow-ups

- `0.9.4`: worldview generation fidelity evaluation.
- `0.9.5`: bounded runtime control and run budgets.
- `0.9.6`: natural-language world direction boundary.
- `0.9.7`: rule-linked evolution and event legality execution.
- `0.9.10`: checker fixtures and scorecard support.
