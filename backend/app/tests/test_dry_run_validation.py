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
