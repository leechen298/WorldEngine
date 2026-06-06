# Intent

Chinese mirror: `intent.zh.md`.

## Problem

v0.9 has completed implementation packages through checker support and the
Validation Client handoff contract, but the LLM-backed lifecycle has not yet
been executed end to end in the current evidence chain. The version cannot
claim LLM-backed lifecycle PASS until the documented suite produces public
artifacts, checker/scorecard output, and second-Agent review.

## Intent

Run the validation as evidence work, not product implementation. The package
should discover and classify the real state:

- PASS when all critical evidence passes.
- FAIL when product, checker, client evidence, redaction, or scenario behavior
  is wrong.
- BLOCKED when provider quota, missing environment, unavailable service, or
  missing precondition prevents a valid run.
- NOT_RUN only when execution is intentionally skipped with documented reason.

## Non-Intent

This package does not repair product code, rewrite generated results, add
fixtures, change checker semantics, implement Validation Client features, or
claim product readiness.
