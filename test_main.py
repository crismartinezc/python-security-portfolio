from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task_success():
    response = client.post("/tasks/", json={
        "title": "Automatizar reporte de datos",
        "description": "Extraer y consolidar archivos con Python",
        "priority": 3,
        "tags": ["python", "automation"]
    })
    assert response.status_code == 201
    data = response.json()
    assert data["task"]["title"] == "Automatizar reporte de datos"
    assert data["task"]["priority"] == 3

def test_create_task_invalid_title():
    # El título es demasiado corto (falla la validación de min_length=3)
    response = client.post("/tasks/", json={
        "title": "AI",
        "priority": 1
    })
    assert response.status_code == 422