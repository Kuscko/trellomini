# projects/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

# Project Views

@login_required
def project_list(request):
    """
    View to list all projects.\n
    Users can see projects they own and projects they are assigned to.
    """
    projects = Project.objects.filter(Q(owner=request.user) | Q(tasks__assignee=request.user)).distinct()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    """View to display project details."""
    project = get_object_or_404(Project.objects.prefetch_related("tasks"), pk=pk)

    if request.user != project.owner and not project.tasks.filter(assignee=request.user).exists():
        return HttpResponseForbidden("You do not have permission to view this project.")

    return render(request, 'projects/project_detail.html', {'project': project})

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
    return render(request, 'projects/project_form.html', {'form': form})

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
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    """View to delete a project."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

# Task Views

@login_required
def task_create(request, project_pk):
    """View to create a new task."""
    project = get_object_or_404(Project, pk=project_pk)

    # Check if the user is the owner of the project or assigned to it
    # This check is necessary to prevent unauthorized users from creating tasks in the project.
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

    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

@login_required
def task_update(request, project_pk, task_pk):
    """View to update an existing task."""
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)

    # Check if the user is the owner of the project or assigned to the task
    if request.user != project.owner and task.assignee != request.user:
        return HttpResponseForbidden("You do not have permission to update this task.")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task)

    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

@login_required
def task_delete(request, project_pk, task_pk):
    """View to delete a task."""
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)

    # Check if the user is the owner of the project or assigned to the task
    if request.user != project.owner and task.assignee != request.user:
        return HttpResponseForbidden("You do not have permission to delete this task.")

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project.pk)

    return render(request, 'projects/task_confirm_delete.html', {'task': task, 'project': project})

@login_required
def task_detail(request, project_pk, task_pk):
    """View to display task details."""
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk, project=project)

    # Check if the user is the owner of the project or assigned to the task
    if request.user != project.owner and task.assignee != request.user:
        return HttpResponseForbidden("You do not have permission to view this task.")

    return render(request, 'projects/task_detail.html', {'task': task, 'project': project})