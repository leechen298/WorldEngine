# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Current State

Current relevant surfaces:

- `backend/app/schemas/world_generation.py` already contains v0.6
  deterministic generation concepts such as `WorldTemplate`,
  `GenerationPlan`, `GenerationMetadata`, diagnostics, preview, lineage, and
  runtime-readiness request/result shapes.
- `backend/app/api/routes/world.py` exposes v0.8 public `POST /worlds` with
  operation id `create_world`. It currently returns deterministic generic
  public initial state and visualization data derived from a prompt digest.
- `backend/app/schemas/world.py` contains public handoff, world creation,
  provider readiness, director guidance, public state, and redaction schemas.
- `backend/app/agent/provider_config.py`, `backend/app/api/routes/provider.py`,
  and `backend/app/schemas/provider.py` define the `0.9.1` provider smoke and
  redacted summary boundary.
- `GET /manifest` now lists `/provider/live-smoke` while warning that provider
  readiness is not live provider call proof.
- The LLM-backed world creation test scenario requires public generated
  state, `world_creation_summary`, redaction scan, scorecard/checker evidence,
  and explicit distinction from deterministic generic output.

`0.9.2` must build on these surfaces without touching `backend/worldengine/`
and without turning validation clients into generation owners.

## Contract Alignment and Invariants

Implementation after review must preserve these invariants:

- Deterministic `POST /worlds` remains available and clearly labeled.
- LLM-backed generation has a separate public classification from
  deterministic fallback.
- WorldEngine owns provider/generation behavior.
- LLM output is untrusted structured data. It must be parsed into a public
  structured model or plan, validated, diagnosed, and classified before it can
  be summarized as runtime-ready.
- Public generated output is structured enough for runtime/checker use.
- Public evidence never includes raw prompts, raw provider payloads, provider
  traces, private Agent state, private evaluator data, hidden context, or
  secrets.
- Full rule/parameter schema remains deferred to `0.9.3`; `0.9.2` may expose
  only outlines and readiness inputs needed for generated world creation.

## Proposed Implementation

After review authorization, implement a small active-backend generation layer:

```text
Public worldview request
  -> request validation and redaction guard
  -> provider readiness / provider smoke boundary classification
  -> LLM-backed generation adapter, safe mock classifier, or blocked/fallback classifier
  -> untrusted structured output normalization
  -> validation, diagnostics, and runtime-readiness classification
  -> public generated world model candidate
  -> validation metadata and diagnostics
  -> public world_creation_summary response or artifact
```

Preferred API shape:

```text
POST /worlds/generate-from-worldview
operation_id: generate_world_from_worldview
```

The endpoint should be additive and should not replace existing
`POST /worlds`. If implementation chooses a different path, the route must
remain public, OpenAPI-discoverable, and clearly separate LLM-backed generation
from deterministic generic creation.

## Candidate Backend Shape

Expected implementation surfaces:

```text
backend/app/agent/provider_config.py
backend/app/agent/worldview_generation.py
backend/app/api/routes/world_generation.py
backend/app/api/routes/__init__.py
backend/app/api/app_factory.py
backend/app/schemas/world_generation.py
backend/app/schemas/world.py
backend/app/tests/test_llm_worldview_generation_api.py
backend/app/tests/test_world_generation_contracts.py
backend/app/tests/test_public_handoff_contract_api.py
```

Alternative file names are allowed if they match local conventions and stay
inside the allowed active backend paths.

## Data Model / Schema Changes

Additive schema concepts should include:

```text
WorldviewGenerationRequest
WorldviewGenerationResponse
PublicGeneratedWorldModel
PublicWorldCreationSummary
WorldviewGenerationValidationMetadata
WorldviewGenerationRedaction
WorldviewGenerationDiagnostic
WorldviewGenerationMode
WorldviewGenerationStatus
```

Required public enum semantics:

```text
generation_mode:
  provider_backed
  deterministic_fallback
  safe_mock
  not_configured
  blocked

generation_status:
  generated
  fallback
  not_configured
  blocked
  failed
  redaction_failure

creation_mode:
  llm_backed_generation
  deterministic_generic_fallback
  safe_mock_non_live
  provider_not_configured
  blocked
```

Required public validation flags or summaries:

```text
llm_backed: true | false
provider_backed: true | false
premise_specific: true | false | unknown
system_digestible: true | false
runtime_ready: true | false | blocked
deterministic_generic_response: true | false
deterministic_generic_fallback_detected: true | false
raw_prompt_included: false
raw_provider_response_included: false
provider_trace_included: false
private_data_included: false
```

If a provider is not configured, the response should return a public blocked or
not-configured classification rather than throwing private provider details.

## Runtime / Service Design

The generation helper should expose narrow functions:

- validate public worldview request.
- build a private provider intent without exposing it in public evidence.
- create a generated model candidate or classify generation as blocked.
- summarize public generated model fields.
- validate redaction before returning public evidence.
- classify deterministic fallback separately from provider-backed generation.
- sanitize request validation errors so rejected raw premise/private field
  values are not echoed.

The helper must not:

- persist generated worlds.
- mutate active runtime state.
- append canonical world events.
- execute bounded runtime ticks.
- install rules or parameters into runtime.
- store provider traces or raw prompt data.

Runtime readiness in this package is a public classification, not actual
runtime execution. Later packages own rule schema, fidelity evaluation, and
bounded runtime execution.

## Compatibility

- `POST /worlds` remains deterministic and compatible.
- `GET /manifest` may add the new generation endpoint and warnings
  additively.
- Existing provider readiness labels remain compatible with `0.9.1`.
- Existing v0.6 generation schemas remain compatible; new schemas should be
  additive and may reuse diagnostics, metadata, and runtime-readiness terms.
- Existing tests for public handoff, world creation, provider redaction, and
  validation error sanitization must continue to pass.

## Redaction Scan Points

Redaction and private-value echo checks must cover:

- request validation errors.
- provider result classification.
- generation metadata.
- public generated model.
- `world_creation_summary`.
- serialized API responses.
- any result artifacts or operation logs created by this package.

Forbidden markers include raw prompt, raw request, raw response,
provider_trace, hidden_context, private memory, private goal, self_state,
authorization, bearer, api_key, secret, token, credential, and concrete
validation-world fixture markers.

## Risks

- Risk: deterministic fallback is overstated as LLM-backed success.
  Mitigation: require explicit `generation_mode` and fallback tests.
- Risk: public evidence leaks raw prompt or provider response text.
  Mitigation: redaction schema plus serialized-response scans with injected
  forbidden markers.
- Risk: generated model is prose-only and not system-digestible.
  Mitigation: schema tests require structured public model sections.
- Risk: implementation drifts into `0.9.3+` rules and runtime execution.
  Mitigation: restrict this package to outlines, summaries, and readiness
  classification.
- Risk: safe mock provider behavior is counted as provider-backed world
  generation.
  Mitigation: explicit `safe_mock_non_live` / `safe_mock_only` classification
  and negative tests.
- Risk: Validation Client becomes a generation owner.
  Mitigation: no external repository changes and WorldEngine-owned generation
  evidence.
