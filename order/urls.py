from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users-view', views.OrderViewSet, basename='order')
router.register(r'admin-view', views.AdminsOrdersViewSets, basename='admin-order-view')

urlpatterns = [
    # path('gathOrder/', views.create_gatherd_orders, name='gathOrder'),
    path('', include(router.urls)),
    
    # path('cart/', views.SingularProducOrdertViewSet
    #         .as_view({'get': 'list'}), name='list_cart'),

]