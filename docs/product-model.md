# Product Model

Status: authoritative product model

## WorldEngine Is

- A recursive world generation engine.
- A world runtime engine.
- An event timeline and memory substrate.
- An agent-in-world cognition substrate.
- A projection provider for dashboards, games, APIs, tools, and external
  clients.
- A system for inspecting and replaying world history, agent experience, and
  state change.

## WorldEngine Is Not

- Just a village game backend.
- Just an NPC chat system.
- Just a story generator.
- Just a game client.
- A claim of real consciousness.
- A repository for game-specific UI, art, sound, animation, packaging, or
  distribution logic.

## Core Domains

### World Generation

World generation turns user direction, templates, structured configuration, or
AI-assisted plans into valid world specs. Generated worlds must be structured,
validated, saved, run, inspected, and extended.

### World Runtime

World runtime advances time, evaluates rules, applies consequences, records
events, updates state, produces snapshots, and supports recovery.

### Agent Domain

Agents are not generic NPC chat wrappers. They have identity, state, needs,
goals, memory, relationships, action intent, feedback, reflection, and
self-narrative over time.

### Persistence

Persistence stores world specs, runtime state, events, snapshots, generation
metadata, agent state, memory records, and reviewable evidence.

### Projection

Projection exposes the running world to different consumers. A dashboard,
game, API client, or external system sees a projection of the same underlying
world model.

## First Product Surface

The first product surface may be a village-like electronic-pet world. It should
consume WorldEngine capabilities instead of owning world runtime or agent
self-continuity logic.
