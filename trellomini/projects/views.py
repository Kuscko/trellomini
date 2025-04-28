# projects/views.py
from django.shortcuts import render, redirect
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from django.contrib import messages
from .services import ProjectService, TaskService
from models import Task

# Project Views
@login_required
def project_list(request, service=ProjectService):
    projects = service.get_user_projects(request.user)
    return render(request, 'dashboard/dashboard.html', {'projects': projects})

@login_required
def project_detail(request, pk, service=ProjectService):
    project = service.get_project(pk)
    statuses = project.tasks.model.STATUS_CHOICES

    if request.user != project.owner and not project.tasks.filter(assignee=request.user).exists():
        messages.error(request, "You do not have permission to view this project.")
        return redirect('project_list')

    return render(request, 'project/project.html', {'project': project, 'statuses': statuses})

@login_required
def project_create(request, service=ProjectService):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, "Project created successfully.")
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form/project_form.html', {'form': form})

@login_required
def project_update(request, pk, service=ProjectService):
    project = service.get_user_project(pk, request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully.")
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form/project_form.html', {'form': form})

@login_required
def project_delete(request, pk, service=ProjectService):
    if request.method == 'POST':
        service.delete_project(pk, request.user)
        messages.success(request, "Project deleted successfully.")
        return redirect('project_list')
    project = service.get_user_project(pk, request.user)
    return render(request, 'project_confirm_delete/project_confirm_delete.html', {'project': project})

# Task Views
@login_required
def task_create(request, project_pk, project_service=ProjectService):
    project = project_service.get_project(project_pk)

    if request.user != project.owner and not project.tasks.filter(assignee=request.user).exists():
        messages.error(request, "You do not have permission to create tasks in this project.")
        return redirect('project_detail', pk=project.pk)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            messages.success(request, "Task created successfully.")
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()
    return render(request, 'task_form/task_form.html', {'form': form, 'project': project})

@login_required
def task_update(request, project_pk, task_pk, project_service=ProjectService, task_service=TaskService):
    project = project_service.get_project(project_pk)
    task = task_service.get_task(project_pk, task_pk)

    if request.user != project.owner and task.assignee != request.user:
        messages.error(request, "You do not have permission to update this task.")
        return redirect('project_detail', pk=project.pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form/task_form.html', {'form': form, 'project': project})

@login_required
def task_delete(request, project_pk, task_pk, project_service=ProjectService, task_service=TaskService):
    if request.method == 'POST':
        deleted_task = task_service.delete_task(project_pk, task_pk, request.user)
        if not deleted_task:
            messages.error(request, "You do not have permission to delete this task.")
            return redirect('project_detail', pk=project_pk)
        messages.success(request, "Task deleted successfully.")
        return redirect('project_detail', pk=project_pk)

    project = project_service.get_project(project_pk)
    task = task_service.get_task(project_pk, task_pk)

    return render(request, 'task_confirm_delete/task_confirm_delete.html', {'task': task, 'project': project})

@login_required
def task_detail(request, project_pk, task_pk, project_service=ProjectService, task_service=TaskService):
    project = project_service.get_project(project_pk)
    task = task_service.get_task(project_pk, task_pk)

    if request.user != project.owner and task.assignee != request.user:
        messages.error(request, "You do not have permission to view this task.")
        return redirect('project_detail', pk=project.pk)

    return render(request, 'task/task.html', {'task': task, 'project': project})

@login_required
@require_POST
def update_task_status(request, task_id, task_service=TaskService):
    try:
        task = task_service.get_user_task(task_id, request.user)
        data = json.loads(request.body)
        task.status = data.get("status", task.status)
        task.save()
        return JsonResponse({"success": True, "status": task.status})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)
