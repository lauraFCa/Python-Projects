# Microblog with Flask

``pip install flask``

To define the main application, set the app as an env variable:  
```
CMD => set FLASK_APP=main.py
PoweShell => Set-Item -Path Env:\FLASK_APP -Value 'main.py'
```

Running the flask app:  
``flask run``

To set environment variables automatically import:  
1. ``pip install python-dotenv``
2. Create file *.flaskenv* on top directory:  
   > FLASK_APP=main.py

To handle forms, install *flask-wtf*:
``pip install flask-wtf``

## Secret Key in Flask

Flask and some of its extensions use the value of the secret key as a cryptographic key, useful to generate signatures or tokens.  
The Flask-WTF extension uses it to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF (pronounced "seasurf").

