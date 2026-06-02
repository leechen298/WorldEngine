# Full Autonomous Scenario: v0.7-readiness-contracts

Status: contract-only / checker-extension-required
Scenario ID: AUTO-FULL-V07-005

## User Goal

As an external validation integrator, confirm that v0.7 readiness artifacts are
public, checker-verifiable, and honest about known blockers and exclusions.

## Autonomous Operation Boundary

Allowed operations:

- Reading public repository docs and contracts.
- Running documented checker commands.
- Recording CLI logs, checker summaries, and public file paths.
- Optional public API reads if future readiness endpoints are added.

Forbidden operations:

- private external validation world data.
- private runner paths, hidden reset endpoints, selector dumps, oracle output,
  unredacted transcripts, seed data, or event payload internals.
- modifying docs, code, schemas, checkers, or fixtures during the run.
- treating JSON syntax success as product readiness PASS.

## Preconditions

- Repository checkout is available.
- Checker dependencies are installed.
- Current code-review blockers are known from
  `docs/testing/results/2026-06-02-v0.7-code-review.md`.

## Steps The Agent May Choose

1. Record branch, commit, and working-tree status.
2. Read the external validation readiness contract.
3. Read the readiness manifest and schema.
4. Read the projection read-model contract and schema.
5. Run the readiness manifest checker.
6. Run the projection read-model checker.
7. Run or inspect the redacted external validation report checker with valid
   and invalid generic fixtures.
8. Compare checker results against known V07-CR findings.
9. Classify each claim as passed, failed, blocked, skipped, or out of scope.

## Expected Assertions

- Public contract files are discoverable by repo-relative paths.
- Checker commands classify valid and invalid artifacts deterministically.
- Known P1/P2 blockers are surfaced and not hidden.
- A schema parse result is not reported as product readiness.
- External suite PASS is blocked or skipped unless a redacted external report
  artifact exists and passes checker.

## Failure Or Blocked Conditions

- Known blockers are omitted from the result.
- Private paths or private validation details appear in evidence.
- Checker failures are reworded as PASS.
- The agent reports projection application readiness without a projection app
  validation artifact.

## Required Artifacts

- `result.json`
- `operation-log.jsonl`
- `api-log.jsonl` only if public APIs are used
- `api-summary.json` or checker summary
- CLI log for every checker command
- `transcript.md`
- `scorecard-summary.json`

## PASS Source

Future full-autonomous scorecard/checker over the saved result directory plus
the documented checker command outputs. Current v0.7 may document this scenario
but must not report it as PASS until the protocol/checker accepts this evidence
and the run has completed.
