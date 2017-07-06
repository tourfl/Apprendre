from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, inputs
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


def addData(results):
    for lesson in results:
        words_query = Words.query.filter_by(lessonId=lesson['id']).all()
        words = wordSchema.dump(words_query, many=True).data

        lesson['data'] = words

    return results


class AllLessonResource(Resource):
    def get(self):

        # parsing
        parser = reqparse.RequestParser()
        parser.add_argument('show', location='args')
        parser.add_argument('category', location='args')
        args = parser.parse_args()

        # lessons query
        if args['category']:
            lesson_query = Lesson.query.filter_by(category=args['category'])
        else:
            lesson_query = Lesson.query

        results = lessonSchema.dump(lesson_query.all(), many=True).data

        # if asked, data query
        if args['show'] == 'more':
            results = addData(results)

        return results

    def post(self):
        json_data = request.get_json(force=True)

        # TO DO: build schema for the whole coming data!

        try:
            dataWords = json_data.pop('data', None)

            dataCat = {'name': json_data.pop('category', None)}

            category = Category.query.filter_by(name=dataCat['name']).first()

            if not category:
                category = categorySchema.load(dataCat).data
                category.add(category)

            json_data['category'] = category.name
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


class LessonResource(Resource):
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


def less_about_lessons(list_lessons):
    for dic in list_lessons:
        for element in dic.keys() ^ ['title', 'id']:
            dic.pop(element)

    return list_lessons


class AllCategoriesResource(Resource):
    def get(self):
        # parsing
        parser = reqparse.RequestParser()
        parser.add_argument('show', location='args')
        args = parser.parse_args()

        # query & deserializing
        query = Category.query.all()
        results = categorySchema.dump(query, many=True).data

        # if required show lessons
        if args['show'] == 'more':
            for dic in results:
                query = Lesson.query.filter_by(category=dic['name']).all()
                l = lessonSchema.dump(query, many=True).data
                dic['lessons'] = less_about_lessons(l)

        return results


class CategoryResource(Resource):
    def get(self, id):
        # parsing
        parser = reqparse.RequestParser()
        parser.add_argument('show', location='args')
        args = parser.parse_args()

        # category query & deserializing
        query = Category.query.filter_by(id=id).first()
        if not query:
            return {'error': 'unable to find category ' + str(id)}, 404
        results = categorySchema.dump(query).data

        # lessons query & deserializing
        query = Lesson.query.filter_by(category=query.name).all()
        results['lessons'] = lessonSchema.dump(query, many=True).data

        if args['show'] == 'less':
            results['lessons'] = less_about_lessons(results['lessons'])

        return results


if __name__ == '__main__':
    api.add_resource(AllLessonResource, '/lessons/')
    api.add_resource(LessonResource, '/lessons/<int:id>')
    api.add_resource(AllCategoriesResource, '/categories/')
    api.add_resource(CategoryResource, '/categories/<int:id>')

    app.run(debug=True)
