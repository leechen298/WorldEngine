"""API route modules."""

from app.api.routes.archive import router as archive_router
from app.api.routes.health import router as health_router
from app.api.routes.runtime import router as runtime_router
from app.api.routes.world import router as world_router
from app.api.routes.world_agent import router as world_agent_router
from app.api.routes.world_generation import router as world_generation_router
from app.api.routes.world_params import router as world_params_router

__all__ = [
    "archive_router",
    "health_router",
    "runtime_router",
    "world_agent_router",
    "world_generation_router",
    "world_router",
    "world_params_router",
]
