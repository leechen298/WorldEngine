# Intent

Chinese mirror: `intent.zh.md`.

## Problem / Purpose

`0.9.2` introduced a non-live public worldview generation surface and `0.9.3`
introduced a generated rule/parameter schema. Those outputs can be structured
and redacted while still failing the user's premise. v0.9 therefore needs a
deterministic public evaluation layer that can say whether generation evidence
is faithful, missing important premise coverage, contradictory, blocked, or
not yet runnable.

## Why Now

The parent v0.9 campaign needs fidelity evidence before bounded runtime
control, natural-language direction, rule-linked evolution, Agent continuity,
and full LLM-backed validation can be claimed. Without this package, later
runtime evidence could look active while drifting away from the original
worldview.

## Relationship To Roadmap

This package advances the v0.9 LLM-backed lifecycle foundation by turning
worldview quality into a public, checker-compatible contract. It supports the
North Star by keeping generated worlds inspectable and rule/evidence driven
instead of relying on subjective impressions.

## Non-goals

- Do not run live provider calls.
- Do not create generated result artifacts.
- Do not implement bounded runtime controls.
- Do not implement rule-linked event legality or parameter evolution.
- Do not implement Agent continuity, consolidation, narrative projection, or
  diagnostic dialogue.
- Do not modify Validation Client code or external repositories.
- Do not store concrete validation-world fixtures, raw prompts, raw provider
  responses, private evaluator oracles, private Agent memory, raw thought, or
  hidden context.

## Expected Handoff

`0.9.4` should hand off public immediate and bounded-run fidelity artifact
schemas plus deterministic helper behavior to `0.9.5`, where actual bounded
runtime controls become available for stronger run-based evidence.

