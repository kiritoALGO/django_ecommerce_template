from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'', views.SizeViewSet, basename='Size')

urlpatterns = router.urls