"""Request/response models."""
from __future__ import annotations

from pydantic import BaseModel, Field


class RecordIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=2000)


class Record(RecordIn):
    id: int
