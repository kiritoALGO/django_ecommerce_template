from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import ShippingRate
from .serializers import ShippingRateSerializer
# Create your views here.
class shippingRateViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        ):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only admins can perform write operations
            self.permission_classes = [permissions.IsAdminUser]
        else:
            # Authenticated users can read, non-authenticated users can view publicly
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return super().get_permissions()

    serializer_class = ShippingRateSerializer
    queryset = ShippingRate.objects.all()