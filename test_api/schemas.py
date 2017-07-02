from marshmallow import validate, Schema, fields, post_load, post_dump, ValidationError
import json
from orm import Lesson, Words, MAX_WORD, MAX_META

meta_size = validate.Length(min=1, max=MAX_META, error='META field cannot be blank or bigger than ' + str(MAX_META))
word_size = validate.Length(min=1, max=MAX_WORD, error='WORD field cannot be blank or bigger than ' + str(MAX_WORD))


def strToList(data, key, many=False):
    if many:
        for element in data:
            element[key] = json.loads(element[key][0])
    else:
        data[key] = json.loads(data[key][0])

    return data


def listToStr(data, key):
    listStr = json.dumps(data[key])

    if len(listStr) > MAX_WORD:  # Validation
        raise ValidationError('WORD field cannot be blank or bigger than ' + str(MAX_WORD))

    return listStr


class LessonSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=meta_size)
    author = fields.String(validate=meta_size)
    nbUse = fields.Integer()
    header = fields.List(fields.String)

    @post_load
    def makeLesson(self, data):
        return Lesson(data['title'], data['author'], listToStr(data, 'header'))

    @post_dump(None, True)
    def changeHeaderType(self, data, many):  # not a lot of inspiration for the name
        return strToList(data, 'header', many)

    class Meta:
        type_ = 'Lessons'


class WordSchema(Schema):
    id = fields.Integer(dump_only=True)
    lessonId = fields.Integer()
    key = fields.List(fields.String)
    values = fields.List(fields.String)

    @post_load
    def makeWords(self, data):
        return Words(data['lessonId'], data['key'], listToStr(data, 'values'))

    @post_dump(None, True)
    def changeHeaderType(self, data, many):  # not a lot of inspiration for the name
        return strToList(data, 'values', many)
