# Full Autonomous Scenario: params-flow

Status: contract-only / checker-extension-required
Scenario ID: AUTO-FULL-V07-002

## User Goal

As an ordinary dashboard user, apply one allowed world parameter, confirm it
affects later runtime evidence, then attempt a reserved path and confirm that
the system rejects it without mutation.

## Autonomous Operation Boundary

Allowed operations:

- UI operations against the dashboard params form.
- Public API reads against `/world/params` and `/world/events`.
- CLI operations to start services and run documented checker commands.
- Artifact creation for screenshots, transcript, operation log, API log, and
  scorecard summary.

Forbidden operations:

- direct private mutation or reset hooks.
- database inspection.
- private fixture/oracle use.
- code, test, checker, scenario, or fixture edits during the run.
- treating UI text alone as PASS when API/checker evidence contradicts it.

## Preconditions

- Dashboard is reachable.
- Public API `/world/params` is readable.
- Runtime step behavior can produce event evidence for changed params.
- The agent records params before and after the invalid-path attempt.

## Steps The Agent May Choose

1. Open the dashboard and inspect current params.
2. Read `/world/params` through the public API.
3. Use the UI params form to set `counter.increment` to a valid numeric value.
4. Confirm the dashboard params JSON displays the new value.
5. Read `/world/params` again and verify the same value.
6. Step runtime through the UI or another documented public control.
7. Read `/world/events` and find event evidence affected by the new param.
8. Attempt to apply `system.secret` or another reserved path through the UI.
9. Confirm visible validation/error feedback.
10. Read `/world/params` again and prove the invalid path did not mutate state.
11. Save required screenshots and logs.

## Expected Assertions

- The valid param appears in the dashboard and public API state.
- Runtime/event evidence reflects the valid param when applicable.
- The reserved path shows a validation or reserved-path error.
- Params before and after the invalid operation remain equal for the invalid
  path.
- No private operation appears in logs.

## Failure Or Blocked Conditions

- The valid param does not persist.
- The reserved path is accepted or mutates state.
- UI and API evidence contradict each other.
- The result lacks before/after API snapshots.
- The agent uses hidden/private APIs.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-log.jsonl`
- before/after params snapshots or `api-summary.json`
- `transcript.md`
- `console.log` or explicit empty-console note
- `scorecard-summary.json`
- screenshots for valid state and invalid error state

## PASS Source

Future full-autonomous scorecard/checker over the saved result directory.
Current v0.7 may document this scenario but must not report it as PASS until
the protocol and checker support public API operations and the result has been
validated.
