# all the imports
from flask import Flask, request, redirect, url_for, render_template, flash, session
import requests
import json

# local imports
from op import get_sorted_list, get_dic


# configuration
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
HOST = '0.0.0.0'
API_URL = '0.0.0.0:4000'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lists', methods=['GET', 'POST'])
def lists():
    error = None
    if request.method == 'POST':
        return "nothing to do"

    r = requests.get('http://' + API_URL + '/l')
    list = get_sorted_list(r.json())
    return render_template('lists.html', list=list)


@app.route('/l/<dir>/<file>')
def l_dir_file():
    return url_for(view_list)


@app.route('/view/<dir>/<file>')
def view(dir, file):
    hd = []
    voc = []
    r = requests.get('http://' + API_URL + '/l/' + dir + '/' + file + '.json')
    dic = r.json()
    if "vocabulary" in dic:
        voc = dic["vocabulary"]
        voc = get_dic(voc)

    if "header" in dic:
        hd = dic["header"]
    return render_template('view.html', dir=dir, file=file, voc=voc, header=hd)


@app.route('/learn/<dir>/<file>')
def learn(dir, file):
    return "nothing to do, sorry!"


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
    app.run(host=HOST)
