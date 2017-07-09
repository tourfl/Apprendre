# all the imports
from flask import Flask, request, redirect, url_for, render_template, flash
import requests
import json

# local imports
from path import mylen


# configuration
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
HOST = '0.0.0.0'
PORT = 4000
API_URL = '127.0.0.1:5000'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/learn/', methods=['GET', 'POST'])
def lists():
    if request.method == 'POST':
        return "nothing to do"

    data = requests.get('http://' + API_URL + '/categories/', params={'show': 'more'}).json()

    data.sort(key=mylen, reverse=True)

    return render_template('lists.html', data=data)


@app.route('/view/<lessonId>')
def view(lessonId):
    data = requests.get('http://' + API_URL + '/lessons/' + lessonId).json()

    return render_template('view.html', data=data)


@app.route('/learn/<lessonId>')
def learn(lessonId):
    try:
        data = requests.get('http://' + API_URL + '/lessons/' + lessonId).json()
    except:
        pass

    return render_template('learn.html', data=data, dumps=json.dumps)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
