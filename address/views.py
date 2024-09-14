from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from main.permissions import IsAuthorOrAdmin

from .models import Address
from .serializer import AddressSerializer
# Create your views here.
class addressViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        ):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Address.objects.filter(user=user)

