# from rest_framework import viewsets, status
# from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import viewsets, mixins
from .models import SingularProductOrder
from .serializers import SingularProductOrderSerializer
from main.permissions import IsAuthorOrAdmin
# Create your views here.





class SingularProducOrdertViewSet(viewsets.GenericViewSet, 
                                    mixins.ListModelMixin,
                                    mixins.CreateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorOrAdmin]
    serializer_class = SingularProductOrderSerializer
    queryset = SingularProductOrder.objects.all()

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





