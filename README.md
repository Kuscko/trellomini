# 🧱 TrelloMini

TrelloMini is a lightweight, Kanban-style task and project management web application developed using Django. Created as the final project for **CEN4031 – Advanced Programming Frameworks**, this app provides a focused, minimal interface for tracking tasks within multiple projects using familiar Trello-like cards and columns.

---

## 🚀 Features

- 🧑‍💼 User authentication (login, logout, registration)
- 📁 Project creation, editing, and deletion
- 📝 Task creation, editing, and deletion within each project
- 🧩 Simple Kanban board layout per project
- 🎯 Real-time task status updates (To Do → In Progress → Done)
- 🎨 Clean Bootstrap 5-powered UI with responsive layout

---

## 🖼️ Preview

[I am not quite sure how to do this with markdown. Please jump in if you know how to.]
> A simple Kanban board interface per project.

---

# ⚙️ Installation

> **Recommended**: Use a virtual environment before running the project.

## Clone the repository
`git clone https://github.com/Kuscko/trellomini.git`

`cd trellomini`

## Activate virtual environment (optional but recommended)
`python -m venv .venv`

`source .venv/Scripts/activate  # Windows`
### OR
`source .venv/bin/activate      # macOS/Linux`

## Install required packages
`pip install -r requirements.txt`

## Run migrations
`python manage.py migrate`

## Start the development server
`python manage.py runserver`

---

# 🧪 Running Tests
`python manage.py test`

---

# 🗂️ Project Structure Overview

```
trellomini/
├── projects/         # Handles Kanban functionality (models, views, templates)
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

# 👥 Contributors
- Tyler Bischoff – [📧Team Lead, Contributor]
- Patrick Kelly – [🤘⭐ Dev, GitHub, Contributor]
- Keaton Knippel – [👑GroupMe King, Contributor]
- Clark Brown – [🥾Bootstrap Bro, Contributor]

---

# 📘 License
This project is licensed under the MIT License. See LICENSE for more details.
Developed for educational purposes as part of CEN4031 – Advanced Programming Frameworks at SPC.
