from django.db import models

# Create your models here.
class ShippingRate(models.Model):
    governorate = models.CharField(max_length=100)
    shipping_price = models.FloatField(default=60,blank=True,null=True)