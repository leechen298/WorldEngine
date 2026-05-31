# Intent

Status: review complete

## Problem

`0.6.5` exposes a generation preview API with bounded metadata. v0.6 still
needs a reviewed way to regenerate from a generation input and to check whether
a generated `WorldSpec` can pass the existing loader and runtime-context bridge
before any later dashboard or runtime-facing work depends on it.

## Goals

- Add bounded regeneration semantics with deterministic lineage metadata.
- Add runtime-readiness checks using `load_worldspec`, `build_runtime_context`,
  and `summarize_runtime_context`.
- Keep readiness checks inert: they must not mutate the live runtime or change
  `RuntimeEngine.step`.
- Expose regeneration/readiness through the existing generation API envelope.
- Preserve existing generation preview, loader, runtime-context, runtime-step,
  event, Agent/memory, and frontend behavior.

## Non-Goals

- No full runtime migration.
- No live runtime mutation by default.
- No durable regeneration history, persistence, repositories, or migrations.
- No dashboard UI or E2E workflow.
- No external validation readiness, projection readiness, product readiness,
  release readiness, generation-quality claim, or autonomous validation claim.
- No live AI provider behavior.

## North Star Alignment

This package advances runnable world generation by proving generated specs can
be loaded and summarized into runtime context. It keeps the proof bounded and
inspectable instead of silently promoting generated worlds into the live
runtime.

## Handoff

When complete, `0.6.7-dashboard-generation-preview-and-e2e-smoke` receives
stable backend/API surfaces for dashboard preview work.
