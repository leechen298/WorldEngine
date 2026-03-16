# Backend (FastAPI)

This folder contains the V1 scaffold backend for WorldEngine.

## Quick Start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API

- `GET /health`: returns a basic service status payload.

## Structure

- `app/api`: FastAPI app factory and routes
- `app/core`: clock, scheduler, event bus, runtime engine placeholders
- `app/world` and `app/agent`: domain services placeholders
- `app/infra`: repository ports and SQLite adapters
- `app/schemas`: shared Pydantic models
- `data`: seed JSON files
