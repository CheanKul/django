from django.shortcuts import render
from .models import Post, User
from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
# Create your views here.


class Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Users(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
