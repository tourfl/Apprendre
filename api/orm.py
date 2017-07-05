# Inspired from https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

MAX_META = 50
MAX_WORD = 250

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./lessons.db'
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


class Category(db.Model, CRUD):
    name = db.Column(db.String(MAX_META), primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class Lesson(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(MAX_META), nullable=False)
    author = db.Column(db.String(MAX_META), nullable=False)
    header = db.Column(db.String(MAX_WORD), nullable=False)
    nbUse = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False)
    categoryName = db.Column(db.String(MAX_META), db.ForeignKey(Category.name), nullable=False)

    def __init__(self, title, author, header, date, categoryName):
        self.title = title
        self.author = author
        self.header = header
        self.nbUse = 0
        self.date = date
        self.categoryName = categoryName

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
