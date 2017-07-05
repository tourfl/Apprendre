# coding: utf-8

from flask import Flask, request, url_for, render_template, make_response, redirect, session
import datetime
import os # random number

from glob import glob

import json

from pprint import pprint



# configuration
DEBUG = False
SECRET_KEY = 'development key'
HOST='0.0.0.0'





app = Flask(__name__)


@app.route("/")
def index():

    return "hej niggah!"




# l for lists
@app.route("/l/", methods=['POST', 'GET'])
def files():
    if request.method == 'POST':

        pprint(request.headers)

        f = open("test.json", 'w')

        data = json.dumps(request.json)

        f.write(data)

        return ""

    elif request.method == 'GET':
        return json.dumps(glob('static/*/*.json'))





@app.route("/l/<file>")
def get_file(file):
    print("here")
    return redirect('/static/' + file)









# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)


if __name__ == "__main__":
    app.run(host=HOST, port='4000')

