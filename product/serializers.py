from rest_framework import serializers
from .models import Product
from tag.models import Tag
from tag.serializers import TagSerializer

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True,many=True)
    tags_details = serializers.ListField(child=serializers.CharField(), required=False)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'description', 'created_at', 'tags', 'tags_details']
        read_only_fields = ['created_at']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'price': {'required': False},
            'image': {'required': False},
            'tags_details': {'required': False},
        }

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        if self.instance is None:  # This means it's a creation operation
            self.fields['name'].required = True
            self.fields['description'].required = True
            self.fields['price'].required = True
            self.fields['image'].required = True
            self.fields['tags_details'].required = False

    def create(self, validated_data):
        print("validated data:", validated_data)  # Add this line
        tags_data = validated_data.pop('tags_details', [])
        print("Tags data:", tags_data)  # Add this line
        product = Product.objects.create(**validated_data)
    
        for tag_data in tags_data:
            print("Tag data:", tag_data)  # Add this line
            tag, created = Tag.objects.get_or_create(name=tag_data)
            product.tags.add(tag)

        return product

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags_details', [])
        instance = super().update(instance, validated_data)
        instance.tags.clear()

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data)
            instance.tags.add(tag)

        return instance
