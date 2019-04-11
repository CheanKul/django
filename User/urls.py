
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import (
    UserCreateAPIView,
    UserLoginAPIView
)


urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]
