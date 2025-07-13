from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializers
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializers
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.object.filter(author=self.request.user)    