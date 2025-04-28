# projects/serializers.py
from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'owner']

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    assignee = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'project', 'assignee', 'created_at', 'updated_at']
