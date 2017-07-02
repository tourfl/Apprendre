from flask import request, jsonify
from flask_restful import Resource, Api
from orm import app, Lesson, LessonSchema
from marshmallow import ValidationError
import sys

api = Api(app)
lessonSchema = LessonSchema(strict=True)


class AllLessonsResource(Resource):
    def get(self):
        lessons_query = Lesson.query.all()
        results = lessonSchema.dump(lessons_query, many=True).data
        return results

    def post(self):
        form = request.form

        try:
            lessonSchema.validate(form)
            lesson = Lesson(form['title'], form['author'])
            lesson.add(lesson)
            return form

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp


class LessonResource(Resource):
    def get(self, title):
        lesson_query = Lesson.query.filter_by(title=title.replace('_', ' ')).first()
        results = lessonSchema.dump(lesson_query).data
        return results


api.add_resource(AllLessonsResource, '/lessons/')
api.add_resource(LessonResource, '/lessons/<string:title>')


if __name__ == '__main__':
    app.run(debug=True)
