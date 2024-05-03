from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from main.permissions import IsAuthorOrAdmin
from order.models import SingularProductOrder
from product.serializers import ProductSerializer
from .models import GatheredOrders
from .serializers import GatheredOrdersSerializer
# Create your views here.

class GatherdOrdersViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    
    def create(self, requset):
        user = requset.user
        orders = SingularProductOrder.objects.filter(user=user, gathered_orders=None)
        if not orders.exists():
            return Response({'details': "not products in cart"})
        gath_order = GatheredOrders.objects.create(user=user)
        gath_order.save()
        for Order in orders:
            order = SingularProductOrder.objects.get(id=Order.id)
            order.gathered_orders = gath_order
            order.save()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, requset):
        user = requset.user
        gath_orders = GatheredOrders.objects.filter(user=user)
        if not GatheredOrders.objects.filter(user=user).exists():
            return Response({'details': "not orders has been confirmed"})
        serializer = GatheredOrdersSerializer(gath_orders, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, requset, pk):
        gath_order = GatheredOrders.objects.get(id=pk)
        serializer = GatheredOrdersSerializer(gath_order)
        data = serializer.data
        x = []
        orders = SingularProductOrder.objects.filter(gathered_orders=gath_order)
        for order in orders:
            d = {}
            prodcut_serializer = ProductSerializer(order.product)
            d["product"] = prodcut_serializer.data
            d["quantity"] = order.quantity
            # print(order)
            x.append(d)
        data["orders"] = x
        return Response(data=data, status=status.HTTP_200_OK)
    
    def update(self, requset, pk):
        user = requset.user
        if not user.is_staff:
            return Response({'error': 'You are not authorized to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        
        gath_order = GatheredOrders.objects.get(id=pk)
        serializer = GatheredOrdersSerializer(gath_order,data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        user = request.user
        if not user.is_staff:
            return Response({'error': 'You are not authorized to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        gath_order = GatheredOrders.objects.get(id=pk)
        gath_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









