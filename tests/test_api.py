from fastapi.testclient import TestClient

from app import main


def client() -> TestClient:
    main.store = main.RecordStore()
    return TestClient(main.app)


def test_crud_over_http():
    c = client()
    created = c.post("/api/deliverys", json={"name": "First"})
    assert created.status_code == 201
    rid = created.json()["id"]
    assert c.get(f"/api/deliverys/{rid}").json()["name"] == "First"
    assert c.put(f"/api/deliverys/{rid}", json={"name": "Renamed"}).json()["name"] == "Renamed"
    assert len(c.get("/api/deliverys").json()) == 1
    assert c.delete(f"/api/deliverys/{rid}").status_code == 204
    assert c.get(f"/api/deliverys/{rid}").status_code == 404


def test_validation_and_health():
    c = client()
    assert c.post("/api/deliverys", json={"name": ""}).status_code == 422
    assert c.get("/health").json() == {"status": "ok"}
