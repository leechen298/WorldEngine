from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def _apply(client: TestClient, patches: list[dict]):
    return client.post("/world/params/apply", json={"patches": patches})


def _event_items(response) -> list[dict]:
    return response.json()["data"]["items"]


def test_unknown_path_is_rejected() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [{"op": "set", "path": "unknown.foo", "value": 1}],
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["code"] == 30
    assert payload["data"]["errors"][0]["reason"] == "unknown_path"


def test_reserved_prefix_is_rejected() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [{"op": "set", "path": "system.secret", "value": "x"}],
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["data"]["errors"][0]["reason"] == "reserved_prefix"


def test_counter_increment_type_mismatch_is_rejected() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [
            {
                "op": "set",
                "path": "counter.increment",
                "value": {"value": "abc", "type": "string"},
            }
        ],
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["data"]["errors"][0]["reason"] == "type_mismatch"


def test_counter_increment_out_of_range_is_rejected() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [
            {
                "op": "set",
                "path": "counter.increment",
                "value": {"value": 999999, "type": "number"},
            }
        ],
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["data"]["errors"][0]["reason"] == "out_of_range"


def test_heartbeat_enabled_type_mismatch_is_rejected() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [
            {
                "op": "set",
                "path": "heartbeat.enabled",
                "value": {"value": 1, "type": "number"},
            }
        ],
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["data"]["errors"][0]["reason"] == "type_mismatch"


def test_valid_patch_is_applied_and_used_by_modules() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [
            {
                "op": "set",
                "path": "counter.increment",
                "value": {"value": 2, "type": "number"},
            }
        ],
    )

    assert response.status_code == 200
    assert response.json()["data"]["counter"]["increment"]["value"] == 2

    client.post("/runtime/step")
    events_response = client.get("/world/events?limit=200")
    counter_events = [
        event for event in _event_items(events_response) if event["type"] == "module.counter"
    ]

    assert counter_events[0]["payload"]["increment"] == 2


def test_invalid_patch_uses_api_error_response_shape() -> None:
    client = TestClient(create_app())

    response = _apply(
        client,
        [{"op": "set", "path": "unknown.foo", "value": 1}],
    )

    assert response.status_code == 422
    payload = response.json()
    assert payload["code"] == 30
    assert payload["msg"] == "Param validation failed"
    assert payload["data"]["errors"]
