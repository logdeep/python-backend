from django.urls import path
from .views import OrderListCreateView, ProductDetailView, ProductListCreateView

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("orders/", OrderListCreateView.as_view(), name="order-list"),
]
