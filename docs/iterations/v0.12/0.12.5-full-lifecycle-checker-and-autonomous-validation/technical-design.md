# Technical Design

Chinese mirror: `technical-design.zh.md`.

## Existing Checker Entry Points

The repository already defines deterministic autonomous checker entry points:

```bash
make validate-agent-autonomous-fixtures
make validate-agent-autonomous-result RESULT_DIR=<dir>
```

These commands use `tools/testing/validate_agent_autonomous_result.py`.

## Supported Evidence Modes

1. `fixture_checker_validation`: validates built-in fixtures and checker
   behavior. This may PASS as checker evidence only.
2. `saved_result_validation`: validates an existing result directory. This may
   PASS only for that saved result and must be labeled historical if the result
   predates v0.12.
3. `fresh_external_validation`: validates a current external Validation Client
   export. This may support v0.12 PASS only if the result directory was created
   for this package/session and passes checker/review.

## Expected Result Docs

After evidence execution, create:

- `full-lifecycle-validation-result.md`: exact commands, result dirs, statuses,
  blocker/partial/fail rationale, and final package classification.
- `scorecard-summary.md`: scorecard/checker items, verdict sources, redaction
  status, and unverified items.
- `read-only-evaluator-review.md`: second-agent read-only review findings.

## Blocker Handling

If a fresh external result directory is unavailable, record:

```text
fresh_external_validation_status: BLOCKED
blocker_owner: WorldEngine-Validation-Client or environment/provider/checker
v0.12_mvp_pass_supported: false
```

Do not create synthetic evidence to make the checker pass.

## Redaction Boundary

All result docs must avoid raw prompts, raw provider responses, raw thought,
private Agent memory, private goals, provider traces, secrets, tokens, and
private evaluator data.
