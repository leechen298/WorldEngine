# Intent

Chinese mirror: `intent.zh.md`.

## Problem / Purpose

WorldEngine currently exposes single-step runtime advancement. v0.9 needs
finite run controls so validation and later user-facing flows can advance a
world for a bounded number of ticks or bounded world-time duration without
creating infinite loops, unbounded provider usage, or ambiguous evidence.

## Why Now

`0.9.4` can evaluate bounded-run fidelity only when public bounded-run evidence
is supplied. `0.9.5` provides that bounded execution foundation before later
packages add natural-language direction, rule-linked event legality, Agent
continuity, checker fixtures, and full lifecycle validation.

## Relationship To Roadmap

This package advances the v0.9 LLM-backed lifecycle foundation by making
runtime execution finite, inspectable, and guard-controlled. It supports the
North Star by keeping world evolution event-backed and reviewable rather than
hidden behind unbounded loops.

## Non-goals

- Do not call live providers.
- Do not implement provider-backed world evolution.
- Do not implement rule-linked parameter evolution or event legality.
- Do not implement natural-language direction semantics.
- Do not implement Agent continuity or consolidation.
- Do not implement durable scheduling, background workers, queues, or
  deployment infrastructure.
- Do not implement frontend UI or Validation Client behavior.
- Do not run checker execution, generated-result creation, external validation,
  E2E, or autonomous validation.
- Do not modify `backend/worldengine/`.

## Expected Handoff

`0.9.5` should hand off bounded runtime controls and public run summaries to
`0.9.6`, where natural-language world direction can rely on finite run windows
instead of uncontrolled progression.

