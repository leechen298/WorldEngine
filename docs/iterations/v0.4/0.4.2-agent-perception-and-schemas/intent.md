# Intent

## Problem / Purpose

Implement read-only perception and additive schemas only.

The package goal is: Add generic Agent-in-World schema models and a bounded perception builder that reads runtime state, recent events, world params, and optional runtime-context summary without mutating state.

## Why Now

v0.3 final closeout is complete and the post-closeout campaign passed with P3 handoffs. That evidence allows v0.4 planning to start, but it does not authorize implementation. This package establishes or consumes the next reviewed gate in the v0.4 sequence.

## Relationship To Roadmap

v0.4 is the Agent-in-World Minimal Loop milestone. It sits after the v0.3 WorldSpec loader/runtime-context bridge and before v0.5 memory and self-continuity. This package must keep those later capabilities out of scope.

## Non-goals

- Do not add memory, episodic memory, relationship state, self-summary, reflection, or personality drift; v0.5 owns that scope.
- Do not add world generation; v0.6 owns that scope.
- Do not add external validation runner readiness or report automation; v0.7 owns that scope.
- Do not add projection application readiness; v0.8 owns that scope.
- Do not add concrete world names, maps, characters, locations, resources, story rules, seed data, UI-specific app behavior, or private validation oracle details.
- Do not add new runtime features under `backend/worldengine/`.

## Expected Handoff

The next package in `CAMPAIGN_PLAN.md` receives only reviewed evidence and explicit handoff notes.
