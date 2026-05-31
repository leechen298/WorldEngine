# Intent

Status: review complete

## Problem / Purpose

v0.6 is the first WorldEngine version that may own world generation. The
roadmap names the goal, but implementation cannot begin from a one-line
roadmap entry. The version needs a reviewable campaign root, child-package
sequence, compatibility baseline, generation boundary, and explicit non-goals
before any schema, service, API, frontend, or test implementation changes.

## Why Now

v0.5 final closeout is complete and hands off to v0.6 only through v0.6's own
reviewed iteration package. The existing `WorldSpec` loader and runtime-context
bridge give v0.6 a validation and readiness baseline, but generation contracts
must be defined before code uses them.

## Relationship To Roadmap

v0.6 implements the roadmap item "World Generation v1": generate runnable
`WorldSpec` data from templates and structured AI-assisted generation with
validation, metadata, preview, and regeneration support.

This package does not implement that capability. It creates the documentation
and review path for later child packages to implement it safely.

## Non-goals

- Do not implement generation schemas, services, APIs, UI, tests, persistence,
  runtime readiness, preview, or regeneration in `0.6.0`.
- Do not add external validation readiness; v0.7 owns that scope.
- Do not add first external projection application readiness; v0.8 owns that
  scope.
- Do not add concrete world content, private validation details,
  application-specific backend behavior, live AI-provider calls, or
  `backend/worldengine/` runtime features.
- Do not claim runtime, API, E2E, frontend, Agent smoke, autonomous, external
  validation, projection, product readiness, or release checks passed.

## Expected Handoff

After review, this package hands off a v0.6 campaign structure and generation
boundary to `0.6.1-world-generation-contracts-and-template-semantics`.
Implementation remains unauthorized until a later mixed/code child records
`implementation_authorized: yes`.

## North Star Alignment

This package aligns with the north star by preparing generic world generation
from structured inputs, templates, and AI-assisted plans while preserving
recursive world architecture and avoiding application-specific backend logic.
