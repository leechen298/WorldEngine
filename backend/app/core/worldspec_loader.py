import json
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Sequence, Tuple

from pydantic import ValidationError

from app.schemas.world_cell import WorldSpec


@dataclass(frozen=True)
class LoadedWorldSpec:
    worldspec: WorldSpec
    source_type: str
    source_label: Optional[str]
    schema_version: str


@dataclass(frozen=True)
class WorldSpecLoaderError:
    code: str
    message: str
    path: Optional[str]
    source_type: str
    source_label: Optional[str]


@dataclass(frozen=True)
class WorldSpecLoaderResult:
    success: bool
    loaded: Optional[LoadedWorldSpec] = None
    errors: Tuple[WorldSpecLoaderError, ...] = ()


def load_worldspec(value: Any, *, source_label: Optional[str] = None) -> WorldSpecLoaderResult:
    if isinstance(value, Mapping):
        return _validate_worldspec(value, source_type="mapping", source_label=source_label)

    if isinstance(value, (str, bytes)):
        try:
            parsed = json.loads(value)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            return _failure(
                "parse_error",
                f"input is not valid JSON: {exc}",
                path=None,
                source_type="json",
                source_label=source_label,
            )
        return _validate_worldspec(parsed, source_type="json", source_label=source_label)

    return _failure(
        "unsupported_input",
        f"unsupported WorldSpec input type: {type(value).__name__}",
        path=None,
        source_type="unsupported",
        source_label=source_label,
    )


def _validate_worldspec(
    value: Any, *, source_type: str, source_label: Optional[str]
) -> WorldSpecLoaderResult:
    try:
        worldspec = WorldSpec.model_validate(value)
    except ValidationError as exc:
        errors = tuple(
            WorldSpecLoaderError(
                code="schema_validation_error",
                message=str(error.get("msg", "schema validation failed")),
                path=_json_pointer(error.get("loc", ())),
                source_type=source_type,
                source_label=source_label,
            )
            for error in exc.errors()
        )
        return WorldSpecLoaderResult(success=False, errors=errors)

    loaded = LoadedWorldSpec(
        worldspec=worldspec,
        source_type=source_type,
        source_label=source_label,
        schema_version=worldspec.schema_version,
    )
    return WorldSpecLoaderResult(success=True, loaded=loaded)


def _failure(
    code: str,
    message: str,
    *,
    path: Optional[str],
    source_type: str,
    source_label: Optional[str],
) -> WorldSpecLoaderResult:
    error = WorldSpecLoaderError(
        code=code,
        message=message,
        path=path,
        source_type=source_type,
        source_label=source_label,
    )
    return WorldSpecLoaderResult(success=False, errors=(error,))


def _json_pointer(loc: Sequence[Any]) -> str:
    if not loc:
        return "/"
    return "/" + "/".join(_escape_pointer_segment(segment) for segment in loc)


def _escape_pointer_segment(segment: Any) -> str:
    return str(segment).replace("~", "~0").replace("/", "~1")
