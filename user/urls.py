from django.urls import path
from .views import login, SignupView, test_token


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login, name='login'),
    path('user/', test_token, name='getuserinfo'),
]
