from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from main.permissions import IsAuthorOrAdmin
from orderItem.models import OrderItem
from product.serializers import ProductSerializer
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthorOrAdmin]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        orderitems = OrderItem.objects.filter(user=user, order=None)
        if not orderitems.exists():
            raise Response({'details': "No products in cart"}, status=status.HTTP_400_BAD_REQUEST)
        order = serializer.save(user=user)
        for orderitem in orderitems:
            orderitem.orders = order
            orderitem.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        x = []
        orderitems = OrderItem.objects.filter(order=instance)
        for orderitem in orderitems:
            d = {}
            product_serializer = ProductSerializer(orderitem.product)
            d["product"] = product_serializer.data
            d["quantity"] = orderitem.quantity
            x.append(d)
        data["orderitems"] = x
        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            return Response({'error': 'You are not authorized to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class AdminsOrdersViewSets(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
