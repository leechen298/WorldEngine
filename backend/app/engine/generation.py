from __future__ import annotations

import hashlib
import json
from typing import Any, Dict

from app.schemas.engine_v1 import (
    PackageReadiness,
    RunnableWorldPackage,
    SCHEMA_VERSION,
    STATE_HASH_ALGORITHM,
    WorldBrief,
)


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    )


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _normalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _normalize(value[key]) for key in sorted(value)}
    if isinstance(value, list):
        normalized = [_normalize(item) for item in value]
        return sorted(normalized, key=canonical_json)
    return value


def normalize_brief(brief: WorldBrief) -> WorldBrief:
    state_variables = sorted(brief.state_variables, key=lambda item: item.key)
    return WorldBrief(
        seed=brief.seed,
        premise=brief.premise.strip(),
        constraints=_normalize(brief.constraints),
        scale_bounds=brief.scale_bounds,
        state_variables=state_variables,
        agent_count=brief.agent_count,
        step_seconds=brief.step_seconds,
    )


def build_runnable_package(brief: WorldBrief) -> RunnableWorldPackage:
    normalized = normalize_brief(brief)
    normalized_brief = normalized.model_dump(mode="json")
    brief_digest = canonical_hash(normalized_brief)
    world_id = f"world-{brief_digest[:16]}"
    agent_id = f"agent-{brief_digest[16:28]}"
    location_id = f"location-{brief_digest[28:40]}"
    entity_id = f"entity-{brief_digest[40:52]}"

    variables = [item.model_dump(mode="json") for item in normalized.state_variables]
    initial_state = {item.key: item.initial for item in normalized.state_variables}

    rule_catalog = [
        {
            "rule_id": "rule.session.ready-package",
            "kind": "session_boot_precondition",
            "evidence_required": True,
        },
        {
            "rule_id": "rule.runtime.lockstep",
            "kind": "bounded_tick_advance",
            "evidence_required": True,
        },
        {
            "rule_id": "rule.direction.no-direct-fact",
            "kind": "operator_boundary",
            "direct_final_fact_allowed": False,
            "evidence_required": True,
        },
        {
            "rule_id": "rule.feedback.manifest",
            "kind": "typed_feedback_boundary",
            "evidence_required": True,
        },
    ]
    action_catalog = []
    for item in normalized.state_variables:
        rule_catalog.append(
            {
                "rule_id": f"rule.range.{item.key}",
                "kind": "bounded_numeric_transition",
                "target_ref": item.key,
                "minimum": item.minimum,
                "maximum": item.maximum,
                "max_delta": item.step * 3,
                "evidence_required": True,
            }
        )
        rule_catalog.append(
            {
                "rule_id": f"rule.direction.{item.key}",
                "kind": "bounded_direction_translation",
                "target_ref": item.key,
                "maximum_magnitude": item.step * 3,
                "direct_final_fact_allowed": False,
                "evidence_required": True,
            }
        )
        action_catalog.append(
            {
                "action_id": f"action.adjust.{item.key}",
                "kind": "bounded_state_adjustment",
                "target_ref": item.key,
                "minimum_amount": -item.step * 3,
                "maximum_amount": item.step * 3,
                "rule_refs": [f"rule.range.{item.key}"],
            }
        )

    world_spec: Dict[str, Any] = {
        "world_id": world_id,
        "premise": normalized.premise,
        "constraints": normalized.constraints,
        "scale_bounds": normalized.scale_bounds.model_dump(mode="json"),
        "step_seconds": normalized.step_seconds,
        "location_graph": [
            {
                "location_id": location_id,
                "kind": "root",
                "connections": [],
            }
        ],
        "entity_catalog": [
            {
                "entity_id": entity_id,
                "kind": "public_state_carrier",
                "location_id": location_id,
                "public_state_refs": sorted(initial_state),
            }
        ],
        "state_variables": variables,
        "initial_state": initial_state,
    }
    agent_seed_set = [
        {
            "agent_id": agent_id,
            "location_id": location_id,
            "policy_id": "policy.deterministic-experience-v1",
            "initial_intent": "observe",
            "initial_decision_mode": "initial_policy",
            "public_experience_refs": [],
        }
    ]
    projection_manifest = {
        "public_fields": [
            "session_id",
            "world_id",
            "source_package_hash",
            "status",
            "tick",
            "world_time_seconds",
            "revision",
            "state_hash",
            "variables",
            "feedback_count",
            "locations",
            "entities",
            "agents",
            "allowed_actions",
            "active_intervention_window",
            "event_cursor",
        ],
        "allowed_feedback_types": ["local_outcome_observed"],
        "polling": {"event_cursor": "after_sequence"},
        "engine_specific_types": [],
    }
    evidence_policy = {
        "state_hash_algorithm": STATE_HASH_ALGORITHM,
        "required_streams": [
            "events",
            "diffs",
            "snapshots",
            "agent_cycles",
            "direction_decisions",
            "request_correlations",
        ],
        "redaction": "public-only",
        "canonical_state_fields": [
            "session_id",
            "world_id",
            "source_package_hash",
            "status",
            "tick",
            "world_time_seconds",
            "revision",
            "variables",
            "feedback_count",
            "agents",
        ],
    }
    hash_payload = {
        "schema_version": SCHEMA_VERSION,
        "brief": normalized_brief,
        "world_spec": world_spec,
        "rule_catalog": rule_catalog,
        "action_catalog": action_catalog,
        "agent_seed_set": agent_seed_set,
        "projection_manifest": projection_manifest,
        "evidence_policy": evidence_policy,
    }
    package_hash = canonical_hash(hash_payload)

    diagnostics = validate_package_payload(hash_payload)
    return RunnableWorldPackage(
        package_id=f"package-{package_hash[:16]}",
        package_hash=package_hash,
        brief=normalized,
        world_spec=world_spec,
        rule_catalog=rule_catalog,
        action_catalog=action_catalog,
        agent_seed_set=agent_seed_set,
        projection_manifest=projection_manifest,
        evidence_policy=evidence_policy,
        readiness=PackageReadiness(
            status="ready" if not diagnostics else "invalid",
            diagnostics=diagnostics,
        ),
    )


