from fastapi.testclient import TestClient

from app.api.app_factory import create_app


def test_env_policy_is_used(monkeypatch) -> None:
    """Env-configured thresholds should be picked up by the dry-run validator."""
    monkeypatch.setenv("WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK", "1")
    monkeypatch.setenv("WORLD_DRYRUN_STEPS", "5")

    app = create_app()
    client = TestClient(app)

    # Default modules (heartbeat + counter) produce >=2 events/tick, so avg > 1 triggers event_flood.
    response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {"value": 2, "type": "number"},
                }
            ]
        },
    )

    assert response.status_code == 422
    payload = response.json()
    errors = payload["data"]["errors"]
    assert any(e["reason"] == "event_flood" for e in errors)
    assert payload["data"]["metrics"]["policy"]["max_avg_events_per_tick"] == 1


def test_world_override_takes_precedence() -> None:
    """World-level validation override should beat the engine default."""
    app = create_app()
    client = TestClient(app)

    # Set a very permissive override on the world state.
    app.state.world_state.set_validation_override({"max_avg_events_per_tick": 999})

    response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {"value": 2, "type": "number"},
                }
            ]
        },
    )

    assert response.status_code == 200


def test_world_override_reflected_in_metrics(monkeypatch) -> None:
    """When env sets a very low threshold but world override raises it, metrics.policy should reflect the override."""
    monkeypatch.setenv("WORLD_DRYRUN_MAX_AVG_EVENTS_PER_TICK", "1")
    monkeypatch.setenv("WORLD_DRYRUN_STEPS", "5")

    app = create_app()
    client = TestClient(app)

    # Override at world level to be permissive.
    app.state.world_state.set_validation_override({"max_avg_events_per_tick": 999})

    response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {"value": 2, "type": "number"},
                }
            ]
        },
    )

    # Should pass because override raised the threshold.
    assert response.status_code == 200


def test_env_policy_max_final_counter_reflected_in_metrics(monkeypatch) -> None:
    """Env-configured max_final_counter triggers numeric_divergence and appears in metrics."""
    monkeypatch.setenv("WORLD_DRYRUN_MAX_FINAL_COUNTER", "1")

    app = create_app()
    client = TestClient(app)

    response = client.post(
        "/world/params/apply",
        json={
            "patches": [
                {
                    "op": "set",
                    "path": "counter.increment",
                    "value": {"value": 2, "type": "number"},
                }
            ]
        },
    )

    assert response.status_code == 422
    payload = response.json()
    errors = payload["data"]["errors"]
    assert any(e["reason"] == "numeric_divergence" for e in errors)
    policy = payload["data"]["metrics"]["policy"]
    assert policy["max_final_counter"] == 1
    assert policy["dry_run_steps"] == 20
