# Plan

Status: review complete

## Files

Create:

- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/README.zh.md`
- `docs/iterations/v0.5/v0.5-plan.md`
- `docs/iterations/v0.5/v0.5-plan.zh.md`
- `docs/iterations/v0.5/GOAL_RUNNER.md`
- `docs/iterations/v0.5/GOAL_RUNNER.zh.md`
- `docs/iterations/v0.5/CURRENT_STATE.md`
- `docs/iterations/v0.5/CURRENT_STATE.zh.md`
- `docs/iterations/v0.5/CAMPAIGN_PLAN.md`
- `docs/iterations/v0.5/CAMPAIGN_PLAN.zh.md`
- `docs/iterations/v0.5/review.md`
- `docs/iterations/v0.5/review.zh.md`
- all required docs and mirrors under
  `docs/iterations/v0.5/0.5.0-v0.5-planning-and-continuity-boundary-baseline/`

Do not touch:

- `backend/app/**`
- `backend/worldengine/**`
- `frontend/**`
- `tools/**`
- `test-results/**`
- `docs/testing/**`
- migrations
- external repositories
- generated result artifacts

## Steps

1. Confirm current branch and working tree with `git status --short --branch`.
2. Confirm no existing `docs/iterations/v0.5/` package is present.
3. Create the v0.5 parent campaign documents and Chinese mirrors.
4. Create the `0.5.0` child package documents and Chinese mirrors.
5. Encode the capability boundary split:
   - working memory: contract now, first implementation candidate later.
   - episodic memory: contract now, first implementation candidate later.
   - relationship state: contract/schema semantics only before behavior.
   - self-summary: contract/schema semantics only before summarization.
   - reflection records: contract/schema semantics only before automatic
     reflection.
   - personality drift signals: contract/schema semantics only before action
     modifiers.
6. Record subagent/evaluator findings in parent and child reviews.
7. Run documentation checks listed in `test-plan.md`.
8. Update `review.md` and `review.zh.md` with exact command results.
9. Stop at documentation-stage ready-for-review state.

## Stop Conditions

Stop and record a blocker if:

- any required parent or child doc is missing.
- any Chinese mirror is missing.
- any changed file appears outside `docs/iterations/v0.5/**`.
- implementation authorization would need to become `yes`.
- runtime, schema, API, frontend, backend test, fixture, migration, generated
  result, external repository, or `backend/worldengine/` files need changes.
- v0.4 evidence is being used as current v0.5 pass evidence.

## Verification

Run:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; parent=Path('docs/iterations/v0.5'); child=parent/'0.5.0-v0.5-planning-and-continuity-boundary-baseline'; parent_docs=['README','v0.5-plan','GOAL_RUNNER','CURRENT_STATE','CAMPAIGN_PLAN','review']; child_docs=['README','intent','contract','technical-design','test-plan','plan','review']; missing=[]; missing += [str(parent/(name+suffix)) for name in parent_docs for suffix in ('.md','.zh.md') if not (parent/(name+suffix)).exists()]; missing += [str(child/(name+suffix)) for name in child_docs for suffix in ('.md','.zh.md') if not (child/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(path) for path in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "import subprocess, sys; allowed='docs/iterations/v0.5/'; out=subprocess.check_output(['git','status','--short'], text=True); bad=[]; [bad.append(line) for line in out.splitlines() if line and not line[3:].startswith(allowed)]; print('out_of_scope=' + str(len(bad))); [print(line) for line in bad]; raise SystemExit(1 if bad else 0)"
```

## Review Update Step

After verification, update both parent and child `review.md` and `.zh.md` with:

- exact changed files.
- commands run and results.
- not-run implementation checks and rationale.
- compatibility review.
- scope review.
- subagent/evaluator findings.
- unresolved P1/P2/P3.
- final assessment.
