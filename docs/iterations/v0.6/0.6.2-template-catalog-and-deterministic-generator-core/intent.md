# Intent

Status: review complete

## Problem / Purpose

v0.6 has reviewed generation concepts from `0.6.1`, but no executable
non-AI generator baseline. The next safe step is a small deterministic core
that can turn reviewed generic templates into valid current `WorldSpec` data
without API, frontend, persistence, AI-provider, or runtime-step changes.

## Why Now

`CURRENT_STATE.md` points to this package after `0.6.1` review complete. The
v0.6 sequence requires deterministic template generation before structured
plan compilation and AI-assisted plan import.

## Relationship To Roadmap

This package is the first implementation-bearing slice of v0.6 World
Generation v1. It implements a generic, inspectable baseline generator while
preserving the v0.3 loader/runtime-context bridge, v0.4 Agent Loop, and v0.5
memory substrate.

## Non-goals

- Do not implement structured generation plan compilation; `0.6.3` owns that.
- Do not implement AI-assisted plan import; `0.6.4` owns that.
- Do not expose backend API routes, metadata/preview API, regeneration,
  dashboard UI, E2E smoke, external validation readiness, or projection
  readiness.
- Do not add durable persistence, migrations, live external AI-provider calls,
  generated seed files, or concrete world content.
- Do not modify existing `WorldSpec`, `WorldCell`, `EntityRef`, loader,
  runtime-context, runtime-step, Agent, memory, API, params, archive, frontend,
  fixture, or `backend/worldengine/` behavior.

## Expected Handoff

After implementation and review, `0.6.3` receives:

- generic generation schemas.
- deterministic template catalog semantics.
- deterministic template-to-`WorldSpec` generation logic.
- focused evidence that generated output is loader-valid and generic.
- compatibility evidence for adjacent schema, loader, and runtime-context
  surfaces.
