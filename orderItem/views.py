from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import viewsets, mixins

from main.serializers import EmptySerializer
from order.models import Order
from .models import OrderItem
from order.serializers import OrderSerializer
from .serializers import OrderItemSerializer
from main.permissions import IsAuthorOrAdmin
# Create your views here.





class orderItemViewSet(viewsets.GenericViewSet, 
                                    mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return OrderItem.objects.filter(user=user, order=None)

# class orderActoinsViewSet(viewsets.GenericViewSet):
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthorOrAdmin]
#     serializer_class = OrderItemSerializer
#     queryset = OrderItem.objects.all()


    # @action(detail=False, methods=['get']) #, url_path='cart')
    @action(detail=False, methods=['get'] , url_path='cart')
    def view_cart_items(self, request):
        user = request.user
        items = OrderItem.objects.filter(user=user, order=None)
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)
    



    # Custom schema to indicate no input parameters
    
    @action(detail=False, methods=['post'], url_path='buy-it-now')
    def buy_single_item(self, request):
        user = request.user
        data = request.data


        # Validate the incoming data with the serializer
        serializer = OrderItemSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            # Create a new Order for the user
            new_order = Order.objects.create(user=user)

            # Create a new OrderItem and associate it with the new order
            order_item = serializer.save(user=user)
            order_item.set_order(new_order)

            # Optionally: Serialize the new order and return a response
            order_serializer = OrderSerializer(new_order)
            return Response({'detail': 'Item purchased and moved to new order.', 'order_item': order_serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'], url_path='move-to-orders', serializer_class=EmptySerializer)
    def move_all_items_to_orders(self, request):
        user = request.user
        items = OrderItem.objects.filter(user=user, order=None)
        if not items.exists():
            return Response({'details': 'No products in cart'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new Order for the user
        new_order = Order.objects.create(user=user)
        
        # Assign all OrderItems to the new Order using the set_order method
        for item in items:
            item.set_order(new_order)
        
        # Optionally: Serialize the new order and return a response
        serializer = OrderSerializer(new_order)
        return Response({'detail': 'All items moved to new order.', 'order_items': serializer.data}, status=status.HTTP_200_OK)

    def perfrom_create(self, serializer):
        serializer.save()


    # def list(self, request):
    #     user = request.user
    #     queryset = SingularProductOrder.objects.filter(user=user, gathered_orders=None)
    #     serializer = SingularProductOrderSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     user = request.user
    #     serializer = SingularProductOrderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     user = request.user
    #     if not SingularProductOrder.objects.filter(user=user, id=pk).exists():
    #         return Response({"details": "not found"} ,status=status.HTTP_404_NOT_FOUND)
    #     order = SingularProductOrder.objects.get(user=user, id=pk)
    #     serializer = SingularProductOrderSerializer(order)
    #     return Response(serializer.data)
    
    # def update(self, request, pk=None):
    #     user = request.user
    #     if not SingularProductOrder.objects.filter(user=user, id=pk).exists():
    #         return Response({"details": "not found OR forbidden"} ,status=status.HTTP_404_NOT_FOUND)
    #     order = SingularProductOrder.objects.get(user=user, id=pk)
    #     serializer = SingularProductOrderSerializer(order, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def destroy(self, request, pk=None):
    #     user = request.user
    #     if not SingularProductOrder.objects.filter(user=user, id=pk).exists():
    #         return Response({"details": "not found OR forbidden"} ,status=status.HTTP_404_NOT_FOUND)
    #     order = SingularProductOrder.objects.get(user=user, id=pk)
    #     order.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)





