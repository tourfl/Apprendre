# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
import requests






# configuration
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
HOST = '0.0.0.0'
PORT = '4000'
API_URL = '0.0.0.0:5000'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)






@app.route('/')
def index():
    return render_template('index.html')





@app.route('/lists', methods=['GET', 'POST'])
def lists():
    if request.method == 'POST':
        return "nothing to do"

    r = requests.get('http://' + API_URL + '/lists')

    return render_template('lists.html')





@app.route('/lists/<list>')
def view(list=list):
    try:
        r = requests.get('http://'+ API_URL + '/listes/' + list + '.json')
    except:
        pass
    return str(r.status_code)








@app.route('/post')
def post():
    return "nothing to do"








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
    app.run(host=HOST, port=PORT)
