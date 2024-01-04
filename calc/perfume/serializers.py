from rest_framework import serializers
from .models import CustomerOrder
from .models import Product


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = "__all__"  # You can specify specific fields if needed


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price_per_gram")
