from app.models import RecordIn
from app.store import RecordStore


def test_crud_cycle():
    store = RecordStore()
    created = store.create(RecordIn(name="First"))
    assert store.get(created.id) == created
    assert store.update(created.id, RecordIn(name="Renamed")).name == "Renamed"
    assert [r.name for r in store.list()] == ["Renamed"]
    assert store.delete(created.id) is True
    assert store.get(created.id) is None


def test_missing_records():
    store = RecordStore()
    assert store.update(99, RecordIn(name="x")) is None
    assert store.delete(99) is False
