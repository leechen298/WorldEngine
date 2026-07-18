# Review

Chinese mirror: `review.zh.md`.

Status: closed / WorldEngine-side verification passed

implementation_authorized: yes
provider_live_call_authorized: no
external_repository_changes_authorized: no
evidence_execution_authorized: no

## Assessment Boundary

This review records implementation and current-session evidence for
`0.13.0-worldengine-runnable-anchor` only. It supports a WorldEngine-side
runnable-anchor result. It does not claim a clean full-repository regression,
complete v0.13 MVP PASS, Godot execution, or an external-checker verdict.

## Implementation Authorization

The user explicitly approved `0.13.0-worldengine-runnable-anchor` for
implementation on 2026-07-18 after the documentation/contract evaluator PASS.
The later instruction to continue without repeated routine questions did not
widen this child to provider live calls, external repository changes, Godot,
or complete-v0.13 evidence execution.

## Changed Files

Package-owned backend implementation:

```text
backend/app/engine/__init__.py
backend/app/engine/models.py
backend/app/engine/generation.py
backend/app/engine/evidence.py
backend/app/engine/rules.py
backend/app/engine/agent_runtime.py
backend/app/engine/session.py
backend/app/schemas/engine_v1.py
backend/app/api/routes/engine_v1.py
backend/scripts/engine_v1_anchor_smoke.py
backend/app/tests/test_engine_v1_generation.py
backend/app/tests/test_engine_v1_session.py
backend/app/tests/test_engine_v1_agent.py
backend/app/tests/test_engine_v1_interventions.py
backend/app/tests/test_engine_v1_protocol.py
```

Shared backend integration files:

```text
backend/app/api/app_factory.py
backend/app/api/routes/__init__.py
```

Only the `engine_v1_router` import/registration and `EngineV1Service` app-state
initialization belong to this package. The same dirty files contain unrelated
session-router changes that this package did not create, revert, or claim.

Package-owned frontend implementation:

```text
frontend/package.json
frontend/pnpm-lock.yaml
frontend/src/App.vue
frontend/src/main.ts
frontend/src/router/index.ts
frontend/src/api/engineV1.ts
frontend/src/api/engineV1.test.ts
frontend/src/pages/RunnableAnchorPage.vue
frontend/src/pages/RunnableAnchorPage.test.ts
frontend/src/components/runnable-anchor/ProjectionPanel.vue
frontend/src/components/runnable-anchor/EvidencePanel.vue
frontend/e2e/minimum-runnable-anchor.spec.ts
```

Current visual evidence:

```text
output/playwright/worldengine-anchor-desktop.png
output/playwright/worldengine-anchor-mobile-top.png
output/playwright/worldengine-anchor-mobile-evidence.png
```

Iteration documentation created or updated by the campaign:

```text
docs/iterations/v0.13/README.md
docs/iterations/v0.13/README.zh.md
docs/iterations/v0.13/CURRENT_STATE.md
docs/iterations/v0.13/CURRENT_STATE.zh.md
docs/iterations/v0.13/GOAL_RUNNER.md
docs/iterations/v0.13/GOAL_RUNNER.zh.md
docs/iterations/v0.13/CAMPAIGN_PLAN.md
docs/iterations/v0.13/CAMPAIGN_PLAN.zh.md
docs/iterations/v0.13/v0.13-plan.md
docs/iterations/v0.13/v0.13-plan.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/README.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/README.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/intent.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/intent.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/contract.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/contract.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/technical-design.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/technical-design.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/test-plan.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/test-plan.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/plan.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/plan.zh.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/review.md
docs/iterations/v0.13/0.13.0-worldengine-runnable-anchor/review.zh.md
docs/project-plan.md
docs/project-plan.zh.md
docs/roadmap.md
docs/roadmap.zh.md
```

## Commands Run

Focused backend verification from `backend/`:

```bash
.venv/bin/python -m pytest \
  app/tests/test_engine_v1_generation.py \
  app/tests/test_engine_v1_session.py \
  app/tests/test_engine_v1_agent.py \
  app/tests/test_engine_v1_interventions.py \
  app/tests/test_engine_v1_protocol.py -q
```

Result: exit `0`; `24 passed in 2.08s`.

Frontend verification from `frontend/`:

```bash
pnpm test
pnpm build
pnpm test:e2e --grep "minimum runnable anchor"
```

