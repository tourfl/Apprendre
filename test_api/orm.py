# Inspired from https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

MAX_META = 50
MAX_WORD = 250

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)


class CRUD():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Lesson(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(MAX_META), nullable=False)
    author = db.Column(db.String(MAX_META), nullable=False)
    header = db.Column(db.String(MAX_WORD), nullable=False)
    nbUse = db.Column(db.Integer)

    def __init__(self, wordList):
        self.title = title
        self.author = author
        self.header = header
        self.nbUse = 0

    def __repr__(self):
        return '<Lesson %r>' % self.title


class Words(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    lessonId = db.Column(db.Integer, db.ForeignKey(Lesson.id), nullable=False)
    key = db.Column(db.String(MAX_WORD), nullable=False)
    values = db.Column(db.String(MAX_WORD), nullable=False)

    def __init__(self, lessonId, key, values):
        self.lessonId = lessonId
        self.key = key
        self.values = values

    def __repr__(self):
        return '<Lesson %r>' % self.key
