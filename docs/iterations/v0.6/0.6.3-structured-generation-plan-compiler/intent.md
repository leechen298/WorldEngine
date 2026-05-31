# Intent

Status: review complete

## Why This Exists

`0.6.2` proved a deterministic template-to-`WorldSpec` baseline. v0.6 also
needs a structured plan path so later AI-assisted generation can hand the
engine normalized data instead of hidden prose side effects.

`0.6.3` creates that compiler boundary. It lets callers describe the intended
world structure as reviewed data, validates that data deterministically, and
compiles it into existing `WorldSpec` shape without adding API, frontend,
runtime, persistence, or provider behavior.

## Intended Outcome

After implementation and review:

- structured plans have explicit schema semantics.
- invalid plans return stable diagnostics with paths and source context.
- valid plans compile into loader-valid `WorldSpec` output.
- template generator behavior from `0.6.2` remains compatible.
- no concrete world content or external-provider behavior enters the core
  repository.

## Non-Goals

- Do not implement AI-assisted plan import; `0.6.4` owns that.
- Do not expose public API routes, dashboard UI, preview API, or regeneration.
- Do not modify runtime tick behavior, Agent/memory behavior, persistence,
  migrations, or external validation/projection readiness.
- Do not make a plan compiler execute prompts, scripts, or arbitrary rules.

## Handoff

`0.6.4-ai-assisted-generation-boundary-and-plan-import` receives reviewed
structured plan input semantics and compiler diagnostics.
