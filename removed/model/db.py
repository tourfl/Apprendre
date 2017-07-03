from flask_sqlalchemy import SQLAlchemy
from api import db
from datetime import datetime

# parameters
TITLE_SIZE=80
AUTHOR_SIZE=20
KEYWORD_SIZE=40

class Thema(db.Model):
    """Thema contains description for a thematic, i.e. a group of words"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(TITLE_SIZE))
    author = db.Column(db.String(AUTHOR_SIZE))
    date = db.Column(db.DateTime)
    usetime = db.Column(db.Integer)

    def __init__(self, title, author, date):
        super(Thema, self).__init__()

        self.title = title
        self.author = author

        if date is None:
            date = datetime.utcnow()

        self.date = date
        self.usetime = 0

    def __repr__(self):
        return '<Thema %r>' % self.title



class Hand(db.Model):
    """Hand contains a set of words"""
    id = db.Column(db.Integer, primary_key=True)
    thema_id = db.Column(db.String(TITLE_SIZE), db.ForeignKey('thema.id'))
    keyword = db.Column(db.String(KEYWORD_SIZE))
    words = db.Column(db.PickleType) # includes keyword! easier for queries

    def __init__(self, id, thema_id, keyword, words):
        super(Hand, self).__init__()
        self.id = id
        self.thema_id = thematic
        self.keyword = keyword
        self.words = words

    def __repr__(self):
        return '<Hand %r>' % self.keyword

if __name__ == '__main__':

    presidents = Thema('Presidents', 'Raph', None)

    db.session.add(presidents)

    print(presidents)
