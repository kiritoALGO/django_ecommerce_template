from django.contrib import admin
from .models import SingularProductOrder
from .models import GatheredOrders, SingularProductOrder
# Register your models here.
admin.site.register(SingularProductOrder)
admin.site.register(GatheredOrders)