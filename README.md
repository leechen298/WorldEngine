# WorldEngine

Status: v0.5 final / closeout complete.

Chinese mirror: `README.zh.md`.

WorldEngine is a recursive world generation and runtime engine.

The `v0.5` branch completes the Memory and Self-Continuity Substrate closeout.
It preserves the v0.4 Agent-in-World Minimal Loop and adds additive generic
working-memory and episodic-memory schemas, a process-local in-memory memory
substrate, and bounded read-only memory context in the Agent Loop perception
path. Action semantics remain unchanged.

WorldEngine is still not a complete recursive world engine implementation.
Durable memory persistence, public memory APIs, automatic reflection,
self-summary generation, relationship behavior, personality drift action
modifiers, world generation, external validation readiness, projection
application readiness, and concrete world/demo content remain future version
scope.

Read first:

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/current-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/releases/v0.3.md`
- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/iterations/v0.3/README.md`
- `docs/iterations/README.md`

## Repository Structure

- `backend/` - FastAPI service.
- `frontend/` - Vue 3 + TypeScript dashboard.
- `docs/` - architecture, release, roadmap, and iteration documents.
- `backend/app/` - active backend path.
- `backend/worldengine/` - legacy pre-v0.1 path; do not add new features there.

## Current v0.5 Capability

v0.5 preserves the v0.1 runtime scaffold, v0.3 loader/runtime bridge, and v0.4
request-driven Agent-in-World loop while adding the first generic memory
substrate. It can:

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

v0.5 still cannot:

- run recursive `WorldCell` structures as active runtime state.
- run loaded `WorldSpec` data as active recursive world state.
- generate worlds from templates or prompts.
- persist memory durably or expose public memory APIs.
- run automatic reflection, self-summary generation, relationship behavior, or
  personality drift action modifiers.
- model full agent pseudo-self continuity.
- run external projection applications as engine consumers.
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

Recorded v0.3 closeout evidence is mapped in
`docs/iterations/v0.3/evidence-index.md` and summarized in
`docs/releases/v0.3.md`.

The v0.1 runtime closeout evidence remains the compatibility baseline and is
mapped in `docs/testing/v0.1-test-map.md`.

Key recorded evidence includes:

- v0.5 final closeout evidence in `docs/iterations/v0.5/review.md` and
  `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`:
  focused backend memory/loop/action compatibility `33 passed`, full backend
  regression `145 passed`, required docs/mirrors `missing=0`, changed-file
  scope guard `out_of_scope=0`, and closeout consistency evaluator PASS.
- v0.4 final closeout evidence in `docs/iterations/v0.4/review.md` and
  `docs/iterations/v0.4/0.4.7-v0.4-final-closeout/final-closeout.md`:
  focused backend/API `35 passed`, full backend `139 passed`, final docs
  mirror check `missing=0`, and final scope guard `out_of_scope=0`.
- v0.3 loader and runtime bridge package evidence, compatibility audit, and
  final closeout review.
- `make check-backend` and `make check-frontend`.
- backend pytest: `63 passed`.
- frontend unit tests: `24 passed`; focused frontend coverage later recorded
  `28 passed`.
- frontend production build: succeeded with a documented chunk-size warning.
- `make test-e2e`: `6 passed`.
- live Agent smoke:
  - `dashboard-params-flow`: 0.1.8 evidence preserved by
    `docs/testing/results/2026-05-24-v0.1.8-params-flow-live-smoke.md` and
    commit `c6da552`.
  - `dashboard-invalid-param`: current validated evidence under
    `test-results/agent-smoke/latest/`.

These are recorded closeout results, not tests rerun by this README update.

Implementation docs:

- `docs/iterations/v0.5/README.md`
- `docs/iterations/v0.5/0.5.7-v0.5-final-closeout/final-closeout.md`
- `docs/iterations/v0.3/README.md`
- `docs/releases/v0.3.md`
- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
