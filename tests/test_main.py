from fastapi.testclient import TestClient
import sys
sys.path.append('..')
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200