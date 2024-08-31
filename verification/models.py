from django.db import models
from django.conf import settings
import random
import string
from django.utils import timezone
from datetime import timedelta

class VerificationCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    @classmethod
    def generate_code(cls):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
