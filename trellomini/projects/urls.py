# projects/urls.py
from django.urls import path
from .views import project_list, project_create, project_update, project_delete, project_detail, task_create, task_update, task_delete, task_detail, update_task_status
from .api_views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView, TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

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
    path("tasks/<int:task_id>/update-status/", update_task_status, name="update_task_status"),

    # API routes
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='api_project_list_create'),
    path('api/projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='api_project_detail'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='api_task_list_create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='api_task_detail'),
]
