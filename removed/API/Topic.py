from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship
from datetime import date


Base = declarative_base()


class Topic(Base):
    """Topic contains metadata for a list of words"""
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    crdate = Column(Date)
    # creator = Column(Integer, ForeignKey("user.id"), nullable=False)
    nb_use = Column(Integer)
    hand = relationship('Hand')

    def __init__(self, dic):
        self.title = dic["title"]
        self.crdate = date.today()
        self.nb_use = 0

    def __repr__(self):
        return "<Topic(title='%s', date='%s', nb_use='%i')>" % (self.title, self.crdate.isoformat(), self.nb_use)


def test():
    dic = {"title": "Negotation"}

    top1 = Topic(dic)

    print(top1)

if __name__ == '__main__':
    test()


from Hand import Hand
