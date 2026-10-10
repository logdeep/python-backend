from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_process_product_calculates_total():
    response = client.post("/products", json={"product_id": "OEM-1", "product_name": "Widget", "quantity": 3, "price": 12.5})
    assert response.status_code == 200
    assert response.json()["total_value"] == 37.5
    assert response.json()["status"] == "processed"


def test_invalid_quantity_is_rejected():
    response = client.post("/products", json={"product_id": "OEM-1", "product_name": "Widget", "quantity": -1, "price": 12.5})
    assert response.status_code == 422


def test_blank_product_name_is_rejected():
    response = client.post("/products", json={"product_id": "OEM-1", "product_name": "   ", "quantity": 1, "price": 1})
    assert response.status_code == 422
