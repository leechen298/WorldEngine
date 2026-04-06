from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _event_items(response) -> list[dict]:
    return response.json()["data"]["items"]


def test_dry_run_rejects_huge_increment() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {
                        "value": 1000000,
                        "type": "number",
                    },
                }
            ]
        },
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["data"]["errors"][0]["reason"] in {"numeric_divergence", "out_of_range"}
    assert client.get("/world/params").json()["data"] == {}


def test_dry_run_accepts_reasonable_increment() -> None:
    app = create_app()
    client = TestClient(app)

    apply_response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {
                        "value": 2,
                        "type": "number",
                    },
                }
            ]
        },
    )

    assert apply_response.status_code == 200

    client.post("/runtime/step")
    client.post("/runtime/step")

    events_response = client.get("/world/events?limit=200")
    assert events_response.status_code == 200

    counter_events = [event for event in _event_items(events_response) if event["type"] == "module.counter"]
    counter_events.sort(key=lambda event: event["tick_id"])

    assert [event["payload"]["increment"] for event in counter_events] == [2, 2]
    assert [event["payload"]["counter"] for event in counter_events] == [2, 4]


def test_static_and_dry_run_errors_share_same_shape() -> None:
    """Both validator paths must return errors with the same field set."""
    app = create_app()
    client = TestClient(app)

    static_response = client.post(
        "/world/params/apply",
        json={"patches": [{"op": "set", "path": "unknown.foo", "value": 1}]},
    )
    dry_run_response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {"op": "set", "path": "counter.increment", "value": {"value": 1000000, "type": "number"}},
            ]
        },
    )

    assert static_response.status_code == 422
    assert dry_run_response.status_code == 422

    static_error = static_response.json()["data"]["errors"][0]
    dry_run_error = dry_run_response.json()["data"]["errors"][0]

    required_keys = {"path", "reason", "expected", "got", "detail"}
    assert set(static_error.keys()) == required_keys
    assert set(dry_run_error.keys()) == required_keys

    assert isinstance(static_error["detail"], str)
    assert isinstance(dry_run_error["detail"], str)


def test_dry_run_does_not_pollute_main_module_state() -> None:
    """Dry-run must use a fresh module tree so the main world counter starts from 1."""
    app = create_app()
    client = TestClient(app)

    # Apply a patch (triggers dry-run internally), then step the main world once.
    apply_response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {"value": 3, "type": "number"},
                }
            ]
        },
    )
    assert apply_response.status_code == 200

    client.post("/runtime/step")

    events_response = client.get("/world/events?limit=200")
    counter_events = [
        e for e in _event_items(events_response) if e["type"] == "module.counter"
    ]

    # The main counter should start at 3 (increment=3 from tick 1), not some large
    # value carried over from the dry-run's 20 ticks.
    assert counter_events[0]["payload"]["counter"] == 3


def test_dry_run_error_includes_metrics() -> None:
    app = create_app()
    client = TestClient(app)

    response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "heartbeat.enabled",
                    "value": {
                        "value": False,
                        "type": "boolean",
                    },
                },
                {
                    "op": "set",
                    "path": "heartbeat.enabled",
                    "value": {
                        "value": True,
                        "type": "boolean",
                    },
                },
            ]
        },
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["msg"] == "Dry-run validation failed"
    assert payload["data"]["errors"][0]["reason"] == "high_frequency_toggle"
    assert payload["data"]["metrics"]["avg_events_per_tick"] >= 0
    assert "total_events" in payload["data"]["metrics"]