Results:

- `pnpm test`: exit `0`; 9 files and 50 tests passed.
- `pnpm build`: exit `0`; type checking and Vite production build passed. Vite
  reported a non-blocking chunk-size warning for the 1.586 MB main bundle.
- focused Playwright E2E: exit `0`; 1 test passed in 3.7 seconds.

The original test-plan spelling used an extra argument separator before
`--grep`; Playwright interpreted the option as a file filter and found no
tests. The English and Chinese test plans now record the successful,
reproducible command above. That unsuccessful invocation is not counted as a
test PASS.

Black-box HTTP smoke from `backend/`:

```bash
.venv/bin/python scripts/engine_v1_anchor_smoke.py
```

Result: exit `0`; classification `WORLDENGINE_SIDE_ANCHOR_PASS`;
`complete_v0_13_claimed=false`; all 11 checks passed and
`missing_checks=[]`. The final projection was tick `2`, revision `7`, event
cursor `10`, with complete evidence. Checks covered manifest discovery,
deterministic package generation, package/session hash handoff, same-window
direction decisions, deferred direction application, exact step count, Agent
causal evidence, action, feedback, complete event polling, and evidence
completeness.

Full backend regression from `backend/`:

```bash
.venv/bin/python -m pytest -q
```

Result: exit `1`; `484 passed, 1 failed`. The failed test was
`app/tests/test_agent_continuity_consolidation_evidence.py::test_manifest_exposes_agent_continuity_endpoint`.
No clean full-backend regression PASS is claimed.

Additional checks:

```bash
env PYTHONPYCACHEPREFIX=/tmp/worldengine-pycache \
  .venv/bin/python -m py_compile \
  scripts/engine_v1_anchor_smoke.py \
  app/engine/session.py \
  app/engine/evidence.py \
  app/schemas/engine_v1.py
git diff --check
```

Results: both exited `0`. A prior bare `py_compile` attempt could not write the
macOS user cache under the filesystem sandbox; rerunning with the explicit
temporary cache path passed and is the recorded syntax result.

## Acceptance Results

| Criterion | Result | Current evidence |
| --- | --- | --- |
| AC-01 deterministic package | PASS | Normalized equivalent briefs produce the same ready hash; allowed input changes alter the relevant field and hash. |
| AC-02 session source and initial state | PASS | Package hash, session source hash, initial snapshot, projection revision, and state hash agree. |
| AC-03 exact lockstep step | PASS | `step N` advances exactly N ticks with monotonic time, revision, and event sequence. |
| AC-04 Agent causal chain | PASS | Perception, decision, request, judgment, result, event, diff, and experience references form one public chain. |
| AC-05 experience-linked later decision | PASS | A later decision cites prior public experience and exposes a machine-observable decision-mode change. |
| AC-06 accepted bounded direction | PASS | A bounded direction is accepted in an explicit window and applied only by a later rule-linked event and non-empty diff. |
| AC-07 rejected final fact | PASS | A direct-final-fact request in the same window receives the stable semantic rejection with no diff or target mutation. |
| AC-08 idempotency and revision conflict | PASS | Duplicate IDs replay only matching payloads; reused IDs with different payloads and stale revisions fail without mutation. |
| AC-09 replayable evidence | PASS | Snapshot/diff/state-hash replay is checked; tampered diff, event, Agent decision, or cross-window direction evidence becomes incomplete. |
| AC-10 manifest-only black-box client | PASS | A separate service process is driven through public HTTP and manifest discovery only. |
| Administration console | PASS | Unit, build, E2E, and real-browser flow prove API-only control and consistent canonical refresh. |
| Full backend regression | FAIL | Executed result is 484 passed and 1 unrelated legacy-manifest assertion failure. |
| Godot and external checker | NOT_RUN | Owned by `0.13.1` and `0.13.2`; forbidden in this child. |
| Complete v0.13 validation | NOT_RUN | Requires a current external Godot/checker run. |
| Provider live path | NOT_RUN | Forbidden and unnecessary for this anchor. |

## Real-browser Verification

The administration console was exercised in a real browser through generation,
session boot, same-window accepted/rejected direction submission, exact two-tick
step, generic client action, typed feedback, projection refresh, and evidence
inspection.

