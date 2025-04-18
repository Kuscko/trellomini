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

from .views import home_view

urlpatterns = [
    # Default Pages
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    # Authentication Pages
    path(
        "accounts/", include("users.urls"), name="accounts"
    ),  # Include the custom authentication urls, put fisrst to avoid conflict with the default authentication urls
    path(
        "accounts/", include("django.contrib.auth.urls"), name="accounts"
    ),  # Include the authentication urls
]
