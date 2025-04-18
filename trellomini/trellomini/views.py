# trellomini/views.py
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")  # Render the home page


def dashboard_view(request):
    return render(request, "/dashboard/dashboard.html")  # Render the dashboard page


def project_view(request):
    return render(request, "/projects/project.html")  # Render the project page


def create_project_view(request):
    return render(
        request, "/projects/create_project.html"
    )  # Render the create project page


def edit_project_view(request):
    return render(
        request, "/projects/edit_project.html"
    )  # Render the edit project page


def task_view(request):
    return render(request, "/tasks/task.html")  # Render the task page


def create_task_view(request):
    return render(request, "/tasks/create_task.html")  # Render the create task page


def edit_task_view(request):
    return render(request, "/tasks/edit_task.html")  # Render the create task page
