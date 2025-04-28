# projects/api_views.py
from rest_framework import generics, permissions
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from .services import ProjectService, TaskService

# Project APIs
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = ProjectService

    def get_queryset(self):
        return self.service.get_user_projects(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = ProjectService

    def get_queryset(self):
        # Return only projects owned by the user
        return Project.objects.filter(owner=self.request.user)

# Task APIs
class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = TaskService

    def get_queryset(self):
        # List tasks related to user's projects
        return Task.objects.filter(project__owner=self.request.user)

    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        project = ProjectService.get_user_project(project_id, self.request.user)
        serializer.save(project=project)

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    service = TaskService

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)
