# EventRef Contract

Status: v0.2 event contract

## Purpose

`EventRef` is a domain-neutral, event-local structured reference. It lets an
event annotate its payload with references to generic objects without requiring
a resolver, registry lookup, causality engine, runtime state binding,
persistence table, memory link, projection behavior, or concrete application
domain.

`Event.refs` is an optional list of `EventRef` objects on `Event`. In v0.2,
refs are schema data carried by the event only. They do not prove that a
referenced object exists or that one event caused another runtime outcome.

## Schema

Source of truth: `backend/app/schemas/event.py`.

`EventRef` fields:

- `id`: required non-empty string. Identifies the referenced object within the
  producer's event-local context or a future public contract context.
- `kind`: required non-empty string. Names the generic reference category. In
  v0.2 it is descriptive schema data only; it does not select a runtime class,
  resolver, storage backend, rule system, memory system, projection target, or
  external fixture concept.
- `role`: optional string. Describes the relationship between the event and
  the referenced object. v0.2 does not define a role catalog or runtime
  semantics for role values.
- `metadata`: optional free-form object with default `{}`. Carries
  domain-neutral annotation data. v0.2 does not interpret metadata keys.

`Event.refs`:

- is optional on `Event`.
- defaults to an empty list when omitted.
- preserves each valid `EventRef` through `model_dump()` and
  `model_validate()` round trips.
- is carried through nested event containers such as `EventPage`, `EventStep`,
  and `EventStepPage` because those containers embed `Event` objects.

## Validation

`EventRef` must reject empty `id` values and empty `kind` values.

`EventRef` must accept omitted `role` and omitted `metadata`. Omitted
`metadata` validates as an empty object.

Current validation is provided by Pydantic model constraints. This contract
does not define uniqueness, referential integrity, cross-event resolution,
timeline ordering, runtime object existence, or metadata interpretation.

## Compatibility

The v0.2 contract is additive:

- Existing valid `Event` payloads without `refs` remain valid.
- Omitted `refs` validate as `[]`.
- Existing valid `Event` payloads with refs remain valid.
- Existing invalid empty `EventRef.id` and `EventRef.kind` values remain
  invalid.
- Existing payload behavior, event log behavior, runtime behavior, API
  response shapes, frontend behavior, fixture behavior, migrations, and legacy
  `backend/worldengine/` behavior remain unchanged.

Future packages may define resolver, causality, memory, projection, or runtime
binding semantics only through a reviewed iteration contract. Those future
packages must preserve existing generic payload compatibility unless an
iteration contract explicitly approves a breaking change.

## Non-Goals

`EventRef` and `Event.refs` do not implement:

- referential integrity resolution.
- timeline causality.
- runtime WorldCell binding.
- WorldSpec loading.
- event log persistence changes.
- API route or response shape changes.
- frontend projection behavior.
- agent action consequences.
- memory or self-continuity links.
- generation behavior.
- external fixture or validation-world semantics.
- domain-specific names, roles, locations, resources, story rules, seed data,
  or product-specific backend logic.
