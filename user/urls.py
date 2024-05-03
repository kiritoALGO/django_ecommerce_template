from django.urls import path
from .views import login, SignupView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login, name='login'),
]
