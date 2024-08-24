from django.db import models

from size.models import Size
from product.models import Product
from user.models import User
# Create your models here.
class Inventory(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    TYPE_CHOICES = [
        ('add', 'Add'),
        ('minus', 'Minus'),
    ]

    type = models.CharField( max_length=20, choices=TYPE_CHOICES, default='add')

    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"

    def save(self, *args, **kwargs):
        # Adjust the size's quantity based on the type
        if self.type == 'minus':
            if self.size.quantity < self.quantity:
                raise ValueError("Not enough quantity in stock")
            self.size.quantity -= self.quantity
        elif self.type == 'add':
            self.size.quantity += self.quantity

        # Save the updated size quantity
        self.size.save()

        # Call the original save method to save the Inventory instance
        super().save(*args, **kwargs)

    # def decrease_quantity(self, quantity):
    #     if self.quantity - quantity < 0:
    #         raise ValueError("Not enough quantity in stock")
    #     self.quantity -= quantity
    #     self.save()
    #     self.size.quantity -= quantity
    #     self.size.save()

    # def increase_quantity(self, quantity):
    #     self.quantity += quantity
    #     self.save()
    #     if not self.size:
    #         Size.objects.create(product=self.product, size_text=self.product.default_size, quantity=quantity)
    #     else:
    #         self.size.quantity += quantity
    #     self.size.save()
    
    