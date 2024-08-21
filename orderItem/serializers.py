from rest_framework import serializers
from orderItem.models import OrderItem
from .models import Order

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = OrderItem
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False}
        }
        # fields = ['id', 'user', 'product', 'quantity', 'gathered_orders']

    def create(self, validated_data):
        # Assign the user from the context (request)
        request = self.context.get('request', None)
        user = request.user if request else None
        
        product = validated_data.get('product', None)
        quantity= validated_data.get('quantity', 1)

        existing_order_item = OrderItem.objects.filter(user=user, product=product, order__isnull=True).first()

        if existing_order_item:
            if quantity:
                existing_order_item.quantity += quantity
            existing_order_item.save()
            return existing_order_item
        else:
            validated_data['user'] = user
            return super().create(validated_data)





# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = "__all__"

# cart -> Order
# 
# 
# 