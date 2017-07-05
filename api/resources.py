from flask import request, jsonify
from flask_restful import Resource, Api
from orm import app, Category, Lesson, Words
from schemas import CategorySchema, LessonSchema, WordSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
import json
import sys

api = Api(app)
categorySchema = CategorySchema(strict=True)
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
            new_results = []

            for lesson in results:
                words_query = Words.query.filter_by(lessonId=lesson['id']).all()
                words = wordSchema.dump(words_query, many=True).data

                lesson['data'] = words
                new_results.append(lesson)

            results = new_results

        return results

    def post(self):
        json_data = request.get_json(force=True)
        processedWords = []

        try:
            dataWords = json_data.pop('data', None)

            dataCat = {'name': json_data.pop('category', None)}
            category = Category.query.filter_by(name=dataCat['name']).first()

            if not category:
                category = categorySchema.load(dataCat).data
                category.add(category)

            json_data['categoryName'] = category.name
            lesson = lessonSchema.load(json_data).data
            lesson.add(lesson)

            for words in dataWords:
                wordsDict = {'lessonId': lesson.id, 'key': words.pop(0), 'values': words}
                words = wordSchema.load(wordsDict).data
                words.add(words)

            return json_data

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp


class lessonResource(Resource):
    def get(self, id):
        results = {}

        try:
            lesson_query = Lesson.query.filter_by(id=id).first()
            results = lessonSchema.dump(lesson_query).data
        except KeyError:
            return {'error': 'unable to find lesson ' + str(id)}, 404

        words_query = Words.query.filter_by(lessonId=results['id']).all()
        results['data'] = wordSchema.dump(words_query, many=True).data

        return results


if __name__ == '__main__':
    api.add_resource(AllLessonResource, '/lessons/')
    api.add_resource(lessonResource, '/lessons/<int:id>')

    app.run(debug=True)
