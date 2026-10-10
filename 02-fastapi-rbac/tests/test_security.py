from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def token_for(username):
    response = client.post("/token", json={"username": username})
    assert response.status_code == 200
    return response.json()["access_token"]


def test_missing_token_returns_401():
    assert client.get("/reports").status_code == 401


def test_viewer_can_read_reports():
    token = token_for("cara")
    response = client.get("/reports", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200


def test_viewer_cannot_create_reports():
    token = token_for("cara")
    response = client.post("/reports", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403


def test_admin_can_delete_reports():
    token = token_for("alice")
    response = client.delete("/reports/7", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["deleted_id"] == 7


def test_unknown_user_cannot_get_token():
    assert client.post("/token", json={"username": "nobody"}).status_code == 401
