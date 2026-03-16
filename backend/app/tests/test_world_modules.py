from fastapi.testclient import TestClient

from app.api.app_factory import create_app
from app.world.module_types import TickContext
from app.world.modules.composite import CompositeModule
from app.world.service import get_default_module_tree


def test_step_emits_module_events_into_world_events() -> None:
    app = create_app()
    client = TestClient(app)

    client.post("/runtime/step")
    client.post("/runtime/step")

    response = client.get("/world/events")
    assert response.status_code == 200

    events = response.json()["data"]
    event_types = {event["type"] for event in events}

    assert "tick.advanced" in event_types
    assert "module.tick" in event_types
    assert "module.counter" in event_types


def test_counter_module_increments_across_ticks() -> None:
    app = create_app()
    client = TestClient(app)

    client.post("/runtime/step")
    client.post("/runtime/step")
    client.post("/runtime/step")

    response = client.get("/world/events?limit=200")
    assert response.status_code == 200

    counter_events = [
        event for event in response.json()["data"] if event["type"] == "module.counter"
    ]

    assert len(counter_events) == 3
    assert [event["payload"]["counter"] for event in counter_events] == [1, 2, 3]
    assert all(event["payload"]["module_path"] == "root.counter" for event in counter_events)


def test_module_events_include_module_path_payload() -> None:
    app = create_app()
    client = TestClient(app)

    client.post("/runtime/step")

    response = client.get("/world/events")
    assert response.status_code == 200

    module_events = [
        event
        for event in response.json()["data"]
        if event["type"] in {"module.tick", "module.counter", "module.aggregate"}
    ]

    assert module_events
    module_paths = {event["payload"].get("module_path") for event in module_events}
    assert "root.heartbeat" in module_paths or "root.counter" in module_paths


def test_module_tick_has_module_path() -> None:
    app = create_app()
    client = TestClient(app)

    client.post("/runtime/step")

    response = client.get("/world/events?limit=200")
    assert response.status_code == 200

    heartbeat_events = [
        event for event in response.json()["data"] if event["type"] == "module.tick"
    ]

    assert len(heartbeat_events) == 1
    assert heartbeat_events[0]["payload"]["module_path"] == "root.heartbeat"


def test_default_module_tree_assigns_stable_child_paths() -> None:
    root_module = get_default_module_tree()

    assert isinstance(root_module, CompositeModule)
    assert root_module.module_path == "root"
    assert [child.module_path for child in root_module.children] == [
        "root.heartbeat",
        "root.counter",
    ]


def test_composite_module_emits_child_events_before_aggregate() -> None:
    root_module = get_default_module_tree()

    result = root_module.on_tick(TickContext(tick_id=1, world_time_seconds=600))

    assert [event.type for event in result.events] == [
        "module.tick",
        "module.counter",
        "module.aggregate",
    ]
    assert result.events[-1].payload["module_path"] == "root"
    assert result.events[-1].payload["child_count"] == 2
