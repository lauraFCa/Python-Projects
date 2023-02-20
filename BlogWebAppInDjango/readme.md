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

## Connection to Databases / Reading Models (objects)

### QuerySet

Commands that allow you to read the data from the database, filter it and order it.

Activating Django shell:  
``python manage.py shell``

**List** all objects from a model (in Django shell): 
```
# this will list all blog posts titles I made previously

>>> from blog.models import Post
>>> Post.objects.all()

# output: <QuerySet [<Post: Fist Django Application>, <Post: A second post to understand Dates>, <Post: Mandatory fields and Creation date>]>
```

**Create** a new object:
```
# List users to use on blog post:
>>> from django.contrib.auth.models import User
>>> Users.objects.All()
# output: <QuerySet [<User: laura>]>

# Create an object (post) with that user
>>> me = User.objects.get(username='laura')
>>> Post.objects.create(author=me, title='Sample title', text='Test')
```

**Filter** objects: 
```
>>> Post.objects.filter(author=me)
>>> Post.objects.filter(title__contains='title')

>>> from django.utils import timezone
>>> Post.objects.filter(published_date__lte=timezone.now())
```

**Publish** a post:
```
>>> post = Post.objects.get(title="Sample title")
>>> post.publish()
```

**Order** objects: 
```
>>> Post.objects.order_by('created_date')
# reverse order:
>>> Post.objects.order_by('-created_date')
```

Mixing query commands: 
``` 
>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
```

### Django Templates

Django template tags allow us to transfer Python-like things into HTML, so you can build dynamic websites faster

Code inside *html* file, to render Python code - the *|linebreaksbr* is piping the posts' text through a filter to convert line-breaks into paragraphs.
```
{% extends 'blog/base.html' %}  # used to extend from a base template

<div class="posts">
   {% for post in posts %}
      <article>
         <time>Published: {{ post.published_date }}</time>
         <h2><a href="">{{ post.title }}</a></h2>
         <p>{{ post.text|linebreaksbr }}</p>
      </article>  
   {% endfor %}
</div>
```

## PythonAnywhere

Creatung a page (after set up free account): 
1. Create API token
2. Use  
   ``new bash console``
3. Define user  
   ``pip3.8 install --user pythonanywhere``
4. Upload files from GitHub  
   ``pa_autoconfigure_django.py --python=3.8 https://github.com/<your-github-username>/my-first-blog.git``
5. Move to correct directory (*cd dir*)  
   ``python manage.py createsuperuser``


To update page with it:
1. ``git pull``
2. [Reload page](https://www.pythonanywhere.com/web_app_setup/)

