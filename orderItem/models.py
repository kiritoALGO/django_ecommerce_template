from django.db import models


from size.models import Size
from user.models import User
from product.models import Product
from order.models import Order
# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='order_items')
    totalOrderItemsPrice = models.IntegerField(null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.quantity == 1:
            return f"{self.quantity} piece of {self.product.name}"
        return f"{self.quantity} pieces of {self.product.name}"
    
    def save(self, *args, **kwargs):
        self.totalOrderItemsPrice = self.quantity * self.product.price
        super(OrderItem, self).save(*args, **kwargs)

# class GatheredOrders(models.Model):
#     """
#     This model is used to gather the 'Singular Prodct Order' elemnts.
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     # total_price = models.DecimalField(max_digits=10, decimal_places=2)
