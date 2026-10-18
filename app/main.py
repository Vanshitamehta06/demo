"""Beginner-friendly **self-healing Ci/cd Pipeline** API."""
from __future__ import annotations

from fastapi import FastAPI, HTTPException, Response

from app.models import Record, RecordIn
from app.store import RecordStore

app = FastAPI(title="Beginner-friendly **self-healing Ci/cd Pipeline** API")
store = RecordStore()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/pipelines", response_model=Record, status_code=201)
def create(body: RecordIn) -> Record:
    return store.create(body)


@app.get("/api/pipelines", response_model=list[Record])
def list_all() -> list[Record]:
    return store.list()


@app.get("/api/pipelines/{record_id}", response_model=Record)
def get_one(record_id: int) -> Record:
    record = store.get(record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Not found")
    return record


@app.put("/api/pipelines/{record_id}", response_model=Record)
def update(record_id: int, body: RecordIn) -> Record:
    record = store.update(record_id, body)
    if record is None:
        raise HTTPException(status_code=404, detail="Not found")
    return record


@app.delete("/api/pipelines/{record_id}", status_code=204)
def delete(record_id: int) -> Response:
    if not store.delete(record_id):
        raise HTTPException(status_code=404, detail="Not found")
    return Response(status_code=204)
