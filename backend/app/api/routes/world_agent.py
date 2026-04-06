"""Agent-driven world param proposal endpoint."""

from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

from app.agent.params_agent import ParamsAgent
from app.schemas.api import ApiResponse

router = APIRouter(prefix="/world/agent", tags=["agent"])


class ProposeAndApplyRequest(BaseModel):
    goal: Optional[str] = None


def get_params_agent(request: Request) -> ParamsAgent:
    return request.app.state.params_agent


@router.post("/params/propose-and-apply", response_model=ApiResponse[Dict[str, Any]])
async def propose_and_apply(
    request_body: ProposeAndApplyRequest = ProposeAndApplyRequest(),
    params_agent: ParamsAgent = Depends(get_params_agent),
) -> Any:
    result = await params_agent.propose_and_apply(goal=request_body.goal)

    if not result["applied"]:
        raise HTTPException(
            status_code=422,
            detail={
                "msg": "Agent proposal rejected after max attempts",
                "errors": result.get("errors", []),
                "metrics": result.get("metrics", {}),
                "data": {
                    "errors": result.get("errors", []),
                    "metrics": result.get("metrics", {}),
                    "attempts": result["attempts"],
                },
            },
        )

    return ApiResponse(data=result)
