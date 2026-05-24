from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field

from app.schemas.entity import EntityRef


class WorldCell(BaseModel):
    id: str = Field(min_length=1)
    label: Optional[str] = None
    kind: Literal["world"] = "world"
    entity_refs: List[EntityRef] = Field(default_factory=list)
    child_cells: List["WorldCell"] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class WorldSpec(BaseModel):
    schema_version: Literal["0.2"] = "0.2"
    id: str = Field(min_length=1)
    label: Optional[str] = None
    root: WorldCell
    metadata: Dict[str, Any] = Field(default_factory=dict)
