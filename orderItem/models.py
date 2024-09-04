from django.db import models


from size.models import Size
from user.models import User
from product.models import Product
from order.models import Order
from inventory.models import Inventory
# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='order_items')
    totalOrderItemsPrice = models.IntegerField(null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.quantity == 1:
            return f"{self.quantity} piece of {self.product.name}"
        return f"{self.quantity} pieces of {self.product.name}"

    def set_order(self, order):
        # Create an inventory record
        description = f'user -id:{self.user.id if self.user else None}_{self.user}- moved {self.quantity} pieces of {self.product.name} to order -id:{order.id}'

        Inventory.objects.create(
            user=self.user,
            product=self.product,
            size=self.size,
            quantity=self.quantity,
            type='minus',  # Adjust this if needed
            description=description
        )
        # Set the order
        self.order = order
        self.save()


    def save(self, *args, **kwargs):
        self.totalOrderItemsPrice = self.quantity * self.product.price
        super(OrderItem, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        inventory = Inventory.objects.create(
            user=self.user,
            product=self.product,
            size=self.size,
            quantity=self.quantity,
            type='minus',
            description=f'user -id:{self.user.id}_{self.user}- deleted {self.quantity} pieces of {self.product.name} -{self.size.size_text}-'
        )

        super(OrderItem, self).delete(*args, **kwargs)
# class GatheredOrders(models.Model):
#     """
#     This model is used to gather the 'Singular Prodct Order' elemnts.
#     """
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#     # total_price = models.DecimalField(max_digits=10, decimal_places=2)
