from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_api():
    response = client.get("/app/api")
    assert response.status_code == 200


def test_getting_by_keyword():
    response = client.get("/app/api")
    assert response.status_code == 200
