# Intent

Status: review complete

## Problem

`0.5.2` added a generic in-memory substrate for working and episodic memory,
but the Agent Loop still cannot perceive that memory. v0.5 needs a bounded,
read-only bridge from substrate records into perception before later packages
can safely reason about relationship, reflection, self-summary, or drift
contracts.

The bridge is risky because perception is part of the loop response. This
package must keep the change additive and avoid changing action semantics.

## Goal

After this package, `PerceptionFrame` can include bounded memory context built
from working and episodic memory records. The loop can expose that context in
the perception part of its response, while action intent/result behavior
remains unchanged.

## Non-goals

- Do not add public memory APIs.
- Do not add loop request fields for memory selection.
- Do not write memory from a loop step.
- Do not modify `ActionIntent`, `ActionResult`, action adapter semantics,
  accepted action types, or params patch validation.
- Do not add persistence, migrations, vector retrieval, summarization,
  relationship behavior, reflection automation, self-summary generation,
  personality drift action modifiers, frontend behavior, fixtures, or concrete
  world content.

## Why Now

The memory substrate exists and passed `0.5.2` review. v0.5 can now add the
smallest read-only consumer path: perception context. This enables later
contract follow-up without making memory change action behavior.

## Roadmap Relationship

This package is the v0.5 step that connects the memory substrate to the
Agent-in-World loop. It does not implement v0.6 generation, v0.7 external
validation readiness, v0.8 projection readiness, or higher-risk self-continuity
behaviors.

## North Star Alignment

The north star requires agents to perceive and act with continuity over lived
experience. This package supports that by exposing bounded, inspectable memory
context to perception while keeping action behavior explicit and testable.

## Expected Handoff

This package hands off to
`0.5.4-reflection-relationship-and-drift-contract-followup` with read-only
memory context integrated and tested.
