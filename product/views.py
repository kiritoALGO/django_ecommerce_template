from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductSerializer, CreateProductSerializer
from .models import Product
# Create your views here.

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions


# all for Prdoucts
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class ProductsViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | ReadOnly]
    print(permission_classes)
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self, request, pk=None):
        if not Product.objects.filter(id=pk).exists():
            return Response({"details": "not found"} ,status=status.HTTP_404_NOT_FOUND)
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    
    # @authentication_classes([SessionAuthentication, TokenAuthentication])
    # @permission_classes([permissions.IsAdminUser])
    def update(self, request, pk=None):
        if not Product.objects.filter(id=pk).exists(): # not checked condition
            return Response({"details": "not found"} ,status=status.HTTP_404_NOT_FOUND)
        product = Product.objects.get(id=pk)

        if not product.gathered_orders:
            return Response({"details": "can not change it"} ,status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @authentication_classes([SessionAuthentication, TokenAuthentication])
    # @permission_classes([permissions.IsAdminUser])
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

