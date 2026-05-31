# Intent

Status: review complete

## Problem

v0.5 has reviewed memory and self-continuity semantics, but the engine still
has no generic substrate for recording working memory or event-linked
episodes. Without a minimal substrate, `0.5.3` cannot safely provide a bounded
read-only memory context to the Agent Loop.

The implementation must be small because the surrounding self-continuity
features are still contract-only. This package should prove records can be
created, bounded, isolated, and inspected without changing runtime or action
semantics.

## Goal

After this package, backend code has:

- additive schema models for working memory and episodic memory.
- an in-memory store for generic agent/world-scoped memory records.
- tests showing bounded working-memory retrieval, episodic event linkage,
  provenance semantics, and copy isolation.
- compatibility evidence that v0.4 Agent Loop behavior remains unchanged.

## Non-goals

- Do not add API routes or public runtime endpoints.
- Do not connect memory to `PerceptionBuilder` or `AgentLoopService`.
- Do not change `LoopStepRequest`, `ActionIntent`, `ActionResult`, action
  result adapter behavior, accepted action types, or params patch semantics.
- Do not add durable persistence, migrations, vector search, summarization,
  relationship state behavior, reflection automation, self-summary generation,
  personality drift action modifiers, frontend behavior, fixtures, or concrete
  world content.

## Why Now

`0.5.1` defined the public concept and schema semantics. The smallest safe code
slice is working and episodic memory only, without loop integration. That
creates a tested substrate for `0.5.3` to consume read-only.

## Roadmap Relationship

This package is the first implementation-bearing slice of the v0.5 Memory and
Self-Continuity Substrate roadmap goal. It implements only the working-memory
and episodic-memory portions that `v0.5-plan.md` identifies as the first safe
implementation candidates.

It does not implement v0.6 world generation, v0.7 external validation
readiness, v0.8 projection application readiness, or later memory behavior
such as relationship updates, self-summary generation, reflection automation,
or personality drift action modifiers.

## North Star Alignment

This package supports the north star by adding inspectable records for agent
memory and lived experience while keeping pseudo-self behavior explicit,
bounded, and reviewable. It does not claim consciousness and does not narrow
WorldEngine into a game-specific or application-specific backend.

## Expected Handoff

This package hands off to `0.5.3-memory-context-loop-integration` with a
generic in-memory substrate that can be read by perception code without
changing action semantics.
