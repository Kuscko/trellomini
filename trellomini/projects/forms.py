# projects/forms.py
from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'name': 'Project Name',
            'description': 'Project Description',
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assignee']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Task Description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'assignee': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
