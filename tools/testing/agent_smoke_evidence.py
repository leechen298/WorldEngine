#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


SUPPORTED_SCENARIOS = {
    "dashboard-basic-runtime",
    "dashboard-params-flow",
    "dashboard-invalid-param",
    "dashboard-agent-autotune",
}


def _request_api_data(base_url: str, path: str) -> Any:
    url = urljoin(base_url.rstrip("/") + "/", path.lstrip("/"))
    request = Request(url, method="GET", headers={"Accept": "application/json"})
    try:
        with urlopen(request, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise RuntimeError(f"GET {path} failed with HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"GET {path} failed: {exc.reason}") from exc

    if not isinstance(payload, dict) or payload.get("code") != 0:
        raise RuntimeError(f"GET {path} returned an invalid API envelope")
    return payload.get("data")


def collect_baseline_state(base_url: str) -> dict[str, Any]:
    health = _request_api_data(base_url, "/health")
    runtime = _request_api_data(base_url, "/runtime/state")
    params = _request_api_data(base_url, "/world/params")
    if not isinstance(health, dict) or not isinstance(runtime, dict) or not isinstance(params, dict):
        raise RuntimeError("Backend returned an unexpected baseline shape")
    return {
        "health_status": health.get("status"),
        "runtime": runtime,
        "world_params": params,
    }


def collect_current_state(base_url: str) -> dict[str, Any]:
    health = _request_api_data(base_url, "/health")
    runtime = _request_api_data(base_url, "/runtime/state")
    params = _request_api_data(base_url, "/world/params")
    events_page = _request_api_data(base_url, "/world/events?limit=200")
    if (
        not isinstance(health, dict)
        or not isinstance(runtime, dict)
        or not isinstance(params, dict)
        or not isinstance(events_page, dict)
        or not isinstance(events_page.get("items"), list)
    ):
        raise RuntimeError("Backend returned an unexpected current-state shape")
    return {
        "health": health,
        "runtime": runtime,
        "params": params,
        "events": events_page["items"],
    }


def _param_raw(params: dict[str, Any], path: str) -> Any:
    current: Any = params
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _param_value(params: dict[str, Any], path: str) -> Any:
    raw = _param_raw(params, path)
    if isinstance(raw, dict) and "value" in raw:
        return raw["value"]
    return raw


def _read_ui_targets(operation_log_path: Path | None) -> set[str]:
    if operation_log_path is None or not operation_log_path.exists():
        return set()

    targets: set[str] = set()
    for line in operation_log_path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            operation = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(operation, dict) and operation.get("type") == "ui":
            target = operation.get("target")
            if isinstance(target, str) and target.strip():
                targets.add(target)
    return targets


def _find_counter_increment_event(events: list[dict[str, Any]], before_tick: int | None) -> dict[str, Any] | None:
    for event in events:
        if event.get("type") != "module.counter":
            continue
        tick_id = event.get("tick_id")
        if before_tick is not None and isinstance(tick_id, int) and tick_id <= before_tick:
            continue
        payload = event.get("payload")
        if isinstance(payload, dict) and payload.get("increment") == 2:
            return event
    return None


def _find_agent_params_applied_event(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    for event in events:
        if event.get("type") != "params.applied":
            continue
        if event.get("source") != "agent.params":
            continue
        payload = event.get("payload")
        if not isinstance(payload, dict) or not isinstance(payload.get("patches"), list):
            continue
        return event
    return None


def _patch_paths(event: dict[str, Any] | None) -> list[str]:
    if event is None:
        return []
    payload = event.get("payload")
    if not isinstance(payload, dict):
        return []
    patches = payload.get("patches")
    if not isinstance(patches, list):
        return []
    paths: list[str] = []
    for patch in patches:
        if not isinstance(patch, dict):
            continue
        path = patch.get("path")
        if isinstance(path, str):
            paths.append(path)
    return paths


def build_api_summary_from_state(
    *,
    scenario: str,
    baseline: dict[str, Any],
    health: dict[str, Any],
    runtime: dict[str, Any],
    params: dict[str, Any],
    events: list[dict[str, Any]],
    operation_log_path: Path | None = None,
) -> dict[str, Any]:
    if scenario not in SUPPORTED_SCENARIOS:
        supported = ", ".join(sorted(SUPPORTED_SCENARIOS))
        raise ValueError(f"Unsupported scenario {scenario!r}; supported scenarios: {supported}")

    baseline_runtime = baseline.get("runtime")
    before_tick = baseline_runtime.get("tick_id") if isinstance(baseline_runtime, dict) else None
    after_tick = runtime.get("tick_id")
    base = {
        "scenario": scenario,
        "health_status": health.get("status"),
    }

    if scenario == "dashboard-basic-runtime":
        return {
            **base,
            "before_tick": before_tick,
            "after_tick": after_tick,
        }

    if scenario == "dashboard-params-flow":
        counter_event = _find_counter_increment_event(
            events,
            before_tick if isinstance(before_tick, int) else None,
        )
        counter_payload = counter_event.get("payload") if isinstance(counter_event, dict) else None
        return {
            **base,
            "param_path": "counter.increment",
            "expected_value": 2,
            "observed_value": _param_value(params, "counter.increment"),
            "before_tick": before_tick,
            "after_tick": after_tick,
            "counter_event_tick": counter_event.get("tick_id") if isinstance(counter_event, dict) else None,
            "counter_event_increment": counter_payload.get("increment") if isinstance(counter_payload, dict) else None,
        }

    if scenario == "dashboard-agent-autotune":
        before_params = baseline.get("world_params")
        baseline_increment = _param_value(before_params, "counter.increment") if isinstance(before_params, dict) else None
        observed_increment = _param_value(params, "counter.increment")
        applied_event = _find_agent_params_applied_event(events)
        patch_paths = _patch_paths(applied_event)
        ui_targets = _read_ui_targets(operation_log_path)
        return {
            **base,
            "baseline_counter_increment": baseline_increment,
            "observed_counter_increment": observed_increment,
            "counter_changed": baseline_increment != observed_increment,
            "patches_count": len(patch_paths),
            "patch_paths": patch_paths,
            "params_applied_event_seen": applied_event is not None,
            "params_applied_event_source": applied_event.get("source") if isinstance(applied_event, dict) else None,
            "ui_success_seen": "world-agent-success" in ui_targets,
            "ui_patches_seen": "world-agent-patches" in ui_targets,
        }

    before_params = baseline.get("world_params")
    ui_targets = _read_ui_targets(operation_log_path)
    return {
        **base,
        "invalid_path": "system.secret",
        "before_params": before_params,
        "after_params": params,
        "params_unchanged": before_params == params,
        "ui_error_seen": "world-params-error" in ui_targets,
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _cmd_baseline(args: argparse.Namespace) -> int:
    baseline = collect_baseline_state(args.base_url)
    _write_json(args.out, baseline)
    return 0


def _cmd_collect(args: argparse.Namespace) -> int:
    baseline = json.loads(args.baseline.read_text())
    current = collect_current_state(args.base_url)
    operation_log_path = args.operation_log
    if operation_log_path is None:
        candidate = args.out.parent / "operation-log.jsonl"
        operation_log_path = candidate if candidate.exists() else None

    summary = build_api_summary_from_state(
        scenario=args.scenario,
        baseline=baseline,
        health=current["health"],
        runtime=current["runtime"],
        params=current["params"],
        events=current["events"],
        operation_log_path=operation_log_path,
    )
    _write_json(args.out, summary)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate deterministic Agent smoke API evidence.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    baseline = subparsers.add_parser("baseline", help="Collect pre-action backend state.")
    baseline.add_argument("--base-url", required=True)
    baseline.add_argument("--out", type=Path, required=True)
    baseline.set_defaults(func=_cmd_baseline)

    collect = subparsers.add_parser("collect", help="Collect scenario-specific checker evidence.")
    collect.add_argument("--scenario", choices=sorted(SUPPORTED_SCENARIOS), required=True)
    collect.add_argument("--base-url", required=True)
    collect.add_argument("--baseline", type=Path, required=True)
    collect.add_argument("--out", type=Path, required=True)
    collect.add_argument("--operation-log", type=Path, default=None)
    collect.set_defaults(func=_cmd_collect)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
