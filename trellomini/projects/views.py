# projects/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def project_list(request):
    """
    View to list all projects.\n
    Users can see projects they own and projects they are assigned to.
    """
    projects = Project.objects.filter(Q(owner=request.user) | Q(tasks__assignee=request.user)).distinct()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    """View to display project details."""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

# @login_required
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

# @login_required
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

# @login_required
def project_delete(request, pk):
    """View to delete a project."""
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})