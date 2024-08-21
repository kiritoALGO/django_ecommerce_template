from rest_framework import serializers
from .models import Product
from tag.models import Tag
from tag.serializers import TagSerializer
from size.models import Size
from size.serializers import SizeSerializer

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True,many=True)
    tags_details = serializers.ListField(child=serializers.CharField(), required=False)
    image = serializers.ImageField(required=False)
    sizes = SizeSerializer(many=True, read_only=True)
    # sizes = SizeSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image', 'description', 'created_at', 'tags', 'tags_details', 'sizes']
        read_only_fields = ['created_at']
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'price': {'required': False},
            'image': {'required': False},
            'tags_details': {'required': False},
            # 'sizes': {'required': True},
        }

    

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        if self.instance is None:  # This means it's a creation operation
            self.fields['name'].required = True
            self.fields['description'].required = True
            self.fields['price'].required = True
            self.fields['image'].required = True
            self.fields['tags_details'].required = False
            # self.fields['sizes'].required = True

    def create(self, validated_data):
        # print("validated data:", validated_data)  # Add this line
        tags_data = validated_data.pop('tags_details', [])
        # sizes_data = validated_data.pop('sizes', [])
        # print("Tags data:", tags_data)  # Add this line
        product = Product.objects.create(**validated_data)
    
        for tag_data in tags_data:
            print("Tag data:", tag_data)  # Add this line
            tag, created = Tag.objects.get_or_create(name=tag_data)
            product.tags.add(tag)
        
        # for size_data in sizes_data:
        #     Size.objects.create(product=product, **size_data)

        return product

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags_details', [])
        # sizes_data = validated_data.pop('sizes', [])
        instance = super().update(instance, validated_data)
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data)
            instance.tags.add(tag)

        # for size_data in sizes_data:
        #     size_text = size_data.get('size_text')
        #     quantity = size_data.get('quantity')

        #     size_instance = instance.sizes.filter(size_text=size_text).first()
        #     if size_instance:
        #         size_instance.quantity += quantity
        #         size_instance.save()
        #     else:
        #         instance.sizes.create(size_text=size_text, quantity=quantity)

        return instance


class AddSizesToProductSerializer(serializers.Serializer):
    sizes = SizeSerializer(many=True)

    def create(self, validated_data):
        product = self.context.get('product')
        sizes_data = validated_data.get('sizes')

        for size_data in sizes_data:
            size_text = size_data.get('size_text')
            quantity = size_data.get('quantity')

            size_instance = product.sizes.filter(size_text=size_text).first()
            if size_instance:
                size_instance.quantity += quantity
                size_instance.save()
            else:
                Size.objects.create(product=product, **size_data)

        return product

