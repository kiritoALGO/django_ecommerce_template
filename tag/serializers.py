from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Tag
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {'required': True},
        }