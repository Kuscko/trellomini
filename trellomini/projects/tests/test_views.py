# projects/tests/test_views.py
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from projects.models import Project, Task
from django.test import Client

User = get_user_model()

@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.project = Project.objects.create(title="Test Project", owner=self.user)
        self.task = Task.objects.create(title="Test Task", project=self.project)

    def test_project_list_view(self):
        url = reverse('project_list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_project_detail_view(self):
        url = reverse('project_detail', args=[self.project.pk])
        response = self.client.get(url)
        assert response.status_code == 200

    def test_project_create_view(self):
        url = reverse('project_create')
        data = {"title": "New Project", "description": "desc"}
        response = self.client.post(url, data)
        assert response.status_code == 302
        assert Project.objects.filter(title="New Project").exists()

    def test_project_update_view(self):
        url = reverse('project_update', args=[self.project.pk])
        data = {"title": "Updated Title", "description": "desc"}
        response = self.client.post(url, data)
        assert response.status_code == 302
        self.project.refresh_from_db()
        assert self.project.title == "Updated Title"

    def test_project_delete_view(self):
        url = reverse('project_delete', args=[self.project.pk])
        response = self.client.post(url)
        assert response.status_code == 302
        assert Project.objects.count() == 0

    def test_task_create_view(self):
        url = reverse('task_create', args=[self.project.pk])
        data = {"title": "New Task", "status": "TODO"}
        response = self.client.post(url, data)
        assert response.status_code == 302
        assert Task.objects.filter(title="New Task").exists()

    def test_task_update_view(self):
        url = reverse('task_update', args=[self.project.pk, self.task.pk])
        data = {"title": "Updated Task", "status": "DOING"}
        response = self.client.post(url, data)
        assert response.status_code == 302
        self.task.refresh_from_db()
        assert self.task.title == "Updated Task"

    def test_task_delete_view(self):
        url = reverse('task_delete', args=[self.project.pk, self.task.pk])
        response = self.client.post(url)
        assert response.status_code == 302
        assert Task.objects.count() == 0

    def test_task_detail_view(self):
        url = reverse('task_detail', args=[self.project.pk, self.task.pk])
        response = self.client.get(url)
        assert response.status_code == 200

    def test_update_task_status_api(self):
        url = reverse('update_task_status', args=[self.task.pk])
        response = self.client.post(url, data={"status": "DONE"}, content_type="application/json")
        assert response.status_code == 200
        self.task.refresh_from_db()
        assert self.task.status == "DONE"

    def test_unauthorized_project_access_redirects(self):
        other_user = User.objects.create_user(username='otheruser', password='password')
        project = Project.objects.create(title="Other Project", owner=other_user)
        url = reverse('project_detail', args=[project.pk])
        response = self.client.get(url)
        assert response.status_code == 302

    def test_project_create_view_invalid(self):
        url = reverse('project_create')
        response = self.client.post(url, data={})
        assert response.status_code == 200
        assert not Project.objects.filter(description="desc").exists()

    def test_project_delete_view_get(self):
        url = reverse('project_delete', args=[self.project.pk])
        response = self.client.get(url)
        assert response.status_code == 200 


