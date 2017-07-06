from marshmallow import validate, Schema, fields, post_load, post_dump, ValidationError
import json
from orm import Category, Lesson, Words, MAX_WORD, MAX_META

meta_size = validate.Length(min=1, max=MAX_META, error='META field cannot be blank or bigger than ' + str(MAX_META))
word_size = validate.Length(min=1, max=MAX_WORD, error='WORD field cannot be blank or bigger than ' + str(MAX_WORD))
one_at_least = validate.Length(min=2, error='LIST field cannot be blank or contained a single element')
not_blank = validate.Length(min=1, error='LIST field cannot be blank')


def strToList(data, key, many=False):
    if many:
        for element in data:
            element[key] = json.loads(element[key][0])
    else:
        data[key] = json.loads(data[key][0])

    return data


def listToStr(data):
    listStr = json.dumps(data)

    if len(listStr) > MAX_WORD:  # Validation
        raise ValidationError('WORD field cannot be blank or bigger than ' + str(MAX_WORD))

    return listStr


class CategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=meta_size)

    @post_load
    def makeCat(self, data):
        return Category(data['name'])

    class Meta:
        type_ = 'Categories'


class LessonSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=meta_size)
    author = fields.String(validate=meta_size)
    nbUse = fields.Integer()
    header = fields.List(fields.String(validate=meta_size))
    date = fields.DateTime()
    category = fields.String()

    @post_load
    def makeLesson(self, data):
        return Lesson(data['title'], data['author'], listToStr(data['header']), data['date'], data['category'])

    @post_dump(None, True)
    def changeHeaderType(self, data, many):  # not a lot of inspiration for the name
        return strToList(data, 'header', many)

    class Meta:
        type_ = 'Lessons'


class WordSchema(Schema):
    id = fields.Integer(dump_only=True)
    lessonId = fields.Integer()
    key = fields.String()
    values = fields.List(fields.String)

    @post_load(None, True)
    def makeWords(self, data, many):

        if many:
            dataProcessed = []
            for words in data:
                dataProcessed.append(Words(words['lessonId'], words['key'], listToStr(words['values'])))
        else:
            dataProcessed = Words(data['lessonId'], data['key'], listToStr(data['values']))

        return dataProcessed

    @post_dump(None, True)
    def changeHeaderType(self, data, many):  # not a lot of inspiration for the name

        data = strToList(data, 'values', many)

        if many:
            dataProcessed = []
            for words in data:
                dataProcessed.append([words['key']] + words['values'])

        else:
            dataProcessed = [words['key']] + words['values']

        return dataProcessed
