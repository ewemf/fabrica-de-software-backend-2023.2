from django.shortcuts import render

from rest_framework import viewsets
from .models import ToDoList, Pessoa
from .serializers import ToDoListSerializer, PessoaSerializer

class ToDoListViewset(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

class PessoaViewset(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer