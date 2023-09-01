from django.shortcuts import render
from rest_framework import viewsets
from .models import Biblioteca, Autor
from .serializers import BibliotecaSerializer, AutorSerializer

class BibliotecaViewset(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

class AutorViewset(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
