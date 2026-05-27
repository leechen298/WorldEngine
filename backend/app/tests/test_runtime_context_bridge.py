from dataclasses import asdict

from app.core.event_bus import InMemoryEventLog
from app.core.runtime_context import (
    RuntimeContextBridgeError,
    build_runtime_context,
    summarize_runtime_context,
)
from app.core.runtime_engine import RuntimeEngine
from app.core.worldspec_loader import LoadedWorldSpec, load_worldspec
from app.schemas.world_cell import WorldSpec


def _payload() -> dict:
    return {
        "schema_version": "0.2",
        "id": "worldspec-neutral",
        "label": "Neutral WorldSpec",
        "root": {
            "id": "cell-root",
            "label": "Cell Root",
            "kind": "world",
            "entity_refs": [],
            "child_cells": [],
            "metadata": {},
        },
        "metadata": {"purpose": "bridge-test"},
    }


def _loaded_worldspec() -> LoadedWorldSpec:
    result = load_worldspec(_payload(), source_label="neutral-input")
    assert result.success is True
    assert result.loaded is not None
    return result.loaded


def test_build_runtime_context_derives_context_from_loaded_worldspec() -> None:
    result = build_runtime_context(_loaded_worldspec())

    assert result.success is True
    assert result.context is not None
    assert result.errors == ()
    assert result.context.worldspec_id == "worldspec-neutral"
    assert result.context.schema_version == "0.2"
    assert result.context.root_cell_id == "cell-root"
    assert result.context.root_cell_type == "world"
    assert result.context.source_type == "mapping"
    assert result.context.source_label == "neutral-input"
    assert result.context.metadata == {}


def test_build_runtime_context_rejects_unsupported_input() -> None:
    result = build_runtime_context(_payload())

    assert result.success is False
    assert result.context is None
    assert len(result.errors) == 1
    assert result.errors[0].code == "unsupported_input"


def test_build_runtime_context_rejects_unsuccessful_loader_result() -> None:
    loader_result = load_worldspec(["not", "valid"])

    result = build_runtime_context(loader_result)

    assert result.success is False
    assert result.errors[0].code == "unsupported_input"


def test_build_runtime_context_rejects_incomplete_loaded_output() -> None:
    loaded = LoadedWorldSpec(
        worldspec=None,  # type: ignore[arg-type]
        source_type="mapping",
        source_label="invalid-loaded",
        schema_version="0.2",
    )

    result = build_runtime_context(loaded)

    assert result.success is False
    assert result.errors[0].code == "invalid_loaded_worldspec"
    assert result.errors[0].path == "/worldspec"
    assert result.errors[0].source_type == "mapping"
    assert result.errors[0].source_label == "invalid-loaded"


def test_build_runtime_context_rejects_inconsistent_loaded_output() -> None:
    loaded = _loaded_worldspec()
    inconsistent = LoadedWorldSpec(
        worldspec=loaded.worldspec,
        source_type=loaded.source_type,
        source_label=loaded.source_label,
        schema_version="9.9",
    )

    result = build_runtime_context(inconsistent)

    assert result.success is False
    assert result.errors[0].code == "invalid_loaded_worldspec"
    assert result.errors[0].path == "/schema_version"


def test_build_runtime_context_reports_derivation_errors() -> None:
    class Unstringable:
        def __str__(self) -> str:
            raise RuntimeError("cannot stringify")

    worldspec = WorldSpec.model_validate(_payload())
    loaded = LoadedWorldSpec(
        worldspec=worldspec,
        source_type=Unstringable(),  # type: ignore[arg-type]
        source_label=None,
        schema_version=worldspec.schema_version,
    )

    result = build_runtime_context(loaded)

    assert result.success is False
    assert result.errors == (
        RuntimeContextBridgeError(
            code="context_derivation_error",
            message="failed to derive runtime context: cannot stringify",
            path=None,
            source_type=None,
            source_label=None,
        ),
    )


def test_context_summary_contains_only_bounded_diagnostic_fields() -> None:
    result = build_runtime_context(_loaded_worldspec())
    assert result.context is not None

    summary = summarize_runtime_context(result.context)

    assert asdict(summary) == {
        "worldspec_id": "worldspec-neutral",
        "schema_version": "0.2",
        "root_cell_id": "cell-root",
        "root_cell_type": "world",
        "source_type": "mapping",
        "source_label": "neutral-input",
        "metadata": {},
    }
    assert "worldspec" not in asdict(summary)
    assert "root" not in asdict(summary)


def test_runtime_engine_defaults_work_without_context() -> None:
    engine = RuntimeEngine()

    before = engine.get_state()
    after = engine.step()

    assert engine.get_runtime_context() is None
    assert before.tick_id == 0
    assert after.tick_id == 1
    assert after.world_time_seconds == before.world_time_seconds + after.step_seconds


def test_runtime_engine_from_env_defaults_work_without_context(monkeypatch) -> None:
    monkeypatch.setenv("WORLD_STEP_SECONDS", "60")

    engine = RuntimeEngine.from_env()

    assert engine.get_runtime_context() is None
    assert engine.get_state().step_seconds == 60


def test_runtime_engine_context_storage_is_inert_for_step_output() -> None:
    context_result = build_runtime_context(_loaded_worldspec())
    assert context_result.context is not None
    engine = RuntimeEngine(step_seconds=600, runtime_context=context_result.context)

    state = engine.step()

    assert engine.get_runtime_context() == context_result.context
    assert state.tick_id == 1
    assert state.world_time_seconds == 600
    assert state.step_seconds == 600
    assert not hasattr(state, "runtime_context")


def test_runtime_engine_with_context_does_not_emit_raw_worldspec_payloads() -> None:
    context_result = build_runtime_context(_loaded_worldspec())
    assert context_result.context is not None
    event_log = InMemoryEventLog()
    engine = RuntimeEngine(
        step_seconds=600,
        event_log=event_log,
        runtime_context=context_result.context,
    )

    engine.step()

    events = event_log.list()
    assert events
    assert all("worldspec" not in event.payload for event in events)
    assert all("root" not in event.payload for event in events)
    assert all(event.payload != _payload() for event in events)
