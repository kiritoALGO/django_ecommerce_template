from django.urls import path
from .views import login, SignupView\
, test_view


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', login, name='login'),
    path('test/', test_view, name='test-view'),
]
