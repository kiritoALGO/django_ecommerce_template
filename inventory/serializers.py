from rest_framework import serializers

from .models import Inventory
from product.models import Product
from size.models import Size

class InventorySerializer(serializers.ModelSerializer):
    size_text = serializers.CharField(write_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta(object):
        model = Inventory
        # fields = '__all__'
        fields = ['id', 'created_at', 'user', 'product',
                    'quantity', 'description', 'type', 'size', 'size_text']
        extra_kwargs = {
            'size': {'required': False},
            'user': {'required': False}
        }
    
    def create(self, validated_data):
        
        # Assign the user from the context (request)
        request = self.context.get('request', None)
        user = request.user if request else None

        size_text = validated_data.pop('size_text', None)

        product = validated_data['product']

        size_instance, created = Size.objects.get_or_create(size_text=size_text, product=product)
        size_instance.save()
        validated_data['size'] = size_instance

        inventory = Inventory.objects.create(user=user, **validated_data)
        return inventory
        

