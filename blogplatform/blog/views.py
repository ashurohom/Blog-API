from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializers
from rest_framework import filters  
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializers
    permission_classes=[permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)    