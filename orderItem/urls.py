from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register(r'', views.orderActoinsViewSet, basename='order-actions')
# router.register(r'items', views.orderItemViewSet, basename='orderItem')
router.register(r'', views.orderItemViewSet, basename='orderItem')

urlpatterns = [
    # path('gathOrder/', views.create_gatherd_orders, name='gathOrder'),
    path('', include(router.urls)),
    
    # path('cart/', views.orderItemViewSet.view_cart_items, name='list_cart'),
    

]