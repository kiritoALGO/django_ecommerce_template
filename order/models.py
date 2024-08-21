from django.db import models


from address.models import Address
from user.models import User
# Create your models here.

class Order(models.Model):
    """
    This model is used to gather the 'OrderItems' elemnts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    # Address = models.ForeignKey(Address)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
