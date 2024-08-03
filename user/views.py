from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSignupSerializer
from .models import User
from django.contrib.auth import login, authenticate
# Create your views here.

class SignupView(APIView):
    """
    post:
    Create a new user and return token and user data.
    """
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data.get('username'))
            user.set_password(request.data.get('password'))
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
@api_view(['POST'])
def login(request):
    """
    Log in a user and return token and user data.
    """
    username=request.data['username']
    password=request.data['password']
    if not username or not password:
        return Response({'detail': 'username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_object_or_404(User, username=username)
    if not user.check_password(password):
        return Response({'detail': 'invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSignupSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data})




from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    # print(request.user.username)
    return Response("Passed for {}".format(request.user.email))

from .serializers import TestSerializer
@api_view(['POST'])
def test_view(request):
    """
    Test view to verify Swagger displays parameters correctly.
    """
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data)
    return Response(serializer.errors, status=400)