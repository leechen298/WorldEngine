# Evidence Matrix

Status: review complete

## Command Evidence

| Surface | Command | Result | Supported claim |
| --- | --- | --- | --- |
| Tools/checker regression | `backend/.venv/bin/python -m pytest tools/testing` | PASS, 86 passed | Existing checker tests pass for Agent smoke saved-result validation, Agent autonomous saved-result validation, external validation report validation, readiness manifest validation, and projection read-model validation. |
| Readiness manifest CLI | `backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json` | PASS | v0.7 readiness manifest validates with the existing manifest checker. |
| Projection read-model CLI | `backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json` | PASS | v0.7 projection read-model schema validates with the existing projection checker. |
| External validation report schema JSON | `backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json` | PASS | Report schema JSON syntax is valid. |
| Readiness manifest schema JSON | `backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json` | PASS | Readiness manifest schema JSON syntax is valid. |
| Readiness manifest JSON | `backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json` | PASS | Readiness manifest JSON syntax is valid. |
| Projection read-model schema JSON | `backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json` | PASS | Projection read-model schema JSON syntax is valid. |
| Formatting | `git diff --check` | PASS | Current diff has no whitespace errors. |
| Scope guard | `python3 -c 'import subprocess ... changed-file scope guard ...'` | PASS, `changed_or_untracked=112`, `out_of_scope_changed_or_untracked=0` | Changed-file boundary remains inside cumulative v0.7 scope. |

## Coverage Classification

| Surface | Classification | Evidence / reason |
| --- | --- | --- |
| External validation report schema/checker | passed | Covered by `tools/testing` regression and JSON parse. |
| Readiness manifest schema/checker | passed | Covered by `tools/testing` regression, CLI validation, and JSON parse. |
| Projection read-model schema/checker | passed | Covered by `tools/testing` regression, CLI validation, and JSON parse. |
| Agent smoke saved-result checker | passed | Covered by `tools/testing/test_validate_agent_smoke_result.py` inside the 86 passed regression. |
| Agent autonomous saved-result checker | passed | Covered by `tools/testing/test_validate_agent_autonomous_result.py` inside the 86 passed regression. |
| Backend runtime/API behavior | out of scope | This package does not change or test runtime/API behavior. |
| Frontend behavior | out of scope | This package does not change or test frontend behavior. |
| Browser E2E | out of scope | This package does not authorize browser E2E execution. |
| Live Agent smoke | out of scope | Saved-result checker tests are not live Agent smoke. |
| Full autonomous runner/full suite | out of scope | Saved-result checker tests are not a full autonomous runner or suite execution. |
| External validation suite | out of scope | No external validation suite ran in this package. |
| Projection application readiness | out of scope | No projection application exists or ran in this package. |
| Product readiness | out of scope | Checker evidence is not product readiness evidence. |
| Generation-quality readiness | out of scope | No generation-quality suite ran in this package. |
| Release readiness | out of scope | Release-candidate and final release checks belong to later packages. |

## Compatibility Notes

- v0.7 checker surfaces pass together in one current-session regression.
- The PASS results support checker/schema/manifest compatibility only.
- Historical v0.6 evidence remains handoff context only.
- Runtime, API, frontend, E2E, live Agent, external suite, projection app,
  product readiness, generation quality, and release readiness remain
  unclaimed by this package.

## Unresolved Findings

- P1: none.
- P2: none.
- P3: none.
