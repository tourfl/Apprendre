# Inspired from https://github.com/Leo-G/Flask-SQLALchemy-RESTFUL-API

from flask import Blueprint, request, jsonify, make_response
from orm import Lesson, LessonSchema, db, app
from flask_restful import Api, Resource
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError


lessons = Blueprint('lists', __name__)
schema = LessonSchema()
api = Api(lessons)


class LessonList(Resource):
    def get(self):
        lessons_query = Lesson.query.all()
        results = schema.dump(lessons_query, many=True).data
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                lesson_dict = raw_dict['data']['attributes']
                lesson = Lesson(lesson_dict['title'], lesson_dict['author'])
                lesson.add(lesson)
                query = Lesson.query.get(lesson.id)
                results = schema.dump(query).data
                return results, 201

        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 403
                return resp

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
                return resp


if __name__ == '__main__':
    api.add_resource(LessonList, '.json')
