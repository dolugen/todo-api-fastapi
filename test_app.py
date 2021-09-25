import pytest
from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_index_empty(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_new_and_get(client):
    data = {"id": 1, "title": "get milk"}
    response = client.post("/", json=data)
    assert response.json() == data

    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == data

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [data]


def test_ok():
    assert True