- Desktop viewport: 1440 x 1000.
- Mobile viewport: 390 x 844.
- A page-level mobile overflow was found during inspection and fixed by
  constraining projection grid children; the final measurement was
  `documentScrollWidth=innerWidth=390` while wide tables remained internally
  scrollable.
- No incoherent overlap or blank rendering remained in the saved images.
- Browser console had one `favicon.ico` 404 and no application/runtime error.

## Independent Evaluator Chain

- Documentation/contract evaluator
  `019f74b5-e8a5-7870-81c9-38e86284454a`: PASS, no P1/P2/P3.
- Implementation-scope evaluator
  `019f7531-b80c-7d62-a0d9-232b01a700e6`: PASS.
- Code-review evaluator
  `019f7532-e3a4-7e22-b2d4-58900d4ed416`: final PASS, no P1/P2/P3 after
  idempotency binding, evidence replay/completeness, privacy, atomic mutation,
  revision consistency, rollback, and same-window anti-splicing repairs.
- Validation-evidence evaluator
  `019f755d-6a3a-7350-9ee8-cb7c27673669`: PASS for the WorldEngine-side
  package boundary; explicitly classified full backend regression as FAIL and
  Godot/external/complete-v0.13 validation as NOT_RUN.
- Closeout-consistency evaluator
  `019f756e-50c6-7913-8784-e9597e47e676`: PASS. It confirmed that closing
  only `0.13.0` and routing to `0.13.1` documentation preparation preserves the
  full-regression failure, NOT_RUN external boundaries, and authorization
  fields without making a complete-v0.13 claim.
- Post-transition consistency evaluator
  `019f7575-5f19-7683-b710-7e40d90e65a0`: PASS, no P1/P2. It re-read the
  final English/Chinese status files and confirmed the closed child, the
  documentation-only `0.13.1` route, all three parent authorizations set to
  `no`, and no full-repository, Godot, or complete-v0.13 claim.

Earlier evaluator attempts that timed out, were interrupted before reading the
updated files, or were shut down produced no usable verdict and were not
counted as PASS. The completed evaluators listed above own the recorded gates.

## Compatibility Review

- Engine V1 is additive under `/api/v1`; historical world, runtime, provider,
  archive, and dashboard routes were not replaced.
- The administration shell adds Vue Router while preserving the historical
  dashboard at `/` and placing the anchor at `/admin/runnable-anchor`.
- Process-local state is intentional for this minimum package; no migration or
  production persistence contract was introduced.
- The full-regression failure is an exact-dictionary-membership assertion in an
  unchanged legacy test. Pre-existing user-owned dirty changes in
  `backend/app/schemas/world.py` and `backend/app/api/routes/world.py` serialize
  additional `maturity`, `validation_status`, and `notes` fields for
  `PublicSurface`. No current evidence attributes that failure to Engine V1,
  and this package did not modify or revert those unrelated surfaces merely to
  force a green suite.

## Scope Review

Implementation stayed in `backend/app/`, `backend/scripts/`, `frontend/`,
package documentation, and generated visual evidence. It did not add code to
`backend/worldengine/`, change the external Validation Client repository, add
Godot content, make provider live calls, expose private Agent state, create a
concrete validation world in core, add production persistence, or allow a
client to write canonical facts.

The smoke classification is deliberately named
`WORLDENGINE_SIDE_ANCHOR_PASS` and emits `complete_v0_13_claimed=false`. It is
not an external verdict and cannot replace the independent checker.

## Unresolved Findings

- P1: none.
- P2: none.
- P3: full backend regression remains `484 passed, 1 failed` because of the
  unrelated dirty legacy manifest/test mismatch described above; no clean
  repository-wide PASS is claimed.
- P3: the production frontend build reports a main-bundle chunk-size warning.
- P3: manual browser inspection reports a favicon-only 404; no visible or
  functional application error was observed.

## Final Assessment

The validation-evidence and closeout-consistency gates pass, and all
`0.13.0`-owned acceptance criteria are currently proven. The package is closed
for its WorldEngine-side scope and hands off to `0.13.1` documentation
preparation only. No implementation or external-repository authorization is
carried into the next child.

Even after `0.13.0` closes, complete v0.13 MVP PASS remains forbidden until
`0.13.1` supplies Godot plus independently checkable external evidence and
`0.13.2` executes the correlated closeout run.
