# WorldEngine

Status: v0.6 final / closeout complete.

Chinese mirror: `README.zh.md`.

WorldEngine is a recursive world generation and runtime engine.

The `v0.6` branch completes World Generation v1. It preserves the v0.5 memory
substrate and v0.4 Agent-in-World Minimal Loop while adding generic
world-generation contracts, deterministic template generation, structured plan
compilation, AI-assisted plan import boundaries, validation metadata,
preview/regeneration/runtime-readiness APIs, and a dashboard generation preview
with focused E2E smoke. Existing runtime and action semantics remain
compatible.

WorldEngine is still not a complete recursive world engine implementation.
External validation readiness, projection application readiness, full product
readiness, new live Agent smoke execution, full autonomous runner/full-suite
coverage, live provider integration, subjective generation-quality approval,
durable memory persistence, public memory APIs, automatic reflection,
self-summary generation, relationship behavior, personality drift action
modifiers, and concrete world/demo content remain future version scope.

Read first:

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/api-reference-v0.6.md`
- `docs/releases/v0.6.md`
- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.md`
- `docs/iterations/v0.6/review.md`
- `docs/iterations/README.md`

## Repository Structure

- `backend/` - FastAPI service.
- `frontend/` - Vue 3 + TypeScript dashboard.
- `docs/` - architecture, release, roadmap, and iteration documents.
- `backend/app/` - active backend path.
- `backend/worldengine/` - legacy pre-v0.1 path; do not add new features there.

## Current v0.6 Capability

v0.6 preserves the v0.1 runtime scaffold, v0.3 loader/runtime bridge, v0.4
request-driven Agent-in-World loop, and v0.5 memory substrate while adding
World Generation v1. It can:

- start backend and frontend development services from the repository root.
- expose health, runtime, world event, world params, archive, and agent params
  routes.
- advance runtime ticks and world time.
- append runtime and module events to an in-memory event log.
- expose cursor-paginated event timelines and grouped event steps.
- execute a small world module tree with heartbeat/counter examples.
- apply validated world parameter patches.
- dry-run world parameter patches before applying them.
- create in-memory snapshots and summaries on configured intervals.
- use an LLM-style params agent service interface to propose and apply patches.
- build a bounded agent perception frame from runtime state, recent events,
  world params, and optional runtime context summary.
- validate inspectable `ActionIntent` payloads and return `ActionResult`
  evidence.
- handle `noop` and validated `params.patch` actions through a small checked
  boundary.
- expose `POST /world/agent/loop/step` for one request-scoped perceive ->
  intent -> validate/apply -> result cycle.
- represent generic working-memory and episodic-memory records with
  inspectable provenance.
- keep process-local working and episodic memory in a bounded in-memory
  backend substrate.
- add optional bounded read-only memory context to Agent Loop perception frames
  without changing action request, intent, or result semantics.
- render a dashboard for runtime controls, timeline, world params, and agent
  params interactions.
- load and validate generic `WorldSpec` data through the minimal loader.
- derive optional inert runtime context from loaded `WorldSpec` data.
- keep runtime step outputs and event payloads free of raw `WorldSpec` or root
  tree data.
- define generic world-generation request, template, plan, validation, and
  provenance schemas.
- generate deterministic generic `WorldSpec` data from reviewed templates.
- compile structured generation plans into inspectable generation material.
- import AI-assisted plan JSON through a strict boundary without live provider
  or runtime AI integration.
- expose preview, regeneration, and runtime-readiness generation APIs under
  `/world/generation`.
- render a dashboard generation preview workflow with validation/readiness
  diagnostics.

v0.6 still cannot:

- run recursive `WorldCell` structures as active runtime state.
- run loaded `WorldSpec` data as active recursive world state.
- claim external validation-world readiness or projection application
  readiness.
- claim full product readiness, new live Agent smoke, full autonomous runner,
  live provider, or generation-quality validation.
- persist memory durably or expose public memory APIs.
- run automatic reflection, self-summary generation, relationship behavior, or
  personality drift action modifiers.
- model full agent pseudo-self continuity.
- provide a packaged external product surface.

## Root-Level Quick Start

```bash
make setup
make dev
```

Useful single-service commands:

```bash
make dev-backend
make dev-frontend
```

### Backend Dev Run

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Dev Run

```bash
cd frontend
pnpm install
pnpm dev
```

Default frontend API target is `http://localhost:8000` (configure via `VITE_API_BASE_URL`).

## Verification

Current v0.6 closeout and post-closeout repair evidence is summarized in:

- `docs/releases/v0.6.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.md`
- `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`
- `docs/iterations/v0.6/review.md`

Earlier v0.1/v0.3 closeout evidence remains compatibility baseline material,
not the current API or implementation map.

Key recorded evidence includes:

- v0.6 0.6.11 reliability repair evidence in
  `docs/testing/results/2026-06-01-v0.6-reliability-validation.md`: focused
  backend/API repair suite `59 passed`, full backend regression `233 passed`,
  frontend unit `36 passed`, frontend build passed with the existing Vite
  large-chunk warning, full E2E `17 passed`, saved Agent smoke checker PASS,
  minimal autonomous saved-result checker PASS, 0.6.11 scope guard
  `out_of_scope=0`, and forbidden implementation sentinel with no output for
  `backend/worldengine`, `backend/app/alembic`, `backend/migrations`, and
  `test-results`.
- v0.6 final closeout evidence in `docs/iterations/v0.6/review.md` and
  `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.md`:
  full backend regression `220 passed`, frontend unit `36 passed`, frontend
  build passed with a Vite large-chunk warning only, E2E `16 passed`, required
  docs/mirrors `missing=0`, changed-file scope guard `out_of_scope=0`, and
  closeout consistency evaluator PASS.
- v0.6 deliberately does not claim external validation readiness, projection
  readiness, product readiness, new live Agent smoke, full autonomous runner,
  live provider, or generation-quality pass.

- v0.5 final closeout evidence in `docs/iterations/v0.5/review.md` and
  `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`:
  focused backend memory/loop/action compatibility `33 passed`, full backend
  regression `145 passed`, required docs/mirrors `missing=0`, changed-file
  scope guard `out_of_scope=0`, and closeout consistency evaluator PASS.
- v0.5 overall validation in
  `docs/testing/results/2026-05-31-v0.5-overall-validation.md`: focused memory
  substrate `7 passed`, focused perception/loop API `16 passed`, focused
  memory/loop/action compatibility `33 passed`, full backend regression
  `145 passed`, frontend unit `28 passed`, focused Agent Loop E2E `9 passed`,
  full E2E `15 passed`, Agent smoke saved-result checker PASS, and minimal
  autonomous saved-result checker PASS.
- v0.4 final closeout evidence in `docs/iterations/v0.4/review.md` and
  `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`:
  focused backend/API `35 passed`, full backend `139 passed`, final docs
  mirror check `missing=0`, and final scope guard `out_of_scope=0`.
- v0.3 loader and runtime bridge package evidence, compatibility audit, and
  final closeout review.

These are recorded closeout results, not tests rerun by this README update.

Implementation docs:

- `docs/iterations/v0.6/README.md`
- `docs/iterations/v0.6/0.6.10-v0.6-final-closeout/final-closeout.md`
- `docs/iterations/v0.6/0.6.11-post-closeout-reliability-and-scope-repair/review.md`
- `docs/releases/v0.6.md`
- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/releases/v0.5.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.6.md`
- `docs/api-reference-v0.5.md` for the v0.5 compatibility API baseline
- `docs/api-reference-v0.1.md` for the legacy v0.1 API reference
- `docs/testing/v0.1-test-map.md`
