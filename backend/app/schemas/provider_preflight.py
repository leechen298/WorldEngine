from __future__ import annotations

from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_core import PydanticCustomError

from app.schemas.world import PublicProviderReadiness
from app.schemas.world_generation import (
    GenerationDiagnostic,
    WorldviewCreationMode,
    WorldviewGenerationMode,
    WorldviewGenerationRedaction,
    WorldviewGenerationRequest,
    WorldviewGenerationStatus,
    WorldviewGenerationValidationMetadata,
    _private_mapping_markers,
    _private_worldview_markers,
)


class ProviderWorldviewPreflightRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    request_id: str = Field(default="provider-worldview-preflight", min_length=1)
    worldview_premise: Optional[str] = Field(default=None, min_length=1, max_length=4000)
    allow_deterministic_fallback: bool = True
    public_constraints: Dict[str, object] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _reject_private_worldview_markers(self) -> "ProviderWorldviewPreflightRequest":
        forbidden_values: list[str] = []
        if self.worldview_premise is not None:
            forbidden_values.extend(_private_worldview_markers(self.worldview_premise))
        forbidden_values.extend(_private_mapping_markers(self.public_constraints))
        if forbidden_values:
            raise PydanticCustomError(
                "private_worldview_input",
                "worldview preflight request contains private or unsupported fields",
            )
        return self

    def to_worldview_request(self) -> Optional[WorldviewGenerationRequest]:
        if self.worldview_premise is None:
            return None
        return WorldviewGenerationRequest(
            request_id=self.request_id,
            worldview_premise=self.worldview_premise,
            allow_deterministic_fallback=self.allow_deterministic_fallback,
            public_constraints=self.public_constraints,
        )


class ProviderWorldviewGenerationPreflightSummary(BaseModel):
    model_config = ConfigDict(extra="forbid")

    generation_status: WorldviewGenerationStatus
    generation_mode: WorldviewGenerationMode
    creation_mode: WorldviewCreationMode
    llm_backed: bool
    provider_backed: bool
    deterministic_generic_fallback_detected: bool
    validation_metadata: WorldviewGenerationValidationMetadata
    redaction: WorldviewGenerationRedaction
    warnings: List[str] = Field(default_factory=list)
    blockers: List[str] = Field(default_factory=list)
    diagnostics: List[GenerationDiagnostic] = Field(default_factory=list)


class ProviderWorldviewPreflightResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["0.11.1"] = "0.11.1"
    preflight_status: Literal[
        "provider_ready_blocked_without_live_authorization",
        "not_configured",
        "deterministic_fallback_available",
        "safe_mock_available",
        "unsupported_provider",
        "no_worldview_request",
    ]
    provider: PublicProviderReadiness
    live_call_authorized: bool = False
    call_attempted: bool = False
    worldengine_owned_generation: bool = True
    worldview: Optional[ProviderWorldviewGenerationPreflightSummary] = None
    warnings: List[str] = Field(default_factory=list)
    blockers: List[str] = Field(default_factory=list)
