# Intent

Chinese mirror: `intent.zh.md`.

## Why This Exists

The 0.8.9 parent package identified a concrete handoff blocker: external
Validation Client probes can reach WorldEngine `/health` and `/openapi.json`,
but cannot discover a public world creation contract or read a public handoff
manifest.

The parent package intentionally stayed documentation-only. This child package
turns the parent handoff plan into a bounded implementation package that can be
reviewed before code changes begin.

## Problem

Without this implementation package:

- a short `/goal implement 0.8.9` request conflicts with the parent package's
  `implementation_authorized: no` gate.
- agents may add runtime/API/schema changes without a reviewed implementation
  contract.
- Validation Client compatibility may be fixed by changing the external client
  instead of exposing the WorldEngine-owned public contract.
- public output may accidentally include private provider, prompt, evaluator,
  or Agent state details.

## Desired Outcome

After review and explicit implementation authorization, this package can add
only the WorldEngine public contract surfaces required for Validation Client
handoff. Closeout may conclude at most `WORLDENGINE_CONTRACT_READY`, not
external validation PASS or human validation PASS.
