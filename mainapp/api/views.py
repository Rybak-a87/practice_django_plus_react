from rest_framework import viewsets    # viewsets содержит в себе - CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView

from .serializers import (
    BlogCategorySerializer,
    BlogPostSerializer,
    BlogPostListRetrieveSerializer,
    BlogCategoryDetailSerializer
)
from ..models import BlogCategory, BlogPost


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()    # обязательный атрибут
    serializer_class = BlogCategorySerializer    # обязательный атрибут

    action_to_serializer = {
        "retrieve": BlogCategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    action_to_serializer = {
        "list": BlogPostListRetrieveSerializer,
        "retrieve": BlogPostListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
