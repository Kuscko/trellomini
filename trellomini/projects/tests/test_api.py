import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from projects.models import Project, Task

User = get_user_model()

@pytest.mark.django_db
class TestProjectTaskAPI:

    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)  # Authenticate automatically
        self.project = Project.objects.create(title="Test Project", owner=self.user)
        self.task = Task.objects.create(title="Test Task", project=self.project)

    def test_list_projects_api(self):
        url = reverse('api_project_list_create')
        response = self.client.get(url)
        assert response.status_code == 200
        assert any(proj['title'] == "Test Project" for proj in response.json())

    def test_create_project_api(self):
        url = reverse('api_project_list_create')
        data = {"title": "API Created Project", "description": "Created via API"}
        response = self.client.post(url, data)
        assert response.status_code == 201
        assert Project.objects.filter(title="API Created Project").exists()

    def test_retrieve_project_api(self):
        url = reverse('api_project_detail', args=[self.project.pk])
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.json()['title'] == "Test Project"

    def test_update_project_api(self):
        url = reverse('api_project_detail', args=[self.project.pk])
        data = {"title": "Updated Project Title", "description": "Updated"}
        response = self.client.put(url, data)
        assert response.status_code == 200
        self.project.refresh_from_db()
        assert self.project.title == "Updated Project Title"

    def test_delete_project_api(self):
        url = reverse('api_project_detail', args=[self.project.pk])
        response = self.client.delete(url)
        assert response.status_code == 204
        assert not Project.objects.filter(pk=self.project.pk).exists()

    def test_list_tasks_api(self):
        url = reverse('api_task_list_create')
        response = self.client.get(url)
        assert response.status_code == 200
        assert any(task['title'] == "Test Task" for task in response.json())

    def test_create_task_api(self):
        url = reverse('api_task_list_create')
        data = {"title": "API Created Task", "status": "TODO", "project": self.project.pk}
        response = self.client.post(url, data)
        assert response.status_code == 201
        assert Task.objects.filter(title="API Created Task").exists()

    def test_retrieve_task_api(self):
        url = reverse('api_task_detail', args=[self.task.pk])
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.json()['title'] == "Test Task"

    def test_update_task_api(self):
        url = reverse('api_task_detail', args=[self.task.pk])
        data = {"title": "Updated Task Title", "status": "DOING", "project": self.project.pk}
        response = self.client.put(url, data)
        assert response.status_code == 200
        self.task.refresh_from_db()
        assert self.task.title == "Updated Task Title"

    def test_delete_task_api(self):
        url = reverse('api_task_detail', args=[self.task.pk])
        response = self.client.delete(url)
        assert response.status_code == 204
        assert not Task.objects.filter(pk=self.task.pk).exists()
