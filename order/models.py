from django.db import models


from user.models import User
from product.models import Product
from gath_order.models import GatheredOrders
# Create your models here.

class SingularProductOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    gathered_orders = models.ForeignKey(GatheredOrders, on_delete=models.CASCADE, blank=True, null=True)


# class GatheredOrders(models.Model):
#     """
#     This model is used to gather the 'Singular Prodct Order' elemnts.
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     # total_price = models.DecimalField(max_digits=10, decimal_places=2)
