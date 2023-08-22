from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer

from rest_framework import viewsets


User = get_user_model()

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer