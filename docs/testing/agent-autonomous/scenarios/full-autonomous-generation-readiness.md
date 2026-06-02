# Full Autonomous Scenario: generation-readiness

Status: contract-only / checker-extension-required
Scenario ID: AUTO-FULL-V07-004

## User Goal

As an ordinary dashboard user, submit a generic world generation preview,
confirm runtime-readiness evidence for the valid preview, then submit an
invalid duplicate-cell preview and confirm diagnostics.

## Autonomous Operation Boundary

Allowed operations:

- UI operations against GenerationPanel.
- Public API reads or calls against `/world/generation/preview` and
  `/world/generation/runtime-readiness` when the runner records them as public
  API evidence.
- CLI operations to start services and run documented checker commands.
- Screenshot, transcript, operation log, API log, and scorecard artifact
  creation.

Forbidden operations:

- external validation world content, seed data, concrete characters,
  locations, resources, story rules, or private validation targets.
- private provider data, hidden runner paths, hidden reset hooks, private
  oracle output, or transcript leakage.
- code, scenario, checker, or fixture edits during the run.

## Preconditions

- Dashboard GenerationPanel is reachable.
- Test data uses generic ids and labels only.
- The future full-autonomous checker can distinguish UI operations from public
  API evidence.

## Steps The Agent May Choose

1. Open the dashboard and locate GenerationPanel.
2. Fill a generic valid preview request with root and child cell ids.
3. Submit the preview.
4. Observe validation status, generation id, source kind, preview summary, and
   runtime-readiness status.
5. Optionally call public generation APIs with equivalent generic data and
   record request/response summaries.
6. Submit an invalid duplicate-cell request.
7. Observe diagnostics and verify readiness is not shown as passed.
8. Inspect output for private or external validation world leakage.
9. Save screenshots and logs for valid and invalid states.

## Expected Assertions

- Valid preview displays validation `passed`.
- A public generation id is visible and starts with `generation-`.
- Source kind is `template`.
- Summary includes public count metadata such as `total_cell_count`.
- Runtime readiness is `passed` only for the valid preview.
- Invalid duplicate-cell input displays validation `failed` and
  `duplicate_cell_id`.
- Invalid preview does not show readiness as passed.
- Output remains generic and public.

## Failure Or Blocked Conditions

- Valid generic preview fails without diagnostic evidence.
- Invalid duplicate-cell preview is accepted or marked readiness passed.
- Output leaks external validation world content or private provider details.
- Required screenshots, API summaries, or scorecard artifacts are missing.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-log.jsonl` when public generation APIs are called
- `api-summary.json`
- `transcript.md`
- `console.log` or explicit empty-console note
- `scorecard-summary.json`
- screenshots for valid preview/readiness and invalid diagnostics

## PASS Source

Future full-autonomous scorecard/checker over the saved result directory.
Current v0.7 may document this scenario but must not report it as PASS until
the protocol and checker support public API operations and the result has been
validated.
