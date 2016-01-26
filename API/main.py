# coding: utf-8

from flask import Flask, request, url_for, render_template, make_response, redirect, session
import subprocess
import os

import json

from pprint import pprint

app = Flask(__name__)


@app.route("/")
def index():

    return render_template('hello.html', name=None)






@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        if 'username' and 'password' in request.form:
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))

    return '''
    <form action="" method="post">
        <p>username<input type=text name=username><br>
        password<input type=text name=password><br>
        <input type=submit value=Login></p>
    </form>
    '''




@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))





@app.route("/listes", methods=['POST', 'GET'])
def listes():
    if "username" and "password" not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':

        pprint(request.headers)

        f = open("data/test.json", 'w')

        data = json.dumps(request.json)

        f.write(data)

        return ""

    elif request.method == 'GET':

        ls = subprocess.Popen(["ls", "-L", "data"], stdout=subprocess.PIPE)

        return ls.communicate()









@app.route("/listes/<file>")
def get(file):
    if "username" and "password" not in session:
        return redirect(url_for('login'))

    with open('data/' + file + '.json') as data_file:
        data = json.load(data_file)

    return json.dumps(data)









# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

