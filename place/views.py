from django.shortcuts import render
from place.models import Place
from place.serializers import PlaceSerializer
from rest_framework import generics


class PlaceListCreate(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# Create your views here.
