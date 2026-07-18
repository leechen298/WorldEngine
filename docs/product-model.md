# Product Model

Status: authoritative product model

## WorldEngine Is

- A recursive world generation engine.
- A world runtime engine.
- An event timeline and memory substrate.
- An agent-in-world cognition substrate.
- A WorldEngine-owned LLM-backed generation and reasoning substrate.
- A projection provider for dashboards, games, APIs, tools, and external
  clients.
- A system for inspecting and replaying world history, agent experience, and
  state change.

## WorldEngine Is Not

- A demo-specific or application-specific backend.
- Just an NPC chat system.
- Just a story generator.
- Just a provider proxy or prompt runner.
- Just a game client.
- A claim of real consciousness.
- A repository for game-specific UI, art, sound, animation, packaging, or
  distribution logic.

## Core Domains

### World Generation

World generation turns user direction, templates, structured configuration, or
AI-assisted plans into valid world specs. Generated worlds must be structured,
validated, saved, run, inspected, and extended.

When generation uses an LLM, WorldEngine owns the provider call and must
convert model output into public, structured, validated world data. Raw prompts
and raw responses are not product surfaces or validation evidence.

### World Runtime

World runtime advances time, evaluates rules, applies consequences, records
events, updates state, produces snapshots, and supports recovery.

Runtime execution should be bounded and inspectable. Consumers may ask the
engine to run one tick, run multiple ticks, run for a world-time duration,
pause, resume, or continue, but the engine remains responsible for state,
rules, event legality, snapshots, and run evidence.

### Direction And Player Boundary

User direction is an external input to WorldEngine, not a direct mutation of
the canonical world. In the MVP track, the user or player is not an in-world
entity unless a later reviewed package creates that bridge.

Direction may influence world-level pressure, environment trends, candidate
events, probabilities, or constraints. It must not directly assign final facts
such as death, injury, inventory changes, private memory changes, or direct
event outcomes. WorldEngine must decide outcomes through public rules,
current state, probability, and event legality.

### Agent Domain

Agents are not generic NPC chat wrappers. They have identity, state, needs,
goals, memory, relationships, action intent, feedback, reflection, and
self-narrative over time.

Agent cognition is not a mandatory per-tick mutation loop. Short-term memory,
long-term memory, personality, skills, intent, and self-narrative should have
explicit public summaries and may consolidate through sleep, rest, or
low-activity phases that can span multiple ticks.

Unless a document explicitly says "external validation agent," the term Agent
means an in-world Agent. External validation agents such as Codex or OpenClaw
operate clients and review evidence from outside the world; they are not
canonical world entities.

### Persistence

Persistence stores world specs, runtime state, events, snapshots, generation
metadata, agent state, memory records, and reviewable evidence.

Persistence may store public summaries, consolidation records, projections,
and redacted evidence. It must not turn raw provider traces, raw thought,
private memory payloads, or diagnostic conversations into canonical evidence
unless a reviewed contract explicitly allows a redacted public form.

### Projection

Projection exposes the running world to different consumers. A dashboard,
game, API client, or external system sees a projection of the same underlying
world model.

Novel-style narrative output, replay views, and out-of-world diagnostic Agent
conversations are projection or inspection surfaces by default. They can help
humans or validators understand the run, but they do not mutate the canonical
world timeline or Agent memory unless a future reviewed bridge explicitly
changes that boundary.

A user-facing narrative projection may summarize a session, tick range,
timeline branch, or Agent-focused public history as readable prose. It must be
derived from public events, diffs, snapshots, Agent public summaries, and
provenance fields.

A user-facing diagnostic conversation may let a human ask why the world
changed, what public state an Agent appears to have, or whether the run still
matches the worldview. It is an out-of-world inspection transcript. It must
not become in-world dialogue, player participation, Agent memory, or a hidden
control channel. If the user wants to affect future world evolution, that
request must go through the direction queue and rule-bound event path instead.

## External Product Surfaces

Product surfaces should live as public WorldEngine consumers. They consume
schemas, APIs, events, projections, and exported contracts instead of owning
world runtime or agent self-continuity logic inside the core repository.
