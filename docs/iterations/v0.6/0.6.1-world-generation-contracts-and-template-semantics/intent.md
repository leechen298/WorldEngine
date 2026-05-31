# Intent

Status: review complete

## Problem / Purpose

v0.6 adds the first world generation capability, but generated worlds can only
be safe engine inputs if their contracts are explicit before code exists.
Without a reviewed contract, later implementation could accidentally:

- store concrete demo-world content in the core repository.
- treat AI output as an unvalidated hidden side effect.
- produce data that does not pass the existing `WorldSpec` loader.
- imply runtime, API, quality, validation, or release claims that current
  evidence does not support.

This package defines those boundaries before implementation starts.

## Why Now

`0.6.0` completed the v0.6 campaign baseline and handed off to this active
child. `CURRENT_STATE.md` now routes the goal to
`0.6.1-world-generation-contracts-and-template-semantics` with implementation
authorization closed. The next package, `0.6.2`, cannot safely implement a
deterministic generator core until the public concepts and template semantics
are reviewable.

## Relationship To Roadmap

The roadmap gives v0.6 ownership of World Generation v1: runnable `WorldSpec`
data generated from templates and structured AI-assisted plans. This package
is the contract layer for that roadmap item. It preserves the v0.3
`WorldSpec` loader/runtime-context bridge, the v0.4 Agent Loop boundary, and
the v0.5 memory substrate while preparing later additive generation work.

## Non-goals

- Do not implement generation schemas, services, APIs, UI, tests, fixtures,
  persistence, or migrations.
- Do not define external validation readiness; v0.7 owns that.
- Do not define projection application readiness; v0.8 owns that.
- Do not add concrete world content, examples, seed data, validation oracle
  details, or application-specific backend behavior.
- Do not add live external AI-provider integration.
- Do not change runtime tick behavior, event emission, loader behavior,
  runtime-context derivation, Agent Loop behavior, memory behavior, params,
  archive, or frontend behavior.

## Expected Handoff

This package hands `0.6.2` a reviewed, documentation-only contract for the
first deterministic generator core. The handoff includes:

- public concept names and field semantics.
- template semantics that stay generic and deterministic.
- validation and diagnostics expectations.
- compatibility constraints against existing engine surfaces.
- conditions that must be met before `0.6.2` may record
  `implementation_authorized: yes`.
