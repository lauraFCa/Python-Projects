# Blog Web App with Django

Create a Blog Web App In Django - [**Project Based Learning**](https://github.com/practical-tutorials/project-based-learning#web-applications-1)

Installing requirements: ``pip install -r requirements.txt``

Starting the project:  
``django-admin startproject <project-name>``

Create a database:  
``python manage.py migrate``

Run the project:  
``python manage.py runserver``

> A model in Django is a special kind of object – it is saved in the database

Creating an app within the project: (keep it organized)  
``python manage.py startapp <app-name>``

Current directory:
```
BlogWebAppInDjango
├── blogwithdjango
│   ├── blog
│   │  ├── admin.py
│   │  ├── apps.py
│   │  ├── __init__.py
│   │  ├── migrations
│   │  │   └── __init__.py
│   │  ├── models.py
│   │  ├── tests.py
│   │  └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── blogwithdjango
│   │  ├── asgi.py
│   │  ├── __init__.py
│   │  ├── settings.py
│   │  ├── urls.py
│   │  └── wsgi.py
├── venv
│   └── ...
├── .gitignore
├── readme.md
└── requirements.txt
```

To update changes on models:  
``python manage.py makemigrations <app-name>``  
``python manage.py migrate blog``

Create a user:  
``python manage.py createsuperuser``

