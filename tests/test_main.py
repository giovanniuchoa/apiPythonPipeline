from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["status"] == "healthy"

def test_create_item():
    response = client.post(
        "/items/",
        json={"nome": "Item Teste", "descricao": "Descrição do item teste"}
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Item Teste"
    assert response.json()["descricao"] == "Descrição do item teste"

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)