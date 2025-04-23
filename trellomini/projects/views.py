# projects/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.http import JsonResponse
import json

# Create your views here.
@login_required
def project_list(request):
    """
    View to list all projects.\n
    Users can see projects they own and projects they are assigned to.
    """
    projects = Project.objects.filter(Q(owner=request.user) | Q(tasks__assignee=request.user)).distinct()
    return render(request, 'dashboard/dashboard.html', {'projects': projects})

def project_detail(request, pk):
    """View to display project details."""
    project = get_object_or_404(Project.objects.prefetch_related("tasks"), pk=pk)
    statuses = Task.STATUS_CHOICES

    if request.user != project.owner and not project.tasks.filter(assignee=request.user).exists():
        return HttpResponseForbidden("You do not have permission to view this project.")

    return render(request, 'project/project.html', {'project': project, 'statuses': statuses})

@login_required
def project_create(request):
    """View to create a new project."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form/project_form.html', {'form': form})

@login_required
def project_update(request, pk):
    """View to update an existing project."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    """View to delete a project."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'project_confirm_delete/project_confirm_delete.html', {'project': project})

# Task Views
@login_required
def task_create(request, project_pk):
    """View to create a new task."""
    project = get_object_or_404(Project, pk=project_pk)

    if request.user != project.owner and not project.tasks.filter(assignee=request.user).exists():
        return HttpResponseForbidden("You do not have permission to create tasks in this project.")

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()

    return render(request, 'task_form/task_form.html', {'form': form, 'project': project})

@login_required
def task_update(request, project_pk, task_pk):
    """View to update an existing task."""
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)

    if request.user != project.owner and task.assignee != request.user:
        return HttpResponseForbidden("You do not have permission to update this task.")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form/task_form.html', {'form': form, 'project': project})

@login_required
def task_delete(request, project_pk, task_pk):
    """View to delete a task."""
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)

    if request.user != project.owner and task.assignee != request.user:
        return HttpResponseForbidden("You do not have permission to delete this task.")

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project.pk)

    return render(request, 'task_confirm_delete/task_confirm_delete.html', {'task': task, 'project': project})

@login_required
def task_detail(request, project_pk, task_pk):
    """View to display task details."""
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)

    if request.user != project.owner and task.assignee != request.user:
        return HttpResponseForbidden("You do not have permission to view this task.")

    return render(request, 'task/task.html', {'task': task, 'project': project})

@login_required
@require_POST
def update_task_status(request, task_id):
    """Change the status of a task."""
    if request.method == "POST":
        try:
            task = Task.objects.get(pk=task_id, project__owner=request.user)
            data = json.loads(request.body)
            task.status = data.get("status", task.status)
            task.save()
            return JsonResponse({"success": True, "status": task.status})
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)
    return JsonResponse({"error": "Invalid method"}, status=405)