# Intent

Status: ready for review

## Purpose

v0.3 is the first version that moves WorldEngine from the v0.2 schema
foundation toward loader and bridge work. Before implementing a WorldSpec
loader or runtime bridge, the project needs a clear compatibility baseline and
package sequence.

## Context

v0.2 established Recursive World Foundation. It defined the north star,
product model, scope boundaries, EntityRef, WorldCell, WorldSpec, EventRef,
optional Event.refs, generic schema smoke validation, external fixture
boundary, validation report template, legacy boundary, compatibility review,
release-candidate evidence, and final closeout docs.

v0.2 intentionally did not implement WorldSpec loading, runtime bridge,
RuntimeEngine migration to WorldCell, Agent-in-World loop, memory,
self-continuity, generation, projection API, external fixture repositories,
external validation repositories, concrete demo runtime, product UI, or game
UI.

## Compatibility Baseline Intent

The accepted v0.2 P3 handoff becomes a hard v0.3 gate: before future packages
modify runtime, API, event, archive, params, frontend-facing, or legacy-path
behavior, they must first provide current-session compatibility evidence for
the existing behavior.

## Package Role

0.3.0 is a planning and baseline package. It is not a development package. It
creates the v0.3 iteration structure, records scope, and prepares future
packages to advance one reviewed step at a time.
