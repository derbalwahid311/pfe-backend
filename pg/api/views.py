from django.shortcuts import render
from rest_framework import generics
from main.models import Enseignant 
from .serializers import Enseignanatserializers
# Create your views here.
class EnAPIView(generics.ListAPIView):
    queryset = Enseignant.objects.all()
    serializer_class = Enseignanatserializers