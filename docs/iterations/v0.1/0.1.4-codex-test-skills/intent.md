# Intent

## Problem

v0.1.3 added deterministic E2E tests and an Agent smoke evidence protocol, but
the operating procedure still depends on the active Codex session remembering
the rules.

The risky parts are:

- reporting E2E success without a fresh command exit code.
- reporting Agent smoke success without `result.json` and validator output.
- omitting raw Agent operation records.
- recording direct API calls as Agent operations instead of UI or CLI actions.

## Goal

Create project-local Codex skills that make the intended workflows explicit:

- one skill for deterministic browser E2E execution.
- one skill for Agent smoke execution with raw operation evidence.

The skills should be committed with the repository and syncable into the local
Codex skills directory.

## Outcome

Future Codex sessions can load these project-specific skills before running
WorldEngine E2E or Agent smoke workflows, reducing drift from the v0.1.3
verification contract.
