from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_process_product() -> None:
    response = client.post(
        "/products",
        json={
            "product_id": "OEM-100",
            "product_name": "Control Module",
            "quantity": 4,
            "price": 12.5,
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "product_id": "OEM-100",
        "product_name": "Control Module",
        "quantity": 4,
        "unit_price": 12.5,
        "total_value": 50.0,
        "status": "processed",
    }


def test_reject_negative_quantity() -> None:
    response = client.post(
        "/products",
        json={
            "product_id": "OEM-100",
            "product_name": "Control Module",
            "quantity": -1,
            "price": 12.5,
        },
    )
    assert response.status_code == 422


def test_reject_blank_product_name() -> None:
    response = client.post(
        "/products",
        json={
            "product_id": "OEM-100",
            "product_name": "   ",
            "quantity": 1,
            "price": 12.5,
        },
    )
    assert response.status_code == 422
