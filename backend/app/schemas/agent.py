from pydantic import BaseModel, Field


class AgentSnapshot(BaseModel):
    agent_id: str = Field(default="agent-v1")
    label: str = Field(default="WorldEngine Seed Agent")
