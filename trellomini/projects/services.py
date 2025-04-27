# projects/services.py

from django.shortcuts import get_object_or_404
from .models import Project, Task
from django.db.models import Q

class ProjectService:
    @staticmethod
    def get_user_projects(user):
        return Project.objects.filter(Q(owner=user) | Q(tasks__assignee=user)).distinct()

    @staticmethod
    def get_project(pk):
        return get_object_or_404(Project.objects.prefetch_related("tasks"), pk=pk)

    @staticmethod
    def get_user_project(pk, user):
        return get_object_or_404(Project, pk=pk, owner=user)

    @staticmethod
    def delete_project(pk, user):
        project = ProjectService.get_user_project(pk, user)
        project.delete()

class TaskService:
    @staticmethod
    def get_task(project_pk, task_pk):
        return get_object_or_404(Task, pk=task_pk, project_id=project_pk)

    @staticmethod
    def get_user_task(task_id, user):
        return Task.objects.get(pk=task_id, project__owner=user)

    @staticmethod
    def delete_task(project_pk, task_pk, user):
        task = TaskService.get_task(project_pk, task_pk)
        project = ProjectService.get_project(project_pk)
        if project.owner != user and task.assignee != user:
            return None
        task.delete()
        return task
