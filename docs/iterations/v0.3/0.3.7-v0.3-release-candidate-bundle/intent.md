# Intent

## Problem

v0.3 now has loader, bridge, external fixture readiness, evidence index, and
compatibility audit artifacts, but they are spread across package reviews and
audit docs. Human / ChatGPT review needs one release-candidate bundle that
maps each claim to evidence and keeps not-implemented scope visible.

## Goal

Create a release-candidate evidence bundle that clearly states:

- what v0.3 planned.
- what v0.3 implemented or documented.
- what verification evidence exists.
- what v0.3 intentionally did not implement.
- what findings, assumptions, and risks remain.
- why final release closeout is deferred to 0.3.8.

## Non-goals

- Do not declare v0.3 final release.
- Do not close 0.3.8 work.
- Do not implement or modify runtime, schema, API, frontend, fixture,
  migration, or test behavior.
- Do not add Agent-in-World loop, memory, self-continuity, generation,
  projection, product UI, game UI, or external validation repositories.
- Do not add concrete demo worlds, characters, locations, resources, story
  rules, seed data, private fixture state, or application-specific backend
  logic.

## Why Now

0.3.6 assembled the evidence index and compatibility audit and reported no
open P1/P2 blocker. The milestone plan next requires a release-candidate
bundle before final closeout, so reviewers can decide whether v0.3 can proceed
to 0.3.8.

## North Star Alignment

This package supports WorldEngine as a generic recursive world runtime by
making the WorldSpec loader and inert runtime-context bridge evidence
reviewable without turning the engine into a concrete product surface or
claiming future agent, memory, generation, or projection behavior.
