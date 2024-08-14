from django.db import models
from user.models import User
from tag.models import Tag
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products', blank=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # is_active = models.BooleanField(default=True)
    # is_delete = models.BooleanField(default=False)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    # brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    # reviews = models.ManyToManyField('Review', blank=True)

    def __str__(self):
        return self.name




