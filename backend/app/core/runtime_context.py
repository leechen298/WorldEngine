from dataclasses import dataclass, field
from typing import Any, Mapping, Optional, Tuple

from app.core.worldspec_loader import LoadedWorldSpec
from app.schemas.world_cell import WorldSpec


@dataclass(frozen=True)
class RuntimeContext:
    worldspec_id: str
    schema_version: str
    root_cell_id: str
    root_cell_type: str
    source_type: str
    source_label: Optional[str]
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RuntimeContextSummary:
    worldspec_id: str
    schema_version: str
    root_cell_id: str
    root_cell_type: str
    source_type: str
    source_label: Optional[str]
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RuntimeContextBridgeError:
    code: str
    message: str
    path: Optional[str]
    source_type: Optional[str] = None
    source_label: Optional[str] = None


@dataclass(frozen=True)
class RuntimeContextBridgeResult:
    success: bool
    context: Optional[RuntimeContext] = None
    errors: Tuple[RuntimeContextBridgeError, ...] = ()


class _RuntimeContextDerivationError(Exception):
    def __init__(self, error: RuntimeContextBridgeError) -> None:
        super().__init__(error.message)
        self.error = error


def build_runtime_context(value: Any) -> RuntimeContextBridgeResult:
    if not isinstance(value, LoadedWorldSpec):
        return _failure(
            "unsupported_input",
            f"unsupported runtime context input type: {type(value).__name__}",
            path=None,
        )

    if not isinstance(value.worldspec, WorldSpec):
        return _failure(
            "invalid_loaded_worldspec",
            "loaded WorldSpec is missing or invalid",
            path="/worldspec",
            source_type=_safe_source_type(value),
            source_label=_safe_source_label(value),
        )

    worldspec = value.worldspec
    root = worldspec.root
    if value.schema_version != worldspec.schema_version:
        return _failure(
            "invalid_loaded_worldspec",
            "loaded schema_version does not match WorldSpec schema_version",
            path="/schema_version",
            source_type=_safe_source_type(value),
            source_label=_safe_source_label(value),
        )

    try:
        context = RuntimeContext(
            worldspec_id=_required_text(worldspec.id, path="/id"),
            schema_version=_required_text(worldspec.schema_version, path="/schema_version"),
            root_cell_id=_required_text(root.id, path="/root/id"),
            root_cell_type=_required_text(root.kind, path="/root/kind"),
            source_type=_required_text(value.source_type, path="/source_type"),
            source_label=_optional_text(value.source_label, path="/source_label"),
            metadata={},
        )
    except _RuntimeContextDerivationError as exc:
        error = exc.error
        if error.source_type is None and error.source_label is None:
            error = RuntimeContextBridgeError(
                code=error.code,
                message=error.message,
                path=error.path,
                source_type=_safe_source_type(value),
                source_label=_safe_source_label(value),
            )
        return RuntimeContextBridgeResult(success=False, errors=(error,))
    except Exception as exc:
        return _failure(
            "context_derivation_error",
            f"failed to derive runtime context: {exc}",
            path=None,
            source_type=_safe_source_type(value),
            source_label=_safe_source_label(value),
        )

    return RuntimeContextBridgeResult(success=True, context=context)


def summarize_runtime_context(context: RuntimeContext) -> RuntimeContextSummary:
    return RuntimeContextSummary(
        worldspec_id=context.worldspec_id,
        schema_version=context.schema_version,
        root_cell_id=context.root_cell_id,
        root_cell_type=context.root_cell_type,
        source_type=context.source_type,
        source_label=context.source_label,
        metadata=dict(context.metadata),
    )


def _failure(
    code: str,
    message: str,
    *,
    path: Optional[str],
    source_type: Optional[str] = None,
    source_label: Optional[str] = None,
) -> RuntimeContextBridgeResult:
    error = RuntimeContextBridgeError(
        code=code,
        message=message,
        path=path,
        source_type=source_type,
        source_label=source_label,
    )
    return RuntimeContextBridgeResult(success=False, errors=(error,))


def _required_text(value: Any, *, path: str) -> str:
    text = str(value)
    if not text:
        raise _RuntimeContextDerivationError(
            RuntimeContextBridgeError(
                code="context_derivation_error",
                message=f"required runtime context field is empty: {path}",
                path=path,
            )
        )
    return text


def _optional_text(value: Any, *, path: str) -> Optional[str]:
    if value is None:
        return None
    text = str(value)
    if not text:
        raise _RuntimeContextDerivationError(
            RuntimeContextBridgeError(
                code="context_derivation_error",
                message=f"optional runtime context field is empty: {path}",
                path=path,
            )
        )
    return text


def _safe_source_type(value: LoadedWorldSpec) -> Optional[str]:
    source_type = value.source_type
    if isinstance(source_type, str):
        return source_type
    return None


def _safe_source_label(value: LoadedWorldSpec) -> Optional[str]:
    source_label = value.source_label
    if source_label is None or isinstance(source_label, str):
        return source_label
    return None
