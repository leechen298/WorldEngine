# Agent Persistent Autonomy Evidence

Status: planned / checker-extension-required

Parent plan: `docs/testing/llm-backed-lifecycle-validation-plan.md`.

## Goal

Prove at least one Agent shows sustained public autonomy evidence across
multiple rounds.

## Required Operations

- Create or load an LLM-backed world with at least one Agent.
- Advance enough ticks to observe multiple Agent decision moments.
- Capture observation, memory summary, public thought or reflection summary,
  intent or no-intent state, selected action, executed action, and event
  reaction.
- Verify the action source is WorldEngine public evidence rather than a client
  script.

## Forbidden Operations

- A single `params.applied` event is treated as persistent autonomy.
- Validation Client scripts Agent action and records it as WorldEngine action.
- Direct private memory, private goal, or hidden context mutation.
- Raw chain-of-thought is exported.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-summary.json`
- `agent-autonomy-summary.json`
- Agent event artifacts
- snapshots before and after Agent decision moments
- `redaction-scan.json`
- `scorecard-summary.json` or checker output

## PASS Source

PASS requires checker or scorecard output showing multi-round continuity and no
client-scripted Agent action.

## FAIL Taxonomy

- `agent_autonomy`
- `world_evolution`
- `redaction`
- `client_evidence`
- `checker_gap`

## Redaction Requirements

Public memory summaries, public thought summaries, public intent summaries,
public action summaries, and public reactions are allowed. Private memory
payloads, private goals, raw thoughts, raw chain-of-thought, hidden context,
and private relationship internals are forbidden.