def validate_package_payload(payload: Dict[str, Any]) -> list[Dict[str, Any]]:
    diagnostics: list[Dict[str, Any]] = []
    world_spec = payload["world_spec"]
    variable_ids = {item["key"] for item in world_spec["state_variables"]}
    location_ids = {item["location_id"] for item in world_spec["location_graph"]}
    rule_ids = {item["rule_id"] for item in payload["rule_catalog"]}

    for action in payload["action_catalog"]:
        if action["target_ref"] not in variable_ids:
            diagnostics.append(
                {
                    "code": "action_target_missing",
                    "path": f"action_catalog.{action['action_id']}.target_ref",
                }
            )
        for rule_ref in action["rule_refs"]:
            if rule_ref not in rule_ids:
                diagnostics.append(
                    {
                        "code": "action_rule_missing",
                        "path": f"action_catalog.{action['action_id']}.rule_refs",
                    }
                )

    for agent in payload["agent_seed_set"]:
        if agent["location_id"] not in location_ids:
            diagnostics.append(
                {
                    "code": "agent_location_missing",
                    "path": f"agent_seed_set.{agent['agent_id']}.location_id",
                }
            )

    required_projection_fields = {
        "session_id",
        "tick",
        "revision",
        "state_hash",
        "agents",
        "locations",
        "entities",
    }
    public_fields = set(payload["projection_manifest"].get("public_fields", []))
    missing_projection = sorted(required_projection_fields - public_fields)
    if missing_projection:
        diagnostics.append(
            {
                "code": "projection_fields_missing",
                "path": "projection_manifest.public_fields",
                "missing": missing_projection,
            }
        )

    required_streams = {
        "events",
        "diffs",
        "snapshots",
        "agent_cycles",
        "direction_decisions",
        "request_correlations",
    }
    streams = set(payload["evidence_policy"].get("required_streams", []))
    missing_streams = sorted(required_streams - streams)
    if missing_streams:
        diagnostics.append(
            {
                "code": "evidence_streams_missing",
                "path": "evidence_policy.required_streams",
                "missing": missing_streams,
            }
        )
    return diagnostics
