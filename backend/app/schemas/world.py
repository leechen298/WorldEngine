from pydantic import BaseModel, Field


class WorldSnapshot(BaseModel):
    world_id: str = Field(default="world-v1")
    label: str = Field(default="WorldEngine Seed World")
