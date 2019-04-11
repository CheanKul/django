from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
# Create your views here.


class Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
