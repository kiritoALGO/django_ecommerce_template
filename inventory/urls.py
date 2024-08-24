from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.InventoryViewSet, basename='inventory')

urlpatterns = router.urls