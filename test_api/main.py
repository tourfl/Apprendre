from flask import request
from flask_restful import Resource, Api
from orm import Lesson, app

api = Api(app)

lessons = []


class AllLessonsResource(Resource):
    def get(self):
        return [lesson['title'] for lesson in lessons]

    def post(self):
        form = request.form

        title = form['title'].replace(" ", "_")

        dic = {'id': title, 'title': form['title'], 'date': form['date']}
        lessons.append(dic)
        return dic


class LessonResource(Resource):
    def get(self, title):

        dic = {}

        for lesson in lessons:
            if lesson['id'] == title:
                dic = lesson
                break
        return dic

    def put(self, title):
        form = request.form

        dic = {'id': title, 'title': form['title'], 'date': form['date']}
        lessons.append(dic)
        return self.get(title)


api.add_resource(AllLessonsResource, '/lessons/')
api.add_resource(LessonResource, '/lessons/<string:title>')


if __name__ == '__main__':
    app.run(debug=True)
