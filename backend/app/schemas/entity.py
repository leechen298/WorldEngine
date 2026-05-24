from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class EntityRef(BaseModel):
    id: str = Field(min_length=1)
    kind: str = Field(min_length=1)
    label: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
