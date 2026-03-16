import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import health_router, runtime_router, world_router
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine


def create_app() -> FastAPI:
    app = FastAPI(
        title="WorldEngine Backend",
        version="0.1.0",
        description="V1 scaffold API for WorldEngine.",
    )

    cors_origins = os.getenv(
        "CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin.strip() for origin in cors_origins.split(",") if origin],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.state.event_log = InMemoryEventLog()
    app.state.runtime_engine = RuntimeEngine.from_env(event_log=app.state.event_log)
    app.include_router(health_router)
    app.include_router(runtime_router)
    app.include_router(world_router)
    return app
