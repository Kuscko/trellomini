# trellomini/views.py
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")  # Render the home page


def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")  # Render the dashboard page


def project_confirm_delete_view(request):
    return render(request, "project_confirm_delete/project_confirm_delete.html")  # Render the project confirm/delete page


def project_form_view(request):
    return render(request, "project_form/project_form.html")  # Render the project form page


def project_view(request):
    return render(request, "project/project.html")  # Render the project page


def task_confirm_delete_view(request):
    return render(request, "task_confirm_delete/task_confirm_delete.html")  # Render the task confirm/delete page


def task_form_view(request):
    return render(request, "task_form/task_form.html")  # Render the task form page


def task_view(request):
    return render(request, "task/task.html")  # Render the task page
