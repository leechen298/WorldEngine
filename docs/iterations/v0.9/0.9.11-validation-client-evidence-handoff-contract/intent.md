# Intent

Chinese mirror: `intent.zh.md`.

## Problem

v0.9 now has WorldEngine-owned provider, world generation, rule, runtime,
direction, Agent continuity, projection/diagnostic, and LLM-backed saved-result
checker support. The Validation Client still needs a stable public contract for
which artifacts it may display or export when validating the LLM-backed
lifecycle.

Without this contract, the client could accidentally become an evaluator,
invent missing LLM behavior, request provider secrets, expose private evidence,
or export artifact shapes that the WorldEngine checker cannot consume.

## Intent

Define a redacted public handoff contract that lets a client carry evidence
from WorldEngine to humans and checkers. The contract must preserve these
boundaries:

- WorldEngine owns provider calls, generated world behavior, and canonical
  evidence.
- The checker owns PASS/FAIL/BLOCKED/NOT_RUN classification.
- The client owns display/export only.
- The evidence bundle is public, redacted, relative-path based, and stable
  enough for later client implementation.

## Non-Intent

This package does not implement client UI, client export code, provider calls,
live validation, generated results, checker changes, or backend runtime
behavior.
