from rest_framework import serializers

from .models import Order
from orderItem.serializers import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta(object):
        model = Order
        fields = ["id", 'user', 'created_at', 'status', 'addressText', 'city', 'country', 'phone_number', 'order_items']
        read_only_fields = ['created_at']