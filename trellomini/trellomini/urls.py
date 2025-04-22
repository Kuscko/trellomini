"""
URL configuration for trellomini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# trellomini/urls.py
from django.contrib import admin
from django.urls import include, path

from .views import (
    dashboard_view,
    home_view,
    project_confirm_delete_view,
    project_form_view,
    project_view,
    task_confirm_delete_view,
    task_form_view,
    task_view,
)

urlpatterns = [
    # Default Pages
    path("", home_view, name="home"),
    path("dashboard/", dashboard_view, name="dashboard"),  # Include the dashboard urls
    
    # Projects Pages
    path("project_confirm_delete/", project_confirm_delete_view, name="project_confirm_delete"),  # Include the dashboard urls
    path("project_form/", project_form_view, name="project_form"),  # Include the dashboard urls
    path("project/", project_view, name="project"),  # Include the dashboard urls
    
    # Task Pages
    path("task_confirm_delete/", task_confirm_delete_view, name="task_confirm_delete"),  # Include the dashboard urls
    path("task_form/", task_form_view, name="task_form"),  # Include the dashboard urls
    path("task/", task_view, name="task"),  # Include the dashboard urls
    path("admin/", admin.site.urls),
    
    # Authentication Pages
    path("accounts/", include("users.urls"), name="accounts"),  # Include the custom authentication urls, put fisrst to avoid conflict with the default authentication urls
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),  # Include the authentication urls
]
