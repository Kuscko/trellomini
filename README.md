[![Deploy Django](https://github.com/Kuscko/trellomini/actions/workflows/django-build.yml/badge.svg)](https://github.com/Kuscko/trellomini/actions/workflows/django-build.yml)

# 🧱 TrelloMini

TrelloMini is a lightweight, Kanban-style task and project management web application developed using Django.

Built as the final project for **CEN4031 – Advanced Programming Frameworks**, it provides a focused, minimal interface for managing tasks within multiple projects using familiar Trello-like cards and columns.

---

## 🚀 Features

- 🧑‍💼 User authentication (login, logout)
- 📁 Project creation, editing, and deletion
- 📝 Task creation, editing, and deletion within projects
- 🧩 Simple Kanban board layout per project
- 🎯 Real-time task status updates (To Do → Doing → Done)
- 🎨 Clean Bootstrap 5-powered responsive UI
- 🔥 Dependency Injection for maintainability
- 🧪 Full unit and integration tests
- 🌐 REST API exposed via Django Rest Framework (DRF)

---

## 🛠 Tech Stack
- Backend: Django 5.1+
- Frontend: Bootstrap 5
- Database: SQLite (local dev)
- API: Django Rest Framework (DRF)
- Testing: pytest + DRF APIClient

---

## ⚙️ Installation

> **Recommended**: Use a virtual environment before running the project.

### Clone the repository
```
git clone https://github.com/Kuscko/trellomini.git
cd trellomini
```

### Set up virtual environment (recommended)
```
python -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # macOS/Linux
```

### Install dependencies
```
pip install -r requirements.txt
```

### Set up the database
```
python manage.py migrate
```

### Create a superuser
```
python manage.py createsuperuser
```

### Run the development server
```
python manage.py runserver
```

---

## 🐳 Docker Deployment
Build and run the container locally:
```
docker build -t trellomini .
docker run -p 8000:8000 trellomini
```
Or pull the latest image from DockerHub:
```
docker pull kusck0/trellomini:latest
docker run --env-file .env -p 8000:8000 kusck0/trellomini:latest
```
Or run it manually:
```
docker pull kusck0/trellomini:latest
docker run \
  -e SECRET_KEY=your-real-secret-key \
  -e EMAIL_HOST_PASSWORD=your-real-smtp-password \
  -e EMAIL_HOST_USER=smtp@mailtrap.io \
  -e EMAIL_HOST=live.smtp.mailtrap.io \
  -e EMAIL_PORT=587 \
  -e EMAIL_USE_TLS=True \
  -e DEBUG=False \
  -p 8000:8000 \
  kusck0/trellomini:latest
```

---

## 📁 Environment Requirements

We suggest creating an account on [mailtrap](https://mailtrap.io) for enabling SMPT capabilities for 1000 free emails a month.

---

## 🔧 Environment Variables
TrelloMini uses a .env file to manage sensitive settings. Example:

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=live.smtp.mailtrap.io
EMAIL_HOST_USER=smtp@mailtrap.io
EMAIL_HOST_PASSWORD=your-password
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=TrelloMini <hello@demomailtrap.co>
EMAIL_SUBJECT_PREFIX=[TrelloMini]
SECRET_KEY=your-django-secret-key
DEBUG=False
```

---

## 🛠️ Post-Deployment Setup
After running the container:

Create database tables:

```
docker exec -it your-container-name python manage.py migrate
```

Create a superuser (admin account):
```
docker exec -it your-container-name python manage.py createsuperuser
```

✅ Now the application is fully functional.

---

## 🔐 Admin Access

- Visit http://localhost:8000/admin
- Log in with your superuser credentials

---

## 🗂️ Project Structure Overview

```
trellomini/
├── projects/         # Handles Kanban functionality (models, views, templates, api)
├── users/            # Handles authentication (sign up, login, logout)
├── trellomini/       # Core Django settings and routing
├── templates/        # HTML templates for dashboard and forms
├── static/           # Static files (CSS, JS, images)
├── db.sqlite3        # Local development database
├── requirements.txt  # Python dependencies
├── manage.py         # Django management utility
└── README.md         # This file
```

---

## 🖼️ Preview

[I am not quite sure how to do this with markdown. Please jump in if you know how to.]
> A simple Kanban board interface per project.

## 🧪 Running Tests
Run all tests:

```
pytest --ds=trellomini.settings
```

Generate a coverage report:

```
pytest --ds=trellomini.settings --cov=projects --cov-report=term-missing
```

Tests cover:

- Project and Task creation
- Task status updates
- Permissions (ownership, assignment)
- REST API endpoints (CRUD for projects and tasks)

---

## 🌐 REST API Endpoints
- `GET /api/projects/ — List your projects`
- `POST /api/projects/ — Create a new project`
- `GET /api/projects/<pk>/ — Retrieve a project`
- `PUT/PATCH /api/projects/<pk>/ — Update a project`
- `DELETE /api/projects/<pk>/ — Delete a project`
- `GET /api/tasks/ — List tasks`
- `POST /api/tasks/ — Create a new task`
- `GET /api/tasks/<pk>/ — Retrieve a task`
- `PUT/PATCH /api/tasks/<pk>/ — Update a task`
- `DELETE /api/tasks/<pk>/ — Delete a task`
**Authentication: Required (via Django session login)**

---

## 🏆 Bonus Enhancements Completed
- 🧩 Dependency Injection used across views and APIs (+5 pts)
- 🧪 Unit and API tests fully written and passing (+5 pts)
- 🌐 REST API exposed using Django Rest Framework (+5 pts)

---

## 👥 Contributors
- Tyler Bischoff – [📧Team Lead, Contributor]
- Patrick Kelly – [🤘⭐ Lead Developer, Contributor]
- Keaton Knippel – [👑 GroupMe King, Contributor]
- Clark Brown – [🥾 Bootstrap Bro, Contributor]

---

## 📘 License
This project is licensed under the MIT License. See LICENSE for more details.

Developed for educational purposes as part of **CEN4031 – Advanced Programming Frameworks at SPC**.
