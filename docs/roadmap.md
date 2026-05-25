# Roadmap

Status: planning guide

This roadmap defines delivery direction. Each version still requires scoped
iteration packages before implementation.

## v0.1 - Runtime Scaffold

Status: current baseline

Goal: establish the monorepo, FastAPI backend, Vue dashboard, runtime tick,
event log, params, archive, and basic API envelope.

## v0.2 - Recursive World Foundation

Goal: establish the documentation governance, north star, recursive world
schema/spec language, additive event contract, generic schema smoke
validation, external fixture boundary, and legacy boundary.

Non-goal: do not migrate RuntimeEngine to WorldCell or build demo-specific
runtime.

Concrete external worlds must not appear inside the core repository as
fixtures, loader inputs, projection targets, or acceptance targets. They may
consume WorldEngine only through public APIs, CLI contracts, schemas, exported
contracts, and redacted validation reports.

### v0.2.5 - Core Boundary Cleanup and Roadmap Reset

Goal: remove concrete external-world anchors from active core docs, fixtures,
and tests, and reset the later roadmap around generic engine consumers.

### v0.2.6 - Generic Recursive World Foundation Closeout

Goal: close v0.2 around generic WorldCell, WorldSpec, EntityRef, EventRef,
schema smoke validation, and external consumer boundaries.

## v0.3 - WorldSpec Loader and Runtime Bridge

Goal: load validated generic WorldSpec data into runtime context without
losing v0.1 runtime compatibility.

## v0.3.5 - External Fixture Contract Readiness

Goal: define how external fixture runners invoke the core repository through
public contracts without creating those repositories inside WorldEngine.

## v0.4 - Agent-in-World Minimal Loop

Goal: let agents perceive world events, produce action intents, receive action
results, and affect world state through a minimal validated loop.

## v0.5 - Memory and Self-Continuity Substrate

Goal: introduce working memory, episodic memory, relationship state,
self-summary, reflection records, and personality drift signals that can affect
future action.

## v0.6 - World Generation v1

Goal: generate runnable WorldSpec data from templates and structured
AI-assisted generation with validation, metadata, preview, and regeneration
support.

## v0.7 - External Validation Readiness / Projection Consumer Readiness

Goal: make WorldEngine ready for external validation suites and projection
consumers through public contracts, redacted reports, and compatibility
evidence.

## v0.8 - First External Projection Application Readiness

Goal: prepare the engine interfaces, evidence, and projection contracts needed
for a first external product application to consume WorldEngine without moving
application-specific behavior into the core repository.
