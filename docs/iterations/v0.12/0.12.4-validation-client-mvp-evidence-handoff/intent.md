# Intent

Chinese mirror: `intent.zh.md`.

## Problem

WorldEngine can now expose public session runtime, rule-bound evolution, Agent
state, Agent memory/consolidation, and read-only inspection surfaces. The
external Validation Client still needs an exact public contract for what to
export and how a checker should read the evidence.

Without this contract, the client would have to infer artifact names,
operation-log semantics, redaction requirements, and Agent terminology from
implementation details.

## User Value

A future Validation Client task can implement MVP evidence export without
guessing WorldEngine behavior or blurring external validation agents with
in-world Agents.

## Engineering Value

The package creates a stable boundary between WorldEngine public evidence and
external validation automation. WorldEngine remains the source of public
artifact semantics; the external client remains a consumer/exporter.

## Non-Goals

- No Validation Client code.
- No provider execution.
- No autonomous validation run.
- No checker PASS/PARTIAL/BLOCKED/FAIL closeout.
- No product code changes unless a later reviewed repair explicitly authorizes
  focused schema/checker support.
