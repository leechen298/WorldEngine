# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Current State

Relevant current surfaces:

- `backend/app/schemas/world_generation.py` contains `0.9.2`
  `WorldviewGenerationRequest`, `WorldviewGenerationResponse`,
  `PublicGeneratedWorldModel`, `PublicWorldCreationSummary`, and validation
  metadata. `PublicGeneratedWorldModel` currently exposes
  `world_parameters_outline`, `rules_outline`, `boundary_conditions`, and
  `runtime_readiness_inputs`.
- `backend/app/agent/worldview_generation.py` creates non-live public generated
  world candidates. It produces rule and parameter outlines but does not
  validate a full rule/parameter set.
- `backend/app/schemas/params.py` defines patch request shape:
  `ParamPatchItem` and `ApplyParamsRequest`.
- `backend/app/world/validation/registry.py` registers writable runtime paths:
  `counter.increment`, `heartbeat.enabled`, and `scene.weather`.
- `backend/app/world/validation/validator.py` validates existing patch ops,
  reserved prefixes, known paths, value types, and bounds.
- `backend/app/api/routes/world_params.py` exposes existing `/world/params`
  read/apply routes and emits `params.applied` events.
- `backend/app/schemas/event.py` provides additive event refs, but event
  legality execution is not part of this package.
- `backend/app/schemas/world_cell.py` provides generic `WorldSpec`; this
  package should not require a breaking schema change there.

## Contract Alignment and Invariants

Implementation after review must preserve:

- existing `/world/params` apply/read behavior.
- existing deterministic `POST /worlds`.
- existing `/world/generation/worldview` response compatibility.
- no `backend/worldengine/` changes.
- no active runtime mutation when validating generated rule parameter sets.
- no live provider calls.
- public redaction of raw prompt/provider/private markers.

The generated rule parameter set is a public candidate contract, not installed
runtime state.

## Proposed Implementation

Preferred implementation shape after review authorization:

```text
Public generated model or explicit rule parameter payload
  -> schema validation
  -> deterministic rule/parameter validation helper
  -> redaction/private-marker scan
  -> public validation result
  -> public world_rule_summary
```

The implementation should add a narrow schema and validation layer rather than
embedding rule semantics into the runtime engine.

## Affected Surfaces

Expected surfaces:

```text
backend/app/schemas/world_generation.py
backend/app/core/world_generation.py or backend/app/core/world_rule_parameters.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/world.py
backend/app/tests/test_world_generation_schema.py
backend/app/tests/test_world_rule_parameter_schema.py
backend/app/tests/test_llm_worldview_generation_api.py
backend/app/tests/test_world_params.py or test_param_validator.py
```

Alternative active-backend file names are acceptable if they stay inside the
contract.

## Data Model / Schema Changes

Additive schema concepts should include:

```text
WorldParameterValueType
WorldParameterVisibility
WorldParameterDefinition
WorldParameterRef
WorldRuleTrigger
WorldRuleCondition
WorldRuleEffect
WorldEvolutionRule
WorldConstraint
WorldBoundary
GeneratedRuleParameterSet
RuleParameterDiagnostic
RuleParameterValidationResult
PublicWorldRuleSummary
```

Candidate field semantics:

- `WorldParameterDefinition.parameter_id`: stable id within the set.
- `WorldParameterDefinition.path`: dot path used for public parameter
  references.
- `WorldParameterDefinition.initial_value`: JSON-compatible value checked
  against `value_type`.
- `WorldEvolutionRule.rule_id`: stable public id.
- `WorldEvolutionRule.target_parameter_refs`: parameter ids that must resolve.
- `WorldEvolutionRule.effects`: structured public operations and public value
  expressions or value deltas.
- `WorldConstraint`: deterministic public constraints over parameters, rules,
  or the generated set.
- `WorldBoundary`: inspectable public boundary category and explanation.
- `RuleParameterValidationResult`: deterministic accept/reject result with
  public diagnostics and redaction status.

## Runtime / Service Design

Validation helper responsibilities:

- ensure unique parameter ids and paths.
- ensure unique rule ids.
- resolve parameter refs and rule refs.
- validate `initial_value` against `value_type`.
- validate structured trigger/effect presence.
- reject private markers in ids, paths, descriptions, evidence, diagnostics,
  and summary fields.
- produce public diagnostics with stable codes and public paths.
- produce a public summary that can become `world-rule-summary.json` later.

The helper must not:

- evaluate rules over time.
- apply parameter patches to `WorldState`.
- append events.
- persist generated data.
- call providers.
- inspect private Agent memory or hidden evaluator data.

## Compatibility

Existing patch validation continues to use the current registry and validator.
Generated rule/parameter schema may reference future or generated parameter
paths, but it must not silently make those paths writable by `/world/params`.
Any bridge from generated definitions into runtime writable params is future
work and requires review.

Existing schema/API additions should be optional and additive.

## Risks

- Risk: generated rules remain untestable prose.
  Mitigation: tests reject rules without structured triggers/effects or target
  refs.
- Risk: generated parameter paths break `/world/params`.
  Mitigation: compatibility tests keep current registered-path behavior.
- Risk: private prompt/provider data leaks through descriptions or evidence.
  Mitigation: serialized schema/summary redaction tests.
- Risk: package drifts into runtime evolution.
  Mitigation: contract forbids applying patches, appending events, or running
  tick-based proof.
