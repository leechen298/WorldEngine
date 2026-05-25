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

They are not:

- the purpose of WorldEngine.
- a reason to make the engine demo-specific.
- a reason to replace recursive world architecture with application-only state.

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
