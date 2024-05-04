
To-Do-List
===
A simple ToDoList web application built using Django framework.
## Table of Contents

[TOC]

## Beginners Guide

If you are a total beginner to this, start here!

1. Clone the repository:
    ```bash
    git clone https://github.com/zaid223r/todolist.git
    ```
2. Navigate to the project directory:
    ```bash
    cd todolist
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```
The application should now be accessible at http://localhost:8000.

Usage
---

1. Register a new account or log in with existing credentials.
2. Once logged in, you can:
    * Add new tasks with due dates and descriptions.
    * Mark tasks as completed.
    * Delete existing tasks.
    * See your completed tasks.
    * Log out when finished.

Features
---
* User authentication: Users can register, log in, and log out.
* CRUD operations: Users can create, read, update, and delete tasks.
* Task management: Users can mark tasks as completed .

Project Structure
---
```bash
.
├── manage.py        # Django's command-line utility for administrative tasks
├── mainapp/           # Main application directory
│   ├── migrations/  # Database migrations
│   ├── templates/   # HTML templates
│   ├── views.py     # View functions for rendering pages
|   ├── urls.py      # URL patterns for the mainapp
|   ├── forms.py     # Forms structures for application forms
│   └── models.py    # Database models
├── README.md        # This README file
├── requirements.txt # List of Python dependencies
└── todolist/            # Django project settings and configuration
    ├── settings.py  # Django project settings
    └── urls.py      # URL patterns for the project

```
