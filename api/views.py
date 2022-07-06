from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Task
from api.serializers import UserSerialzer, TaskSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TaskSerializer
