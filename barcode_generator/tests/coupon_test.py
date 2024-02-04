import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def app_client():
    client = TestClient(app)
    return client

@pytest.mark.parametrize("test_input,expected", [(6, 6), (7, 7), (100, 100)])
def test_can_generate_random_characters(app_client, test_input, expected):
    response = app_client.post("/", json={"length": test_input})
    data = response.json()
    assert data.get("result", None) is not None
    assert len(data.get("result")) == expected

def test_can_get_health(app_client):
    response = app_client.get("/health")
    assert response.status_code == 200