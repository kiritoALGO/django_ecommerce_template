from rest_framework import serializers

from .models import Order
from orderItem.serializers import OrderItemSerializer
from user.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    # address = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id", 
            'created_at', 
            'status', 
            'order_items', 
            'addressText', 
            'city', 
            'country', 
            'phone_number', 
            'user',
          ]
        read_only_fields = ['created_at']

    def get_address(self, obj):
        return {
            "addressText": obj.addressText,
            "city": obj.city,
            "country": obj.country,
            "phone_number": obj.phone_number,
        }
    
    def update(self, instance, validated_data):
        # Update user data if it's provided in PATCH request
        user_data = self.context.get('request').data.get('user', None)
        if user_data:
            instance.user.first_name = user_data.get('first_name', instance.user.first_name)
            instance.user.last_name = user_data.get('last_name', instance.user.last_name)
            instance.user.save()

        # address_data = self.context.get('request').data.get('adderss', None)
        # if address_data:
        #     instance.address.country = address_data.get('country', instance.address.country)
        #     instance.address.city = address_data.get('city', instance.address.city)
        #     instance.address.addressText = address_data.get('addressText', instance.address.addressText)
        #     instance.address.phone_number = address_data.get('phone_number', instance.address.phone_number)
        #     instance.address.save()

        # Update address fields
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.addressText = validated_data.get('addressText', instance.addressText)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()

        # Update status fields
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        
        return instance
