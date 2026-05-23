# WorldEngine

Status: v0.1 scaffold complete, v0.2 planned.

WorldEngine is a recursive world generation and runtime engine. The current
v0.1 branch is an experimental monorepo scaffold that proves the first runtime,
event, params, archive, agent-assist, and dashboard surfaces. It is not yet a
recursive world engine implementation.

Read first:

- `docs/project-north-star.md`
- `docs/product-model.md`
- `docs/current-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/releases/v0.1.md`
- `docs/iterations/README.md`

## Repository Structure

- `backend/` - FastAPI service.
- `frontend/` - Vue 3 + TypeScript dashboard.
- `docs/` - architecture, release, roadmap, and iteration documents.
- `backend/app/` - active backend path.
- `backend/worldengine/` - legacy pre-v0.1 path; do not add new features there.

## Current v0.1 Capability

v0.1 can:

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
- render a dashboard for runtime controls, timeline, world params, and agent
  params interactions.

v0.1 cannot:

- represent recursive `WorldCell` structures.
- load a structured `WorldSpec`.
- generate worlds from templates or prompts.
- run agents through a perception/action/memory loop.
- model agent pseudo-self continuity.
- run a reference village world.
- provide a user-facing game surface.

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

Latest v0.1 closeout verification is recorded in
`docs/testing/results/2026-05-23-v0.1-closeout.md`.

Fresh results from that pass:

- backend: `63 passed`.
- frontend unit tests: `24 passed`.
- frontend production build: succeeded with a chunk-size warning.

Implementation docs:

- `docs/current-implementation.md`
- `docs/backend-implementation.md`
- `docs/frontend-implementation.md`
- `docs/api-reference-v0.1.md`
- `docs/testing/v0.1-test-map.md`
