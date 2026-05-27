# v0.3 ChatGPT Planning Seed

Status: planning seed

## Purpose

This seed establishes the v0.3 direction before any loader or bridge
implementation starts. v0.3 is the first version that moves WorldSpec toward
runtime, so it must begin with boundaries, compatibility evidence requirements,
and package sequencing.

## Current State From v0.2

v0.2 is the Recursive World Foundation. It established:

- project north star.
- product model.
- scope boundaries.
- EntityRef, WorldCell, and WorldSpec schema foundation.
- EventRef and optional Event.refs as additive event contract.
- generic schema smoke validation.
- external fixture and validation boundary.
- validation report template.
- legacy boundary and compatibility review.
- release-candidate and final closeout documentation.

v0.2 did not implement:

- WorldSpec loader.
- runtime bridge.
- RuntimeEngine migration to WorldCell.
- Agent-in-World loop.
- memory or self-continuity substrate.
- world generation.
- projection API.
- external fixture repository.
- external validation repository.
- concrete demo world runtime.
- product UI or game UI.

## v0.3 Goal

WorldSpec Loader and Runtime Bridge.

v0.3 should let WorldEngine load validated generic WorldSpec data and connect
that data to runtime context without breaking v0.1 runtime compatibility.

## v0.3 Boundaries

v0.3 may work on loader contracts, loader implementation, runtime context
bridge contracts, minimal bridge implementation, compatibility evidence,
external fixture runner contract readiness, evidence audit, release-candidate
docs, and final closeout docs.

v0.3 must not implement agent loop, memory, self-continuity, world generation,
projection API, product UI, game backend, concrete demo worlds, external
repositories, story generation, NPC chat, or self-awareness claims.

## Planned Packages

- `0.3.0-v0.3-planning-and-compatibility-baseline`
- `0.3.1-worldspec-loader-contract`
- `0.3.2-worldspec-loader-implementation`
- `0.3.3-runtime-context-bridge-contract`
- `0.3.4-runtime-context-bridge-implementation`
- `0.3.5-external-fixture-contract-readiness`
- `0.3.6-runtime-bridge-evidence-and-compatibility-audit`
- `0.3.7-v0.3-release-candidate-bundle`
- `0.3.8-v0.3-final-closeout`

## Required Compatibility Baseline

Before a future v0.3 package changes runtime, API, event, archive, params,
frontend-facing, or legacy-path behavior, it must produce current-session
compatibility evidence for:

- `RuntimeEngine` tick and `world_time_seconds` behavior.
- API envelope and error shape.
- `/runtime/step`.
- `/world/events`.
- `/world/event-steps`.
- world params and params apply behavior.
- archive snapshot and summary behavior.
- optional `Event.refs` response compatibility.
- frontend-facing response shapes.
- legacy `backend/worldengine/` boundary.

## External Automation Consumption Note

WorldEngine docs may be consumed by external automation controllers. The core
repository provides deterministic package specs, allowed changes, forbidden
changes, deliverables, verification expectations, and review templates. It
does not implement the controller, agent role assignment, retry loop, or
scheduler.

## No Concrete Demo World Rule

Do not add concrete demo world names, maps, characters, locations, resources,
story rules, seed data, UI selectors, private validation oracle details, or
external repository internals to WorldEngine core.

## Human / ChatGPT Review Expectation

0.3.0 should stop at `ready for human / ChatGPT review`. Later implementation
packages require reviewed package docs before code changes start.
