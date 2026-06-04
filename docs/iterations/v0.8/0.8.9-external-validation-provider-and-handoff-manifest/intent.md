# Intent

Chinese mirror: `intent.zh.md`.

## Why This Exists

The external validation client can now record evidence bundles, Agent
operation logs, and human-validation handoff material. WorldEngine still needs
a clearer core-side plan for two prerequisites:

1. LLM provider readiness that can be configured and observed without exposing
   secrets.
2. A public handoff manifest that external validation consumers can read
   without learning private validator details.

This package makes those prerequisites explicit before any future code, API,
schema, or checker implementation starts.

## Problem

Without this plan, future agents may confuse responsibilities:

- the validation client may try to manage LLM keys or providers.
- WorldEngine may leak provider traces, private prompts, or validation
  internals into public reports.
- external Agent validation may expect fields that WorldEngine has not
  defined.
- historical v0.7/v0.8 closeout evidence may be overclaimed as external
  validation readiness.

## Desired Outcome

After this package is reviewed, a future implementation chat can create a
scoped child package to expose a redacted handoff manifest and provider
readiness contract. The external validation client can then consume those
public surfaces while keeping validation implementation and human judgment
outside the WorldEngine core repository.
