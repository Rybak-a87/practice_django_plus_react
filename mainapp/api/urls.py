from django.urls import path

from rest_framework import routers    # аналог django.urls для viewsets

from .views import BlogCategoryViewSet, BlogPostViewSet


router = routers.SimpleRouter()
router.register("category", BlogCategoryViewSet, basename="category")    # регистрация url (аналог path)
router.register("blogpost", BlogPostViewSet, basename="blogpost")

urlpatterns = []
urlpatterns += router.urls
