# Review

Status: final / closeout complete

## Changed Files

Final v0.4 closeout includes three classes of changes:

- Public status surfaces: `README.md`, `README.zh.md`, `docs/roadmap.md`, `docs/roadmap.zh.md`.
- v0.4 iteration package and evidence docs under `docs/iterations/v0.4/**`.
- Authorized backend implementation/test files:
  - `backend/app/schemas/agent_loop.py`
  - `backend/app/agent/perception.py`
  - `backend/app/agent/action_adapter.py`
  - `backend/app/agent/loop_service.py`
  - `backend/app/api/routes/world_agent.py`
  - `backend/app/api/app_factory.py`
  - `backend/app/tests/test_agent_perception.py`
  - `backend/app/tests/test_agent_action_adapter.py`
  - `backend/app/tests/test_agent_loop_service.py`
  - `backend/app/tests/test_agent_loop_api.py`

No frontend, fixture, migration, external validation runner, projection app, or legacy `backend/worldengine/` implementation files are changed.

## Files Read

- `AGENTS.md`
- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/scope-boundaries.md`
- `docs/roadmap.md`
- `docs/iterations/README.md`
- `docs/iterations/AGENTS.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- active v0.4 package documents under `docs/iterations/v0.4/**`
- active backend files under `backend/app/**` touched by v0.4

## Commands Run

TDD and backend verification:

```bash
cd backend && .venv/bin/python -m pytest app/tests/test_agent_action_adapter.py app/tests/test_agent_loop_api.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_agent_perception.py app/tests/test_agent_action_adapter.py app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py -q
cd backend && .venv/bin/python -m pytest app/tests/test_agent_loop_service.py app/tests/test_agent_loop_api.py app/tests/test_params_agent.py app/tests/test_event_api_compat.py app/tests/test_runtime_step.py -q
cd backend && .venv/bin/python -m pytest app/tests tests -q
```

Documentation and scope verification:

```bash
git status --short --branch
git diff --check
python3 -c "from pathlib import Path; base=Path('docs/iterations/v0.4/0.4.7-v0.4-final-closeout'); docs=['README','intent','contract','technical-design','test-plan','plan','review','final-closeout']; missing=[str(base/(name+suffix)) for name in docs for suffix in ('.md','.zh.md') if not (base/(name+suffix)).exists()]; print('missing=' + str(len(missing))); [print(x) for x in missing]; raise SystemExit(1 if missing else 0)"
python3 -c "<changed-file scope guard over git status --short>"
python3 -c "<stale public-status scan over README.md, README.zh.md, docs/roadmap.md, docs/roadmap.zh.md>"
python3 -c "<stale v0.4 status scan excluding command-log self-matches>"
```

## Test Results

- Red regression run for review feedback: `3 failed, 12 passed`; failures proved that `noop` accepted patches and loop request/action intent extra fields were silently ignored.
- Focused regression after fixes: `15 passed in 0.29s`.
- Focused perception/action/loop/API command: `24 passed in 0.36s`.
- Focused backend/API compatibility command: `35 passed in 0.55s`.
- Full backend regression: `139 passed in 0.98s`.
- `git diff --check` passed.
- Final closeout docs/mirrors check passed with `missing=0`.
- Changed-file scope guard passed with `changed_files_count=82` and `out_of_scope=0` against the authorized v0.4 public status, docs, backend implementation, and backend test file set.
- Stale public-status scan found no obsolete planning, ready-for-review, or unimplemented v0.4 claims in current public status surfaces.
- Stale final-status scan found no obsolete in-progress, candidate, or incomplete final-route claims under active v0.4 status surfaces.

## Compatibility Review

v0.4 remains additive:

- `PerceptionFrame`, `ActionIntent`, `ActionResult`, `LoopStepRequest`, and `LoopStepResponse` are new agent-loop schemas.
- `ActionIntent`, `LoopStepRequest`, and loop action patch items now reject unknown fields with the existing 422 API envelope, preventing silent action-boundary payload loss.
- `noop` remains no-effect, but now rejects unexpected `patches` without emitting events or mutating state.
- `params.patch` uses strict `ActionParamPatchItem` schemas that remain `ParamPatchItem` compatible, then reuses `ParamValidator`, `ParamDryRunValidator`, and `WorldState.apply_patch()`.
- `POST /world/agent/loop/step` is additive.
- Existing `/world/agent/params/propose-and-apply`, runtime, event APIs, archive behavior, frontend, fixtures, migrations, and legacy `backend/worldengine/` remain compatible.

## Scope Review

The final scope guard is not docs-only. It explicitly allows the reviewed v0.4 backend implementation/test files and public status docs. It rejects unrelated files and currently reports `out_of_scope=0`.

v0.4 still excludes memory/self-continuity, world generation, external validation runner readiness, projection readiness, concrete world/demo content, frontend changes, fixtures, migrations, and new runtime features under `backend/worldengine/`.

## Subagent / Evaluator Checkpoint

Subagent/evaluator checkpoints were used across the campaign:

- documentation/contract authorization checks for implementation children;
- implementation-scope review;
- code review;
- validation-evidence review;
- documentation closeout consistency checks;
- release-candidate review;
- final closeout review.

The final closeout evaluator approved the final status flip. A later external review found P1/P2/P3 inconsistencies after that flip; this review records the repair.

Post-repair subagent/evaluator checkpoints completed:

- code/API evaluator confirmed no P1/P2, found one P3 API-level coverage gap for `noop` plus `patches`;
- the P3 was fixed with a route-level API regression covering HTTP 200 rejected result, no params mutation, and no `params.applied` event;
- documentation/status evaluator confirmed no P1 and found one P2 scope wording issue plus P3 documentation clarity issues;
- the wording and evidence-entry issues were fixed in parent README, root README, and 0.4.7 docs;
- final read-only evaluator rechecked public status, active child state, changed-file scope, stale status scans, and API coverage, and reported no P1/P2/P3.
- a later P2 review found nested `patches[*]` unknown fields were still silently discarded; this was fixed with strict loop patch-item schema validation and an API regression proving 422, no mutation, and no `params.applied` event.

## External Review Repair

Fixed findings from the latest review:

- P1: root `README.md`, `README.zh.md`, `docs/roadmap.md`, and `docs/roadmap.zh.md` now report v0.4 `final / closeout complete`.
- P1: this top-level review now records the actual mixed docs/backend changed-file scope instead of the obsolete initial docs-only scope.
- P2: `ActionIntent` and `LoopStepRequest` now forbid unknown fields; API regressions verify 422 and no mutation.
- P2: nested loop `params.patch` items now forbid unknown fields through strict `ActionParamPatchItem`; API regressions verify 422, no mutation, and no event.
- P2: `CURRENT_STATE.md` and parent README now agree that no active child remains after final closeout.
- P3: `noop` with unexpected patches now returns rejected `ActionResult` without mutation or event emission.

## Commands Not Run

Frontend, browser E2E, Agent smoke, build, fixture, migration, and external validation runner commands were not run because v0.4 did not modify or authorize those surfaces.

## Unresolved P1/P2/P3

- P1: none.
- P2: none.
- P3: none.

## Final Assessment

final / closeout complete
