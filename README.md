# 📝 Django To-Do App

A simple To-Do List web application built with Django and Bootstrap.

## Features
- Add tasks
- Mark tasks as complete
- Delete tasks
- Admin panel to manage tasks

## How to run
```bash
git clone https://github.com/<your-username>/django-todo-app.git
cd django-todo-app
python -m venv env
source env/bin/activate   # (on Windows: env\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
