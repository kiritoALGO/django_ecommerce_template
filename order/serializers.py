from rest_framework import serializers
from order.models import SingularProductOrder


class SingularProductOrderSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = SingularProductOrder
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False}
        }
        # fields = ['id', 'user', 'product', 'quantity', 'gathered_orders']

