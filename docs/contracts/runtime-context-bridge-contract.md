# Runtime Context Bridge Contract

Status: ready for review

## Purpose

The runtime context bridge is the v0.3 contract for how validated
`WorldSpec`-derived data may become optional runtime context in a later
implementation package.

The bridge is not a runtime migration, not a world generator, not an Agent
loop, not an API projection, and not a replacement for the current
`RuntimeEngine` module tree.

## Public Concepts

- `RuntimeContextBridge`: future boundary that derives runtime context from a
  validated loader result.
- `RuntimeContextInput`: accepted bridge input, consisting of a
  `LoadedWorldSpec` or reviewed equivalent from the WorldSpec loader.
- `RuntimeContext`: optional, inert context object that may be held by runtime
  code after a later reviewed implementation.
- `RuntimeContextSummary`: small diagnostic view of the context, intended for
  tests and review evidence, not product UI.
- `RuntimeContextBridgeError`: structured bridge failure for unsupported or
  invalid bridge input.

## Accepted Input

The bridge may accept only validated loader output:

- a successful `LoadedWorldSpec` from `docs/contracts/worldspec-loader-contract.md`.
- a reviewed equivalent produced by the 0.3.2 loader implementation.

The bridge must not accept raw dictionaries, raw JSON, unvalidated
`WorldSpec` payloads, API request bodies, fixture directories, generated-world
prompts, database records, or product-specific payloads.

Loader metadata may be carried only as neutral diagnostics. It must not drive
runtime behavior.

## Runtime Context Shape

A future `RuntimeContext` may expose only generic, derived fields:

- `worldspec_id`: the validated `WorldSpec.id`.
- `schema_version`: the validated `WorldSpec.schema_version`.
- `root_cell_id`: the validated root `WorldCell.id`.
- `root_cell_type`: the validated root `WorldCell.cell_type`.
- `source_type`: neutral loader source category.
- `source_label`: optional neutral diagnostic label.
- `metadata`: optional domain-neutral metadata copied only if reviewed by the
  implementation package.

The context must not include:

- raw, unbounded `WorldSpec` payloads in event payloads.
- generated runtime modules.
- concrete world logic.
- Agent state, memory, or self-continuity data.
- product UI or external validation internals.

## Relationship To RuntimeEngine

The current `RuntimeEngine` owns tick state:

- `tick_id`
- `world_time_seconds`
- `step_seconds`
- `updated_at`

The bridge contract does not change those fields or their semantics. If a
later implementation lets `RuntimeEngine` hold context, that storage must be
optional and inert when no context is supplied.

Runtime context must not, by itself:

- change `RuntimeEngine.step()`.
- change `world_time_seconds` advancement.
- change `tick.advanced` event creation.
- change module execution order.
- change archive callbacks.
- change params reads or writes.

## Relationship To World Modules

`WorldCell` is a schema structure, not a runtime module. A `WorldCell` must not
be treated as a `WorldModule` unless a later reviewed package defines and
tests an explicit mapping.

The default module tree remains the v0.1 scaffold:

- `root.heartbeat`
- `root.counter`

The bridge contract does not authorize replacing, deriving, or extending that
module tree from `WorldSpec` data.

## Relationship To Events, Params, Archive, And API

The bridge contract preserves existing behavior:

- `/runtime/state` and `/runtime/step` response envelopes remain compatible.
- `/world/events` and `/world/event-steps` pagination and grouping remain
  compatible.
- `tick.advanced`, `module.tick`, `module.counter`, and `module.aggregate`
  event shapes remain compatible.
- world params and params apply behavior remain compatible.
- archive snapshots and summaries remain compatible.
- frontend-facing response shapes remain compatible.
- legacy `backend/worldengine/` remains unwired.

A later implementation may expose context only through reviewed, additive
paths. It must not place raw `WorldSpec` data into event payloads or existing
API responses.

## Error Model

Bridge failures must use structured errors with:

- `code`: stable machine-readable code.
- `message`: concise diagnostic.
- `path`: optional bridge-input location.
- `source_type`: input source category when known.
- `source_label`: optional neutral source label.

Required error categories:

- `unsupported_input`: input is not a successful loader result or reviewed
  equivalent.
- `invalid_loaded_worldspec`: loader output is incomplete or internally
  inconsistent for bridge derivation.
- `context_derivation_error`: validated data could not be transformed into
  the reviewed context shape.

Bridge errors must not reinterpret schema validation failures. Schema
validation remains loader responsibility.

## Compatibility Evidence Required Before Implementation

Before any later bridge implementation changes runtime-facing code, it must
record current-session evidence for:

- `RuntimeEngine` tick and `world_time_seconds` behavior.
- `/runtime/state` and `/runtime/step`.
- API success and error envelope shape.
- `/world/events`.
- `/world/event-steps`.
- world params and params apply behavior.
- archive snapshot and summary behavior.
- optional `Event.refs` response compatibility.
- frontend-facing response shapes.
- legacy `backend/worldengine/` boundary.
- no raw `WorldSpec` event payloads or API response fields.
- no concrete demo-world or external validation-world anchors.

## Compatibility Constraints

- Runtime behavior must remain compatible unless a later reviewed package
  explicitly allows an additive change.
- API response shapes must remain compatible unless a later reviewed package
  explicitly allows an additive change.
- Event, archive, params, frontend-facing, fixture, migration, and legacy
  behavior must remain compatible.
- Schema changes are not authorized by this contract.
- Runtime context remains optional and inert until a later implementation
  proves otherwise.

## Forbidden Inferences

This contract does not authorize:

- bridge implementation in this documentation-only package.
- changes to `RuntimeEngine`.
- API route or response changes.
- event emission or event payload changes.
- archive writes.
- params application or params migration.
- persistence model changes.
- frontend changes.
- fixture or migration changes.
- concrete world logic.
- world generation.
- Agent-in-World loop, memory, self-continuity, projection, story generation,
  or NPC chat behavior.
- external fixture or validation repositories.

## Handoff

After this contract is reviewed, `0.3.4-runtime-context-bridge-implementation`
may implement a minimal optional runtime context bridge. That implementation
must follow this contract and provide current-session compatibility evidence
before closing.
