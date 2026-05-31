# Contract

Status: review complete

implementation_authorized: no

## Public Concepts

`0.6.1` defines names and semantics only. These concepts are planned contract
terms for later additive schemas and services; this package does not create
runtime classes, Pydantic models, routes, frontend components, tests, or
generated data files.

### `WorldGenerationRequest`

A reviewable request to generate a candidate `WorldSpec`.

Required semantics for later implementation:

- carries a stable request id or caller-supplied correlation id.
- selects exactly one primary generation input path:
  - a `WorldTemplate` plus explicit constraints, or
  - a validated `GenerationPlan`.
- may include generic constraints such as target cell count bounds, allowed
  entity reference kinds, metadata tags, and deterministic seed material.
- records provenance for the request source without storing private external
  validation details.
- must not include concrete demo-world names, story content, private oracle
  data, or application-specific behavior.

### `WorldTemplate`

A generic, reusable generation shape that constrains how a future deterministic
generator may create `WorldSpec` data.

Required semantics for later implementation:

- has a template id and version.
- declares generic cell patterns, entity reference slots, metadata defaults,
  and validation constraints.
- may use placeholder identifiers and labels only when they are generic and do
  not encode a concrete external world.
- must not contain concrete maps, characters, locations, resources, story
  rules, seed data, validation oracle details, or UI-specific behavior.
- must be deterministic when combined with the same request constraints and
  seed material.

### `GenerationPlan`

A normalized structured plan that can be validated before it is compiled into
`WorldSpec`.

Required semantics for later implementation:

- describes intended `WorldSpec` structure as data, not executable code.
- includes root cell intent, child-cell plan entries, entity reference plan
  entries, metadata entries, and constraints.
- is provider-independent. A plan may have been produced by a user, tool, or
  AI system, but import validation must treat it as untrusted structured data.
- must fail with diagnostics when it cannot produce valid `WorldSpec` data.
- must not bypass `load_worldspec` or runtime-readiness checks in later
  packages.

### `GeneratedWorldSpec`

A candidate generated output consisting of `WorldSpec` data plus generation
metadata.

Required semantics for later implementation:

- generated `WorldSpec` data must preserve current `WorldSpec` invariants:
  `schema_version` is `"0.2"`, `id` is non-empty, `root` exists, root and child
  cell ids are non-empty, `kind` remains `"world"`, `entity_refs` contain
  non-empty `id` and `kind`, and metadata remains additive.
- generated output is not considered runnable until it passes reviewed loader
  and runtime-readiness checks in the package that owns those checks.
- generated output must keep diagnostics and provenance inspectable.
- generation provenance may be carried by wrapper metadata, generation
  metadata, or reviewed source labels, but must not mutate `LoadedWorldSpec`
  fields or require the loader to accept new input types in this package.
- generated output must not be written as a durable fixture or seed data in
  this package.

### `GenerationMetadata`

Inspectable evidence about how generation happened.

Required semantics for later implementation:

- records request id, generation id, template id/version or plan id/version,
  deterministic seed material or seed digest where applicable, validation
  status, diagnostics, and generation timestamp or source clock semantics.
- records provider-independent provenance for AI-assisted plan imports without
  requiring live provider calls.
- records lineage from a `RegenerationRequest` when generation revises prior
  generated output.
- must not store private prompts, private validation oracle internals, secrets,
  credentials, or external application data.

### `GenerationPreview`

A bounded, inspectable summary of a generated candidate before runtime use.

Required semantics for later implementation:

- summarizes ids, schema version, root cell id/kind, child-cell counts,
  entity-ref counts, metadata keys, validation status, and diagnostics.
- may include excerpts of generic labels or placeholder labels only when they
  do not encode concrete demo-world content.
- is not a runtime state snapshot, not an E2E pass claim, and not a quality
  verdict.

### `RegenerationRequest`

A request to revise a prior generation through explicit lineage and
constraints.

Required semantics for later implementation:

- references the source generation id or request id.
- declares which constraints changed and which compatibility expectations must
  remain stable.
- records lineage in `GenerationMetadata`.
- does not imply durable persistence, migrations, or versioned storage unless
  a later reviewed child explicitly authorizes them.

### Generation Diagnostics

Structured explanations for parse, schema, constraint, template, plan,
validation, and compatibility failures.

Required semantics for later implementation:

- diagnostics must include stable machine-readable codes, human-readable
  messages, optional paths, severity, and source context when available.
- diagnostics must align with existing loader-style failure reporting:
  `unsupported_input`, `parse_error`, and `schema_validation_error` remain
  existing loader codes, and schema locations use JSON Pointer-style paths such
  as `/schema_version` or `/root/id`.
