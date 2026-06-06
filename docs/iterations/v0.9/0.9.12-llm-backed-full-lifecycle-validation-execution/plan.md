# Plan

Chinese mirror: `plan.zh.md`.

Status: documentation reviewed / evidence execution authorized

## Objective

Prepare the reviewed evidence-execution package for the LLM-backed full
lifecycle validation run.

## Authoritative Inputs Read

- `AGENTS.md`
- `.agents/skills/worldengine-iteration-docs/SKILL.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/iterations/v0.9/CURRENT_STATE.md`
- `docs/iterations/v0.9/v0.9-plan.md`
- `docs/testing/llm-backed-lifecycle-validation-plan.md`
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md`
- all LLM-backed scenario docs under `docs/testing/agent-autonomous/scenarios/`
- `docs/testing/agent-autonomous/llm-backed-artifact-contract.md`
- `docs/testing/agent-autonomous/llm-backed-scorecard.md`
- `docs/testing/agent-autonomous/second-agent-review-protocol.md`
- `docs/iterations/v0.9/0.9.10-llm-backed-autonomous-checker-and-fixtures/`
- `docs/iterations/v0.9/0.9.11-validation-client-evidence-handoff-contract/`

## Files

Create this package's 14 documentation files and update parent v0.9 route docs
to documentation-review-needed.

Allowed after review:

- `docs/testing/results/**`
- ignored `test-results/agent-autonomous/**`
- this package and parent route/review docs.

Forbidden:

- code, checker, fixture, frontend, Validation Client, generated-result rewrite,
  provider credential, external repository, or `backend/worldengine/` changes.

## Steps

1. Draft package docs.
2. Run documentation checks.
3. Send docs to read-only documentation evaluator.
4. Documentation evaluator reported PASS; status is updated to
   evidence-execution-authorized.
5. Run the staged validation or classify blockers.
6. Run checker/scorecard and second-Agent review.
7. Write durable result summaries.
8. Route to 0.9.13 closeout with PASS or classified FAIL/BLOCKED/NOT_RUN.

## Stop Conditions

- Documentation review reports P0/P1/blocking P2.
- Provider credentials are missing or cannot be used without exposing secrets.
- Validation requires code changes.
- Required artifacts cannot be produced or redacted.
- Checker or second-Agent review blocks PASS.
