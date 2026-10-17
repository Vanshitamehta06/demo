"""In-memory record store."""
from __future__ import annotations

from app.models import Record, RecordIn


class RecordStore:
    def __init__(self) -> None:
        self._records: dict[int, Record] = {}
        self._next_id = 1

    def create(self, data: RecordIn) -> Record:
        record = Record(id=self._next_id, **data.model_dump())
        self._records[record.id] = record
        self._next_id += 1
        return record

    def list(self) -> list[Record]:
        return list(self._records.values())

    def get(self, record_id: int) -> Record | None:
        return self._records.get(record_id)

    def update(self, record_id: int, data: RecordIn) -> Record | None:
        if record_id not in self._records:
            return None
        record = Record(id=record_id, **data.model_dump())
        self._records[record_id] = record
        return record

    def delete(self, record_id: int) -> bool:
        return self._records.pop(record_id, None) is not None
