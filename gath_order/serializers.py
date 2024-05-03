from rest_framework import serializers
from .models import GatheredOrders


class GatheredOrdersSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = GatheredOrders
        fields = "__all__"
        read_only_fields = ['created_at']