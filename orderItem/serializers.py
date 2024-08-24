from rest_framework import serializers
from orderItem.models import OrderItem

from size.models import Size
from product.serializers import ProductSerializer 
from .models import Order
class OrderItemSerializer(serializers.ModelSerializer):
    size_text = serializers.CharField(write_only=True)
    product = ProductSerializer(read_only=True)
    class Meta(object):
        model = OrderItem
        fields = ['id', 'user', 'product', 'quantity', 'order', 'totalOrderItemsPrice', 'size', 'size_text']
        # fields = "__all__"
        extra_kwargs = {
            'user': {'required': False},
            'order': {'required': False},
            'totalOrderItemsPrice': {'required': False},
            'qunatity': {'required': False},
            'size': {'required': False},
            'product': {'required': True},
            'size_text': {'required': True}
        }

    def create(self, validated_data):
        # Assign the user from the context (request)
        request = self.context.get('request', None)
        user = request.user if request else None
        
        size_text = validated_data.pop('size_text', None)
        product = validated_data.get('product', None)
        quantity= validated_data.get('quantity', 1)
        validated_data['size'] = Size.objects.get(size_text=size_text, product=product)
        # validated_data['order'] = validated_data.get('order', None)

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