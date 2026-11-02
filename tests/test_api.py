from starlette.testclient import TestClient
from tools.api_servidor import app

client = TestClient(app)

def test_leer_raiz():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ONLINE"
    assert response.json()["author"] == "Chris"

def test_consultar_logs():
    response = client.get("/auditoria/logs")
    assert response.status_code == 200
    data = response.json()
    assert "total_records" in data
    assert "logs" in data
    assert isinstance(data["logs"], list)

def test_registrar_incidente():
    payload = {
        "evento": "Test automatizado de seguridad con pytest",
        "nivel_riesgo": "BAJO"
    }
    response = client.post("/auditoria/logs", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "SUCCESS"
    assert data["data"]["evento"] == payload["evento"]