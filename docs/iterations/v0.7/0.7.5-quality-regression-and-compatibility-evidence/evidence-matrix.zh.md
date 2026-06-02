# Evidence Matrix

Status: review complete

## Command Evidence

| Surface | Command | Result | Supported claim |
| --- | --- | --- | --- |
| Tools/checker regression | `backend/.venv/bin/python -m pytest tools/testing` | PASS, 86 passed | Existing checker tests pass：Agent smoke saved-result validation、Agent autonomous saved-result validation、external validation report validation、readiness manifest validation、projection read-model validation。 |
| Readiness manifest CLI | `backend/.venv/bin/python tools/testing/validate_readiness_manifest.py docs/contracts/v0.7-readiness-manifest.json` | PASS | v0.7 readiness manifest 可通过 existing manifest checker。 |
| Projection read-model CLI | `backend/.venv/bin/python tools/testing/validate_projection_read_model_contract.py docs/contracts/projection-read-model-schema.json` | PASS | v0.7 projection read-model schema 可通过 existing projection checker。 |
| External validation report schema JSON | `backend/.venv/bin/python -m json.tool docs/testing/external-validation-report-schema.json` | PASS | Report schema JSON syntax valid。 |
| Readiness manifest schema JSON | `backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest-schema.json` | PASS | Readiness manifest schema JSON syntax valid。 |
| Readiness manifest JSON | `backend/.venv/bin/python -m json.tool docs/contracts/v0.7-readiness-manifest.json` | PASS | Readiness manifest JSON syntax valid。 |
| Projection read-model schema JSON | `backend/.venv/bin/python -m json.tool docs/contracts/projection-read-model-schema.json` | PASS | Projection read-model schema JSON syntax valid。 |
| Formatting | `git diff --check` | PASS | Current diff 无 whitespace errors。 |
| Scope guard | `python3 -c 'import subprocess ... changed-file scope guard ...'` | PASS，`changed_or_untracked=112`，`out_of_scope_changed_or_untracked=0` | Changed-file boundary 仍在 cumulative v0.7 scope 内。 |

## Coverage Classification

| Surface | Classification | Evidence / reason |
| --- | --- | --- |
| External validation report schema/checker | passed | 由 `tools/testing` regression 和 JSON parse 覆盖。 |
| Readiness manifest schema/checker | passed | 由 `tools/testing` regression、CLI validation 和 JSON parse 覆盖。 |
| Projection read-model schema/checker | passed | 由 `tools/testing` regression、CLI validation 和 JSON parse 覆盖。 |
| Agent smoke saved-result checker | passed | 由 86 passed regression 中的 `tools/testing/test_validate_agent_smoke_result.py` 覆盖。 |
| Agent autonomous saved-result checker | passed | 由 86 passed regression 中的 `tools/testing/test_validate_agent_autonomous_result.py` 覆盖。 |
| Backend runtime/API behavior | out of scope | 本 package 不改变或测试 runtime/API behavior。 |
| Frontend behavior | out of scope | 本 package 不改变或测试 frontend behavior。 |
| Browser E2E | out of scope | 本 package 不授权 browser E2E execution。 |
| Live Agent smoke | out of scope | Saved-result checker tests 不是 live Agent smoke。 |
| Full autonomous runner/full suite | out of scope | Saved-result checker tests 不是 full autonomous runner 或 suite execution。 |
| External validation suite | out of scope | 本 package 未运行 external validation suite。 |
| Projection application readiness | out of scope | 本 package 没有 projection application，也没有运行相关验证。 |
| Product readiness | out of scope | Checker evidence 不是 product readiness evidence。 |
| Generation-quality readiness | out of scope | 本 package 未运行 generation-quality suite。 |
| Release readiness | out of scope | Release-candidate 与 final release checks 属于后续 packages。 |

## Compatibility Notes

- v0.7 checker surfaces 在同一 current-session regression 中通过。
- PASS results 只支持 checker/schema/manifest compatibility。
- Historical v0.6 evidence 仍只作为 handoff context。
- Runtime、API、frontend、E2E、live Agent、external suite、projection app、product readiness、
  generation quality 和 release readiness 均不由本 package 声明。

## Unresolved Findings

- P1：none。
- P2：none。
- P3：none。
