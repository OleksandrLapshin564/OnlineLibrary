# OnlineLibrary/apps/users/urls_api.py
from django.urls import path
from .views_api import UserRegisterAPI, CustomAuthToken

urlpatterns = [
    path('register/', UserRegisterAPI.as_view(), name='api_register'),
    path('login/', CustomAuthToken.as_view(), name='api_login'),
]
