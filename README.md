# WorldEngine

WorldEngine is an engine for generating a world, advancing its authoritative
history, running Agents, accepting bounded interventions, and publishing public
projections to independent clients.

Current work is driven by the runnable MVP contract in
[`docs/current/MVP.zh.md`](docs/current/MVP.zh.md). Historical version packages
under `docs/iterations/` are retained as reference, not as active workflow gates.

## Repository

- `backend/app/`: active FastAPI engine and public API.
- `frontend/`: Vue administration console.
- `backend/worldengine/`: legacy code; do not add new runtime features there.
- External renderers and validation clients live in separate repositories.

## Run

```bash
make setup
make dev
```

Backend: <http://127.0.0.1:8000>

Administration console: <http://127.0.0.1:5173>

Runnable anchor: <http://127.0.0.1:5173/admin/runnable-anchor>

## Verify

```bash
make test-mvp
make smoke-mvp
make test
```

MVP completion additionally requires the independent external Godot client and
checker flow defined in the current contract.

Chinese README: [`README.zh.md`](README.zh.md)
