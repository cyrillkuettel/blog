import pytest

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_request_matterjs():
    response = client.get("/app/matterjs")
    assert response.status_code == 200


def test_mounted_directory_path_correct():
    response = client.get("/app/templates/angry_birds/bird.js")
    r = response.content
    assert "class Bird" in str(r)
    assert response.status_code == 200

def test_client_can_fetch_images():
    response = client.get("app/templates/angry_birds/images/dot.png")
    assert response.status_code == 200
