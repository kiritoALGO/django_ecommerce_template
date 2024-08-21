from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from main.permissions import IsAuthorOrAdmin
from .serializers import SizeSerializer
from .models import Size
# Create your views here.
class SizeViewSet(viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    ):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Size.objects.all()
    serializer_class = SizeSerializer