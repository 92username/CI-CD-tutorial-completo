from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_event():
    resp = client.get("/api/v1/event")
    assert resp.status_code == 200
    assert resp.json() == {"message": "evento gerado"}

def test_metrics():
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "api_requests_total" in resp.text
