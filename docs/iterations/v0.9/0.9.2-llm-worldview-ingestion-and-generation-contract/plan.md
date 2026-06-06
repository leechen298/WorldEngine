# Plan

Chinese mirror: `plan.zh.md`.

## Ordered Steps

1. Read v0.9 parent docs, v0.6 generation contracts, v0.8 public world
   creation handoff, `0.9.1` provider smoke/redaction docs, and the LLM-backed
   world creation scenario.
2. Create the full `0.9.2` package document set and Chinese mirrors.
3. Run documentation checks from `test-plan.md`.
4. Send this package to a read-only documentation/contract evaluator.
5. Fix or record evaluator findings.
6. If no P0/P1/blocking P2 remains, update `review.md` to
   `implementation_authorized: yes`; otherwise stop before code changes.
7. Implement only the reviewed active-backend worldview generation contract.
8. Add public schemas, route wiring, generation helper, and focused backend
   tests.
9. Preserve existing deterministic `POST /worlds`, provider smoke, manifest,
   and validation error sanitization behavior.
10. Run focused backend tests and any checker tests changed by this package.
11. Run backend regression if implementation touches shared backend surfaces.
12. Update `review.md` with commands, results, compatibility review, scope
    review, unresolved findings, final assessment, and handoff to `0.9.3`.

## Phase Boundaries

Documentation phase:

- Create and review package documents.
- No runtime, API, schema, backend test, checker, fixture, provider, generated
  result, external repository, Validation Client, or `backend/worldengine/`
  files may change before authorization.

Implementation phase:

- May start only after this package review records
  `implementation_authorized: yes`.
- Must stay inside the allowed active-backend and focused checker/test scope.
- Must not reinterpret deterministic fallback as LLM-backed success.

Evidence execution phase:

- Live provider calls are closed by default.
- If no provider authorization exists, record not-configured, fallback, or
  blocked behavior, not provider-backed PASS.
- Generated public evidence must be redacted and structured.
- Safe mock behavior may support deterministic tests but must be labeled as
  non-live and must not count as provider-backed generation PASS.

## Files

Create during documentation phase:

```text
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/README.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/README.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/intent.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/intent.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/contract.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/contract.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/technical-design.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/technical-design.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/test-plan.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/test-plan.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/plan.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/plan.zh.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/review.md
docs/iterations/v0.9/0.9.2-llm-worldview-ingestion-and-generation-contract/review.zh.md
```

Allowed after implementation authorization:

```text
backend/app/agent/
backend/app/api/routes/
backend/app/api/app_factory.py
backend/app/schemas/
backend/app/tests/
tools/testing/validate_agent_autonomous_result.py
```

Do not touch:

```text
backend/worldengine/
frontend/
external repositories
Validation Client repository
generated result directories
concrete validation fixtures
migrations
```

## Verification

Documentation phase:

- required child docs and mirrors.
- required term coverage.
- markdown whitespace/final newline check.
- `git diff --check`.
- subagent/evaluator review.

Implementation phase after authorization:

- focused backend API/schema/redaction tests.
- existing public handoff tests.
- backend regression when shared backend surfaces change.
- checker validation only if checker support changes.

## Stop Conditions

Stop if:

- package docs conflict with v0.9 parent scope.
- evaluator reports unresolved P0/P1/blocking P2.
- implementation requires Validation Client changes.
- implementation requires `backend/worldengine/` changes.
- generated output cannot be structured without concrete demo content.
- premise specificity can only be proven by exposing raw prompt or raw
  provider response.
- deterministic fallback would be presented as LLM-backed PASS.
- safe mock or provider readiness would be presented as provider-backed world
  generation evidence.
- tests cannot prove redaction, fallback classification, and compatibility.

## Review Update Step

Before closeout, `review.md` must record:

- changed files.
- commands run.
- documentation/contract evaluator evidence.
- test results or docs-only no-test rationale.
- provider live-call status.
- compatibility review.
- scope review.
- unresolved P1/P2/P3 findings.
- final assessment and handoff.
