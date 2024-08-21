from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import login, authenticate
# Create your views here.



class UserViewSet(  viewsets.GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,  ):
    """
    A viewset that provides the standard actions
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer()


    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """
        Log in a user and return token and user data.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'detail': 'Invalid username or password'}, status=status.HTTP_404_NOT_FOUND)

        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})

    @action(detail=False, methods=['get'], url_path='test-token', authentication_classes=[TokenAuthentication])
    def test_token(self, request):
        """
        Test view to verify token authentication.
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)




# class SignupView(APIView):
#     """
#     post:
#     Create a new user and return token and user data.
#     """
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = User.objects.get(username=request.data.get('username'))
#             user.set_password(request.data.get('password'))
#             user.save()
#             token = Token.objects.create(user=user)
#             return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.shortcuts import get_object_or_404
# from rest_framework.authtoken.models import Token
# @api_view(['POST'])
# def login(request):
#     """
#     Log in a user and return token and user data.
#     """
#     username=request.data['username']
#     password=request.data['password']
#     if not username or not password:
#         return Response({'detail': 'username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
#     user = get_object_or_404(User, username=username)
#     if not user.check_password(password):
#         return Response({'detail': 'invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
    
#     token, created = Token.objects.get_or_create(user=user)
#     serializer = UserSerializer(instance=user)
#     return Response({'token': token.key, 'user': serializer.data})

# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def test_token(request):
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data, status=status.HTTP_302_FOUND)

# # from .serializers import TestSerializer
# # @api_view(['POST'])
# # def test_view(request):
# #     """
# #     Test view to verify Swagger displays parameters correctly.
# #     """
# #     serializer = TestSerializer(data=request.data)
# #     if serializer.is_valid():
# #         return Response(serializer.validated_data)
# #     return Response(serializer.errors, status=400)