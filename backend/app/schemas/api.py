from __future__ import annotations

from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    code: int = 0
    data: T
    msg: str = "ok"


class ApiErrorResponse(BaseModel):
    code: int
    msg: str
    data: Optional[object] = None
