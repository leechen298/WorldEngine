# Projection Consumer Contract

Status: review complete / v0.7.1

## Purpose

This contract defines public boundaries for future projection consumers of
WorldEngine. A projection consumer is an external application, dashboard,
tool, or validation surface that reads public WorldEngine state and evidence
without becoming part of the core engine repository.

This document is documentation-only. It does not implement projection
endpoints, read models, frontend UI, product packaging, persistence, or a
projection application.

## Public Concepts

- `ProjectionConsumer`: an external consumer that reads public WorldEngine
  contracts.
- `ProjectionReadModel`: a read-only public payload shape intended for
  consumers.
- `ProjectionSurface`: a reviewed public API, schema, contract, manifest, or
  evidence bundle that a consumer may read.
- `ProjectionReadinessClaim`: a scoped claim about contract, report, core-side
  compatibility, or external consumer evidence.
- `RedactedProjectionEvidence`: evidence that describes public consumer
  behavior without private app state, UI selectors, product content, or
  external-world details.

## Allowed Consumer Surfaces

Future packages may define read-only projection surfaces for:

- runtime state summaries.
- event timeline summaries.
- Agent loop perception/action/result summaries.
- bounded memory context summaries.
- world generation preview and runtime-readiness summaries.
- readiness manifests and public contract bundles.
- redacted validation report summaries.

Each surface must be explicitly reviewed before implementation. A future
surface may be documentation-only, schema-only, API-backed, or manifest-backed,
but the active package must state which.

## Read-Only Boundary

Projection consumer surfaces must be read-only unless a future reviewed
package explicitly defines a generic engine write contract. v0.7 does not
authorize:

- product-specific write APIs.
- hidden reset APIs.
- private runner hooks.
- projection app state mutation.
- generated-world execution as active recursive runtime state.
- durable persistence or migrations.
- frontend product packaging.

## Redaction And Exposure Rules

Projection payloads and evidence must not expose:

- private external application state.
- concrete validation worlds, character name values, location name values,
  maps, resources, story rule details, seed data, or private transcripts.
- UI selectors or hidden reset details.
- validation oracle internal behavior.
- private fixture repository paths.
- raw memory records beyond reviewed bounded summaries.
- provider secrets, prompts, private traces, or non-redacted external event
  payloads.

Projection payloads may expose generic public identifiers, public contract
surface ids, runtime tick ids, event type summaries, redacted evidence ids,
and bounded summaries explicitly authorized by the active package.

## Readiness Claim Taxonomy

Projection work may use these claim values:

- `projection consumer contract ready`: public read-model semantics are
  documented and reviewed.
- `projection report format ready`: redacted consumer evidence semantics are
  documented or implemented and reviewed.
- `core-side compatibility ready`: current-session evidence proves core
  public surfaces remain compatible.
- `external consumer pass`: an external consumer exercised public surfaces and
  returned accepted redacted PASS evidence.
- `out of scope`: the claim belongs to v0.8 or an external app.

Do not use these values to claim first projection application readiness,
product readiness, or external suite PASS unless the exact evidence exists.

## Compatibility Requirements

- Existing dashboard behavior remains compatible.
- Existing runtime, event, Agent loop, memory, generation, and API envelope
  behavior remains unchanged by this contract.
- Future projection payloads must be additive and versioned.
- Memory and Agent context exposure must remain bounded and redacted.
- Existing generated-world preview/runtime-readiness behavior must not be
  reinterpreted as active generated-world runtime execution.

## Authorization Criteria For Later Packages

Before a future package implements projection read models or APIs, it must
record:

- the exact read models or API surfaces authorized.
- the fields allowed in each payload.
- redaction and bounded-exposure rules.
- focused tests for payload shape, compatibility, and no write side effects.
- explicit exclusions for v0.8 projection application behavior.

`0.7.4-projection-consumer-read-model-contracts` owns any reviewed projection
read-model implementation. `0.7.1` only defines public boundaries.

## Non-Goals

- Do not build a projection application.
- Do not add product-specific frontend, UI, art, packaging, or routing.
- Do not add write APIs, reset APIs, migrations, persistence, or live provider
  behavior.
- Do not claim v0.8 readiness or product readiness.
