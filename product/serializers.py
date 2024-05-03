from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at']
        read_only_fields = ['created_at']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'price': {'required': False},
        }

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at']
        read_only_fields = ['created_at']
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'price': {'required': True},
        }