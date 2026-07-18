# Architecture

Status: current architecture overview and v0.2 direction

## System Architecture Flowchart

The project-level architecture flowchart is maintained in
`docs/system-architecture-flowchart.md`. The source-only Mermaid copy is
`docs/system-architecture-flowchart.mmd`.

It summarizes the reasoned target relationship between World Generation, World
Runtime, Agent Runtime, shared event/evidence contracts, and external
projection consumers. It is an architecture planning artifact, not proof that
every node is implemented in the current codebase.

For a development-readable target loop that breaks the product into a small
overview plus detailed World Generation, World Runtime, and Agent Runtime
flows, see `docs/living-world-development-flow.md`. Chinese mirror:
`docs/living-world-development-flow.zh.md`.

## Current v0.1 State

WorldEngine v0.1 is an experimental monorepo scaffold:

- `backend/app/` contains the active FastAPI backend.
- `frontend/` contains the active Vue dashboard.
- `docs/` contains architecture and process documents.
- `backend/worldengine/` contains older pre-v0.1 code and is not the active
  implementation path.

The current active backend already has basic runtime primitives:

- `backend/app/core/` for clock, scheduler, event bus, and runtime engine.
- `backend/app/world/` for world service boundaries, params, archive, modules,
  validation, and storage placeholders.
- `backend/app/agent/` for agent service boundaries.
- `backend/app/schemas/` for shared Pydantic models.
- `backend/app/api/` for HTTP routes and app factory.

## v0.2 Architecture Direction

v0.2 is the Recursive World Foundation. It should establish schema and spec
language before runtime migration:

- `WorldCell` as a minimal recursive world unit.
- `WorldSpec` as the structured representation of a generated or loadable
  world.
- `EntityRef` as a shared reference shape for entities, agents, resources,
  rules, locations, and future memory links.
- additive `Event` fields for source, target, location, visibility,
  importance, and causal references.
- generic schema smoke validation that proves WorldSpec recursion, entity
  references, and round-trip behavior without storing external-world details.

## Runtime Boundary

v0.2 must not replace `RuntimeEngine` with WorldCell execution. Runtime bridging
belongs to later work after WorldSpec and event contracts are stable.

## Legacy Boundary

`backend/worldengine/` should be treated as legacy unless a later iteration
contract explicitly allows cleanup or migration. New features should target
`backend/app/`.

## Projection Boundary

Game, dashboard, and API projections should consume engine state and events.
They should not own core world rules, agent memory, or agent pseudo-self
formation.
