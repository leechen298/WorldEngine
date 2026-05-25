# Intent

## Problem

WorldEngine's core mission is a recursive world generation and runtime engine
with event, agent, memory, feedback, projection, and pseudo-self continuity
substrates. It is not a specific village Demo, electronic-pet Demo, or game
backend.

Previous v0.2 documents and implementation artifacts used Tiny Village,
village-like game, reference village world, and related concrete terms as
fixture or validation anchors. Those anchors were meant to make schema work
concrete, but they now create a direction risk:

- Codex, Claude, or other coding agents may infer that the core repository is
  supposed to know Demo world details.
- Future implementation may drift from generic recursive world infrastructure
  into a game-specific backend.
- Tests and fixtures may begin shaping engine contracts around concrete
  locations, roles, resources, or narrative rules.
- External fixture worlds may accidentally become upstream design drivers
  instead of downstream consumers of the public WorldEngine contracts.

## Goal

0.2.5 prepares a boundary cleanup that removes concrete Demo world anchors from
active WorldEngine planning, fixture data, and fixture tests while preserving
the generic recursive world schema and event foundation already established in
v0.2.

After implementation, the core repository should keep only:

- generic schema contracts.
- generic runtime contracts.
- generic event contracts.
- generic agent-in-world contracts.
- generic memory and self-continuity contracts.
- generic projection contracts.
- generic smoke tests.
- redacted validation report formats.

Future fixture worlds and validation worlds should live outside the core
repository and consume WorldEngine through public interfaces.

## Non-goals

- Do not create an external fixture repository.
- Do not create an external validation repository.
- Do not implement a WorldSpec loader.
- Do not implement a runtime bridge.
- Do not implement an Agent loop.
- Do not implement memory or self-continuity.
- Do not implement world generation.
- Do not implement or replace the frontend dashboard.
- Do not modify v0.1 runtime behavior.
- Do not introduce a different concrete Demo world to replace the old one.

## Why Now

v0.2 has already established generic recursive-world schema language and event
references. That is the right time to correct the project direction before v0.3
loader or runtime bridge work begins. If the concrete Demo anchors remain in
active docs and tests, later code may use them as architecture facts.

0.2.5 should make the boundary explicit before loader, runtime bridge,
agent-in-world, memory, generation, validation, or projection milestones build
on top of the v0.2 foundation.

## North Star Alignment

This cleanup keeps WorldEngine aligned with its north star by treating concrete
worlds as external consumers, not core identity. The core repository remains a
generic substrate for recursive worlds, event evidence, agents living in
worlds, memory continuity, self-continuity, and projections.

The cleanup preserves the schema vocabulary required for future worlds while
removing the implication that the first understandable validation surface is
part of the core engine.
