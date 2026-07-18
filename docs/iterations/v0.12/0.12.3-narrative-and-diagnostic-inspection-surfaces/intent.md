# Intent

Chinese mirror: `intent.zh.md`.

## Problem

v0.12 now has public session Agent state, runtime steps, memory summaries, and
rest consolidation evidence. Humans and validation tools still need a readable
inspection layer that summarizes those public artifacts without becoming a
world mutation path.

Earlier external projection work already established a boundary for
world-level narrative projection and diagnostic dialogue evaluation. The MVP
needs a session-oriented version of that boundary so validators can ask:

- what happened in this session and tick range?
- which branch or Agent evidence was used?
- did the projection stay read-only?
- did diagnostic inspection remain out-of-world and outside Agent memory?

## User Value

The MVP validator can inspect public behavior through readable narrative and
diagnostic summaries instead of scanning raw event lists only.

## Engineering Value

This package connects v0.11 rule/evolution evidence and v0.12 Agent evidence
to future Validation Client evidence handoff without embedding client logic in
WorldEngine.

## Non-Goals

- No story generation as canonical world evolution.
- No diagnostic chat as in-world dialogue.
- No personality, skill, relationship, inventory, injury, death, or memory
  mutation from inspection.
- No provider live call.
- No external Validation Client implementation.
- No full MVP checker/closeout.
