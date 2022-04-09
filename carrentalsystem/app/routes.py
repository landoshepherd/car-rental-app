from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mr. Shepherd'}
    posts = [
        {
            'author': {'username': 'Lando'},
            'body': 'Beautiful day in Virginia'
        },
        {
            'author': {'username': 'Butkus'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/rent')
def rent():
    return render_template('rent.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/account')
def account():
    return render_template('account.html')