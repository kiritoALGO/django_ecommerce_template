from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from .serializers import ProductSerializer
from .models import Product
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions


# all for Prdoucts
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

# from rest_framework import mixins, viewsets 
# class ProductsViewSet(viewsets.ViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
class ProductsViewSet(viewsets.GenericViewSet, 
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser | ReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    parser_classes = [MultiPartParser, FormParser] # Added by Abdo

    # Added by Abdo
    def create(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Log request data for debugging
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Errors:", serializer.errors)  # Log any validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    # # def list(self, request):
    # #     products = Product.objects.all()
    # #     serializer = ProductSerializer(products, many=True)
    # #     return Response(serializer.data)


    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    # # def create(self, request):
    # #     serializer = ProductSerializer(data=request.data)
    # #     if serializer.is_valid():
    # #         serializer.save()
    # #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # def retrieve(self, request, pk=None):
    #     if not Product.objects.filter(id=pk).exists():
    #         return Response({"details": "not found"} ,status=status.HTTP_404_NOT_FOUND)
    #     product = Product.objects.get(id=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    
    
    # def update(self, request, pk=None):
    #     if not Product.objects.filter(id=pk).exists(): # not checked condition
    #         return Response({"details": "Product not found"} ,status=status.HTTP_404_NOT_FOUND)
    #     product = Product.objects.get(id=pk)

    #     serializer = ProductSerializer(instance=product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # def destroy(self, request, pk=None):
    #     product = Product.objects.get(id=pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
