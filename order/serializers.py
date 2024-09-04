from rest_framework import serializers

from .models import Order
from orderItem.serializers import OrderItemSerializer
from user.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    address = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["id", 'created_at', 'status', 'order_items', 'address', 'user']
        read_only_fields = ['created_at']

    def get_address(self, obj):
        return {
            "addressText": obj.addressText,
            "city": obj.city,
            "country": obj.country,
            "phone_number": obj.phone_number
        }
