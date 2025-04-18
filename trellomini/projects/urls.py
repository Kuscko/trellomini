# projects/urls.py
from django.urls import path
from .views import project_list, project_create, project_update, project_delete, project_detail, task_create, task_update, task_delete, task_detail, change_task_status

urlpatterns = [
    # Project URLs
    path('', project_list, name='project_list'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/edit/', project_update, name='project_update'),
    path('<int:pk>/delete/', project_delete, name='project_delete'),
    # Task URLs
    path('<int:project_pk>/tasks/create/', task_create, name='task_create'),
    path('<int:project_pk>/tasks/<int:task_pk>/edit/', task_update, name='task_update'),
    path('<int:project_pk>/tasks/<int:task_pk>/delete/', task_delete, name='task_delete'),
    path('<int:project_pk>/tasks/<int:task_pk>/', task_detail, name='task_detail'),
    # Change Task Status URL
    path('<int:project_pk>/tasks/<int:pk>/status/<str:new_status>/', change_task_status, name='change_task_status'),

    # path('<int:project_pk>/tasks/<int:task_pk>/detail/', task_detail, name='task_detail'), # Optional detail view for tasks
]
