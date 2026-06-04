# Intent

Chinese mirror: `intent.zh.md`.

## Problem

The current WorldEngine autonomous validation checker supports historical
dashboard saved-result scenarios. It does not support the user's requested
complete capability chain: create a world, run it over time, observe in-world
Agent autonomous behavior, apply external direction, and export evidence for
review.

Without a checker-supported scenario, a validation chat could run UI smoke and
overclaim WorldEngine readiness.

## Goal

Add a precise full-lifecycle autonomous validation case and checker support so
future validation can fail or pass on evidence rather than narrative.

## Non-goals

- Do not implement or repair WorldEngine runtime behavior.
- Do not implement live provider calls.
- Do not modify the Validation Client repository.
- Do not store concrete demo worlds, characters, maps, story rules, or private
  validation oracle content in this repository.
- Do not claim live autonomous PASS from checker fixtures.

## Why Now

0.8.9.1 made the public handoff contract available, but it explicitly did not
claim Codex autonomous validation, live provider, full lifecycle, or product
readiness. The next validation run needs a complete case before it can test the
right thing.

## North Star Alignment

This package supports the north star by making world generation, world runtime,
Agent-in-world behavior, event evidence, and external projection validation
observable without narrowing WorldEngine into a single game backend.
