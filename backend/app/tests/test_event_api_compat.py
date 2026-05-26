from fastapi.testclient import TestClient

from app.api.app_factory import create_app
from app.schemas.event import Event


LEGACY_EVENT_KEYS = {
    "id",
    "tick_id",
    "world_time_seconds",
    "type",
    "source",
    "payload",
    "created_at",
}


def test_world_event_endpoints_omit_empty_refs_for_existing_events() -> None:
    app = create_app()
    client = TestClient(app)

    step_response = client.post("/runtime/step")
    assert step_response.status_code == 200

    events_response = client.get("/world/events?limit=200")
    assert events_response.status_code == 200
    events = events_response.json()["data"]["items"]
    assert events
    assert all(set(event) == LEGACY_EVENT_KEYS for event in events)

    steps_response = client.get("/world/event-steps?limit=200")
    assert steps_response.status_code == 200
    step_events = [
        event
        for step in steps_response.json()["data"]["items"]
        for event in step["items"]
    ]
    assert step_events
    assert all(set(event) == LEGACY_EVENT_KEYS for event in step_events)


def test_world_event_endpoints_include_non_empty_refs() -> None:
    app = create_app()
    app.state.event_log.append(
        Event(
            id="event-with-ref",
            tick_id=1,
            world_time_seconds=30,
            type="reference.annotated",
            source="system",
            payload={"message": "annotated"},
            refs=[
                {
                    "id": "ref-1",
                    "kind": "generic_ref",
                    "role": "target",
                    "metadata": {"source": "test"},
                }
            ],
            created_at="2026-05-26T00:00:00Z",
        )
    )
    client = TestClient(app)

    events_response = client.get("/world/events?limit=1")
    assert events_response.status_code == 200
    event = events_response.json()["data"]["items"][0]
    assert event["id"] == "event-with-ref"
    assert event["refs"] == [
        {
            "id": "ref-1",
            "kind": "generic_ref",
            "role": "target",
            "metadata": {"source": "test"},
        }
    ]

    steps_response = client.get("/world/event-steps?limit=1")
    assert steps_response.status_code == 200
    step_event = steps_response.json()["data"]["items"][0]["items"][0]
    assert step_event["id"] == "event-with-ref"
    assert step_event["refs"] == event["refs"]
