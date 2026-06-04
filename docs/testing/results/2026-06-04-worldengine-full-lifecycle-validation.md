# WorldEngine Full Lifecycle Autonomous Validation

Status: FAIL
Mode: live full lifecycle validation plus saved-result checker
Date: 2026-06-04

Chinese mirror: `2026-06-04-worldengine-full-lifecycle-validation.zh.md`.

## Scope

This record captures the first formal `worldengine-full-lifecycle-autonomous`
validation run after the full lifecycle scenario, checker support, and generic
fixture were added under the testing assets.

This is a testing result, not an iteration package. It does not consume a
WorldEngine product iteration number.

## Scenario

Authoritative scenario:

- `docs/testing/agent-autonomous/scenarios/worldengine-full-lifecycle-autonomous.md`

Checker:

- `tools/testing/validate_agent_autonomous_result.py`

Result directory:

- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/`

## Command

```bash
make validate-agent-autonomous-result RESULT_DIR=test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle
```

Result: failed.

Checker failure:

```text
FAIL: world-lifecycle-summary.json evidence_integrity.redaction_scan_passed must be true
```

## Covered Evidence

The run covered the required lifecycle surfaces before failing redaction:

- WorldEngine-backed world creation through the Validation Client.
- Public world id: `world-16df0fbcaa35`.
- Runtime progression: tick `0` to tick `10`.
- Events observed: `42`.
- Snapshots observed: `1`.
- WorldEngine-backed Agent action event observed: `1`.
- Director guidance accepted through the public surface.
- Evidence bundle exported by Validation Client.

Supporting artifacts:

- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/result.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/world-lifecycle-summary.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/scorecard-summary.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/validation-client-evidence-bundle.json`
- `test-results/agent-autonomous/20260604T172208+0800-worldengine-full-lifecycle/raw/`

## Failure Analysis

The failure is not a UI smoke failure and not a missing tick/event/snapshot
failure. The direct checker failure is evidence integrity.

Validation Client exported:

```json
"private_worldengine_internals_included": true
```

and warned:

```text
sensitive content redacted from evidence records
```

The redaction trigger is consistent with the WorldEngine public director
guidance response containing private/internal marker terms in its public
explanation. The public response text currently names protected concepts such
as private Agent memory, goal, identity, relationship, `self_state`, and hidden
context. Validation Client correctly treats those markers conservatively and
redacts the explanation in the evidence bundle.

## Boundary

Do not convert this result to PASS by relaxing the checker or ignoring the
redaction flag.

The correct follow-up is a new product repair iteration that changes
WorldEngine public output so it communicates the boundary without emitting
private/internal marker terms.

## Recommended Follow-up

Create a new reviewed implementation package, for example:

```text
0.8.9.2-director-guidance-public-redaction-repair
```

Recommended repair scope:

- WorldEngine public director guidance response must use public-safe wording.
- Public output must not include private marker terms such as private memory,
  private goals, relationship internals, `self_state`, hidden context, raw
  provider traces, or private prompts.
- Autonomous checker should also reject operation-log entries that disguise
  direct public API calls as CLI operations. Direct API evidence belongs in
  `api-summary.json`, not the Agent operation log.

After repair, rerun the same full lifecycle validation and checker command.
