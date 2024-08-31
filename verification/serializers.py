from rest_framework import serializers
from .models import VerificationCode
from user.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class VerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        code = data.get('code')

        try:
            user = User.objects.get(email=email)
            verification_code = VerificationCode.objects.get(user=user, code=code)

            if verification_code.is_expired():
                raise serializers.ValidationError('Code has expired.')

        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError('Invalid code.')

        return data

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        email = data.get('email')

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found.')

        return data

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def validate(self, data):
        email = data.get('email')
        code = data.get('code')

        try:
            user = User.objects.get(email=email)
            verification_code = VerificationCode.objects.get(user=user, code=code)

            if verification_code.is_expired():
                raise serializers.ValidationError('Code has expired.')

        except VerificationCode.DoesNotExist:
            raise serializers.ValidationError('Invalid code.')

        return data
