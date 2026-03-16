from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def test_apply_params_changes_counter_increment() -> None:
    app = create_app()
    client = TestClient(app)

    apply_response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": 2,
                }
            ]
        },
    )
    assert apply_response.status_code == 200
    assert apply_response.json()["data"] == {"counter": {"increment": 2}}

    client.post("/runtime/step")
    client.post("/runtime/step")

    events_response = client.get("/world/events?limit=200")
    assert events_response.status_code == 200

    counter_events = [
        event
        for event in events_response.json()["data"]
        if event["type"] == "module.counter"
    ]

    assert [event["payload"]["increment"] for event in counter_events] == [2, 2]
    assert [event["payload"]["counter"] for event in counter_events] == [2, 4]


def test_apply_params_can_disable_heartbeat() -> None:
    app = create_app()
    client = TestClient(app)

    apply_response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "heartbeat.enabled",
                    "value": False,
                }
            ]
        },
    )
    assert apply_response.status_code == 200

    step_response = client.post("/runtime/step")
    assert step_response.status_code == 200

    events_response = client.get("/world/events?limit=200")
    assert events_response.status_code == 200

    heartbeat_events = [
        event for event in events_response.json()["data"] if event["type"] == "module.tick"
    ]

    assert heartbeat_events == []


def test_params_applied_event_emitted() -> None:
    app = create_app()
    client = TestClient(app)

    apply_response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": 3,
                }
            ]
        },
    )
    assert apply_response.status_code == 200

    events_response = client.get("/world/events?limit=200")
    assert events_response.status_code == 200

    params_events = [
        event
        for event in events_response.json()["data"]
        if event["type"] == "params.applied"
    ]

    assert len(params_events) == 1
    assert params_events[0]["tick_id"] == 0
    assert params_events[0]["world_time_seconds"] == 0
    assert params_events[0]["payload"]["patches"] == [
        {
            "op": "set",
            "path": "counter.increment",
            "value": 3,
        }
    ]
    assert params_events[0]["payload"]["updated_at"]
