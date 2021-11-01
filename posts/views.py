from django.shortcuts import render
from rest_framework import generics
from .models import Post
# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
