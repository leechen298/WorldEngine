# Project North Star

Status: authoritative project direction

## Core Mission

WorldEngine is a recursive world generation and runtime engine. It is also the
runtime substrate for agents that form continuity, memory, feedback-shaped
behavior, and pseudo-self through lived experience inside worlds.

WorldEngine exists to support five long-term capabilities:

1. Generate worlds from structured inputs, templates, and AI-assisted
   generation.
2. Run worlds over time as stateful systems with events, rules, timelines,
   resources, history, snapshots, and recovery.
3. Support recursive world structures where worlds can contain child worlds,
   projected worlds, subjective worlds, and specialized runtime cells.
4. Let agents live in worlds, perceive events, act, accumulate memory, update
   goals, and change through feedback.
5. Let agents develop a sustained pseudo-self: identity continuity,
   self-narrative, relationship history, personality drift, and decision
   patterns shaped by prior experience.

## LLM-backed Execution Direction

AI-assisted generation and reasoning are engine-owned capabilities. External
clients may provide user input, display projections, and export evidence, but
WorldEngine owns provider configuration, provider calls, redaction boundaries,
structured outputs, and the public evidence needed to validate those outputs.

LLM output is not accepted as hidden truth. It must be transformed into public,
structured, inspectable world models, rules, events, summaries, projections, or
validation artifacts that the runtime and checker can reason about.

## Agent Continuity Direction

Agent continuity should be designed as a cognition substrate, not as a
per-tick status updater or chat wrapper. Memory, personality, skill, intent,
and self-narrative should evolve through explicit state, experience, feedback,
and consolidation processes.

Longer-term Agent design may use sleep, rest, or low-activity phases where
working memory, long-term memory, personality summaries, and skill summaries
settle across multiple ticks. WorldEngine must not assume that meaningful
memory, personality, or skill changes happen on every tick.

## What This Does Not Claim

WorldEngine does not claim real consciousness. "Pseudo-self" means an
engineered continuity model whose behavior can be inspected, tested, and
improved. It is a product and engineering target, not a metaphysical claim.

## External Projection Applications

External projection applications are consumers and validation surfaces for
WorldEngine. They exercise public engine contracts without becoming part of
the core repository.

They are:

- public consumers of the engine.
- external validation consumers for runtime, events, memory, and agent
  continuity.
- places where product-specific UI and application behavior may live outside
  the core repository.
- narrative, replay, diagnostic, and inspection surfaces that may help humans
  understand a running world without becoming the world itself.

They are not:

- the purpose of WorldEngine.
- a reason to make the engine demo-specific.
- a reason to replace recursive world architecture with application-only state.
- a place to own provider behavior, Agent private memory, canonical world
  mutation, or authoritative evaluation.

Narrative projections and out-of-world diagnostic conversations can be useful
external views. By default, they must read from public world evidence and must
not mutate canonical world state, world timelines, or Agent memory.

## Architecture Anchor

World is a recursive runtime unit. A world may contain child worlds, locations,
agents, rules, resources, timelines, event streams, projection config, and
external connectors. Later milestones may model an agent's subjective memory or
self-narrative space as specialized world cells, but v0.2 only establishes the
foundation for that direction.

## Decision Rule

When a proposed feature conflicts with this document, the proposal must change
or be rejected. If the north star itself needs to change, update this document
first and record the decision in an iteration package.
