# Test Plan

状态：documentation-stage test plan

## Documentation Gate

```bash
git diff --check
```

Expected result：passed with no output。

```bash
missing=0
for pkg in docs/iterations/v0.8/0.8.{0..8}-*/; do
  for f in README.md README.zh.md intent.md intent.zh.md contract.md contract.zh.md technical-design.md technical-design.zh.md test-plan.md test-plan.zh.md plan.md plan.zh.md review.md review.zh.md; do
    test -f "$pkg$f" || { printf 'missing %s\n' "$pkg$f"; missing=$((missing+1)); }
  done
  case "$pkg" in
    *0.8.6-v0.8-evidence-and-boundary-audit/)
      for f in audit-report.md audit-report.zh.md; do
        test -f "$pkg$f" || { printf 'missing %s\n' "$pkg$f"; missing=$((missing+1)); }
      done
      ;;
    *0.8.7-v0.8-release-candidate-bundle/)
      for f in release-candidate-summary.md release-candidate-summary.zh.md; do
        test -f "$pkg$f" || { printf 'missing %s\n' "$pkg$f"; missing=$((missing+1)); }
      done
      ;;
    *0.8.8-v0.8-final-closeout/)
      for f in final-closeout-summary.md final-closeout-summary.zh.md; do
        test -f "$pkg$f" || { printf 'missing %s\n' "$pkg$f"; missing=$((missing+1)); }
      done
      ;;
  esac
done
printf 'missing_child_docs=%s\n' "$missing"
```

Expected result：`missing_child_docs=0`。

```bash
missing=0
for f in \
docs/iterations/v0.8/0.8.0-v0.8-planning-and-v0.7-handoff-baseline/review.md \
docs/iterations/v0.8/0.8.1-minimum-working-state-contract/review.md \
docs/iterations/v0.8/0.8.2-core-observable-surface-boundary/review.md \
docs/iterations/v0.8/0.8.3-generation-runtime-agent-loop-readiness/review.md \
docs/iterations/v0.8/0.8.4-external-validation-handoff-contract/review.md \
docs/iterations/v0.8/0.8.5-core-working-state-smoke-evidence/review.md \
docs/iterations/v0.8/0.8.6-v0.8-evidence-and-boundary-audit/audit-report.md \
docs/iterations/v0.8/0.8.7-v0.8-release-candidate-bundle/release-candidate-summary.md \
docs/testing/results/2026-06-02-v0.7-code-review.md \
docs/testing/results/2026-06-02-v0.7-overall-validation.md \
docs/contracts/v0.7-readiness-manifest.json \
docs/contracts/projection-read-model-schema.json; do
  test -f "$f" || { printf 'missing %s\n' "$f"; missing=$((missing+1)); }
done
printf 'required_evidence_refs=12\n'
printf 'missing_evidence_refs=%s\n' "$missing"
```

Expected result：`required_evidence_refs=12` 且 `missing_evidence_refs=0`。

```bash
rg -n "in progress / 0\.8\.8 ready for review|documentation-review-needed|0\.8\.8-v0\.8-final-closeout|ready for review|final_closeout_authorized: no|final_verification_authorized: no" docs/iterations/v0.8/README.md docs/iterations/v0.8/README.zh.md docs/iterations/v0.8/CURRENT_STATE.md docs/iterations/v0.8/CURRENT_STATE.zh.md docs/iterations/v0.8/GOAL_RUNNER.md docs/iterations/v0.8/GOAL_RUNNER.zh.md docs/iterations/v0.8/CAMPAIGN_PLAN.md docs/iterations/v0.8/CAMPAIGN_PLAN.zh.md docs/iterations/v0.8/v0.8-plan.md docs/iterations/v0.8/v0.8-plan.zh.md docs/iterations/v0.8/review.md docs/iterations/v0.8/review.zh.md docs/iterations/v0.8/0.8.8-v0.8-final-closeout/README.md docs/iterations/v0.8/0.8.8-v0.8-final-closeout/README.zh.md docs/iterations/v0.8/0.8.8-v0.8-final-closeout/review.md docs/iterations/v0.8/0.8.8-v0.8-final-closeout/review.zh.md docs/iterations/v0.8/0.8.8-v0.8-final-closeout/final-closeout-summary.md docs/iterations/v0.8/0.8.8-v0.8-final-closeout/final-closeout-summary.zh.md
```

Expected result before review：parent status 为 `in progress / 0.8.8 ready for review`，
active child 为 `0.8.8-v0.8-final-closeout`，route 为 `documentation-review-needed`，
`final_verification_authorized` 和 `final_closeout_authorized` 都是 `no`。

```bash
changed_total=$(git status --short | wc -l | tr -d ' ')
out_of_scope=$(git status --short | awk '{print $2}' | grep -Ev '^(docs/iterations/v0\.8/|backend/app/api/routes/world_generation\.py$|backend/app/core/world_generation\.py$|backend/app/schemas/world_generation\.py$|backend/app/tests/test_generation_core_readiness\.py$|backend/app/tests/test_generation_core_readiness_api\.py$)' | wc -l | tr -d ' ')
printf 'changed_or_untracked=%s\n' "$changed_total"
printf 'out_of_scope_changed_or_untracked=%s\n' "$out_of_scope"
```

Expected result：changed files 只在 `docs/iterations/v0.8/**` 和已 review 的 `0.8.3`
backend/app schema/helper/route/test files 内。

```bash
awk 'BEGIN{bad=0} /[ \t]$/{bad++} END{printf "trailing_whitespace=%d\n", bad}' docs/iterations/v0.8/*.md docs/iterations/v0.8/*/*.md
awk 'BEGIN{bad=0} /^\t/{bad++} END{printf "tab_lines=%d\n", bad}' docs/iterations/v0.8/*.md docs/iterations/v0.8/*/*.md
find docs/iterations/v0.8 -name '*.md' | wc -l | tr -d ' ' | awk '{print "markdown_files=" $1}'
```

Expected result：无 trailing whitespace，无 tab characters。

## Final Verification Authorization

`review.md` 记录 `final_verification_authorized: yes` 前，不得运行 final verification commands。

如果 review 授权，final verification commands 为：

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_generation_core_readiness.py backend/app/tests/test_generation_core_readiness_api.py -q
```

```bash
PYTHONPATH=backend uv run --with-requirements backend/requirements.txt --no-project pytest backend/app/tests/test_generation_preview_api.py backend/app/tests/test_generation_regeneration_api.py backend/app/tests/test_runtime_context_bridge.py backend/app/tests/test_agent_loop_service.py backend/app/tests/test_agent_loop_api.py backend/app/tests/test_runtime_step.py -q
```

```bash
rg -n 'external validation PASS|external consumer PASS|product readiness|projection application readiness|generation quality PASS|full autonomous PASS|final v0.8 readiness|private repository path|UI selector|oracle internals|raw prompt|provider trace|secret|concrete validation world|external validator command' docs/iterations/v0.8 docs/testing/results
```

Allowed matches 必须位于 forbidden、non-claim、redaction-check、audit、release-candidate、
final-closeout 或 historical handoff contexts。

## Skipped Checks

除非后续 reviewed package 授权，以下检查保持 out of scope：

- frontend build or E2E。
- live Agent smoke。
- autonomous runner or suite。
- external validation。
- external application validation。
- deployment verification。
- generation-quality evaluation。
