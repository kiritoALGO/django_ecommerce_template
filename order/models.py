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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES, default='pending')
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f'{self.id}- {self.user.username} --toAddress--> {self.address}'
