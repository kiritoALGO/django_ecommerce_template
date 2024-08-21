from rest_framework.serializers import ModelSerializer


from .models import Size



class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ['size_text', 'quantity']
        