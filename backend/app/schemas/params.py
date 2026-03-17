from typing import Any, Optional

from pydantic import BaseModel


class ParamPatchItem(BaseModel):
    op: str
    path: str
    value: Optional[Any] = None


class ApplyParamsRequest(BaseModel):
    patches: list[ParamPatchItem]
