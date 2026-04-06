from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.routes import health_router, runtime_router, world_params_router, world_router
from app.core.event_bus import InMemoryEventLog
from app.core.runtime_engine import RuntimeEngine
from app.schemas.api import ApiErrorResponse
from app.world.dry_run import ParamDryRunValidator
from app.world.service import get_default_module_tree
from app.world.state import WorldState
from app.world.validation import ParamRegistry, ParamValidator


def _error_code_from_status(status_code: int) -> int:
    error_codes = {
        400: 10,
        401: 20,
        403: 21,
        404: 24,
        409: 29,
        422: 30,
        500: 50,
    }
    return error_codes.get(status_code, status_code)


def _stringify_detail(detail: object, fallback: str) -> str:
    if isinstance(detail, str):
        return detail
    if isinstance(detail, dict):
        for key in ("msg", "detail", "message"):
            value = detail.get(key)
            if isinstance(value, str) and value:
                return value
    if isinstance(detail, list) and detail:
        first_error = detail[0]
        if isinstance(first_error, dict):
            return str(first_error.get("msg", fallback))
    return fallback


def _data_from_detail(detail: object) -> object | None:
    if not isinstance(detail, dict):
        return None
    data = detail.get("data")
    if data is not None:
        return data
    if "errors" in detail:
        result: dict[str, object] = {"errors": detail["errors"]}
        if "metrics" in detail:
            result["metrics"] = detail["metrics"]
        return result
    return None


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
    app.state.world_state = WorldState()
    app.state.world_root_module = get_default_module_tree()
    app.state.param_validator = ParamValidator(ParamRegistry.default())
    app.state.param_dry_run_validator = ParamDryRunValidator.from_env()
    app.state.runtime_engine = RuntimeEngine.from_env(
        event_log=app.state.event_log,
        world_root_module=app.state.world_root_module,
        params_provider=app.state.world_state.get_params,
    )

    @app.exception_handler(StarletteHTTPException)
    async def handle_http_exception(_, exc: StarletteHTTPException) -> JSONResponse:
        payload = ApiErrorResponse(
            code=_error_code_from_status(exc.status_code),
            msg=_stringify_detail(exc.detail, "Request failed"),
            data=_data_from_detail(exc.detail),
        )
        return JSONResponse(status_code=exc.status_code, content=payload.model_dump())

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(_, exc: RequestValidationError) -> JSONResponse:
        payload = ApiErrorResponse(
            code=_error_code_from_status(422),
            msg=_stringify_detail(exc.errors(), "Validation error"),
            data={"errors": exc.errors()},
        )
        return JSONResponse(status_code=422, content=payload.model_dump())

    app.include_router(health_router)
    app.include_router(runtime_router)
    app.include_router(world_router)
    app.include_router(world_params_router)
    return app
