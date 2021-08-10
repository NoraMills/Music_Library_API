from django.urls import path, include
from . import views
 #allows get and post requests
from rest_framework import routers


router = routers.DefaultRouter()
router.register('music', views.SongView)

urlpatterns = [
    path('', include(router.urls)),
]