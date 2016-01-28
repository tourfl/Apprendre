# coding: utf-8

from flask import Flask, request, url_for, render_template, make_response, redirect, session
import subprocess
import os
import datetime

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





@app.route("/lists", methods=['POST', 'GET'])
def lists():
    if request.method == 'POST':

        pprint(request.headers)

        f = open("test.json", 'w')

        data = json.dumps(request.json)

        f.write(data)

        return ""

    elif request.method == 'GET':

        ls = subprocess.Popen(["ls"], stdout=subprocess.PIPE)

        return ls.communicate()









@app.route("/lists/<file>")
def get(file):

    data = None

    with open(file + 'json') as file_data:
        data = json.load(file_data)

    if data == None:
        return 'no data man'

    return 'there is data man'









# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

