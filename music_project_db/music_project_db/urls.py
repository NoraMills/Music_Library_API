from django.contrib import admin
from django.urls import path, include
from rest_framework import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('music.urls')),
]
