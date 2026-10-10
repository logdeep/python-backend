from rest_framework import generics

from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.select_related("product").all().order_by("id")
    serializer_class = OrderSerializer
