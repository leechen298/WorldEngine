# Backend

Status: v0.1 active backend

This folder contains the FastAPI backend used by the current WorldEngine v0.1
scaffold. The active implementation lives under `backend/app/`.

`backend/worldengine/` is legacy pre-v0.1 code and is not wired into the active
FastAPI application.

## Quick Start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend defaults to `http://localhost:8000`.

## Environment

| Variable | Default | Purpose |
|---|---:|---|
| `APP_HOST` | `0.0.0.0` | Host when running `python app/main.py`. |
| `APP_PORT` | `8000` | Port when running `python app/main.py`. |
| `CORS_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Allowed frontend origins. |
| `WORLD_STEP_SECONDS` | `600` | Seconds advanced per runtime step. |
| `WORLD_SNAPSHOT_INTERVAL_TICKS` | `10` | Snapshot creation interval. |
| `WORLD_SUMMARY_INTERVAL_TICKS` | `20` | Summary creation interval. |
| `WORLD_DRYRUN_STEPS` | `20` | Dry-run simulation length. |
| `WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK` | `20` | Dry-run event-rate limit. |
| `WORLD_DRYRUN_MAX_TOTAL_EVENTS` | `500` | Dry-run total event limit. |
| `WORLD_DRYRUN_MAX_FINAL_COUNTER` | `100000` | Dry-run counter upper bound. |

## Current API Groups

- `GET /health`
- `GET /runtime/state`
- `POST /runtime/step`
- `GET /world/events`
- `GET /world/event-steps`
- `GET /world/params`
- `POST /world/params/apply`
- `POST /world/agent/params/propose-and-apply`
- `GET /world/snapshots`
- `GET /world/snapshots/{snapshot_id}`
- `GET /world/summaries`
- `GET /world/summaries/{summary_id}`

See `../docs/api-reference-v0.1.md` for endpoint-level details.

## Current Runtime Behavior

- `RuntimeEngine` advances manual ticks through `/runtime/step`.
- `InMemoryEventLog` stores runtime, module, and params events.
- the default world module tree runs `heartbeat` and `counter` examples.
- world param patches are statically validated and dry-run before apply.
- snapshots and summaries are created in memory on configured intervals.
- `ParamsAgent` can propose and apply validated world param patches through a
  mock LLM provider.

v0.1 does not load `WorldSpec`, generate worlds, persist production world
state, or run an agent perception/action/memory loop.

## Structure

- `app/api` - FastAPI app factory, exception handling, and routes.
- `app/core` - clock, scheduler, event bus, and runtime engine.
- `app/world` - world state, params, modules, validation, dry-run, and archive.
- `app/agent` - params-agent service and LLM provider protocol.
- `app/infra` - placeholder repository ports and SQLite adapters.
- `app/schemas` - shared Pydantic models.
- `data` - placeholder seed JSON files; not an active WorldSpec input in v0.1.

## Verification

```bash
cd backend
.venv/bin/python -m pytest app/tests
```

Latest recorded closeout result:

- `63 passed in 2.93s`

See `../docs/testing/v0.1-test-map.md` and
`../docs/testing/results/2026-05-23-v0.1-closeout.md`.
