from django.contrib.auth.mixins import LoginRequiredMixin
from place.models import Place
from place.serializers import PlaceSerializer
from rest_framework import generics


class PlaceListCreate(LoginRequiredMixin, generics.ListCreateAPIView):
    login_url = '/admin/login/'
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# Create your views here.
