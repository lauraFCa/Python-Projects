from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """Render the website main page

    Returns:
        page: Main page - url = /index or default (/)
    """
    user = {'username': 'Lulala'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='TituloDaPage', user = user, posts=posts)


@app.route('/login')
def login():
    """Render the login page - url = /login

    Returns:
        page: Login page
    """
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

