from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import VerificationCode
from user.models import User
from .serializers import (
    VerificationCodeSerializer,
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import make_password




class SendVerificationCodeView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                self.send_verification_code(user)
                return Response({'detail': 'Verification code sent.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_verification_code(self, user):
        code = VerificationCode.generate_code()
        expires_at = timezone.now() + timedelta(minutes=10)
        VerificationCode.objects.create(user=user, code=code, expires_at=expires_at)
        send_mail(
            'Your Verification Code',
            f'Your verification code is {code}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )


class VerifyCodeView(generics.GenericAPIView):
    serializer_class = VerificationCodeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            try:
                user = User.objects.get(email=email)
                verification_code = VerificationCode.objects.get(user=user, code=code)
                verification_code.delete()  # Optionally delete code after successful verification
                user.is_active = True
                user.save()
                return Response({'detail': 'Code verified.'}, status=status.HTTP_200_OK)
            except VerificationCode.DoesNotExist:
                return Response({'detail': 'Invalid code.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                self.send_verification_code(user)
                return Response({'detail': 'Password reset code sent.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_verification_code(self, user):
        code = VerificationCode.generate_code()
        expires_at = timezone.now() + timedelta(minutes=10)
        VerificationCode.objects.create(user=user, code=code, expires_at=expires_at)
        send_mail(
            'Your Password Reset Code',
            f'Your password reset code is {code}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )


class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            new_password = serializer.validated_data['new_password']
            try:
                user = User.objects.get(email=email)
                verification_code = VerificationCode.objects.get(user=user, code=code)
                user.password = make_password(new_password)
                user.save()
                verification_code.delete()  # Optionally delete code after successful password reset
                return Response({'detail': 'Password reset successful.'}, status=status.HTTP_200_OK)
            except VerificationCode.DoesNotExist:
                return Response({'detail': 'Invalid code.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

