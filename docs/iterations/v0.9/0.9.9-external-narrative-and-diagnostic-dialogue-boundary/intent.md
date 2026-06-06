# Intent

Chinese mirror: `intent.zh.md`.

## Problem

WorldEngine now has public Agent continuity and consolidation evidence, but
future validators and clients still need readable projection surfaces:

- narrative projection that summarizes the world as external prose or a public
  read model.
- diagnostic Agent dialogue that lets a user or validator ask about an Agent
  without making that exchange part of the world timeline.

Both surfaces are useful for inspection, but they are dangerous if they are
confused with canonical world state. A narrative paragraph must not become an
event merely because it exists, and diagnostic questions must not be written
into Agent memory by default.

## Purpose

This package creates a reviewed boundary for projection and diagnostics before
any LLM-backed checker or Validation Client handoff depends on those outputs.

## Desired Outcome

After implementation, WorldEngine should be able to expose public artifacts
that say:

- which canonical public evidence was used.
- whether the artifact is external to canonical world state.
- whether canonical events, snapshots, Agent memory, or Agent continuity were
  mutated.
- whether redaction passed.

The package must not claim narrative quality, in-world chat, human-like Agent
interiority, product readiness, checker PASS, or full v0.9 validation PASS.

## Non-Goals

- No frontend chat UI.
- No product-specific narrative/game content.
- No live provider narrative generation.
- No diagnostic-to-memory bridge.
- No checker fixture implementation.
- No Validation Client implementation.
