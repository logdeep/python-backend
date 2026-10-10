import pytest
from rest_framework.test import APIClient

from .models import Order, Product

pytestmark = pytest.mark.django_db


def test_product_can_be_created():
    response = APIClient().post("/api/products/", {"sku": "SKU-1", "name": "Widget", "price": "5.50", "stock": 10}, format="json")
    assert response.status_code == 201
    assert Product.objects.get(sku="SKU-1").stock == 10


def test_order_reduces_stock_and_records_price():
    product = Product.objects.create(sku="SKU-2", name="Gadget", price="3.25", stock=8)
    response = APIClient().post("/api/orders/", {"product": product.id, "quantity": 3}, format="json")
    assert response.status_code == 201
    product.refresh_from_db()
    assert product.stock == 5
    assert Order.objects.get().unit_price == product.price


def test_order_rejects_insufficient_stock():
    product = Product.objects.create(sku="SKU-3", name="Gadget", price="3.25", stock=1)
    response = APIClient().post("/api/orders/", {"product": product.id, "quantity": 2}, format="json")
    assert response.status_code == 400
    product.refresh_from_db()
    assert product.stock == 1
