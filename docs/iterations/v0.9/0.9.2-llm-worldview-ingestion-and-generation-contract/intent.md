# Intent

Chinese mirror: `intent.zh.md`.

## Problem

WorldEngine currently exposes deterministic generic public world creation.
That path is useful for v0.8 handoff and compatibility, but it does not prove
that WorldEngine can take a user's basic worldview premise and generate a
premise-specific, system-digestible world model with LLM support.

v0.9 also now has a provider smoke boundary, but provider readiness or a
provider smoke endpoint does not by itself create a generated world. The next
gap is the contract that connects public worldview input, WorldEngine-owned
generation, provider/fallback classification, redacted evidence, and a
runtime-digestible generated world output shape.

## Goal

Create a complete, reviewable mixed-package contract for `0.9.2` that can
later be implemented to:

- accept a public basic worldview premise.
- produce a public generated world model summary that is not merely the
  deterministic generic response.
- classify whether generation was provider-backed, deterministic fallback,
  not configured, or blocked.
- expose validation metadata for premise specificity, system digestibility,
  runtime readiness, and redaction.
- preserve compatibility with existing deterministic `POST /worlds` behavior.

## Non-goals

- Do not implement code during the documentation stage.
- Do not authorize implementation before documentation/contract review.
- Do not run live provider calls.
- Do not claim LLM-backed world creation PASS.
- Do not create concrete demo-world fixtures or validation seed worlds.
- Do not modify Validation Client or make it generate content.
- Do not implement world rules beyond a public outline needed for the
  generated world summary.
- Do not implement bounded runtime controls, rule-linked evolution, event
  legality, Agent continuity, narrative projection, diagnostic dialogue,
  checker scorecards, or full lifecycle validation.

## Why Now

The v0.8 basic lifecycle handoff showed that basic world creation can support
external validation readiness, but the LLM-backed validation suite remains
blocked on provider proof, LLM-backed world creation, rule-linked evolution,
event legality, persistent Agent autonomy evidence, and checker/schema
support. `0.9.1` addressed the provider smoke and redaction boundary without
generating worlds. `0.9.2` is the next required bridge: a generated world
contract that can be inspected and validated without leaking provider internals
or narrowing the engine into a concrete application world.

## North Star Alignment

This work supports WorldEngine's north star by making world generation a
generic engine-owned capability. It keeps generated worlds structured,
validated, and inspectable, preserves runtime compatibility, and keeps
external projection or validation clients as consumers of public contracts
rather than owners of LLM behavior.
