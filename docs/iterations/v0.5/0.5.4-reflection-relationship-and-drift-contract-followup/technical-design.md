# Technical Design

Status: review complete

## Design Type

Documentation-only contract refinement.

No runtime, schema, service, API, frontend, migration, fixture, or test
implementation is authorized in `0.5.4`.

## Concept Boundaries

The four concepts are kept separate to avoid hidden behavior coupling:

- relationship state describes agent-to-target relationship facts.
- self-summary describes agent continuity state in an auditable summary.
- reflection record captures a review or self-assessment event.
- personality drift signal captures a possible tendency change signal.

They may share evidence-reference patterns in a later schema package, but this
package does not select concrete Python model names, modules, storage, routes,
or persistence behavior.

## Future Schema Shape Guidance

A future schema package should keep these design constraints:

- use generic identifiers and references, not world-specific entities.
- include evidence references, source, timestamps, and review status where
  applicable.
- make supersession/versioning explicit for summaries and mutable-looking
  continuity state.
- keep proposed updates separate from applied state.
- model drift as reviewable signal data, not behavior.

## Loop Boundary

`0.5.3` added bounded read-only memory context to perception. `0.5.4` does not
extend that context with relationship, self-summary, reflection, or drift data.

No part of this package changes:

- loop request fields.
- `ActionIntent`.
- `ActionResult`.
- action adapter behavior.
- params patch semantics.
- memory ranking or selection.

## Evidence Boundary

`0.5.4` produces documentation evidence only. Current code evidence from
`0.5.2` and `0.5.3` remains valid for those packages and will be included in
the `0.5.5` audit, but it is not expanded into new behavior here.

## Future Implementation Notes

If a later package implements schemas, likely surfaces are additive schema
models under `backend/app/schemas/` and focused tests under `backend/app/tests/`.
That package must make its own technical design, run TDD, and update
compatibility evidence for any touched loop/API surface.
