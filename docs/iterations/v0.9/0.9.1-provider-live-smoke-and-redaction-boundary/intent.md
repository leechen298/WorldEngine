# Intent

## Problem / Purpose

Current `GET /manifest` can report public provider environment readiness, but
it does not prove that WorldEngine can make a live provider call. v0.9 needs a
minimal, safe, WorldEngine-owned smoke path before later packages use provider
behavior for LLM-backed world creation.

This package creates the provider boundary and redaction evidence needed by
later LLM-backed validation layers.

## Why Now

`0.9.0` completed the v0.9 handoff baseline and selected this package as the
next route. `0.9.2` cannot honestly implement LLM-backed world generation
until provider calls have a reviewed WorldEngine-owned entrypoint, safe
unconfigured behavior, and redacted evidence semantics.

## Relationship To Roadmap

This package is v0.9 layer 1: provider live smoke. It supports the north star
by enabling AI-assisted world generation later, while keeping provider
ownership in the core engine and preventing the external Validation Client
from becoming the LLM caller or evaluator.

## Non-Goals

- Do not implement LLM-backed world creation.
- Do not implement generated world rules, worldview fidelity, runtime run
  controls, user direction, event legality, Agent continuity, consolidation,
  narrative projection, diagnostic dialogue, or Validation Client handoff.
- Do not execute provider-backed lifecycle validation.
- Do not build a product UI or game client.
- Do not add concrete world content.
- Do not store or expose raw provider inputs or outputs.

## Expected Handoff

`0.9.2-llm-worldview-ingestion-and-generation-contract` receives:

- a WorldEngine-owned provider smoke call path.
- redacted provider live summary semantics.
- failure taxonomy for live provider availability.
- evidence that `/manifest` readiness and live provider smoke are distinct.
- provider redaction tests and unresolved provider blockers, if any.
