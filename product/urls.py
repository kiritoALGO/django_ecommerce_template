from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'', views.ProductsViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/add-sizes/', views.AddSizesToProductView.as_view(), name='add-sizes-to-product'),
]
