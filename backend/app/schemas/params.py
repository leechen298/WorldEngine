from typing import Any, Literal, Optional

from pydantic import BaseModel


class ParamPatchItem(BaseModel):
    op: Literal["add", "set", "remove"]
    path: str
    value: Optional[Any] = None


class ApplyParamsRequest(BaseModel):
    patches: list[ParamPatchItem]
