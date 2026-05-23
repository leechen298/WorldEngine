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
schema/spec language, additive event contract, reference WorldSpec fixture, and
legacy boundary.

Non-goal: do not migrate RuntimeEngine to WorldCell or build village runtime.

Tiny Village may appear before v0.7 as a reference fixture, schema validation
target, loader test input, or projection acceptance target. It must not become
game-specific runtime logic inside WorldEngine before the roadmap explicitly
allows that work.

## v0.3 - WorldSpec Loader and Runtime Bridge

Goal: load validated WorldSpec data into runtime context without losing v0.1
runtime compatibility.

## v0.4 - Agent-in-World Minimal Loop

Goal: let agents perceive world events, produce action intents, receive action
results, and affect world state through a minimal validated loop.

## v0.5 - Memory and Self Continuity

Goal: introduce working memory, episodic memory, relationship state,
self-summary, reflection records, and personality drift signals that can affect
future action.

## v0.6 - World Generation v1

Goal: generate runnable WorldSpec data from templates and structured
AI-assisted generation with validation, metadata, preview, and regeneration
support.

## v0.7 - Reference Village World

Goal: build the first complete reference world that validates world generation,
world runtime, recursive structure, agent continuity, and player projection
without turning the engine into game-specific backend code.

## v0.8 - First Game Surface

Goal: start a user-facing game surface that consumes WorldEngine APIs and
projections while leaving world runtime and agent self-continuity inside the
engine.
