# Intent

## Problem

The current Event schema carries flexible event-specific data through
`payload`, but it does not provide a lightweight structured place to name the
world, cell, entity, agent, resource, memory record, or external projection
that an event refers to.

Future recursive-world, agent, memory, and projection work needs a way to
attach structured pointers to events without forcing runtime coupling now.

## Intended Outcome

Add a minimal, additive EventRef layer to the Event contract after this gate is
reviewed and approved:

- `EventRef` describes an event-local pointer.
- `Event.refs` defaults to an empty list.
- Existing Event construction and API response compatibility remain preserved.
- `payload` remains unchanged and fully backward compatible.

## Why EventRef Is Separate From EntityRef

`EntityRef` belongs to WorldSpec and WorldCell structure. It describes
schema-level world contents and future loadable world structure.

`EventRef` belongs to an individual event. It can point at future world specs,
world cells, entities, agents, resources, memory records, or external
projections without importing or resolving those concepts now.

Keeping the concepts separate prevents the event schema from becoming coupled
to recursive-world schemas before the runtime bridge exists.

## Non-Goals

- Do not implement code in this documentation stage.
- Do not change Event `payload` semantics.
- Do not require `refs` for existing events.
- Do not connect EventRef to WorldCell runtime.
- Do not resolve refs or enforce referential integrity.
- Do not change runtime engine behavior, event log storage, API routes,
  modules, frontend, or `backend/worldengine/`.
- Do not implement WorldSpec loader, concrete demo runtime, agent memory,
  pseudo-self, or 0.2.4.

## North Star Fit

The Event Contract extension supports the north star by making future world,
agent, memory, and projection evidence easier to structure. It does not turn
WorldEngine into an application-specific backend and does not move v0.2 beyond its
recursive-world foundation boundary.
