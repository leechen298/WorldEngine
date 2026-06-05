# LLM-backed World Creation

Status: planned / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Goal

Prove a basic user premise can produce a public, system-digestible,
LLM-backed world state through WorldEngine.

## Required Operations

- Enter a basic world premise through the Validation Client or another public
  external surface.
- Create the world through WorldEngine.
- Capture public initial state, locations, entities, Agents, items,
  environment state, parameters, rule definitions, boundary conditions, and
  visualization payload.
- Compare the result against the current deterministic generic world response.

## Forbidden Operations

- Validation Client generates or rewrites world content.
- Deterministic fallback is marked as LLM-backed.
- Raw prompt or raw provider response is exported.
- User premise is copied directly into final state without WorldEngine
  generated structures.
- Concrete validation world seed data is stored in the WorldEngine repository.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `world-creation-summary.json`
- `world-rule-summary.json`
- `initial-snapshot.json` or equivalent public snapshot artifact
- `redaction-scan.json`
- `scorecard-summary.json` or checker output

## PASS Source

PASS requires checker or scorecard output proving the generated world is:

- premise-specific.
- system-digestible by WorldEngine.
- redacted.
- not the deterministic generic response.
- supported by provider-backed generation evidence when LLM-backed lifecycle is
  in scope.

## FAIL Taxonomy

- `world_creation`
- `provider`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

Store public generated state and public rule summaries only. Do not store raw
prompts, raw provider responses, private traces, hidden generation internals,
private evaluator data, or concrete external world seed data.
