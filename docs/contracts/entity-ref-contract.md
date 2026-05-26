# EntityRef Contract

Status: v0.2 schema contract

## Purpose

`EntityRef` is a domain-neutral schema reference to an entity-like object. It
lets recursive world specifications point at entities without requiring a
runtime registry, loader, resolver, persistence table, or concrete application
domain.

## Schema

Source of truth: `backend/app/schemas/entity.py`.

Fields:

- `id`: required non-empty string. Identifies the referenced entity within the
  surrounding specification or future public contract context.
- `kind`: required non-empty string. Names the generic reference category. In
  v0.2 it is descriptive schema data only; it does not select a runtime class,
  resolver, storage backend, rule system, or external fixture concept.
- `label`: optional string. Provides display or human-review text and has no
  identity semantics.
- `metadata`: optional free-form object with default `{}`. Carries
  domain-neutral annotation data. v0.2 does not interpret metadata keys.

## Validation

`EntityRef` must reject empty `id` values and empty `kind` values.

`EntityRef` must accept omitted `label` and omitted `metadata`. Omitted
`metadata` validates as an empty object.

Current validation is provided by Pydantic model constraints. This contract
does not define a uniqueness rule, registry lookup, referential-integrity
check, or cross-document resolution step.

## Compatibility

The v0.2 contract is additive:

- Existing valid `EntityRef` payloads with non-empty `id` and `kind` remain
  valid.
- Existing invalid empty identity fields remain invalid.
- Additional metadata keys may be added by producers without changing
  WorldEngine runtime behavior in v0.2.

Future packages may narrow or interpret reference categories only through a
reviewed contract update. They must preserve existing generic payload
compatibility unless an iteration contract explicitly approves a breaking
change.

## Non-Goals

`EntityRef` does not implement:

- runtime entity loading.
- registry lookup.
- event causality.
- agent memory or self-continuity links.
- projection-specific identity.
- external fixture or validation-world semantics.
- domain-specific roles, locations, resources, story rules, or seed data.
