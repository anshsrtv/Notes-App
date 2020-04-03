from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer


class BlogView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Blog.objects.all().order_by('created_at')
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)