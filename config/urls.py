from django.contrib import admin
from django.urls import path, include

from mainapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("category/<int:id>/", views.category_detail),
    path("posts/<int:id>/", views.post_detail),
    path("api/", include("mainapp.api.urls")),
]
