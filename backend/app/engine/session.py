from __future__ import annotations

import os
from copy import deepcopy
from threading import RLock
from typing import Any, Dict, Iterable, List, Optional, Tuple
from uuid import uuid4

from pydantic import BaseModel

from app.engine.agent_runtime import plan_agent_cycle
from app.engine.evidence import (
    capture_snapshot,
    evidence_integrity_checks,
    next_diff_id,
    next_event_id,
    state_hash,
)
from app.engine.generation import build_runnable_package, canonical_hash
from app.engine.models import EngineSessionRecord, QueuedDirection
from app.engine.rules import RuleDecision, judge_action, judge_direction, judge_feedback
from app.schemas.engine_v1 import (
    ActionRequest,
    ActionResult,
    AgentCycleEvidence,
    AgentExperienceRef,
    AgentPublicState,
    CapabilityManifest,
    CapabilityOperation,
    DiffOperation,
    DiffRecord,
    DirectionDecision,
    DirectionRequest,
    EventPage,
    EventRecord,
    EvidenceBundle,
    EvidenceCompleteness,
    FeedbackRequest,
    FeedbackResult,
    InterventionWindow,
    PublicProjection,
    RunnableWorldPackage,
    SessionCreateRequest,
    SessionStepRequest,
    SessionStepResult,
    WorldPackageCreateRequest,
    WorldSessionView,
)


class EngineV1NotFoundError(Exception):
    pass


class EngineV1ConflictError(Exception):
    def __init__(self, reason_code: str, message: str, data: Optional[dict] = None):
        super().__init__(message)
        self.reason_code = reason_code
        self.data = data or {}


class EngineV1InternalError(Exception):
    def __init__(self, reason_code: str, message: str, data: Optional[dict] = None):
        super().__init__(message)
        self.reason_code = reason_code
        self.data = data or {}


