from typing import Any
from django.db import models


from address.models import Address
from user.models import User
# Create your models here.

class Order(models.Model):
    """
    This model is used to gather the 'OrderItems' elemnts.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipping', 'Shipping'),
        ('delivered', 'Delivered'),
        # ('cancelled', 'Cancelled'),
    ]
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES, default='pending')
    # address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    addressText = models.CharField(max_length=1000)
    city = models.CharField(max_length=100, default='Cairo')
    country = models.CharField(max_length=100, default='Egypt')
    phone_number = models.CharField(max_length=20, default="", null=True, blank=True)
    
    # total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def show_the_address(self):
        return self.addressText + ' - ' + self.city + ', ' + self.country
    

    def __str__(self) -> str:
        return f'{self.id}- {self.user} --toAddress--> {self.show_the_address()}'
