from rest_framework.serializers import ModelSerializer
from .models import ShippingRate

class ShippingRateSerializer(ModelSerializer):
    class Meta:
        model = ShippingRate
        fields = "__all__"
        
