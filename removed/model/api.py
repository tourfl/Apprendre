# coding: utf-8

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text # more comfortable with textual SQL

from db_to_json import * # import json

## Restful:
#  Uniform Interface
#  Stateless
#  Cacheable
#  Client-Server
#  Layered System
#  Code on Demand (optional)

# configuration
DEBUG = False
SECRET_KEY = 'development key'
HOST = '0.0.0.0'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/test.db'
db = SQLAlchemy(app)


@app.route("/thema", methods=['POST', 'GET'])
def thema_collection():
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        return 'Try'


@app.route("/thema/<myth>")
def thema_element(myth):
    return json.dumps(['money', 'corporate world'])


if __name__ == "__main__":
    app.run(host=HOST, port=4000)
