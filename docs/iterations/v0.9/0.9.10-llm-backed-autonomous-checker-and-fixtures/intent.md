# Intent

Chinese mirror: `intent.zh.md`.

## Problem

The LLM-backed autonomous validation documents define provider live smoke,
LLM-backed world creation, rule parameter evolution, rule-compliant event
generation, Agent persistent autonomy evidence, and full lifecycle validation,
but they remain `checker-extension-required`.

The current saved-result autonomous checker supports basic dashboard and basic
WorldEngine lifecycle artifacts. It cannot yet classify LLM-backed scenarios
from their required public artifact set, cannot enforce the LLM-backed
scorecard critical items, and cannot distinguish a real structured result from
a claimed PASS with missing checker support.

## Goal

After this package, LLM-backed autonomous result directories have deterministic
checker support, scenario fixture coverage, redaction regression coverage, and
documented PASS/FAIL/BLOCKED/NOT_RUN classification rules.

## Non-goals

- Do not run live provider calls.
- Do not create or rewrite generated-result evidence to force PASS.
- Do not change product runtime behavior, public APIs, or frontend UI.
- Do not implement Validation Client export behavior.
- Do not claim LLM-backed lifecycle PASS.
- Do not change `backend/worldengine/`.

## Why Now

Earlier v0.9 packages created public provider, generated world, rules,
runtime, direction, event legality, Agent continuity, and projection evidence
surfaces. The next blocker is not another runtime capability; it is making the
LLM-backed autonomous suite checker-supported so later handoff and full-run
packages can use honest automated verdicts.

## North Star Alignment

This package supports the North Star by making LLM-backed world and Agent
evidence inspectable and verifiable. It keeps WorldEngine generic because it
validates public artifact contracts and redaction boundaries instead of adding
concrete demo worlds, seed data, game UI, or application-specific logic.