class EngineV1Service:
    def __init__(self) -> None:
        self._lock = RLock()
        self._packages: Dict[str, RunnableWorldPackage] = {}
        self._package_requests: Dict[str, RunnableWorldPackage] = {}
        self._package_request_fingerprints: Dict[str, str] = {}
        self._sessions: Dict[str, EngineSessionRecord] = {}
        self._session_requests: Dict[str, WorldSessionView] = {}
        self._session_request_fingerprints: Dict[str, str] = {}
        self._diagnostics: List[Dict[str, Any]] = []
        self.instance_id = f"instance-{uuid4().hex[:16]}"
        self.engine_build = os.getenv("WORLDENGINE_BUILD_ID", "worldengine-mvp-dev")

    def capabilities(self) -> CapabilityManifest:
        operations = [
            CapabilityOperation(
                operation_id="health_health_get",
                method="GET",
                path="/health",
            ),
            CapabilityOperation(
                operation_id="capabilities.read",
                method="GET",
                path="/api/v1/capabilities",
            ),
            CapabilityOperation(operation_id="openapi.read", method="GET", path="/openapi.json"),
            CapabilityOperation(
                operation_id="world_packages.create",
                method="POST",
                path="/api/v1/world-packages",
            ),
            CapabilityOperation(
                operation_id="world_packages.read",
                method="GET",
                path="/api/v1/world-packages/{package_id}",
            ),
            CapabilityOperation(
                operation_id="sessions.create",
                method="POST",
                path="/api/v1/sessions",
            ),
            CapabilityOperation(
                operation_id="sessions.read",
                method="GET",
                path="/api/v1/sessions/{session_id}",
            ),
            CapabilityOperation(
                operation_id="sessions.step",
                method="POST",
                path="/api/v1/sessions/{session_id}/steps",
            ),
            CapabilityOperation(
                operation_id="directions.submit",
                method="POST",
                path="/api/v1/sessions/{session_id}/directions",
            ),
            CapabilityOperation(
                operation_id="actions.submit",
                method="POST",
                path="/api/v1/sessions/{session_id}/actions",
            ),
            CapabilityOperation(
                operation_id="feedback.submit",
                method="POST",
                path="/api/v1/sessions/{session_id}/feedback",
            ),
            CapabilityOperation(
                operation_id="projection.read",
                method="GET",
                path="/api/v1/sessions/{session_id}/projection",
            ),
            CapabilityOperation(
                operation_id="events.poll",
                method="GET",
                path="/api/v1/sessions/{session_id}/events",
            ),
            CapabilityOperation(
                operation_id="evidence.export",
                method="GET",
                path="/api/v1/sessions/{session_id}/evidence",
            ),
        ]
        return CapabilityManifest(
            engine_build=self.engine_build,
            instance_id=self.instance_id,
            operations=operations,
        )

    def create_package(self, request: WorldPackageCreateRequest) -> RunnableWorldPackage:
        with self._lock:
            fingerprint = self._request_fingerprint(request)
            existing = self._package_requests.get(request.request_id)
            if existing is not None:
                self._assert_same_request(
                    expected=self._package_request_fingerprints[request.request_id],
                    actual=fingerprint,
                    operation="world_packages.create",
                    request_id=request.request_id,
                )
                return existing.model_copy(deep=True)

            package = build_runnable_package(request.brief)
            stored = self._packages.get(package.package_id)
            if stored is None:
                self._packages[package.package_id] = package
                stored = package
            self._package_requests[request.request_id] = stored
            self._package_request_fingerprints[request.request_id] = fingerprint
            return stored.model_copy(deep=True)

    def get_package(self, package_id: str) -> RunnableWorldPackage:
        with self._lock:
            package = self._packages.get(package_id)
            if package is None:
                raise EngineV1NotFoundError("Unknown package_id")
            return package.model_copy(deep=True)

    def create_session(self, request: SessionCreateRequest) -> WorldSessionView:
        with self._lock:
            fingerprint = self._request_fingerprint(request)
            existing = self._session_requests.get(request.request_id)
            if existing is not None:
                self._assert_same_request(
                    expected=self._session_request_fingerprints[request.request_id],
                    actual=fingerprint,
                    operation="sessions.create",
                    request_id=request.request_id,
                )
                return existing.model_copy(deep=True)

            package = self._packages.get(request.package_id)
            if package is None:
                raise EngineV1NotFoundError("Unknown package_id")
            if request.package_hash != package.package_hash:
                raise EngineV1ConflictError(
                    "package_hash_mismatch",
                    "package_hash does not match the stored runnable package",
                    {
                        "package_id": package.package_id,
                        "expected_package_hash": package.package_hash,
                    },
                )
            if package.readiness.status != "ready":
                raise EngineV1ConflictError(
                    "package_not_ready",
                    "Runnable package is not ready for session boot",
                )

            session_id = f"session-{uuid4().hex[:16]}"
            variables = dict(package.world_spec["initial_state"])
            agents = {
                item["agent_id"]: AgentPublicState(
                    agent_id=item["agent_id"],
                    location_id=item["location_id"],
                    cycle_count=0,
                    last_intent=item["initial_intent"],
                    decision_mode=item["initial_decision_mode"],
                )
                for item in package.agent_seed_set
            }
            window = InterventionWindow(
                window_id=f"window-{session_id}-t0",
                open_tick=0,
                status="open",
            )
            record = EngineSessionRecord(
                session_id=session_id,
                package=package,
                world_id=package.world_spec["world_id"],
                status="ready",
                tick=0,
                world_time_seconds=0.0,
                revision=0,
                variables=variables,
                feedback_count=0,
                agents=agents,
                windows={window.window_id: window},
                active_window_id=window.window_id,
            )
            initial_snapshot = capture_snapshot(record)
            boot_event = self._record_event_only(
                record,
                event_type="session.booted",
                source="worldengine.session",
                status="accepted",
                request_id=request.request_id,
                rule_refs=["rule.session.ready-package"],
                payload={
                    "package_id": package.package_id,
                    "source_package_hash": package.package_hash,
                    "initial_snapshot_id": initial_snapshot.snapshot_id,
                },
            )
            self._record_correlation(
                record,
                "sessions.create",
                request.request_id,
                "accepted",
                [boot_event.event_id],
            )
            self._sessions[session_id] = record
            view = self._session_view(record)
            self._session_requests[request.request_id] = view
            self._session_request_fingerprints[request.request_id] = fingerprint
            return view.model_copy(deep=True)

    def get_session(self, session_id: str) -> WorldSessionView:
        with self._lock:
            record = self._require_session(session_id)
            return self._session_view(record)

    def get_projection(self, session_id: str) -> PublicProjection:
        with self._lock:
            return self._projection(self._require_session(session_id))

    def step_session(self, session_id: str, request: SessionStepRequest) -> SessionStepResult:
        with self._lock:
            record = self._require_session(session_id)
            cached = self._cached_result(record, "sessions.step", request)
            if cached is not None:
                return cached.model_copy(deep=True)
            self._check_revision(record, request.expected_revision)
            if record.status != "ready":
                raise EngineV1ConflictError(
                    "session_not_ready",
                    "Session must be ready before stepping",
                    {"status": record.status},
                )

            start_tick = record.tick
            start_revision = record.revision
            start_hash = state_hash(record)
            start_event_count = len(record.events)
            start_snapshot_count = len(record.snapshots)
            backup = deepcopy(record)
            try:
                for offset in range(request.step_count):
                    self._step_once(record, request.request_id, offset)
            except Exception as exc:
                self._sessions[session_id] = backup
                raise self._internal_operation_error(
                    operation="sessions.step",
                    session_id=session_id,
                    request_id=request.request_id,
                    revision=backup.revision,
                    exc=exc,
                ) from None

            result = SessionStepResult(
                request_id=request.request_id,
                status="completed",
                step_count=request.step_count,
                start_tick=start_tick,
                end_tick=record.tick,
                start_revision=start_revision,
                end_revision=record.revision,
                start_state_hash=start_hash,
                end_state_hash=state_hash(record),
                event_refs=[event.event_id for event in record.events[start_event_count:]],
                snapshot_refs=[
                    snapshot.snapshot_id
                    for snapshot in record.snapshots[start_snapshot_count:]
                ],
                projection=self._projection(record),
            )
            self._store_result(record, "sessions.step", request, result)
            self._record_correlation(
                record,
                "sessions.step",
                request.request_id,
                "completed",
                result.event_refs,
            )
            return result.model_copy(deep=True)

    def submit_direction(
        self,
        session_id: str,
        request: DirectionRequest,
    ) -> DirectionDecision:
        with self._lock:
            record = self._require_session(session_id)
            cached = self._cached_result(record, "directions.submit", request)
            if cached is not None:
                return cached.model_copy(deep=True)
            self._check_revision(record, request.expected_revision)
            window = record.windows.get(request.window_id)
            if window is None:
                raise EngineV1ConflictError(
                    "unknown_intervention_window",
                    "Intervention window does not exist",
                    {"window_id": request.window_id},
                )
            if window.status != "open" or request.window_id != record.active_window_id:
                raise EngineV1ConflictError(
                    "intervention_window_closed",
                    "Intervention window is closed",
                    {"window_id": request.window_id, "open_tick": window.open_tick},
                )

            before_hash = state_hash(record)
            judgment = judge_direction(record.package, request)
            if judgment.accepted:
                event = self._record_event_only(
                    record,
                    event_type="direction.accepted",
                    source="operator",
                    status="accepted",
                    request_id=request.request_id,
                    rule_refs=judgment.rule_refs,
                    payload={
                        "window_id": request.window_id,
                        "kind": request.kind,
                        "target_ref": request.target_ref,
                        "magnitude": request.magnitude,
                        "summary": request.summary,
                        "application_status": "queued",
                    },
                )
                decision = DirectionDecision(
                    request_id=request.request_id,
                    window_id=request.window_id,
                    status="accepted",
                    reason_code=judgment.reason_code,
                    public_reason=judgment.public_reason,
                    queued=True,
                    rule_refs=judgment.rule_refs,
                    event_ref=event.event_id,
                    tick=record.tick,
                    revision=record.revision,
                    state_hash_before=before_hash,
                    state_hash_after=state_hash(record),
                )
                record.queued_directions.append(
                    QueuedDirection(request=request, decision=decision)
                )
            else:
                event = self._record_event_only(
                    record,
                    event_type="direction.rejected",
                    source="operator",
                    status="rejected",
                    request_id=request.request_id,
                    rule_refs=judgment.rule_refs,
                    payload={
                        "window_id": request.window_id,
                        "kind": request.kind,
                        "target_ref": request.target_ref,
                        "reason_code": judgment.reason_code,
                        "summary": request.summary,
                    },
                )
                decision = DirectionDecision(
                    request_id=request.request_id,
                    window_id=request.window_id,
                    status="rejected",
                    reason_code=judgment.reason_code,
                    public_reason=judgment.public_reason,
                    queued=False,
                    rule_refs=judgment.rule_refs,
                    event_ref=event.event_id,
                    tick=record.tick,
                    revision=record.revision,
                    state_hash_before=before_hash,
                    state_hash_after=state_hash(record),
                )

            record.direction_decisions.append(decision)
            self._store_result(record, "directions.submit", request, decision)
            self._record_correlation(
                record,
                "directions.submit",
                request.request_id,
                decision.status,
                [decision.event_ref],
            )
            return decision.model_copy(deep=True)

    def submit_action(self, session_id: str, request: ActionRequest) -> ActionResult:
        with self._lock:
            record = self._require_session(session_id)
            cached = self._cached_result(record, "actions.submit", request)
            if cached is not None:
                return cached.model_copy(deep=True)
            self._check_revision(record, request.expected_revision)

            current_value = record.variables.get(request.target_ref, 0)
            judgment = judge_action(record.package, request, current_value)
            if judgment.accepted:
                event, diff = self._apply_operations(
                    record,
                    request_id=request.request_id,
                    event_type="client.action.accepted",
                    source="client",
                    rule_refs=judgment.rule_refs,
                    operations=[
                        (f"/variables/{request.target_ref}", current_value + request.amount)
                    ],
                    payload={
                        "action_id": request.action_id,
                        "target_ref": request.target_ref,
                        "amount": request.amount,
                    },
                )
                capture_snapshot(record)
                status = "accepted"
                diff_refs = [diff.diff_id]
            else:
                event = self._record_event_only(
                    record,
                    event_type="client.action.rejected",
                    source="client",
                    status="rejected",
                    request_id=request.request_id,
                    rule_refs=judgment.rule_refs,
                    payload={
                        "action_id": request.action_id,
                        "target_ref": request.target_ref,
                        "reason_code": judgment.reason_code,
                    },
                )
                status = "rejected"
                diff_refs = []

            result = ActionResult(
                request_id=request.request_id,
                status=status,
                reason_code=judgment.reason_code,
                rule_refs=judgment.rule_refs,
                event_ref=event.event_id,
                applied_diff_refs=diff_refs,
                projection=self._projection(record),
            )
            self._store_result(record, "actions.submit", request, result)
            self._record_correlation(
                record,
                "actions.submit",
                request.request_id,
                status,
                [event.event_id],
            )
            return result.model_copy(deep=True)

    def submit_feedback(
        self,
        session_id: str,
        request: FeedbackRequest,
    ) -> FeedbackResult:
        with self._lock:
            record = self._require_session(session_id)
            cached = self._cached_result(record, "feedback.submit", request)
            if cached is not None:
                return cached.model_copy(deep=True)
            self._check_revision(record, request.expected_revision)
            judgment = judge_feedback(record.package, request)
            if (
                judgment.accepted
                and request.related_event_ref is not None
                and request.related_event_ref
                not in {event.event_id for event in record.events}
            ):
                judgment = RuleDecision(
                    accepted=False,
                    reason_code="feedback_reference_not_found",
                    public_reason="Feedback reference does not identify a session event.",
                    rule_refs=["rule.feedback.manifest"],
                )

            if judgment.accepted:
                event, diff = self._apply_operations(
                    record,
                    request_id=request.request_id,
                    event_type="client.feedback.accepted",
                    source="client",
                    rule_refs=judgment.rule_refs,
                    operations=[("/feedback_count", record.feedback_count + 1)],
                    payload={
                        "feedback_type": request.feedback_type,
                        "summary": request.summary,
                        "related_event_ref": request.related_event_ref,
                    },
                )
                capture_snapshot(record)
                status = "accepted"
                diff_refs = [diff.diff_id]
            else:
                event = self._record_event_only(
                    record,
                    event_type="client.feedback.rejected",
                    source="client",
                    status="rejected",
                    request_id=request.request_id,
                    rule_refs=judgment.rule_refs,
                    payload={
                        "feedback_type": request.feedback_type,
                        "reason_code": judgment.reason_code,
                    },
                )
                status = "rejected"
                diff_refs = []

            result = FeedbackResult(
                request_id=request.request_id,
                status=status,
                reason_code=judgment.reason_code,
                rule_refs=judgment.rule_refs,
                event_ref=event.event_id,
                applied_diff_refs=diff_refs,
                projection=self._projection(record),
            )
            self._store_result(record, "feedback.submit", request, result)
            self._record_correlation(
                record,
                "feedback.submit",
                request.request_id,
                status,
                [event.event_id],
            )
            return result.model_copy(deep=True)

    def get_events(
        self,
        session_id: str,
        after_sequence: int = 0,
        limit: int = 100,
    ) -> EventPage:
        with self._lock:
            record = self._require_session(session_id)
            matches = [event for event in record.events if event.sequence > after_sequence]
            items = matches[:limit]
            next_sequence = items[-1].sequence if items else after_sequence
            return EventPage(
                session_id=session_id,
                after_sequence=after_sequence,
                items=[item.model_copy(deep=True) for item in items],
                next_sequence=next_sequence,
                has_more=len(matches) > len(items),
            )

    def get_evidence(self, session_id: str) -> EvidenceBundle:
        with self._lock:
            record = self._require_session(session_id)
            checks = self._completeness_checks(record)
            missing = [name for name, passed in checks.items() if not passed]
            return EvidenceBundle(
                package=record.package.model_copy(deep=True),
                projection=self._projection(record),
                events=[item.model_copy(deep=True) for item in record.events],
                diffs=[item.model_copy(deep=True) for item in record.diffs],
                snapshots=[item.model_copy(deep=True) for item in record.snapshots],
                agent_cycles=[item.model_copy(deep=True) for item in record.agent_cycles],
                direction_decisions=[
                    item.model_copy(deep=True) for item in record.direction_decisions
                ],
                request_correlations=deepcopy(record.request_correlations),
                completeness=EvidenceCompleteness(
                    status="complete" if not missing else "incomplete",
                    checks=checks,
                    missing=missing,
                ),
            )

    def _step_once(self, record: EngineSessionRecord, request_id: str, offset: int) -> None:
        current_window = record.windows[record.active_window_id]
        record.windows[current_window.window_id] = current_window.model_copy(
            update={"status": "closed"}
        )
        tick_request_id = f"{request_id}:tick:{offset + 1}"
        self._apply_operations(
            record,
            request_id=tick_request_id,
            event_type="runtime.tick_advanced",
            source="worldengine.runtime",
            rule_refs=["rule.runtime.lockstep"],
            operations=[
                ("/tick", record.tick + 1),
                (
                    "/world_time_seconds",
                    record.world_time_seconds + record.package.brief.step_seconds,
                ),
            ],
            payload={"step_request_id": request_id, "step_offset": offset + 1},
        )

        queued = [
            item
            for item in record.queued_directions
            if item.request.window_id == current_window.window_id
        ]
        for item in queued:
            self._apply_queued_direction(record, item)
        record.queued_directions = [
            item
            for item in record.queued_directions
            if item.request.window_id != current_window.window_id
        ]

        self._run_agent_cycle(record, tick_request_id)
        new_window = InterventionWindow(
            window_id=f"window-{record.session_id}-t{record.tick}",
            open_tick=record.tick,
            status="open",
        )
        record.windows[new_window.window_id] = new_window
        record.active_window_id = new_window.window_id
        capture_snapshot(record)

    def _apply_queued_direction(
        self,
        record: EngineSessionRecord,
        queued: QueuedDirection,
    ) -> None:
        request = queued.request
        current = record.variables[request.target_ref]
        magnitude = request.magnitude or 0
        variable = next(
            item
            for item in record.package.world_spec["state_variables"]
            if item["key"] == request.target_ref
        )
        next_value = current + magnitude
        if not variable["minimum"] <= next_value <= variable["maximum"]:
            self._record_event_only(
                record,
                event_type="direction.application_rejected",
                source="worldengine.rules",
                status="rejected",
                request_id=request.request_id,
                rule_refs=queued.decision.rule_refs,
                payload={
                    "accepted_event_ref": queued.decision.event_ref,
                    "reason_code": "direction_target_range_violation",
                },
            )
            return
        event, diff = self._apply_operations(
            record,
            request_id=request.request_id,
            event_type="direction.applied",
            source="worldengine.rules",
            rule_refs=queued.decision.rule_refs,
            operations=[(f"/variables/{request.target_ref}", next_value)],
            payload={
                "accepted_event_ref": queued.decision.event_ref,
                "window_id": request.window_id,
                "target_ref": request.target_ref,
                "magnitude": magnitude,
            },
        )
        queued.decision.application_event_refs.append(event.event_id)
        queued.decision.applied_diff_refs.append(diff.diff_id)
        queued.decision.tick = record.tick
        queued.decision.revision = record.revision
        queued.decision.state_hash_after = diff.state_hash_after

    def _run_agent_cycle(self, record: EngineSessionRecord, tick_request_id: str) -> None:
        plan = plan_agent_cycle(record)
        agent = record.agents[plan.agent_id]
        action_request = ActionRequest(
            request_id=f"{tick_request_id}:agent:{plan.agent_id}",
            expected_revision=record.revision,
            action_id=plan.action_id,
            target_ref=plan.target_ref,
            amount=plan.amount,
        )
        judgment = judge_action(
            record.package,
            action_request,
            record.variables[plan.target_ref],
        )
        perception = {
            "state_hash": state_hash(record),
            "visible_variables": deepcopy(record.variables),
            "available_actions": [item["action_id"] for item in record.package.action_catalog],
            "recent_event_refs": [event.event_id for event in record.events[-5:]],
        }
        decision = {
            "intent": plan.intent,
            "decision_mode": plan.decision_mode,
            "experience_ref_ids": [ref.ref_id for ref in plan.experience_refs_used],
        }

        if not judgment.accepted:
            event = self._record_event_only(
                record,
                event_type="agent.action.rejected",
                source=plan.agent_id,
                status="rejected",
                request_id=action_request.request_id,
                rule_refs=judgment.rule_refs,
                payload={"reason_code": judgment.reason_code},
            )
            record.agent_cycles.append(
                AgentCycleEvidence(
                    cycle_id=f"cycle-{plan.agent_id}-{agent.cycle_count + 1}",
                    agent_id=plan.agent_id,
                    tick=record.tick,
                    perception=perception,
                    decision=decision,
                    action_request=action_request.model_dump(mode="json"),
                    rule_judgment={
                        "accepted": False,
                        "reason_code": judgment.reason_code,
                        "rule_refs": judgment.rule_refs,
                    },
                    action_result={"status": "rejected", "event_ref": event.event_id},
                    experience_refs_used=plan.experience_refs_used,
                    event_refs=[event.event_id],
                    diff_refs=[],
                )
            )
            return

        predicted_event_id = next_event_id(record)
        new_experience = AgentExperienceRef(
            ref_id=predicted_event_id,
            ref_type="action_result",
            source_tick=record.tick,
            public_effect=f"{plan.target_ref}:{plan.amount:+d}",
        )
        next_refs = [*agent.experience_refs, new_experience][-5:]
        event, diff = self._apply_operations(
            record,
            request_id=action_request.request_id,
            event_type="agent.action.accepted",
            source=plan.agent_id,
            rule_refs=judgment.rule_refs,
            operations=[
                (
                    f"/variables/{plan.target_ref}",
                    record.variables[plan.target_ref] + plan.amount,
                ),
                (f"/agents/{plan.agent_id}/cycle_count", agent.cycle_count + 1),
                (f"/agents/{plan.agent_id}/last_intent", plan.intent),
                (f"/agents/{plan.agent_id}/decision_mode", plan.decision_mode),
                (f"/agents/{plan.agent_id}/experience_refs", next_refs),
            ],
            payload={
                "agent_id": plan.agent_id,
                "action_id": plan.action_id,
                "target_ref": plan.target_ref,
                "amount": plan.amount,
                "decision_mode": plan.decision_mode,
                "experience_ref_ids": [ref.ref_id for ref in plan.experience_refs_used],
            },
        )
        record.agent_cycles.append(
            AgentCycleEvidence(
                cycle_id=f"cycle-{plan.agent_id}-{agent.cycle_count}",
                agent_id=plan.agent_id,
                tick=record.tick,
                perception=perception,
                decision=decision,
                action_request=action_request.model_dump(mode="json"),
                rule_judgment={
                    "accepted": True,
                    "reason_code": judgment.reason_code,
                    "rule_refs": judgment.rule_refs,
                },
                action_result={
                    "status": "accepted",
                    "event_ref": event.event_id,
                    "diff_refs": [diff.diff_id],
                    "experience_ref": new_experience.model_dump(mode="json"),
                },
                experience_refs_used=plan.experience_refs_used,
                event_refs=[event.event_id],
                diff_refs=[diff.diff_id],
            )
        )

    def _apply_operations(
        self,
        record: EngineSessionRecord,
        *,
        request_id: str,
        event_type: str,
        source: str,
        rule_refs: List[str],
        operations: Iterable[Tuple[str, Any]],
        payload: Dict[str, Any],
    ) -> Tuple[EventRecord, DiffRecord]:
        before_hash = state_hash(record)
        event_id = next_event_id(record)
        diff_id = next_diff_id(record)
        staged_operations = [
            (path, deepcopy(value)) for path, value in operations
        ]
        shadow = deepcopy(record)
        diff_operations: List[DiffOperation] = []
        for path, value in staged_operations:
            before = self._get_path(shadow, path)
            self._set_path(shadow, path, value)
            diff_operations.append(
                DiffOperation(
                    path=path,
                    before=self._json_value(before),
                    after=self._json_value(value),
                )
            )

        old_revision = shadow.revision
        shadow.revision += 1
        diff_operations.append(
            DiffOperation(path="/revision", before=old_revision, after=shadow.revision)
        )
        after_hash = state_hash(shadow)
        diff = DiffRecord(
            diff_id=diff_id,
            request_id=request_id,
            event_ref=event_id,
            tick=shadow.tick,
            revision=shadow.revision,
            state_hash_before=before_hash,
            state_hash_after=after_hash,
            operations=diff_operations,
        )
        event = EventRecord(
            sequence=len(record.events) + 1,
            event_id=event_id,
            event_type=event_type,
            source=source,
            status="accepted",
            request_id=request_id,
            tick=shadow.tick,
            revision=shadow.revision,
            state_hash_before=before_hash,
            state_hash_after=after_hash,
            rule_refs=rule_refs,
            diff_refs=[diff_id],
            payload=deepcopy(payload),
        )
        for path, value in staged_operations:
            self._set_path(record, path, deepcopy(value))
        record.revision = shadow.revision
        record.diffs.append(diff)
        record.events.append(event)
        return event, diff

    def _record_event_only(
        self,
        record: EngineSessionRecord,
        *,
        event_type: str,
        source: str,
        status: str,
        request_id: str,
        rule_refs: List[str],
        payload: Dict[str, Any],
    ) -> EventRecord:
        current_hash = state_hash(record)
        event = EventRecord(
            sequence=len(record.events) + 1,
            event_id=next_event_id(record),
            event_type=event_type,
            source=source,
            status=status,
            request_id=request_id,
            tick=record.tick,
            revision=record.revision,
            state_hash_before=current_hash,
            state_hash_after=current_hash,
            rule_refs=rule_refs,
            diff_refs=[],
            payload=deepcopy(payload),
        )
        record.events.append(event)
        return event

    def _projection(self, record: EngineSessionRecord) -> PublicProjection:
        return PublicProjection(
            session_id=record.session_id,
            world_id=record.world_id,
            source_package_hash=record.package.package_hash,
            status=record.status,
            tick=record.tick,
            world_time_seconds=record.world_time_seconds,
            revision=record.revision,
            state_hash=state_hash(record),
            variables=deepcopy(record.variables),
            feedback_count=record.feedback_count,
            locations=deepcopy(record.package.world_spec["location_graph"]),
            entities=deepcopy(record.package.world_spec["entity_catalog"]),
            agents=[
                record.agents[key].model_copy(deep=True) for key in sorted(record.agents)
            ],
            allowed_actions=[
                item["action_id"] for item in record.package.action_catalog
            ],
            active_intervention_window=record.windows[
                record.active_window_id
            ].model_copy(deep=True),
            event_cursor=len(record.events),
        )

    def _session_view(self, record: EngineSessionRecord) -> WorldSessionView:
        return WorldSessionView(
            session_id=record.session_id,
            package_id=record.package.package_id,
            source_package_hash=record.package.package_hash,
            initial_snapshot_id=record.snapshots[0].snapshot_id,
            projection=self._projection(record),
        )

    def _completeness_checks(self, record: EngineSessionRecord) -> Dict[str, bool]:
        checks = {
            "package_ready": record.package.readiness.status == "ready",
            "initial_snapshot": bool(record.snapshots)
            and record.snapshots[0].revision == 0,
            "agent_cycle": bool(record.agent_cycles),
        }
        checks.update(evidence_integrity_checks(record))
        return checks

    def _require_session(self, session_id: str) -> EngineSessionRecord:
        record = self._sessions.get(session_id)
        if record is None:
            raise EngineV1NotFoundError("Unknown session_id")
        return record

    def _internal_operation_error(
        self,
        *,
        operation: str,
        session_id: str,
        request_id: str,
        revision: int,
        exc: Exception,
    ) -> EngineV1InternalError:
        diagnostic_id = f"diagnostic-{uuid4().hex[:16]}"
        self._diagnostics.append(
            {
                "diagnostic_id": diagnostic_id,
                "operation_id": operation,
                "session_id": session_id,
                "request_id": request_id,
                "revision": revision,
                "exception_type": type(exc).__name__,
                "redaction_status": "safe-metadata-only",
            }
        )
        self._diagnostics = self._diagnostics[-200:]
        return EngineV1InternalError(
            "atomic_operation_failed",
            "WorldEngine could not commit the requested atomic operation",
            {"diagnostic_id": diagnostic_id},
        )

    def _check_revision(
        self,
        record: EngineSessionRecord,
        expected_revision: Optional[int],
    ) -> None:
        if expected_revision is not None and expected_revision != record.revision:
            raise EngineV1ConflictError(
                "stale_revision",
                "expected_revision does not match current session revision",
                {
                    "expected_revision": expected_revision,
                    "current_revision": record.revision,
                    "current_state_hash": state_hash(record),
                },
            )

    @staticmethod
    def _request_fingerprint(request: BaseModel) -> str:
        return canonical_hash(request.model_dump(mode="json"))

    @staticmethod
    def _assert_same_request(
        *,
        expected: str,
        actual: str,
        operation: str,
        request_id: str,
    ) -> None:
        if expected != actual:
            raise EngineV1ConflictError(
                "idempotency_key_reused",
                "request_id was already used with different public input",
                {"operation_id": operation, "request_id": request_id},
            )

    def _cached_result(
        self,
        record: EngineSessionRecord,
        operation: str,
        request: BaseModel,
    ) -> Any:
        key = (operation, str(getattr(request, "request_id")))
        result = record.request_results.get(key)
        if result is None:
            return None
        self._assert_same_request(
            expected=record.request_fingerprints[key],
            actual=self._request_fingerprint(request),
            operation=operation,
            request_id=key[1],
        )
        return result

    def _store_result(
        self,
        record: EngineSessionRecord,
        operation: str,
        request: BaseModel,
        result: Any,
    ) -> None:
        request_id = str(getattr(request, "request_id"))
        key = (operation, request_id)
        record.request_results[key] = result.model_copy(deep=True)
        record.request_fingerprints[key] = self._request_fingerprint(request)

    @staticmethod
    def _record_correlation(
        record: EngineSessionRecord,
        operation: str,
        request_id: str,
        status: str,
        event_refs: List[str],
    ) -> None:
        record.request_correlations.append(
            {
                "operation_id": operation,
                "request_id": request_id,
                "status": status,
                "event_refs": list(event_refs),
                "tick": record.tick,
                "revision": record.revision,
                "state_hash": state_hash(record),
            }
        )

    @staticmethod
    def _get_path(record: EngineSessionRecord, path: str) -> Any:
        parts = path.strip("/").split("/")
        if parts[0] == "variables":
            return deepcopy(record.variables[parts[1]])
        if parts[0] == "agents":
            return deepcopy(getattr(record.agents[parts[1]], parts[2]))
        return deepcopy(getattr(record, parts[0]))

    @staticmethod
    def _set_path(record: EngineSessionRecord, path: str, value: Any) -> None:
        parts = path.strip("/").split("/")
        if parts[0] == "variables":
            record.variables[parts[1]] = value
            return
        if parts[0] == "agents":
            setattr(record.agents[parts[1]], parts[2], value)
            return
        setattr(record, parts[0], value)

    @staticmethod
    def _json_value(value: Any) -> Any:
        if isinstance(value, BaseModel):
            return value.model_dump(mode="json")
        if isinstance(value, list):
            return [EngineV1Service._json_value(item) for item in value]
        if isinstance(value, dict):
            return {
                key: EngineV1Service._json_value(item) for key, item in value.items()
            }
        return deepcopy(value)
