
from app.app import app


def test_homepage():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"CloudOps Dashboard" in response.data


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_readiness():
    response = app.test_client().get("/ready")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ready"


def test_version():
    response = app.test_client().get("/version")
    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "CloudOps Dashboard"
    assert "version" in data
    assert "environment" in data
