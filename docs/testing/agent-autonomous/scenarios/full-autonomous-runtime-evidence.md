# Full Autonomous Scenario: runtime-evidence

Status: contract-only / checker-extension-required
Scenario ID: AUTO-FULL-V07-001

## User Goal

As an ordinary dashboard user, confirm that WorldEngine runtime can advance one
step and that the dashboard timeline plus public API evidence agree about the
new tick.

## Autonomous Operation Boundary

Allowed operations:

- UI operations against the dashboard.
- Public API reads against `/runtime/state` and `/world/events`.
- CLI operations to start services and run documented checker commands.
- Screenshot, transcript, API log, and final result artifact creation.

Forbidden operations:

- hidden reset APIs.
- database or private in-process state inspection.
- private oracle, private fixture hooks, or external validation world internals.
- code, scenario, checker, or fixture edits during the run.
- Codex self-declared PASS without checker/scorecard evidence.

## Preconditions

- Backend and frontend are reachable through recorded URLs.
- The test user does not assume the initial tick value.
- The result directory can store `operation-log.jsonl`, `api-log.jsonl`,
  `api-summary.json`, screenshots, transcript, and scorecard output.

## Steps The Agent May Choose

The autonomous agent may vary exact order, but must complete this evidence path:

1. Record branch, commit, app URL, and API URL.
2. Open the dashboard.
3. Read current health and tick from the UI.
4. Read `/runtime/state` through the public API.
5. Click the dashboard `Step` control once.
6. Read the updated tick from the UI.
7. Read `/runtime/state` again.
8. Read `/world/events` for the updated tick or recent event window.
9. Capture at least one screenshot showing runtime/timeline evidence.
10. Write operation, API, transcript, and scorecard artifacts.

## Expected Assertions

- Dashboard health is visible and indicates the backend is available.
- The UI tick increases by exactly 1 after the step.
- `/runtime/state.tick_id` agrees with the UI tick after the step.
- `/world/events` contains `tick.advanced` or `module.*` evidence for the new
  tick.
- No private operation appears in the operation or API log.

## Failure Or Blocked Conditions

- Backend or frontend cannot be reached.
- UI tick and API tick disagree.
- Tick advances but no public event evidence exists.
- Required artifacts are missing.
- The agent uses hidden/private state to prove the result.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-log.jsonl`
- `api-summary.json`
- `transcript.md`
- `console.log` or explicit empty-console note
- `scorecard-summary.json`
- `screenshots/`

## PASS Source

Future full-autonomous scorecard/checker over the saved result directory.
Current v0.7 may document this scenario but must not report it as PASS until
the protocol and checker support public API operations and the result has been
validated.
