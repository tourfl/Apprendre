# Inspired from https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API

from flask import Flask
from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy

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
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250))

    def __init__(self, title, author):
        self.title = title
        self.author = author

    # why not just a function returning JSON?
    def to_json():
        pass

    def __repr__(self):
        return '<Lesson %r>' % self.title


class LessonSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=not_blank)
    author = fields.String(validate=not_blank)

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/lessons/"
        else:
            self_link = "/lessons/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'lessons'
