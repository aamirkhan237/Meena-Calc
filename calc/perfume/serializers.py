from rest_framework import serializers
from .models import CustomerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = "__all__"  # You can specify specific fields if needed
