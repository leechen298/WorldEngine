# Intent

## Problem

v0.1 has backend, frontend, unit/API tests, and build evidence, but the closeout
explicitly recorded no live browser smoke, no API curl smoke, and no E2E suite.

The project also needs a safe way for Codex to operate the app during exploratory
smoke testing without letting the agent's natural-language judgment become the
final PASS source.

## Goal

Add a v0.1 post-closeout verification hardening package that provides:

- deterministic dashboard E2E tests.
- stable dashboard test selectors.
- an agent-assisted smoke protocol for `dashboard-basic-runtime`.
- structured local evidence under `test-results/`.
- a deterministic checker for agent smoke result directories.

## Non-Goals

- Do not change runtime behavior.
- Do not add WorldSpec or WorldCell behavior.
- Do not implement village runtime or a game surface.
- Do not change `backend/worldengine/`.
- Do not treat Codex observations as final PASS evidence.

## North Star Relationship

This package improves evidence quality for the v0.1 scaffold. It does not
reinterpret v0.1 as a recursive world engine and does not narrow WorldEngine into
a game-specific backend.
