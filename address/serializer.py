from rest_framework.serializers import Serializer
from .models import Address

class AddressSerializer(Serializer):
    class Meta:
        model = Address
        fields = "__all__"
        
