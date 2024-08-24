from django.db import models


from product.models import Product
# Create your models here.

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes')
    size_text = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"<{self.product.name}> - {self.size_text} - {self.quantity} units"