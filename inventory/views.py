from rest_framework import viewsets, mixins, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


from .models import Inventory
from .serializers import InventorySerializer
# Create your views here.
class InventoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer