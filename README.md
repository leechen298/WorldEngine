# WorldEngine
## Monorepo V1 Development

This repository is now scaffolded as a monorepo with:

- `backend/` FastAPI service
- `frontend/` Vue 3 + TypeScript dashboard
- `docs/` architecture notes

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
npm install
npm run dev
```

Default frontend API target is `http://localhost:8000` (configure via `VITE_API_BASE_URL`).
