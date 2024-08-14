from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from main.permissions import IsAuthorOrAdmin
from order.models import SingularProductOrder
from product.serializers import ProductSerializer
from .models import GatheredOrders
from .serializers import GatheredOrdersSerializer

class GatheredOrdersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                            mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    serializer_class = GatheredOrdersSerializer
    queryset = GatheredOrders.objects.all()
    
    def get_queryset(self):
        user = self.request.user
        return GatheredOrders.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        orders = SingularProductOrder.objects.filter(user=user, gathered_orders=None)
        if not orders.exists():
            raise Response({'details': "No products in cart"}, status=status.HTTP_400_BAD_REQUEST)
        gath_order = serializer.save(user=user)
        for order in orders:
            order.gathered_orders = gath_order
            order.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        x = []
        orders = SingularProductOrder.objects.filter(gathered_orders=instance)
        for order in orders:
            d = {}
            product_serializer = ProductSerializer(order.product)
            d["product"] = product_serializer.data
            d["quantity"] = order.quantity
            x.append(d)
        data["orders"] = x
        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            return Response({'error': 'You are not authorized to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
