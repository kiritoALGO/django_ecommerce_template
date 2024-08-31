from django.urls import path
from .views import (
    SendVerificationCodeView,
    VerifyCodeView,
    PasswordResetRequestView,
    PasswordResetConfirmView
)

urlpatterns = [
    path('send-verification-code/', SendVerificationCodeView.as_view(), name='send_verification_code'),
    path('verify-code/', VerifyCodeView.as_view(), name='verify_code'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
