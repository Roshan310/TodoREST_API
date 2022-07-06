from csv import field_size_limit
from rest_framework import serializers
from .models import User, Task

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'user')