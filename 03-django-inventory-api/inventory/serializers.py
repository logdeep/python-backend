from django.db import transaction
from rest_framework import serializers

from .models import Order, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "sku", "name", "price", "stock", "created_at"]
        read_only_fields = ["id", "created_at"]


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "product", "quantity", "unit_price", "total", "created_at"]
        read_only_fields = ["id", "unit_price", "total", "created_at"]

    def create(self, validated_data):
        with transaction.atomic():
            product = Product.objects.select_for_update().get(pk=validated_data["product"].pk)
            quantity = validated_data["quantity"]
            if quantity < 1:
                raise serializers.ValidationError({"quantity": "Must be at least 1."})
            if product.stock < quantity:
                raise serializers.ValidationError({"quantity": "Insufficient stock."})
            product.stock -= quantity
            product.save(update_fields=["stock"])
            return Order.objects.create(product=product, quantity=quantity, unit_price=product.price)
