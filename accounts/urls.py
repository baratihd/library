from django.urls import path

from .views import UserRegisterCreateView


app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    # path('login/', , name='login'),
]
