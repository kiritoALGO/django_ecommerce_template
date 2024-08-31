from django.db import models
from user.models import User
# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addressText = models.CharField(max_length=1000)
    city = models.CharField(max_length=100, default='Cairo')
    country = models.CharField(max_length=100, default='Egypt')
    phone_number = models.CharField(max_length=20, default="", null=True, blank=True)
    is_default = models.BooleanField(default=False)
    def __str__(self):
        return self.addressText + ' - ' + self.city + ', ' + self.country
