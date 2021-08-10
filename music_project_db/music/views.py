from django.shortcuts import render
from .models import Song
from rest_framework import viewsets
from .serializers import SongSerializer
from music_project_db.music import serializers


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
 