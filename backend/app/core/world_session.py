from __future__ import annotations

from datetime import datetime, timezone
from typing import Callable
from uuid import uuid4

from app.core.runtime_engine import RuntimeEngine
from app.core.world_rule_parameters import (
    build_public_world_rule_summary,
    validate_generated_rule_parameter_set,
)
from app.schemas.session import (
    SessionAgentEventEvidence,
    SessionAgentPublicState,
    SessionCreateRequest,
    SessionDirectionSummaryResponse,
    SessionEvidenceRefs,
    SessionGenerationSummary,
    SessionRuleSummaryResponse,
    SessionRuntimeRef,
    SessionStatus,
    SessionStatusResponse,
    WorldSession,
)
from app.schemas.world_direction import (
    WorldDirectionClassification,
    WorldDirectionQueueItem,
    WorldDirectionRequest,
    classify_world_direction,
)
from app.schemas.world_generation import GeneratedRuleParameterSet
from app.schemas.world_generation import RuleParameterDiagnostic


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class InMemoryWorldSessionStore:
    """Process-local store for public MVP world sessions."""

    def __init__(
        self,
        *,
        runtime_engine: RuntimeEngine,
        event_count_provider: Callable[[], int],
        snapshot_count_provider: Callable[[], int],
    ) -> None:
        self._runtime_engine = runtime_engine
        self._event_count_provider = event_count_provider
        self._snapshot_count_provider = snapshot_count_provider
        self._sessions: dict[str, WorldSession] = {}
        self._agents: dict[str, dict[str, SessionAgentPublicState]] = {}
        self._accepted_rule_sets: dict[str, GeneratedRuleParameterSet] = {}
        self._order: list[str] = []

    def create(
        self,
        request: SessionCreateRequest,
        *,
        status: SessionStatus = "created",
        generation_summary: SessionGenerationSummary | None = None,
    ) -> WorldSession:
        session_id = f"session-{uuid4().hex[:12]}"
        world_id = request.world_id or "world-v1"
        now = _utc_now_iso()
        event_count = self._event_count_provider()
        snapshot_count = self._snapshot_count_provider()
        session = WorldSession(
            session_id=session_id,
            world_id=world_id,
            public_label=request.public_label or "WorldEngine MVP session",
            status=status,
            runtime_ref=self._runtime_ref(),
            evidence_refs=SessionEvidenceRefs(
                event_count_at_create=event_count,
                snapshot_count_at_create=snapshot_count,
                current_event_count=event_count,
                current_snapshot_count=snapshot_count,
            ),
            generation_summary=generation_summary,
            created_at=now,
            updated_at=now,
        )
        self._sessions[session_id] = session
        self._order.append(session_id)
        return session

    def list(self) -> list[WorldSession]:
        return [self._refresh(self._sessions[session_id]) for session_id in self._order]

    def get(self, session_id: str) -> WorldSession | None:
        session = self._sessions.get(session_id)
        if session is None:
            return None
        return self._refresh(session)

    def status(self, session_id: str) -> SessionStatusResponse | None:
        session = self.get(session_id)
        if session is None:
            return None
        return SessionStatusResponse(
            session_id=session.session_id,
            status=session.status,
            runtime_ref=session.runtime_ref,
            evidence_refs=session.evidence_refs,
            updated_at=session.updated_at,
        )

    def set_status(
        self,
        session_id: str,
        status: SessionStatus,
    ) -> WorldSession | None:
        session = self.get(session_id)
        if session is None:
            return None
        updated = session.model_copy(
            update={
                "status": status,
                "updated_at": _utc_now_iso(),
            }
        )
        self._sessions[session_id] = updated
        return self._refresh(updated)

    def attach_rules(
        self,
        session_id: str,
        rule_set: GeneratedRuleParameterSet,
    ) -> SessionRuleSummaryResponse | None:
        session = self.get(session_id)
        if session is None:
            return None
        validation = validate_generated_rule_parameter_set(rule_set)
        if rule_set.world_id != session.world_id:
            validation = validation.model_copy(
                update={
                    "validation_status": "rejected",
                    "accepted_parameter_count": 0,
                    "accepted_rule_count": 0,
                    "diagnostics": [
                        *validation.diagnostics,
                        RuleParameterDiagnostic(
                            code="session_world_mismatch",
                            message="rule set world_id must match session world_id",
                            path="/world_id",
                        ),
                    ],
                }
            )
        summary = build_public_world_rule_summary(rule_set, validation)
        attachment_status = (
            "attached" if validation.validation_status == "accepted" else "rejected"
        )
        if attachment_status == "attached":
            self._accepted_rule_sets[session_id] = rule_set
            updated = session.model_copy(
                update={
                    "rule_summary": summary,
                    "rule_validation": validation,
                    "updated_at": _utc_now_iso(),
                }
            )
            self._sessions[session_id] = updated
        return SessionRuleSummaryResponse(
            session_id=session_id,
            world_id=session.world_id,
            attachment_status=attachment_status,
            summary=summary,
            validation=validation,
            redaction_status=validation.redaction_status,
        )

    def accepted_rule_set(
        self,
        session_id: str,
    ) -> GeneratedRuleParameterSet | None:
        if session_id not in self._sessions:
            return None
        return self._accepted_rule_sets.get(session_id)

    def classify_direction(
        self,
        session_id: str,
        request: WorldDirectionRequest,
    ) -> tuple[WorldSession, WorldDirectionClassification] | None:
        session = self.get(session_id)
        if session is None:
            return None
        public_context_keys = sorted(request.public_context.keys())
        classification = classify_world_direction(
            request.instruction_text,
            branch_id=request.branch_id,
            public_context_keys=public_context_keys,
            public_context_values=request.public_context.values(),
        )
        return session, classification

    def queue_direction(
        self,
        session_id: str,
        request: WorldDirectionRequest,
        classification: WorldDirectionClassification,
    ) -> tuple[WorldSession, WorldDirectionQueueItem] | None:
        session = self.get(session_id)
        if session is None:
            return None
        public_context_keys = sorted(request.public_context.keys())
        event_public_context_keys = (
            [] if classification.redaction_status == "redacted" else public_context_keys
        )
        queue_item = WorldDirectionQueueItem(
            direction_id=f"direction-{uuid4().hex[:12]}",
            world_id=session.world_id,
            classification=classification,
            public_summary=classification.public_reason,
            apply_after_tick=request.apply_after_tick,
            expires_after_tick=request.expires_after_tick,
            public_context_keys=event_public_context_keys,
            redaction_status=classification.redaction_status,
        )
        updated = session.model_copy(
            update={
                "direction_queue": [*session.direction_queue, queue_item],
                "updated_at": _utc_now_iso(),
            }
        )
        self._sessions[session_id] = updated
        return self._refresh(updated), queue_item

    def reject_direction(self, session_id: str) -> WorldSession | None:
        session = self.get(session_id)
        if session is None:
            return None
        updated = session.model_copy(
            update={
                "direction_rejected_count": session.direction_rejected_count + 1,
                "updated_at": _utc_now_iso(),
            }
        )
        self._sessions[session_id] = updated
        return self._refresh(updated)

    def direction_summary(
        self,
        session_id: str,
    ) -> SessionDirectionSummaryResponse | None:
        session = self.get(session_id)
        if session is None:
            return None
        return SessionDirectionSummaryResponse(
            session_id=session.session_id,
            world_id=session.world_id,
            queued_items=session.direction_queue,
            rejected_count=session.direction_rejected_count,
            queue_status="available" if session.direction_queue else "empty",
        )

    def list_agents(self, session_id: str) -> list[SessionAgentPublicState] | None:
        session = self.get(session_id)
        if session is None:
            return None
        return list(self._ensure_agents(session).values())

    def get_agent(
        self,
        session_id: str,
        agent_id: str,
    ) -> SessionAgentPublicState | None:
        session = self.get(session_id)
        if session is None:
            return None
        return self._ensure_agents(session).get(agent_id)

    def update_agent(
        self,
        session_id: str,
        agent: SessionAgentPublicState,
    ) -> SessionAgentPublicState | None:
        session = self.get(session_id)
        if session is None:
            return None
        agents = self._ensure_agents(session)
        agents[agent.agent_id] = agent
        self._agents[session_id] = agents
        return agent

    def _refresh(self, session: WorldSession) -> WorldSession:
        updated = session.model_copy(
            update={
                "runtime_ref": self._runtime_ref(),
                "evidence_refs": session.evidence_refs.model_copy(
                    update={
                        "current_event_count": self._event_count_provider(),
                        "current_snapshot_count": self._snapshot_count_provider(),
                    }
                ),
                "updated_at": _utc_now_iso(),
            }
        )
        self._sessions[session.session_id] = updated
        return updated

    def _runtime_ref(self) -> SessionRuntimeRef:
        state = self._runtime_engine.get_state()
        return SessionRuntimeRef(
            tick_id=state.tick_id,
            world_time_seconds=state.world_time_seconds,
            step_seconds=state.step_seconds,
        )

    def _ensure_agents(
        self,
        session: WorldSession,
    ) -> dict[str, SessionAgentPublicState]:
        agents = self._agents.get(session.session_id)
        if agents is not None:
            return agents
        now = _utc_now_iso()
        default_agent = SessionAgentPublicState(
            session_id=session.session_id,
            world_id=session.world_id,
            agent_id="agent.observer",
            display_name="Observer",
            state="observing",
            public_status="ready",
            last_observation_summary="Awaiting public session events.",
            current_intent="maintain_observation",
            visible_action="observing the public session state",
            runtime_ref=self._runtime_ref(),
            evidence_refs=SessionAgentEventEvidence(
                event_count_before=self._event_count_provider(),
                event_count_after=self._event_count_provider(),
                event_delta_count=0,
            ),
            client_scripted_action=False,
            updated_at=now,
        )
        self._agents[session.session_id] = {default_agent.agent_id: default_agent}
        return self._agents[session.session_id]