- future API exposure of generation diagnostics must fit the current error
  envelope: HTTP status maps to numeric `code`, `msg` remains a string, and
  optional `data` may carry `errors` and, where reviewed, `metrics`.
- diagnostics are evidence, not hidden control flow.

## Compatibility Requirements

- `WorldSpec`, `WorldCell`, and `EntityRef` remain unchanged in this package.
- Future generated `WorldSpec` data must validate against the current
  `WorldSpec` schema unless a later reviewed child authorizes an additive
  schema extension.
- `load_worldspec`, `LoadedWorldSpec`, `WorldSpecLoaderResult`, and
  `WorldSpecLoaderError` semantics remain unchanged in this package. Normal
  parse and schema failures return loader result errors rather than raising.
- `RuntimeContext`, `RuntimeContextSummary`, `build_runtime_context`, and
  `summarize_runtime_context` remain unchanged in this package. Runtime
  context remains bounded to ids, schema version, root type, source fields, and
  metadata summary; it must not leak raw `WorldSpec` or root payloads.
- `RuntimeEngine.get_runtime_context`, `RuntimeEngine.step`, tick/time
  behavior, event emission, and params behavior remain unchanged. Runtime step
  events must not include raw generated specs or root payloads unless a later
  reviewed child explicitly authorizes an additive evidence surface.
- v0.4 Agent Loop schemas and `POST /world/agent/loop/step` remain unchanged.
- v0.5 working-memory and episodic-memory context surfaces remain unchanged.
- Existing API envelope and error shape remain unchanged:
  successful responses use `code`, `data`, and `msg`; error responses use
  `code`, `msg`, and optional `data`.
- Existing routes, archive behavior, event routes, params routes, frontend
  behavior, fixture boundaries, migrations, and legacy `backend/worldengine/`
  behavior remain unchanged.
- Historical v0.5 evidence remains handoff context only and does not count as
  current v0.6 pass evidence.

## Allowed Changes

- Create or update documentation under this package directory.
- Define planned public concept semantics and field-level meanings in prose.
- Define documentation-only compatibility, scope, evidence, and authorization
  criteria.
- Record documentation checks, subagent/evaluator evidence, findings, and
  review status.

## Forbidden Changes

- Do not modify runtime, schema, service, API, frontend, backend test, fixture,
  migration, generated result, external repository, or `backend/worldengine/`
  implementation files.
- Do not create planned future implementation paths such as
  `backend/app/schemas/world_generation.py`,
  `backend/app/world/generation.py`,
  `backend/app/api/routes/world_generation.py`,
  `backend/app/tests/test_world_generation_*.py`, or
  `frontend/src/components/GenerationPanel.vue`.
- Do not define concrete generated world examples beyond generic placeholder
  identifiers.
- Do not require live external AI-provider calls or provider-specific secrets.
- Do not introduce external validation readiness, projection readiness,
  durable persistence, migrations, release status, or product-readiness claims.
- Do not mark `implementation_authorized: yes` for this package.

## Authorization Criteria For `0.6.2`

`0.6.2-template-catalog-and-deterministic-generator-core` may record
`implementation_authorized: yes` only after its own package documents exist and
review evidence confirms all of the following:

- it reads this reviewed `0.6.1` contract and keeps generated content generic.
- it identifies exactly which backend schema/service/test files it may create
  or modify.
- it limits implementation to deterministic template catalog and
  template-to-`WorldSpec` generator core behavior.
- it does not add structured plan compilation, AI-assisted plan import,
  backend API routes, frontend preview UI, regeneration, durable persistence,
  migrations, external validation readiness, or projection readiness.
- it defines focused tests proving deterministic output, invalid template
  diagnostics, and generated `WorldSpec` loader compatibility.
- it defines adjacent compatibility regression evidence for loader and
  runtime-context surfaces touched by the implementation, including preserving
  loader error codes, JSON Pointer paths, bounded runtime context summaries,
  and existing API envelopes.
- it includes a documentation/contract evaluator report with no unresolved
  P1/P2 findings.

## North Star Check

This contract supports the north star by making world generation a generic,
inspectable engine capability. It keeps external applications as consumers,
keeps concrete world content out of the core repository, and preserves the
event/runtime/memory spine that later generated worlds must plug into.

## Out-of-Scope Follow-ups

- `0.6.2`: deterministic template catalog and generator core.
- `0.6.3`: structured generation plan compiler.
- `0.6.4`: provider-independent AI-assisted plan import.
- `0.6.5`: generation validation, metadata, and preview API.
- `0.6.6`: regeneration and runtime-readiness integration.
- `0.6.7`: dashboard generation preview and E2E smoke.
- `0.6.8`: evidence and compatibility audit.
- `0.6.9`: release-candidate bundle.
- `0.6.10`: final closeout.
- v0.7 external validation readiness.
- v0.8 projection application readiness.
