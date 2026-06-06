# Plan

Chinese mirror: `plan.zh.md`.

Status: implementation complete / verification passed

## Objective

Convert the LLM-backed autonomous validation suite from
`checker-extension-required` documentation into checker-supported saved-result
contracts, fixtures, and regression tests.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/AGENTS.md`
- `docs/project-north-star.md`
- `docs/scope-boundaries.md`
- `docs/iterations/README.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md`
- LLM-backed scenario docs under `docs/testing/agent-autonomous/scenarios/`
- current saved-result checker and fixtures under `tools/testing/`

## Files

Create:

- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/README.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/README.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/intent.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/intent.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/contract.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/contract.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/technical-design.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/technical-design.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/test-plan.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/test-plan.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/plan.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/plan.zh.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/review.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/review.zh.md`

Modify after documentation review only:

- Parent v0.9 route/status docs moved from documentation-review-needed to
  implementation-authorized after the evaluator reported no P0/P1/P2 findings.

Implementation files after authorization:

- `tools/testing/validate_agent_autonomous_result.py`
- `tools/testing/test_validate_agent_autonomous_result.py`
- `tools/testing/fixtures/agent-autonomous/**`
- `docs/testing/agent-autonomous/result-schema.json`
- LLM-backed testing docs under `docs/testing/agent-autonomous/**`

Do not touch:

- `backend/worldengine/**`
- product runtime behavior under `backend/app/**`
- `frontend/**`
- external repositories or Validation Client code
- generated result directories used as evidence unless they are explicit
  checker fixtures for this package.

## Steps

1. Draft the complete 0.9.10 package document set.
2. Run documentation checks.
3. Send package docs to a read-only documentation/contract evaluator.
4. Documentation/contract evaluator reported PASS with no P0/P1/P2 findings;
   child and parent docs are updated to implementation-authorized.
5. Implement only the authorized checker/fixture/test/documentation scope.
6. Run the commands in `test-plan.md`.
7. Send implementation to an implementation-scope evaluator before closeout.
8. Update `review.md` and parent route to `0.9.11` only after verification and
   evaluator review pass.

## Verification

Documentation-stage verification:

- `git diff --check`
- package completeness scan.
- status/authorization scan for accidental implementation authorization.

Implementation-stage verification:

- `make validate-agent-autonomous-fixtures`
- `backend/.venv/bin/python -m pytest tools/testing/test_validate_agent_autonomous_result.py -q`
- `backend/.venv/bin/python -m pytest tools/testing -q`
- `git diff --check`
- scope scan for forbidden runtime/frontend/Validation Client changes.

## Stop Conditions

- Required package documents or mirrors are missing.
- Documentation review reports P0/P1/blocking P2.
- Implementation needs product runtime, provider call, frontend, or Validation
  Client changes.
- Checker PASS would depend on subjective judgment or missing public artifacts.
- Redaction requirements cannot be enforced with saved-result artifacts.
