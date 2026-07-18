# Intent

Chinese mirror: `intent.zh.md`.

## Problem

WorldEngine has accumulated framework-shaped capabilities and historical MVP
claims, but the project still lacks one current, independently verifiable run
that proves world generation, world runtime, Agent runtime, operator
intervention, projection, and evidence belong to the same canonical history.

Designing from current implementation risks preserving the wrong boundaries.
This package instead starts from the approved living-world flow and uses
existing code only as optional implementation inventory after the contract is
fixed.

## Goal

Create the WorldEngine-side half of the smallest complete v0.13 anchor:

```text
structured brief + seed
-> deterministic runnable package + hash
-> session boot from that exact hash
-> exact lockstep steps
-> Agent causal loop
-> accepted/rejected intervention judgment
-> event/diff/snapshot/projection/evidence
-> administration console over the same APIs
```

## Why Now

The project needs a stable acceptance target before adding more world quality,
Agent depth, or game-engine presentation. A deterministic path removes live
provider, network, and external-client blockers while preserving every core
link that the later Godot run must exercise.

## Relationship To Roadmap

v0.13 follows the historical v0.10-v0.12 `PARTIAL` track with a fresh anchor
contract. It does not reopen those versions or reuse their evidence as current
proof. It creates the stable public surface consumed by the external
`0.13.1` Godot/checker package.

## Non-goals

- No live LLM generation or Agent decision dependency.
- No concrete external scenario in this repository.
- No Godot project or external repository modification.
- No per-frame synchronization or WebSocket requirement.
- No production persistence, recovery execution, branching, or deployment.
- No multi-Agent society, recursive worlds, full memory consolidation,
  personality drift, narrative projection, or diagnostic conversation.
- No polished application or game-release claim.

## Expected Handoff

Publish a stable manifest, schemas, API examples, and evidence-bundle contract
that an external Godot executor and independent checker can consume without
reading WorldEngine code or storage.
