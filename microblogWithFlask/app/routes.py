from flask import render_template, flash, redirect, url_for
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


@app.route('/login', methods=['GET', 'POST'])  # default = accept only GET requests
def login():
    """Render the login page - url = /login

    Returns:
        page: Login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        # flash = used to send a message to the user
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

