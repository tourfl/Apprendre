from flask import request, jsonify
from flask_restful import Resource, Api
from orm import app, Lesson, Words
from schemas import LessonSchema, WordSchema
from marshmallow import ValidationError
import json
import sys

api = Api(app)
lessonSchema = LessonSchema(strict=True)
wordSchema = WordSchema(strict=True)


class AllLessonResource(Resource):
    def get(self):
        try:
            data = json.loads(request.args['data'])
        except (KeyError, ValueError):
            data = False

        lesson_query = Lesson.query.all()
        results = lessonSchema.dump(lesson_query, many=True).data

        if data:
            results = []

        return results

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data, file=sys.stderr)

        try:
            lesson = lessonSchema.load(json_data['meta']).data
            lesson.add(lesson)

            ## TO DO: words stuff!

            return json_data

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp


class lessonResource(Resource):
    def get(self, title):
        results = {}

        lesson_query = Lesson.query.filter_by(title=title.replace('_', ' ')).first()
        results['meta'] = lessonSchema.dump(lesson_query).data

        words_query = Words.query.filter_by(lessonId=results['meta']['id']).all()
        results['data'] = wordSchema.dump(words_query, many=True).data

        return results


api.add_resource(AllLessonResource, '/lessons/')
api.add_resource(lessonResource, '/lessons/<string:title>')


if __name__ == '__main__':
    app.run(debug=True)
