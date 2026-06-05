# Complete Product Validation Runbook

Status: planned runbook, not executed

Chinese mirror: `runbook.zh.md`.

## Purpose

This runbook describes how a future validation chat should execute complete
WorldEngine product validation. It does not claim that validation has run.

## Preflight

1. Read:
   - `AGENTS.md`.
   - `docs/project-north-star.md`.
   - `docs/product-model.md`.
   - `docs/scope-boundaries.md`.
   - `docs/roadmap.md`.
   - `docs/testing/complete-product-validation/README.md`.
   - `docs/testing/complete-product-validation/validation-spec.md`.
   - `docs/testing/complete-product-validation/scenario-matrix.md`.
   - `docs/testing/product-capability-validation-playbook.md`.
2. Record current branch, commit, dirty files, and any ignored generated
   artifact directories.
3. Identify the validation scope:
   - current product baseline only.
   - LLM-backed lifecycle included or excluded.
   - external Validation Client included or excluded.
4. Create a result directory:

```text
test-results/product-validation/<timestamp>-complete-product-validation/
```

If the run is LLM-backed autonomous validation, also create:

```text
test-results/agent-autonomous/<timestamp>-llm-backed-full-lifecycle/
```

## Execution Order

### Stage 0: Documentation and scope audit

- Confirm no claim contradicts `docs/iterations/**/CURRENT_STATE.md`.
- Confirm no product PASS is inferred from historical closeout.
- Confirm no external validation world content is in core docs or fixtures.
- Record scope exclusions.

### Stage 1: Schema, contract, and checker fixtures

Run the version-appropriate schema and checker commands. A complete run should
include current checker fixtures where available:

```bash
make validate-agent-smoke-fixtures
make validate-agent-autonomous-fixtures
```

Add contract-specific commands from the active version or result plan.

### Stage 2: Backend focused tests

Run focused backend tests tied to the capability matrix before broad
regression. The exact files are version-specific, but the set should cover:

- recursive schemas and loader bridge.
- runtime, events, params, snapshots, and archive behavior.
- Agent loop and memory substrate.
- generation and import boundaries.
- projection/readiness/report checkers when in scope.

### Stage 3: Backend broad regression

Run the broad backend suite for the active code path.

### Stage 4: Frontend unit and build

Run frontend unit tests and build when dashboard behavior is in scope.

### Stage 5: Browser E2E

Run current E2E scenarios. E2E PASS requires assertions, not only page load.
Cross-check state-changing flows against API/event evidence where possible.

### Stage 6: Agent smoke

Run or validate Agent smoke result directories only through deterministic
checker output:

```bash
make validate-agent-smoke-result RESULT_DIR=<smoke-result-dir>
```

### Stage 7: Autonomous saved-result validation

Run or validate autonomous result directories only through the documented
checker:

```bash
make validate-agent-autonomous-result RESULT_DIR=<autonomous-result-dir>
```

Do not describe saved-result validation as a full autonomous runner.

### Stage 8: LLM-backed lifecycle

Run only when explicitly in scope and implementation support exists. Follow:

- `docs/testing/llm-backed-lifecycle-validation-plan.md`.
- `docs/testing/agent-autonomous/llm-backed-suite-execution.md` when present.

Required sequence:

1. provider live smoke.
2. LLM-backed world creation.
3. rule parameter evolution.
4. rule-compliant event generation.
5. persistent Agent autonomy evidence.
6. evidence export.
7. checker or scorecard.
8. second-Agent read-only review.

### Stage 9: External client evidence review

If Validation Client is in scope:

- operate only through public WorldEngine APIs/contracts.
- confirm client did not own LLM, generation, Agent action, or evaluator logic.
- confirm operation logs distinguish UI/CLI actions from API evidence.
- confirm exported evidence bundle is redacted.

### Stage 10: Final verdict audit

Fill the coverage matrix and result template. Every capability must be:

- `pass`.
- `fail`.
- `blocked`.
- `skipped`.
- `out_of_scope`.

## Stop Rules

Stop and classify the result if:

- secrets or private provider/Agent/evaluator data appear in evidence.
- a direct API call is recorded as an Agent UI/CLI operation.
- deterministic mock behavior is used as proof of live behavior.
- LLM-backed validation lacks a WorldEngine-owned live provider call path.
- required artifacts are missing.
- checker support is missing for the claimed PASS source.
- user direction directly becomes final world fact without rule adjudication.

## Durable Result

Write the result under:

```text
docs/testing/results/YYYY-MM-DD-complete-product-validation.md
docs/testing/results/YYYY-MM-DD-complete-product-validation.zh.md
```

Use `result-template.md` and `result-template.zh.md`.
